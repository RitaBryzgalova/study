# Minecraft AI ChatBot с Яндекс API

AI чат-бот для сервера Minecraft, помогающий игрокам находить рецепты крафтов в модах через общение в чате.

## 🎯 Архитектура

```
Игрок пишет в чат
    ↓
Плагин Minecraft ловит сообщение
    ↓
Отправляет HTTP запрос на Python backend
    ↓
Backend отправляет запрос в Яндекс API
    ↓
Получает ответ с информацией о крафте
    ↓
Ответ выводится в чат игроку
```

## 📁 Структура проекта

```
minecraft-ai-chatbot/
├── backend/              # Python приложение
│   ├── src/
│   │   ├── main.py      # Точка входа Flask приложения
│   │   ├── yandex_api.py # Интеграция с Яндекс API
│   │   ├── crafting.py  # Обработка данных о крафтах
│   │   └── utils.py     # Утилиты
│   ├── requirements.txt  # Зависимости Python
│   └── .env.example     # Шаблон переменных окружения
├── plugin/              # Java плагин для Minecraft
│   └── src/
├── configs/             # Конфигурационные файлы
│   └── config.yaml      # Основная конфигурация
├── data/                # Данные (крафты, логи и т.д.)
└── README.md           # Этот файл
```

## 🚀 Начало работы

### 1. Backend (Python)

```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# Отредактируйте .env с вашим Яндекс API ключом
python src/main.py
```

### 2. Plugin (Java)

```bash
cd plugin
# Компилируйте и устанавливайте на сервер
```

## ⚙️ Конфигурация

### Переменные окружения (.env)

```
YANDEX_API_KEY=your_api_key_here
YANDEX_API_URL=https://llm.api.yandex.cloud/...
MINECRAFT_SERVER_HOST=localhost
MINECRAFT_SERVER_PORT=8080
LOG_LEVEL=INFO
```

## 📚 Популярные моды с крафтами

- Tinkers' Construct
- Immersive Engineering
- Mekanism
- Applied Energistics 2
- Industrial Craft 2
- Thermal Expansion

## 🔧 Требования

- Python 3.8+
- Java 11+ (для плагина)
- Minecraft сервер Spigot/Paper 1.19+
- Яндекс API ключ

## 📝 Лицензия

MIT
