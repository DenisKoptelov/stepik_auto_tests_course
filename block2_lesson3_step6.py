from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try: 
    #даем браузеру ссылку
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    #нажимаем на кнопку
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
    
    #меняем вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(browser.window_handles[1])
    
    # ждем прогрузки страницы
    time.sleep(1)
    
    #достаем значение для переменной X   
    x = browser.find_element(By.ID, "input_value").text
    #находим поле для ввода ответа и вставляем вычисленное значение
    res = browser.find_element(By.ID, "answer")
    res.send_keys(str(math.log(abs(12*math.sin(int(x))))))
    
    # ждем прогрузки страницы
    time.sleep(1)
    
    #Сабмит кнопка
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    
    # ждем прогрузки страницы
    time.sleep(1)
   

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()