from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


# 1. Открываем Firefox
driver = webdriver.Firefox()

# 2. Открываем страницу
driver.get("http://the-internet.herokuapp.com/login")
sleep(1)

# 3. Вводим логин и пароль
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# 4. Нажимаем кнопку
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
sleep(2)

# 5. Проверяем результат
if "secure" in driver.current_url:
    print("Тест пройден! Успешный вход")
else:
    print("Ошибка входа")

# 6. Закрываем браузер
driver.quit()
print("\nТест завершен!")