from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent


import random
import time

def random_sleep(min_second , max_second ):
    time.sleep(random.uniform(min_second, max_second))

def handle_whatsapp(driver, bot, message, record):
    print(f"WhatsApp обработчик запущен на добавлении записи - {record}")

    print(1)
    random_sleep(3, 7)
    answer1 = login_whatsapp(driver, "636194225", bot, message)
    if not answer1:
        random_sleep(3, 7)

        send_whatsapp(driver, record)
        bot.send_message(message.chat.id, "Запись для месенджера Whatsapp успешно отправлена.")
    driver.close()  # Закрывает вкладку
    driver.quit()

def login_whatsapp(driver, phone_number, bot, message):
    driver.get("https://web.whatsapp.com/")
    random_sleep(3, 5)
    try:
        log_phone_but = driver.find_elements(By.CLASS_NAME, "xujl8zx.xopvzan.xewurvo.x3pynha.x1hql6x6.xk50ysn.x1xnyc8c")
        log_phone_but[1].click()
        random_sleep(2, 4)

        country_select = driver.find_element(By.CLASS_NAME, "x78zum5.x6s0dn4.x3pnbk8.xfex06f.x1f6kntn.x16h55sf.x1fcty0u.xw2npq5")
        country_select.click()
        random_sleep(2, 4)

        country = driver.find_element(By.CLASS_NAME,"selectable-text.copyable-text.x15bjb6t.x1n2onr6")
        country.send_keys("Україна")
        random_sleep(2, 4)
        
        country_but = driver.find_element(By.CLASS_NAME,"x1lkfr7t.xdbd6k5.x1fcty0u.xw2npq5")
        country_but.click()
        random_sleep(2, 4)

        phone_input = driver.find_elements(By.TAG_NAME, "input")
        phone_input[0].send_keys("636194225")
        random_sleep(2, 4)
        
        button = driver.find_elements(By.TAG_NAME, "button")
        button[2].click()
        random_sleep(2, 4)
        password = driver.find_elements(By.CLASS_NAME, "x2b8uid.xk50ysn.x1aueamr.x1jzgpr8.xzwifym")
        passw = ""
        for char in password:
            passw += char.text
        
        passw = passw[:4:] + "-" + passw[4::]
        bot.send_message(message.chat.id, f"Пожалуйста авторизуйтесь в приложении whatsapp. Ваш пароль - {passw}, у вас есть 45 секунд.")
        time.sleep(45)
        
    except:
        pass
    
    try:
        chats = driver.find_elements(By.CLASS_NAME, "_ak72.false._ak73")
        bot.send_message(message.chat.id, "Вы авторизованы, начинаю рассылку.")
    except:
        bot.send_message(message.chat.id, "Вы не авторизованы, начните процедуру заново.")
        return 1

    
def send_whatsapp(driver, record):
    chats = driver.find_elements(By.CLASS_NAME, "_ak72.false._ak73")
    for chat in range(len(chats)):
        chats[chat].click()
        random_sleep(4, 7)
        text = driver.find_elements(By.CLASS_NAME, "selectable-text.copyable-text.x15bjb6t.x1n2onr6")
        for char in record:

            text[1].send_keys(char)
            random_sleep(0.05, 0.2)

        random_sleep(2, 4)
        text[1].send_keys(Keys.ENTER)
        random_sleep(2, 4)
        print(chat)




