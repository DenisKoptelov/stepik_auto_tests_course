from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    
    result = browser.find_element(By.ID, "answer")
    result.send_keys(str(math.log(abs(12*math.sin(int(x))))))
    
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()
    
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option1.click()
    # Отправляем заполненную форму
    button = browser.find_element(by=By.CLASS_NAME, value='btn.btn-default')
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
   

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()