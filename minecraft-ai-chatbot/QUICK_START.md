# 🎯 Minecraft AI ChatBot - Быстрая справка

## 📋 Что было создано?

Полнофункциональная архитектура AI чат-бота для Minecraft с поддержкой Яндекс API:

### Backend (Python)
- ✅ Flask приложение с REST API
- ✅ Интеграция с Яндекс LLM API
- ✅ База данных популярных модов Minecraft
- ✅ Обработка и форматирование ответов
- ✅ Система логирования

### Plugin (Java)
- ✅ Плагин для Spigot/Paper сервера
- ✅ Перехват сообщений в чате
- ✅ Асинхронные запросы к backend
- ✅ Форматированный вывод в чат
- ✅ Конфигурируемость

### Документация
- ✅ README.md - общий обзор
- ✅ INSTALLATION.md - пошаговая установка
- ✅ test_api.py - тестирование API
- ✅ Конфигурационные файлы

---

## 🚀 Быстрый старт

### 1️⃣ Запустить Backend

```bash
cd C:\Users\Рита\Desktop\прогораммирование\minecraft-ai-chatbot\backend

# Установить зависимости
pip install -r requirements.txt

# Создать .env файл
copy .env.example .env

# ⚠️ ВАЖНО: Заполните YANDEX_API_KEY и YANDEX_CATALOG_ID в .env файле

# Запустить сервер
python src/main.py
```

✓ Сервер будет доступен на `http://localhost:8080`

### 2️⃣ Протестировать Backend

```bash
# В отдельной консоли:
cd C:\Users\Рита\Desktop\прогораммирование\minecraft-ai-chatbot

python test_api.py
```

### 3️⃣ Скомпилировать и установить Plugin

```bash
cd C:\Users\Рита\Desktop\прогораммирование\minecraft-ai-chatbot\plugin

# Нужен Maven и Java 11+
mvn clean package

# JAR файл будет в target/ai-chatbot-plugin-1.0.0.jar
# Скопируйте его в папку plugins вашего Minecraft сервера
```

### 4️⃣ Использовать в игре

В чате Minecraft:
```
!ai как сделать алмазную кирку?
!ai tinkers construct молот
!ai mekanism начало
```

---

## 🔑 Получение Яндекс API ключа

1. Перейти на https://cloud.yandex.ru
2. Создать проект (или использовать существующий)
3. Включить API "Yandex Foundation Models"
4. Создать сервисный аккаунт
5. Создать API ключ
6. Скопировать значения в `.env` файл

Подробнее: https://cloud.yandex.ru/docs/iam/concepts/authorization/key-pairs

---

## 📁 Структура файлов

```
minecraft-ai-chatbot/
├── backend/
│   ├── src/
│   │   ├── main.py          # 🎯 Главное Flask приложение
│   │   ├── yandex_api.py    # Интеграция с Яндекс API
│   │   └── crafting.py      # Обработка данных модов
│   ├── requirements.txt      # Python зависимости
│   └── .env.example         # Шаблон конфигурации
│
├── plugin/
│   ├── src/main/java/
│   │   └── AIChatBotPlugin.java  # 🎯 Основной класс плагина
│   ├── src/main/resources/
│   │   └── plugin.yml            # Конфигурация плагина
│   └── pom.xml                   # Maven конфигурация
│
├── configs/
│   └── plugin-config.yaml    # Конфиг для плагина
│
├── README.md                 # Обзор проекта
├── INSTALLATION.md           # Пошаговая установка
└── test_api.py              # Тестирование API
```

---

## 🔧 Основные Endpoints

### Health Check
```bash
GET /health
```

### Получить список модов
```bash
GET /mods
```

### Отправить запрос
```bash
POST /chat
Content-Type: application/json

{
  "player": "PlayerName",
  "message": "как сделать...",
  "timestamp": "2024-01-01T12:00:00"
}
```

### Тестовый запрос
```bash
POST /test
Content-Type: application/json

{
  "message": "как сделать алмазную кирку?"
}
```

---

## 💡 Примеры запросов

### curl
```bash
curl -X POST http://localhost:8080/chat \
  -H "Content-Type: application/json" \
  -d '{
    "player": "Steve",
    "message": "как получить железо?"
  }'
```

### Python
```python
import requests

response = requests.post('http://localhost:8080/chat', json={
    'player': 'Steve',
    'message': 'как получить железо?'
})

print(response.json())
```

---

## 🎮 Команды в игре

| Команда | Результат |
|---------|-----------|
| `!ai как сделать X?` | Спросить AI про крафт X |
| `!ai tinkers construct Y` | Вопрос о моде Tinkers Construct |
| `!ai mekanism начало` | Вопрос о начале работы с модом |

---

## 🆘 Troubleshooting

### Плагин не подключается к серверу
```bash
# Проверить, работает ли backend:
curl http://localhost:8080/health
```

### Ошибка про Яндекс API
- Проверьте, что `.env` заполнен
- Убедитесь в правильности ключей
- Проверьте, что API включен в облаке Яндекса

### Таймаут при запросе
- Увеличьте таймауты в конфиге
- Проверьте интернет
- Проверьте логи backend сервера

---

## 📊 Поддерживаемые моды

- 🔨 Tinkers' Construct
- ⚡ Immersive Engineering
- 🔬 Mekanism
- 💾 Applied Energistics 2
- 🌡️ Thermal Expansion
- И другие...

---

## 🎯 Следующие шаги

1. ✅ Установить и запустить Backend
2. ✅ Получить Яндекс API ключ
3. ✅ Протестировать API
4. ✅ Скомпилировать плагин
5. ✅ Установить на сервер Minecraft
6. ✅ Использовать в игре!

---

## 📚 Полная документация

- `README.md` - Архитектура и обзор
- `INSTALLATION.md` - Детальная установка
- `backend/src/main.py` - Комментарии кода
- `plugin/src/main/java/AIChatBotPlugin.java` - Java код

---

## 📞 Поддержка

Если возникли вопросы:
1. Проверьте логи
2. Прочитайте INSTALLATION.md
3. Проверьте конфигурацию

Удачи! 🚀
