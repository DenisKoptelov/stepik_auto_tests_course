from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try: 
    #даем браузеру ссылку
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #достаем значение для переменной X   
    x = browser.find_element(By.ID, 'input_value').text
    #находим поле для ввода ответа и вставляем вычисленное значение
    result = browser.find_element(By.ID, "answer")
    result.send_keys(str(math.log(abs(12*math.sin(int(x))))))
    #скроллим страницу вниз
    browser.execute_script("window.scrollBy(0, 100);")
    #кликаем чек-бокс Я робот
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()
    #выбираем радиобаттон роботы рулят
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option1.click()
    #еще скроллим страницу вниз
    browser.execute_script("window.scrollBy(0, 200);")
    #Сабмит кнопка
    button = browser.find_element(By.CLASS_NAME, 'btn btn-primary')
    button.click()

    # ждем прогрузки страницы
    time.sleep(1)
   

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()