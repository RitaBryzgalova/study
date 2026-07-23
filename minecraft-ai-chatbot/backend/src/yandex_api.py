"""
Интеграция с Яндекс API для обработки запросов о крафтах
"""
import os
import requests
import logging
from typing import Optional, Dict, Any
from pydantic import BaseModel

logger = logging.getLogger(__name__)


class YandexAPIRequest(BaseModel):
    """Модель запроса к Яндекс API"""
    prompt: str
    max_tokens: int = 500
    temperature: float = 0.7


class YandexAPI:
    """Класс для работы с Яндекс LLM API"""
    
    def __init__(self):
        self.api_key = os.getenv("YANDEX_API_KEY")
        self.api_url = os.getenv("YANDEX_API_URL")
        self.catalog_id = os.getenv("YANDEX_CATALOG_ID")
        self.model_name = os.getenv("MODEL_NAME", "yandexgpt-lite")
        
        if not all([self.api_key, self.catalog_id]):
            raise ValueError("YANDEX_API_KEY и YANDEX_CATALOG_ID должны быть установлены")
    
    def get_crafting_advice(self, query: str) -> Optional[str]:
        """
        Получить рекомендацию о крафте через Яндекс API
        
        Args:
            query: Вопрос о крафте от игрока
            
        Returns:
            Ответ от AI модели или None если ошибка
        """
        try:
            system_prompt = """Ты помощник для игры Minecraft. 
Твоя задача помогать игрокам находить рецепты крафтов, особенно в модах.
Давай краткие и понятные ответы на русском языке.
Если ты не знаешь про мод, скажи об этом честно."""
            
            messages = [
                {
                    "role": "system",
                    "text": system_prompt
                },
                {
                    "role": "user",
                    "text": query
                }
            ]
            
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "modelUri": f"gpt://{self.catalog_id}/{self.model_name}/latest",
                "completionOptions": {
                    "stream": False,
                    "temperature": 0.7,
                    "maxTokens": 500
                },
                "messages": messages
            }
            
            response = requests.post(
                self.api_url,
                json=payload,
                headers=headers,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                # Яндекс API возвращает результат в result.choices[0].message.text
                if "result" in result and "alternatives" in result["result"]:
                    answer = result["result"]["alternatives"][0]["message"]["text"]
                    logger.info(f"AI ответ получен: {answer[:50]}...")
                    return answer
                else:
                    logger.error(f"Неожиданный формат ответа: {result}")
                    return None
            else:
                logger.error(f"Ошибка API: {response.status_code} - {response.text}")
                return None
                
        except requests.exceptions.Timeout:
            logger.error("Таймаут при обращении к Яндекс API")
            return None
        except Exception as e:
            logger.error(f"Ошибка при обращении к Яндекс API: {e}")
            return None
    
    def validate_connection(self) -> bool:
        """Проверить подключение к API"""
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "modelUri": f"gpt://{self.catalog_id}/{self.model_name}/latest",
                "completionOptions": {
                    "stream": False,
                    "temperature": 0.1,
                    "maxTokens": 10
                },
                "messages": [
                    {"role": "user", "text": "test"}
                ]
            }
            
            response = requests.post(
                self.api_url,
                json=payload,
                headers=headers,
                timeout=10
            )
            
            return response.status_code == 200
        except Exception as e:
            logger.error(f"Ошибка проверки подключения: {e}")
            return False
