# 🚀 Инструкция по установке и запуску

## Часть 1: Backend (Python сервис)

### Требования
- Python 3.8+
- pip

### Шаги установки

1. **Перейти в папку backend**
   ```bash
   cd backend
   ```

2. **Создать виртуальное окружение (опционально, но рекомендуется)**
   ```bash
   python -m venv venv
   
   # На Windows:
   venv\Scripts\activate
   
   # На Linux/Mac:
   source venv/bin/activate
   ```

3. **Установить зависимости**
   ```bash
   pip install -r requirements.txt
   ```

4. **Создать файл .env с конфигурацией**
   ```bash
   cp .env.example .env
   ```

5. **Отредактировать .env и заполнить ключи Яндекс API**
   ```
   YANDEX_API_KEY=your_api_key_here
   YANDEX_CATALOG_ID=your_catalog_id
   ```
   
   [Как получить Яндекс API ключ](https://cloud.yandex.ru/docs/iam/concepts/authorization/key-pairs)

6. **Запустить сервис**
   ```bash
   python src/main.py
   ```

   Сервер должен запуститься на `http://localhost:8080`

### Проверка работы

```bash
# Проверить здоровье сервиса
curl http://localhost:8080/health

# Получить список модов
curl http://localhost:8080/mods

# Тестовый запрос
curl -X POST http://localhost:8080/test \
  -H "Content-Type: application/json" \
  -d '{"message": "как сделать алмазную кирку?"}'
```

---

## Часть 2: Плагин (Minecraft)

### Требования
- Java 11+
- Maven (для компиляции)
- Spigot/Paper сервер Minecraft 1.19+

### Шаги установки

1. **Перейти в папку plugin**
   ```bash
   cd plugin
   ```

2. **Компилировать плагин**
   ```bash
   mvn clean package
   ```

   JAR файл будет создан в `target/ai-chatbot-plugin-1.0.0.jar`

3. **Скопировать плагин на сервер**
   ```bash
   cp target/ai-chatbot-plugin-1.0.0.jar /path/to/minecraft/server/plugins/
   ```

4. **Перезагрузить сервер Minecraft**
   ```
   /reload confirm
   # или перезапустить сервер
   ```

5. **Проверить, что плагин загружен**
   ```
   /plugins
   ```

### Конфигурация плагина

Отредактируйте файл конфигурации сервера (создается автоматически):

**Путь:** `plugins/AI ChatBot/config.yml`

```yaml
enabled: true
backend-url: "http://localhost:8080"
```

Убедитесь, что `backend-url` указывает на адрес Python сервиса.

---

## Часть 3: Использование

### В игре

Игроки могут использовать команду в чате:

```
!ai как сделать сеткой?
!ai tinkers construct молот рецепт
!ai mekanism как начать?
```

### Ответ будет выглядеть примерно так:

```
[AI] 🤖 В Tinkers' Construct сеть делается из...
```

---

## 🔧 Troubleshooting

### Плагин не подключается к backend

1. Проверьте, запущен ли Python сервис:
   ```bash
   curl http://localhost:8080/health
   ```

2. Проверьте URL в конфиге плагина

3. Проверьте логи сервера:
   ```
   /logs
   ```

### Ошибка "API ключ неверный"

1. Проверьте, что `YANDEX_API_KEY` правильно установлен в `.env`
2. Убедитесь, что ключ не истек
3. Проверьте, что `YANDEX_CATALOG_ID` правильный

### Таймауты при запросах

1. Увеличьте `request-timeout` в конфиге плагина
2. Проверьте интернет соединение
3. Проверьте, не перегружена ли Яндекс API

---

## 🐳 Docker (опционально)

Для более удобного развертывания можно использовать Docker:

```bash
docker build -t minecraft-ai-bot .
docker run -p 8080:8080 -e YANDEX_API_KEY=your_key minecraft-ai-bot
```

---

## 📝 Логи и отладка

### Python backend логи
Находятся в консоли при запуске, или в файле если настроен logging.

### Плагин логи
Проверьте в `logs/latest.log` сервера Minecraft.

---

## 🚀 Production развертывание

Для production используйте:

1. **Gunicorn вместо Flask встроенного сервера:**
   ```bash
   gunicorn -w 4 -b 0.0.0.0:8080 src.main:app
   ```

2. **Systemd сервис для автозапуска**

3. **Nginx как reverse proxy**

4. **SSL сертификаты**

---

## ❓ Вопросы?

Проверьте:
- README.md для обзора архитектуры
- Логи для ошибок
- Конфигурационные файлы для правильных значений
