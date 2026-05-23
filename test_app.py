import json
import time

def test_logic():
    # Проверяем, что логика получения времени работает
    current_time = int(time.time())
    print(f"Testing time logic: {current_time}")
    assert current_time > 0, "Ошибка: Время должно быть больше нуля!"
    print("Test passed!")

if __name__ == "__main__":
    test_logic()
