from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Настройка Firefox
firefox_options = Options()
firefox_options.set_preference('devtools.console.stdout.level', 'warn')

# Создаем драйвер
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()),
    options=firefox_options
)

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(2)  # Ждем загрузки модального окна

try:
    # Находим и закрываем модальное окно
    close_btn = driver.find_element(By.CSS_SELECTOR, "div.modal-footer p")
    close_btn.click()
    print("Модальное окно закрыто")
    
    # Даем время на анимацию закрытия
    sleep(1)
    
    # Проверяем, что окно действительно исчезло
    modal_windows = driver.find_elements(By.CSS_SELECTOR, "div.modal")
    if not modal_windows:
        print("Проверка: окно успешно скрыто")
    else:
        # Проверяем, может быть окно просто невидимо
        if not modal_windows[0].is_displayed():
            print("Проверка: окно скрыто (невидимо)")
        else:
            print("Предупреждение: окно все еще отображается")

finally:
    # Закрываем браузер
    driver.quit()
    print("\nТест успешно завершен!")