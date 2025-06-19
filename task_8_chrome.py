from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Настройка параметров Chrome чтобы избежать лишних ошибок в терминале связанных с логами 
chrome_options = Options()
chrome_options.add_argument("--log-level=3")  # Уменьшение логов
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Инициализация драйвера
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=chrome_options
)

try:
    # 1. Открываем страницу авторизации
    driver.get("http://the-internet.herokuapp.com/login")
    sleep(1)  # Ждём загрузки страницы

    # 2. Вводим логин
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")
    print("Введён логин: tomsmith")

    # 3. Вводим пароль
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    print("Введён пароль: SuperSecretPassword!")

    # 4. Нажимаем кнопку Login
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    print("Нажата кнопка Login")
    sleep(2)  # Ждём завершения авторизации

    # 5. Проверяем успешность входа
    if "secure" in driver.current_url:
        print("Успешная авторизация! Текущая страница:", driver.current_url)
    else:
        print("Ошибка авторизации!")

    # 6. Проверяем сообщение об успехе
    try:
        flash_message = driver.find_element(By.ID, "flash").text
        if "You logged into" in flash_message:
            print("Сообщение системы:", flash_message.split("!")[0] + "!")
    except:
        print("Сообщение об успехе не найдено")

finally:
    driver.quit()
    
print("Тест завершен!")   