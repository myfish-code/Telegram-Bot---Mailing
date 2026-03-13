

#def handle_viber(record):
 #   pass

    


#handle_viber(123)



from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import pytest
import time
import random

from telegram_handler import login_telegram

#capabilities = dict(
#    platformName='Android',
#    automationName='uiautomator2',
#    deviceName='Android',
#    appPackage='com.viber.voip',  # Это package для Viber
#    appActivity='.WelcomeActivity',  # Это activity для Viber
#    language='en',
#    locale='US',
#    noReset=True,  # <<< Оставляет данные приложения после завершения сессии
#    dontStopAppOnReset=True  # <<< Не перезапускает приложение при повторном запуске теста
#)

#capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
#appium_server_url = 'http://localhost:4723'
def random_sleep(min_sleep, max_sleep):
    time.sleep(random.uniform(min_sleep, max_sleep))

#def driver():
 #   app_driver = webdriver.Remote(appium_server_url, options=capabilities_options)
 #   yield app_driver
  #  if app_driver:
  #      app_driver.quit()

def handle_viber(bot, message, driver1, record):
    random_sleep(2, 4)
    try:
        app =  driver1.find_element(AppiumBy.XPATH, '//*[contains(@text, "Viber")]')
        

        app.click()
        random_sleep(4, 5)
    except:
        print(113123)
    try:
        app = driver1.find_element(AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Predicted app: Viber"]')

        app.click()
        random_sleep(4, 5)
    except:
        print(113123)
    
    try:
        change_phone = driver1.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.viber.voip:id/text" and @text="Change your phone number"]')

        change_phone.click()
        random_sleep(4, 5)
    except:
        print(113123)

    print(1)
    answer1 = login_viber(bot, message, driver1)
    if not answer1:
        send_message(driver1, record)
    
        bot.send_message(message.chat.id, "Запись для месенджера Viber успешно отправлена.")
    #driver1.close()
    #driver1.quit()
#def create_driver():
#    driver = webdriver.Remote(appium_server_url, options=capabilities_options)
#    return driver


def login_viber(bot, message, driver) -> None:
    try:
        chat = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.viber.voip:id/messages"]/android.view.ViewGroup[1]')
        chat.click()
        random_sleep(2, 4)
        chat_end = driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
        chat_end.click()
        bot.send_message(message.chat.id, "Вы авторизованы, приступаю к отправке.")
        return 0
    except:
        pass
    #driver = create_driver()
    # Ожидаем, чтобы приложение открылось
    random_sleep(4, 6)  # Можно использовать явные ожидания, но тут для простоты достаточно простого ожидания
    try:
        # Пример поиска кнопки "Разрешить доступ к медиа"
        allow_button = driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
        allow_button.click()
        random_sleep(2, 3)
    except Exception as e:
        print("Кнопка разрешения не найдена или она не отображается:", e)
    

    try:
        start_button = driver.find_element(AppiumBy.ID, "com.viber.voip:id/okBtn")
        start_button.click()
        random_sleep(5, 8)
    except:
        pass


    try:
        button_rem = driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Cancel"]')
        button_rem.click()
        random_sleep(5, 8)
    except:
        pass


    try:
        country_btn = driver.find_element(AppiumBy.ID, "com.viber.voip:id/registration_country_btn")
        country_btn.click()
        random_sleep(5, 6)
    except:
        pass


    try:
        country_search = driver.find_element(AppiumBy.ID, "com.viber.voip:id/search_src_text")
        country_search.send_keys("+380")
        random_sleep(5, 6)
    except:
        pass
    

    try:
        country_select = driver.find_element(AppiumBy.ID, "com.viber.voip:id/name")
        country_select.click()
        random_sleep(5, 6)
    except:
        pass
    

    try:
        enter_phone = driver.find_element(AppiumBy.ID, "com.viber.voip:id/registration_phone_field")
        enter_phone.send_keys("990078921")
        random_sleep(3 , 5)
    except:
        pass
    

    try:
        button_continue = driver.find_element(AppiumBy.ID, "com.viber.voip:id/btn_continue")
        button_continue.click()
        random_sleep(3 , 5)
    except:
        pass


    try:
        yes_button = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.viber.voip:id/yes_btn"]')
        yes_button.click()
        random_sleep(3 , 5)
    except:
        pass


    try:
        window_continue = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.viber.voip:id/continue_btn"]')
        window_continue.click()
        random_sleep(3 , 5)
    except:
        pass

    
    for item in range(5):
        try:
            # Пример поиска кнопки "Разрешить доступ к медиа"
            allow_button = driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
            allow_button.click()
            random_sleep(5, 6)
        except:
            pass
        	
    try:
        next_but = driver.find_element(AppiumBy.ID, "com.viber.voip:id/call_me_button")
        next_but.click()
        random_sleep(2, 4)
        call_me = driver.find_element(AppiumBy.ID, "com.viber.voip:id/btn_call_me")
        call_me.click()
        bot.send_message(message.chat.id, "Скажите последние 4 цифры номера телефона, с которого вам позвонили. У вас есть 45 секунд.")
        random_sleep(45, 50)
    except:
        bot.send_message(message.chat.id, "Превышен лимит отправок на данный номер, попробуйте позже.")
        return 1
    
    try:
        # Пример поиска кнопки "Разрешить доступ к медиа"
        allow_button = driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
        allow_button.click()
        time.sleep(2)
    except Exception as e:
        print("Кнопка разрешения не найдена или она не отображается:", e)

    try:
        chat = driver.find_element(AppiumBy.ID, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.viber.voip:id/messages"]/android.view.ViewGroup[1]')
        chat.click()
        bot.send_message(message.chat.id, "Вы авторизованы, приступаю к отправке.")
        return 0
    except:
        bot.send_message(message.chat.id, "Не удалось авторизоваться попробуйте еще раз.")
        return 1
        
            
    
    
        
   
    
    


def send_message(driver, record):

    try:
        i = 1
        while True:
            
            chat = driver.find_element(AppiumBy.XPATH, f'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.viber.voip:id/messages"]/android.view.ViewGroup[{i}]')
            chat.click()
            random_sleep(2, 4)
            sender = driver.find_element(AppiumBy.ID, "com.viber.voip:id/send_text")
            sender.send_keys(record)
            random_sleep(2, 4)
            chat = driver.find_element(AppiumBy.ID, "com.viber.voip:id/send_icon_background_container")
            chat.click()
            random_sleep(2, 4)
            chat_end = driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
            chat_end.click()
            random_sleep(2, 4)
            i += 1
    except:
        pass

    

def input_code_viber(driver, code):
    for i in range(4):
        field = driver.find_element(AppiumBy.ID, f'//android.widget.LinearLayout[@resource-id="com.viber.voip:id/enter_code"]/android.widget.EditText[{i}]')
        field.send_keys(code[i])
        random_sleep(0.05, 0.2)
    
    
    random_sleep(3, 5)
    for item in range(5):
        try:
                # Пример поиска кнопки "Разрешить доступ к медиа"
            allow_button = driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
            allow_button.click()

            random_sleep(2, 4)
        except Exception as e:
            print("Кнопка разрешения не найдена или она не отображается:", e)
    
    button_later = driver.find_element(AppiumBy.ID, "com.viber.voip:id/buttonMaybeLater")
    button_later.click()
    random_sleep(2, 4)
    #сделать дальнейший скип всех разрешений и т д и полностью подготовить парсер 


#нажать кнопку галочки 	 id com.viber.voip:id/continueButtonView
# 4 раза разрешить доступ 
# id 	com.viber.voip:id/buttonMaybeLater может позже контакты
# группа //androidx.recyclerview.widget.RecyclerView[@resource-id="com.viber.voip:id/messages"]/android.view.ViewGroup[2]
# группа //androidx.recyclerview.widget.RecyclerView[@resource-id="com.viber.voip:id/messages"]/android.view.ViewGroup[6]
# отправка com.viber.voip:id/send_text
# 	com.viber.voip:id/btn_send_icon_2 com.viber.voip:id/send_icon_background_container