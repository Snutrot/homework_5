from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Настройка Firefox
firefox_options = Options()
firefox_options.set_preference('log.level', 'fatal')

# Создаем драйвер
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()),
    options=firefox_options
)

# Открываем страницу
driver.get("http://uitestingplayground.com/classattr")
sleep(1)

# Находим и кликаем синюю кнопку 3 раза
for i in range(3):
    print(f"\nПопытка {i+1}:")
    
    button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()
    print("Клик по синей кнопке выполнен")
    
    # Проверяем всплывающее окно
    try:
        alert = driver.switch_to.alert
        alert.accept()
        print("Закрыли всплывающее окно")
    except:
        print("Всплывающего окна нет")
    
    sleep(0.5)

# Завершаем тест
driver.quit()
print("\nТест успешно завершен!")