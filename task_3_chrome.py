from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Настройка параметров Chrome чтобы избежать лишних ошибок в терминале связанных с логами 
chrome_options = Options()
chrome_options.add_argument("--log-level=3")  # Устанавливаем минимальный уровень логов
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Отключаем логи драйвера

# Инициализация драйвера с использованием webdriver-manager
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=chrome_options
)

try:
    # Шаг 1: Открыть страницу
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
    sleep(1)  # Даем странице время для загрузки

    # Шаг 2: Пять раз кликнуть на кнопку "Add Element"
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    for _ in range(5):
        add_button.click()
        sleep(0.3)  # Небольшая пауза между кликами

    # Шаг 3: Собрать со страницы список кнопок "Delete"
    delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")

    # Шаг 4: Вывести в терминале число кнопок
    print(f"Количество кнопок Delete: {len(delete_buttons)}")

finally:
    # Закрытие браузера
    driver.quit()

print("Тест завершен!")