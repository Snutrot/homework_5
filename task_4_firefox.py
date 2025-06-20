from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


def click_blue_button():
    """Выполняет клик по синей кнопке с динамическим ID."""
    # Настройка параметров Firefox
    firefox_options = Options()
    firefox_options.set_preference('log.level', 'fatal')

    # Инициализация драйвера
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()),
        options=firefox_options
    )

    driver.get("http://uitestingplayground.com/dynamicid")
    sleep(1)
    
    blue_button = driver.find_element(
        By.XPATH,
        "//button[contains(@class, 'btn-primary')]"
    )
    blue_button.click()
    print("Успешный клик по синей кнопке")
    sleep(0.5)
    
    driver.quit()


# Запускаем скрипт 3 раза подряд
for i in range(3):
    print(f"\nПопытка {i+1}:")
    click_blue_button()
    sleep(0.5)

print("\nТест завершен!")