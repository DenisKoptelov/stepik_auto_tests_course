from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 


try: 
    #даем браузеру ссылку
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    #заполняем поля
    first_name = browser.find_element(By.NAME, 'firstname')
    first_name.send_keys("Name")

    second_name = browser.find_element(By.NAME, 'lastname')
    second_name.send_keys("LastName")
    
    male = browser.find_element(By.NAME, 'email')
    male.send_keys("qq@qq.ru")
    
    #добавляем файл
    current_dir = os.path.abspath(os.path.dirname(__file__)) #получаем путь к директории текущего исполняемого файла  
    file_path = os.path.join(current_dir, 'text.txt') #добавляем к этому пути имя файла  
    element = browser.find_element(By.ID, 'file') #задаем переменную для файла, т.е кнопку в которую он будет файл добавлять
    element.send_keys(file_path)
    
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