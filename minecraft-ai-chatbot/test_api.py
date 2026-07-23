"""
Скрипт для тестирования AI ChatBot API
"""
import requests
import json
from typing import Dict, Any

BASE_URL = "http://localhost:8080"

class ChatBotTester:
    """Тестер для API ChatBot"""
    
    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url.rstrip('/')
    
    def test_health(self) -> bool:
        """Проверить здоровье сервиса"""
        try:
            print("🔍 Проверка здоровья сервиса...")
            response = requests.get(f"{self.base_url}/health", timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                print(f"✓ Сервис работает: {data}")
                return True
            else:
                print(f"✗ Ошибка: {response.status_code}")
                return False
        except Exception as e:
            print(f"✗ Не удалось подключиться: {e}")
            return False
    
    def test_mods(self) -> bool:
        """Получить список модов"""
        try:
            print("\n📚 Получение списка модов...")
            response = requests.get(f"{self.base_url}/mods", timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                print(f"✓ Доступно модов: {data['count']}")
                for mod in data['mods']:
                    print(f"  - {mod['name']}: {mod['description']}")
                return True
            else:
                print(f"✗ Ошибка: {response.status_code}")
                return False
        except Exception as e:
            print(f"✗ Ошибка: {e}")
            return False
    
    def test_chat(self, message: str, player: str = "TestPlayer") -> bool:
        """Тестировать запрос к чату"""
        try:
            print(f"\n💬 Отправка запроса: '{message}'")
            
            payload = {
                "player": player,
                "message": message
            }
            
            response = requests.post(
                f"{self.base_url}/chat",
                json=payload,
                timeout=30
            )
            
            print(f"Статус: {response.status_code}")
            data = response.json()
            
            if response.status_code == 200 and data.get('success'):
                print(f"✓ Ответ получен:")
                print(f"  Оригинальный: {data.get('ai_response')}")
                print(f"  Для чата: {data.get('response')}")
                if data.get('mod'):
                    print(f"  Мод: {data.get('mod')}")
                return True
            else:
                print(f"✗ Ошибка: {data.get('error', 'Unknown error')}")
                return False
        except requests.exceptions.Timeout:
            print(f"✗ Таймаут при запросе (>30 сек)")
            return False
        except Exception as e:
            print(f"✗ Ошибка: {e}")
            return False
    
    def run_all_tests(self):
        """Запустить все тесты"""
        print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                     🤖 Minecraft AI ChatBot Tester                           ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """)
        
        # Тест 1: Health check
        health_ok = self.test_health()
        
        if not health_ok:
            print("\n✗ Сервис недоступен. Убедитесь, что он запущен:")
            print("  cd backend")
            print("  python src/main.py")
            return
        
        # Тест 2: Mods list
        self.test_mods()
        
        # Тест 3: Chat requests
        test_messages = [
            "как сделать сеть в tinkers construct?",
            "mekanism как начать?",
            "Привет!",  # Не о крафте - должно быть проигнорировано
            "как получить индастриал крафт?",
        ]
        
        print("\n" + "="*80)
        print("🧪 ТЕСТИРОВАНИЕ ЗАПРОСОВ")
        print("="*80)
        
        results = []
        for msg in test_messages:
            result = self.test_chat(msg)
            results.append((msg, result))
        
        # Итоги
        print("\n" + "="*80)
        print("📊 ИТОГИ")
        print("="*80)
        
        successful = sum(1 for _, result in results if result)
        
        print(f"\nВсего тестов: {len(results)}")
        print(f"Успешных: {successful}")
        print(f"Провалено: {len(results) - successful}")
        
        if successful == len(results):
            print("\n✓ Все тесты пройдены успешно!")
        else:
            print("\n⚠ Некоторые тесты провалены")
            print("\nПровалено:")
            for msg, result in results:
                if not result:
                    print(f"  - '{msg}'")


if __name__ == "__main__":
    import sys
    
    # Можно передать URL как аргумент
    url = sys.argv[1] if len(sys.argv) > 1 else BASE_URL
    
    tester = ChatBotTester(url)
    tester.run_all_tests()
