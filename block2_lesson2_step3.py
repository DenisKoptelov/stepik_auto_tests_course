from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try: 
    #даем браузеру ссылку
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #достаем значения для суммы и переводим в текст    
    x = browser.find_element(By.ID, 'num1').text
    y = browser.find_element(By.ID, 'num2').text
    #находим выпадающее меню и туда вставляем сумму найденных значений (при сложении переводим в числа, потом в строку)
    result = browser.find_element(By.CSS_SELECTOR, "select#dropdown")
    result.send_keys(str(int(x)+int(y))) #где в () сумма чисел
   
   
    #Сабмит кнопка
    button = browser.find_element(by=By.CLASS_NAME, value='btn.btn-default')
    button.click()

    # ждем прогрузки страницы
    time.sleep(1)
   

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()