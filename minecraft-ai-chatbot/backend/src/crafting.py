"""
Модуль для обработки информации о крафтах
"""
import logging
from typing import Dict, List, Optional
import json

logger = logging.getLogger(__name__)


class CraftingDatabase:
    """База данных рецептов из популярных модов"""
    
    # Популярные моды и их характеристики
    POPULAR_MODS = {
        "tinkers_construct": {
            "name": "Tinkers' Construct",
            "description": "Мод для создания и модификации инструментов",
            "items": ["Tool Station", "Smeltery", "Tool Forge"]
        },
        "immersive_engineering": {
            "name": "Immersive Engineering",
            "description": "Индустриальный мод с электричеством",
            "items": ["Metal Press", "Blast Furnace", "Workbench"]
        },
        "mekanism": {
            "name": "Mekanism",
            "description": "Индустриальный мод с многоуровневой сложностью",
            "items": ["Metallurgic Infuser", "Enrichment Chamber", "Combiner"]
        },
        "applied_energistics": {
            "name": "Applied Energistics 2",
            "description": "Мод для автоматизации с сетью ME",
            "items": ["ME Controller", "Crafting Terminal", "Storage Cells"]
        },
        "thermal_expansion": {
            "name": "Thermal Expansion",
            "description": "Мод с тепловыми машинами",
            "items": ["Furnace", "Crucible", "Transposer"]
        }
    }
    
    @staticmethod
    def get_mod_info(mod_name: str) -> Optional[Dict]:
        """Получить информацию о моде"""
        mod_key = mod_name.lower().replace(" ", "_").replace("'", "")
        return CraftingDatabase.POPULAR_MODS.get(mod_key)
    
    @staticmethod
    def list_mods() -> List[str]:
        """Получить список всех известных модов"""
        return [mod["name"] for mod in CraftingDatabase.POPULAR_MODS.values()]
    
    @staticmethod
    def format_crafting_context(query: str) -> str:
        """
        Форматировать контекст для AI модели на основе запроса
        
        Args:
            query: Вопрос игрока
            
        Returns:
            Отформатированный контекст
        """
        # Определяем, о каком моде речь
        mentioned_mods = []
        for mod_key, mod_info in CraftingDatabase.POPULAR_MODS.items():
            if mod_info["name"].lower() in query.lower():
                mentioned_mods.append(mod_info)
        
        context = f"Вопрос: {query}\n\n"
        
        if mentioned_mods:
            context += "Релевантные моды:\n"
            for mod in mentioned_mods:
                context += f"- {mod['name']}: {mod['description']}\n"
        else:
            context += "Доступные моды для помощи:\n"
            for mod in CraftingDatabase.POPULAR_MODS.values():
                context += f"- {mod['name']}\n"
        
        return context


class CraftingHelper:
    """Помощник для ответов о крафтах"""
    
    @staticmethod
    def extract_mod_from_query(query: str) -> Optional[str]:
        """Извлечь название мода из запроса"""
        for mod_key, mod_info in CraftingDatabase.POPULAR_MODS.items():
            if mod_info["name"].lower() in query.lower():
                return mod_info["name"]
        return None
    
    @staticmethod
    def format_ai_response(ai_answer: str, mod_name: Optional[str] = None) -> str:
        """Отформатировать ответ AI для вывода в чат"""
        # Добавляем префикс для эмодзи и красивого формата
        response = f"🤖 {ai_answer}"
        
        if mod_name:
            response = f"[{mod_name}] {response}"
        
        # Обрезаем до 256 символов для Minecraft чата
        if len(response) > 256:
            response = response[:253] + "..."
        
        return response
    
    @staticmethod
    def is_crafting_question(query: str) -> bool:
        """Проверить, является ли вопрос о крафте"""
        crafting_keywords = [
            "как сделать", "как крафтить", "рецепт", "как получить",
            "как собрать", "где найти", "как создать", "как построить",
            "what is the recipe", "how to craft", "how to make"
        ]
        
        query_lower = query.lower()
        return any(keyword in query_lower for keyword in crafting_keywords)
