from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Настройка параметров Chrome чтобы избежать лишних ошибок в терминале связанных с логами 
chrome_options = Options()
chrome_options.add_argument("--log-level=3") 
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Инициализация драйвера
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=chrome_options
)

try:
    # 1. Открываем страницу
    driver.get("http://the-internet.herokuapp.com/inputs")
    sleep(1)  # Ждём загрузки страницы

    # 2. Находим поле ввода
    input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")

    # 3. Вводим 1000
    input_field.send_keys("1000")
    print("Введено значение: 1000")
    sleep(1)  # Пауза для наглядности

    # 4. Очищаем поле
    input_field.clear()
    print("Поле очищено")
    sleep(1)

    # 5. Вводим 999
    input_field.send_keys("999")
    print("Введено значение: 999")
    sleep(1)

    # 6. Проверяем результат
    current_value = input_field.get_attribute("value")
    if current_value == "999":
        print("Проверка пройдена: поле содержит 999")
    else:
        print(f"Ошибка: поле содержит {current_value} вместо 999")

finally:
    driver.quit()

print("Тест завершен!")    