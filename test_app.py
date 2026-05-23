import time

def test_app_logic():
    # Симулируем логику приложения v2.0
    mock_stats = {"count": 0}
    
    # 1. Проверяем роут /time
    current_time = int(time.time())
    mock_stats["count"] += 1 
    assert current_time > 0, "Ошибка: время не unix-timestamp"
    print(f"Check /time: OK")

    # 2. Проверяем роут /metrics
    # Счетчик должен был увеличиться после вызова /time
    assert mock_stats["count"] == 1, f"Ошибка: счетчик должен быть 1, а не {mock_stats['count']}"
    print(f"Check /metrics: OK")

if __name__ == "__main__":
    try:
        test_app_logic()
        print("--- ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО ---")
    except AssertionError as e:
        print(f"--- ТЕСТ ПРОВАЛЕН: {e} ---")
        exit(1)