from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


# Настройка параметров Firefox
firefox_options = Options()
firefox_options.set_preference('devtools.console.stdout.level', 'warn')

# Инициализация драйвера
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()),
    options=firefox_options
)

try:
    # 1. Открытие страницы
    driver.get("http://the-internet.herokuapp.com/inputs")
    sleep(1)

    # 2. Поиск поля ввода
    input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")

    # 3. Ввод значения 1000
    input_field.send_keys("1000")
    print("Введено значение: 1000")
    sleep(1)

    # 4. Очистка поля
    input_field.clear()
    print("Поле очищено")
    sleep(1)

    # 5. Ввод значения 999
    input_field.send_keys("999")
    print("Введено значение: 999")
    sleep(1)

    # 6. Проверка результата
    current_value = input_field.get_attribute("value")
    if current_value == "999":
        print("Проверка пройдена: поле содержит 999")
    else:
        print(f"Ошибка: поле содержит {current_value} вместо 999")

finally:
    # 7. Закрытие браузера
    driver.quit()
    print("\nТест завершен!")