from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


# Настройка параметров Firefox
firefox_options = Options()
firefox_options.set_preference('log.level', 'fatal') 

# Инициализация драйвера
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()),
    options=firefox_options
)

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
sleep(1)

# Кликнуть 5 раз на кнопку "Add Element"
add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
for _ in range(5):
    add_button.click()
    sleep(0.3)

# Собрать все кнопки Delete
delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
print(f"Количество кнопок Delete: {len(delete_buttons)}")

driver.quit()
print("\nТест завершен!")