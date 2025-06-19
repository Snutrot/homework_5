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
    driver.get("http://the-internet.herokuapp.com/entry_ad")
    sleep(2)  # Ждём загрузки модального окна

    # 2. Находим и закрываем модальное окно
    modal = driver.find_element(By.CSS_SELECTOR, "div.modal")
    close_button = modal.find_element(By.XPATH, ".//p[text()='Close']")
    close_button.click()
    print("Модальное окно успешно закрыто")

    # 3. Проверяем, что окно исчезло
    sleep(1)
    if len(driver.find_elements(By.CSS_SELECTOR, "div.modal")) == 0:
        print("Проверка: модальное окно больше не отображается")
    
finally:
    driver.quit()

print("Тест завершен!")