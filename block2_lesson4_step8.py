from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try: 
    #даем браузеру ссылку
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)    
    
    #задаем счетчик ожидания
    WebDriverWait(browser, "12").until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    #указываем кнопку
    btn = browser.find_element(By.ID,"book")
    #жмем кнопку
    btn.click()
        
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
    button = browser.find_element(By.ID, 'solve')
    button.click()
    
    # ждем прогрузки страницы
    time.sleep(1)
   

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()