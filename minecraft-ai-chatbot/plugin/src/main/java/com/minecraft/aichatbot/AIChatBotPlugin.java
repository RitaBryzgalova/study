package com.minecraft.aichatbot;

import org.bukkit.Bukkit;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listeners;
import org.bukkit.event.player.AsyncPlayerChatEvent;
import org.bukkit.plugin.java.JavaPlugin;
import org.bukkit.scheduler.BukkitRunnable;

import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.logging.Level;

/**
 * Основной класс плагина AI ChatBot для Minecraft
 * 
 * Функции:
 * - Перехватывает сообщения в чате
 * - Отправляет запросы на Python сервер
 * - Выводит ответы AI в чат
 */
public class AIChatBotPlugin extends JavaPlugin implements Listeners {
    
    private String backendUrl;
    private boolean enabled;
    private static final String PLUGIN_NAME = "AI ChatBot";
    private static final String PREFIX = "§b[AI] §r";
    
    @Override
    public void onEnable() {
        // Сохраняем конфиг по умолчанию
        saveDefaultConfig();
        
        // Загружаем конфигурацию
        backendUrl = getConfig().getString("backend-url", "http://localhost:8080");
        enabled = getConfig().getBoolean("enabled", true);
        
        if (!enabled) {
            getLogger().info("Плагин отключен в конфиге");
            return;
        }
        
        // Регистрируем обработчик событий
        getServer().getPluginManager().registerEvents(this, this);
        
        // Проверяем подключение к backend
        checkBackendConnection();
        
        getLogger().log(Level.INFO, PREFIX + "§aПлагин включен!");
        getLogger().log(Level.INFO, "Backend URL: " + backendUrl);
    }
    
    @Override
    public void onDisable() {
        getLogger().log(Level.INFO, PREFIX + "§cПлагин отключен");
    }
    
    /**
     * Обработчик событий сообщений в чате
     */
    @EventHandler
    public void onPlayerChat(AsyncPlayerChatEvent event) {
        if (!enabled) return;
        
        Player player = event.getPlayer();
        String message = event.getMessage();
        
        // Если сообщение начинается с !ai, отправляем на обработку
        if (!message.startsWith("!ai")) return;
        
        // Удаляем префикс и обрабатываем
        String query = message.substring(3).trim();
        
        if (query.isEmpty()) {
            player.sendMessage(PREFIX + "§cИспользование: !ai <вопрос>");
            return;
        }
        
        getLogger().info("Новый запрос от " + player.getName() + ": " + query);
        
        // Запускаем асинхронный запрос к серверу
        new BukkitRunnable() {
            @Override
            public void run() {
                try {
                    String response = sendRequestToBackend(player.getName(), query);
                    
                    // Выводим ответ в основном потоке
                    Bukkit.getScheduler().runTask(AIChatBotPlugin.this, () -> {
                        if (response != null) {
                            player.sendMessage(PREFIX + response);
                        } else {
                            player.sendMessage(PREFIX + "§cОшибка при получении ответа");
                        }
                    });
                } catch (Exception e) {
                    getLogger().log(Level.SEVERE, "Ошибка обработки запроса", e);
                    Bukkit.getScheduler().runTask(AIChatBotPlugin.this, () -> {
                        player.sendMessage(PREFIX + "§cОшибка сервера: " + e.getMessage());
                    });
                }
            }
        }.runTaskAsynchronously(this);
    }
    
    /**
     * Отправить запрос на Python backend
     */
    private String sendRequestToBackend(String playerName, String message) {
        try {
            URL url = new URL(backendUrl + "/chat");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/json");
            conn.setConnectTimeout(10000);
            conn.setReadTimeout(15000);
            
            // Формируем JSON запрос
            String jsonRequest = String.format(
                "{\"player\": \"%s\", \"message\": \"%s\", \"timestamp\": \"%s\"}",
                escapeJson(playerName),
                escapeJson(message),
                new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss").format(new Date())
            );
            
            // Отправляем запрос
            conn.setDoOutput(true);
            try (OutputStream os = conn.getOutputStream()) {
                byte[] input = jsonRequest.getBytes(StandardCharsets.UTF_8);
                os.write(input, 0, input.length);
            }
            
            // Читаем ответ
            int responseCode = conn.getResponseCode();
            
            if (responseCode == HttpURLConnection.HTTP_OK) {
                String response = readResponse(conn.getInputStream());
                
                // Парсим JSON и извлекаем ответ
                String answer = extractResponseFromJson(response);
                return answer;
            } else {
                getLogger().warning("Ошибка backend: код " + responseCode);
                return null;
            }
            
        } catch (Exception e) {
            getLogger().log(Level.WARNING, "Ошибка подключения к backend", e);
            return null;
        }
    }
    
    /**
     * Проверить подключение к backend серверу
     */
    private void checkBackendConnection() {
        new BukkitRunnable() {
            @Override
            public void run() {
                try {
                    URL url = new URL(backendUrl + "/health");
                    HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                    conn.setConnectTimeout(5000);
                    conn.setReadTimeout(5000);
                    
                    int responseCode = conn.getResponseCode();
                    if (responseCode == 200) {
                        getLogger().log(Level.INFO, "✓ Подключение к backend установлено");
                    } else {
                        getLogger().log(Level.WARNING, "⚠ Backend ответил с кодом: " + responseCode);
                    }
                } catch (Exception e) {
                    getLogger().log(Level.WARNING, "✗ Не удалось подключиться к backend: " + e.getMessage());
                }
            }
        }.runTaskAsynchronously(this);
    }
    
    /**
     * Читать ответ из потока
     */
    private String readResponse(InputStream inputStream) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream, StandardCharsets.UTF_8));
        StringBuilder response = new StringBuilder();
        String line;
        while ((line = reader.readLine()) != null) {
            response.append(line);
        }
        reader.close();
        return response.toString();
    }
    
    /**
     * Извлечь ответ из JSON
     */
    private String extractResponseFromJson(String json) {
        try {
            // Простой парсинг JSON без библиотеки
            String key = "\"response\":\"";
            int startIndex = json.indexOf(key);
            if (startIndex == -1) return null;
            
            startIndex += key.length();
            int endIndex = json.indexOf("\"", startIndex);
            
            if (endIndex == -1) return null;
            
            return json.substring(startIndex, endIndex)
                    .replace("\\n", "\n")
                    .replace("\\\"", "\"");
        } catch (Exception e) {
            getLogger().log(Level.WARNING, "Ошибка парсинга JSON ответа", e);
            return null;
        }
    }
    
    /**
     * Экранировать строку для JSON
     */
    private String escapeJson(String string) {
        return string
                .replace("\\", "\\\\")
                .replace("\"", "\\\"")
                .replace("\n", "\\n")
                .replace("\r", "\\r");
    }
}
