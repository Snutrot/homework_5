from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def click_blue_button():
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
        # Шаг 1: Открыть страницу
        driver.get("http://uitestingplayground.com/classattr")
        sleep(1)

        # Шаг 2: Кликнуть на синюю кнопку через CSS-класс
        blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
        blue_button.click()
        print("Успешный клик по синей кнопке через CSS-класс")
        
        # Обработка алерта (если появится)
        try:
            alert = driver.switch_to.alert
            alert.accept()
        except:
            pass
        
        sleep(0.5)
        
    finally:
        # Закрытие браузера
        driver.quit()

# Запускаем скрипт 3 раза подряд
for i in range(3):
    print(f"\nПопытка {i+1}:")
    click_blue_button()
    sleep(0.5)  # Пауза между запусками

print("Тест завершен!")