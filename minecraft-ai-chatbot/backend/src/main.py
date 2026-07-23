"""
Главное Flask приложение для Minecraft AI ChatBot
"""
import logging
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from datetime import datetime

from yandex_api import YandexAPI
from crafting import CraftingHelper, CraftingDatabase

# Загружаем переменные окружения
load_dotenv()

# Настройка логирования
log_level = os.getenv("LOG_LEVEL", "INFO")
logging.basicConfig(
    level=getattr(logging, log_level),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Инициализация Flask приложения
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# Инициализация Яндекс API
try:
    yandex_api = YandexAPI()
    logger.info("✓ Яндекс API инициализирован")
except Exception as e:
    logger.error(f"✗ Ошибка инициализации Яндекс API: {e}")
    yandex_api = None


# ============================================================================
# ROUTES
# ============================================================================

@app.route("/health", methods=["GET"])
def health():
    """Проверка здоровья приложения"""
    api_connected = yandex_api.validate_connection() if yandex_api else False
    
    return jsonify({
        "status": "ok",
        "timestamp": datetime.now().isoformat(),
        "api_connected": api_connected
    }), 200


@app.route("/chat", methods=["POST"])
def chat():
    """
    Основной endpoint для обработки сообщений из чата Minecraft
    
    Ожидает JSON:
    {
        "player": "PlayerName",
        "message": "как сделать...",
        "timestamp": "2024-01-01T12:00:00"
    }
    """
    try:
        data = request.get_json()
        
        if not data or "message" not in data:
            return jsonify({
                "success": False,
                "error": "Отсутствует поле 'message'"
            }), 400
        
        player = data.get("player", "Unknown")
        message = data.get("message", "").strip()
        
        # Логируем запрос
        logger.info(f"📨 Сообщение от {player}: {message}")
        
        # Проверяем, является ли вопрос о крафте
        if not CraftingHelper.is_crafting_question(message):
            logger.info(f"⚠️  Сообщение не о крафте, игнорируем")
            return jsonify({
                "success": False,
                "message": "Это сообщение не выглядит как вопрос о крафте",
                "action": "ignore"
            }), 400
        
        # Получаем ответ от AI
        if not yandex_api:
            return jsonify({
                "success": False,
                "error": "AI API недоступен"
            }), 503
        
        ai_response = yandex_api.get_crafting_advice(message)
        
        if not ai_response:
            return jsonify({
                "success": False,
                "error": "Не удалось получить ответ от AI"
            }), 500
        
        # Форматируем ответ для Minecraft чата
        mod_name = CraftingHelper.extract_mod_from_query(message)
        formatted_response = CraftingHelper.format_ai_response(ai_response, mod_name)
        
        logger.info(f"✓ Ответ для {player}: {formatted_response[:60]}...")
        
        return jsonify({
            "success": True,
            "player": player,
            "query": message,
            "response": formatted_response,
            "ai_response": ai_response,
            "mod": mod_name,
            "timestamp": datetime.now().isoformat()
        }), 200
    
    except Exception as e:
        logger.error(f"✗ Ошибка обработки запроса: {e}", exc_info=True)
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route("/mods", methods=["GET"])
def get_mods():
    """Получить список известных модов"""
    mods = []
    for mod_key, mod_info in CraftingDatabase.POPULAR_MODS.items():
        mods.append({
            "id": mod_key,
            "name": mod_info["name"],
            "description": mod_info["description"]
        })
    
    return jsonify({
        "success": True,
        "mods": mods,
        "count": len(mods)
    }), 200


@app.route("/test", methods=["POST"])
def test():
    """Endpoint для тестирования"""
    try:
        message = request.json.get("message", "как сделать алмазную кирку?")
        logger.info(f"🧪 Тестовый запрос: {message}")
        
        if not yandex_api:
            return jsonify({"error": "API не инициализирован"}), 500
        
        response = yandex_api.get_crafting_advice(message)
        
        return jsonify({
            "query": message,
            "response": response
        }), 200
    except Exception as e:
        logger.error(f"Ошибка тестирования: {e}")
        return jsonify({"error": str(e)}), 500


# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": "Endpoint не найден"
    }), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "success": False,
        "error": "Внутренняя ошибка сервера"
    }), 500


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    host = os.getenv("FLASK_HOST", "0.0.0.0")
    port = int(os.getenv("FLASK_PORT", 8080))
    debug = os.getenv("FLASK_ENV", "production") == "development"
    
    logger.info(f"""
    
╔══════════════════════════════════════════════════════════════════════════════╗
║                  🤖 Minecraft AI ChatBot Server                              ║
║                                                                              ║
║  Сервер запущен:  http://{host}:{port}                                      ║
║  Режим:           {'DEBUG' if debug else 'PRODUCTION'}                      ║
║  Документация:    http://{host}:{port}/docs                                  ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)
    
    app.run(host=host, port=port, debug=debug)
