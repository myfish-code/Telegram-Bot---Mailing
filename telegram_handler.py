
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from database import get_account, clear_account, add_account
from fake_useragent import UserAgent

import asyncio
import pickle
import random
import time

def random_sleep(min_second , max_second ):
    time.sleep(random.uniform(min_second, max_second))
    
def handle_telegram(driver, bot, message, record):
    print(f"Telegram обработчик запущен на добавлении записи - {record}")

    
    
    answer1 = login_telegram(bot, message, driver, "636194225")
    if not answer1:
        send_chat(driver, record)
        bot.send_message(message.chat.id, "Запись для месенджера Telergam успешно отправлена.")

    driver.close()
    driver.quit()
    
    


def login_telegram(bot, message, driver, phone_number):
    driver.get("https://web.telegram.org/k/")  
    #driver.execute_script("""
    #localStorage.setItem('account1', '{"dc1_auth_key":"80d9c15fa522df21c14c04cd5e2e9979bd559265e0e92a95562b02ae72d8502bbb865a7d1c0f3de0db05613304b9eb4a1043269f808b0d1e5057172abf4409c7f532e06c0140bec1c999c463839b8ba29dbd3db20e4a126646f998172ea443537cbc01ce8103ad832e4213621e3998d8bb0303e6291c1a4b520c41f29f5fbd79da6e973c11e27b26913849f59df665b4d133888d70f9db77d5cb1b75890188bc8e29fb4c2bb12c59c561a636aa12cb7344abf8e278bb96f1c0cef7ede50e336f9dd3ea70a04764dc425abdd27ef43a6293be0df5d907cde3f4217cd151081cba2ef5d3ef44dd262fb5f68d7204184e001cd69195e42e1db3e93c2453efd3fd62","dc1_server_salt":"87a06506a62d6f13","dc2_auth_key":"9c0cf16beb810197768dc7e12832e41e557671829b78fcd46684131519b63b9ac78c51e3d7650bf21210dcd9db09b00c93780e5d38cc558f74e28b46c834b46e80c7eaca286f58a96728e2df21e3978556b09735e4057d8f962e27be5032c7208ea82371f78fbf58f15cd75b290c6598d0cb8aa38e768a790b74ae3792111de62a048d2747788668deda1d75412ec7ddfb45e98524d1460dade190398f4698b008cc0377b8de2be049566666f936cc5b6eafa96e5b69d72a04d3db248704e8fd67b34572414a3624e17882ec0d5e58ac2373dc1e098f5670dd7e520b7b1d3bd3b415d8cb09036104cb99bacc191fd4f81b12c5bc2384b251ca23199593360328","dc2_server_salt":"f7a27c9aa22b098c","dc3_auth_key":"3683134b309b81ed590a7aa76d6f6533859609b3baaac88988f60d80711c1f81b83fce626d0be358af1ed919891d35cd3c09c25b7dcd61f619f615ec0f0bccc7b591da31fd516af61e39cc62d11c2b87cee27c860c2f6801bf6123c16412ff39f6c41ee72818d5aedc1213fb1003f0016356ca3acc558b49701d8e7274667b17fe78469d1365288a4a150c41e9a7e374c03fae6cc6de90ed5d0802bc56237991563f180ed4977431e15dca92a5bf8df4a6395155793e180451575e2c0eed7ab5220f7e51aedde1ef5fe624c781b02fd412f5c0be5df61ba928bd61bf2e3fc91ddb2ebdc35cb55b95bf602a0a9558c616f88be6946347aa38f20f391f5f17edce","dc3_server_salt":"47e935b7943a5909","dc4_auth_key":"3c9f8970d8fba76e170be730e4174d86b7916793ad0376fc42986e70f52b977a34f170d68a1899565d1ec1f76951696d7b90ae591b7622b187d0622731e6bec2f7649398990296509ad1633a55f60f08a98aef3974d3009e42b68bf0921bc345d52ba6270d6672ce6f50cce4e1e1983feffe5d47cf5f4b8e222a146fc13a01abbfb3fed497f922f8abd86dcad03b64fc714ebaa81874a4a57f355c09105312079b1bf61f1c8803d599b0dd9880ffeea26e6eb4b90439474b6241efb27e3a9beed68e0cf33f88f74b4dae34737e97217bfd3eeccab6466072230d8dd163154cc612f2d2e957617011e877a97868004139d4ccce4cb21f35ea9abe9fffd8f175c0","dc4_server_salt":"3cf899caad06849c","dc5_auth_key":"9f43e23831d86d58f061d153c5ba3c5b48124f2d6272306a52e14184b451abe1a04728161e86ced2ee01d2abbfa2d059f8f3a9bebebbc2fbdb66540096f9008e680f8c2f0b7e312148a2d04441d9ff0a8fcddd5c6bc67d4f1ddfedb64ea8a43513d07c33f1d44da62b320ad6a4e042bf9e9352d4ca8cefb721746ffa38385b0eb76d02b785fa379bc51800514b12481cb3960b8df106c3d2d3ebc70e67092757c54cabc29422a6e3b51b24173664c4067dfeae14169114fe8a78037b26fcf7ff7de4529bfb7a1caa71ed4197d00e11285f9ace1a845f7b51861f661984dbdff64bf7dfd0d78736065e9086681d3129c90a7e38c8eb245e5415c96bd006478eb9","dc5_server_salt":"6f40a664705ade51","userId":1029343957,"dcId":2,"date":1740687461}');""")
    random_sleep(1, 2)
    data = get_account("Telegram")
    if data:
        driver.execute_script(f"""
        localStorage.setItem("{data[0]}",'{data[1]}');""")
        print(data)
    else:
        print(None)
    driver.refresh()
    
    random_sleep(8, 12)



    try:
        text = driver.find_element(By.CLASS_NAME, "i18n")
        if text.text == "Log in to Telegram by QR Code":
            if data:
                clear_account("Telegram")
            
            log_by_phone = driver.find_element(By.CLASS_NAME, "c-ripple")
            log_by_phone.click()
            random_sleep(1, 2)
            phone_input = driver.find_elements(By.CLASS_NAME, "input-field-input")
            phone_input[1].send_keys(phone_number)
            random_sleep(1, 2)
            button_log = driver.find_element(By.CLASS_NAME, "c-ripple")
            button_log.click()
            bot.send_message(message.chat.id, "Введите 5-значный код проверки для телеграмма, у вас есть 45 секунд.")
            time.sleep(45)
            account_key_value = driver.execute_script("""
            let key = Object.keys(localStorage).find(k => k.startsWith('account'));
            return [key, localStorage.getItem(key)];
            """)
            print(1)
            add_account("Telegram",account_key_value[0], account_key_value[1])
            print(1)
            
    except:
        try:
            random_sleep(2, 4)
            chats = driver.find_elements(By.CLASS_NAME, "c-ripple")
            chats[0].click()
            bot.send_message(message.chat.id, "Вы авторизованы, приступаю к отправке.")
        except:
            bot.send_message(message.chat.id, "Не удалось авторизоваться.")
            return 1
           

    random_sleep(7, 10)
    

def send_chat(driver, record):
    chats = driver.find_elements(By.CLASS_NAME, "c-ripple")
    text_chat = driver.find_elements(By.CLASS_NAME, "peer-title")
    for chat in range(6, len(chats)):
        
        
        print(chat)
        if chat - 6 == len(text_chat):
            break
        if text_chat[chat - 6].text[:4:] != "test":
            continue

        chats[chat].click()
        random_sleep(3, 6)

        keyboard = driver.find_element(By.CLASS_NAME, "input-message-input")
        for char in record:

            keyboard.send_keys(char)
            random_sleep(0.05, 0.2)
        random_sleep(2, 4)

        keyboard.send_keys(Keys.ENTER)
        random_sleep(2, 4)
    


def input_code_telegram(driver, code):
    field = driver.find_element(By.CLASS_NAME, "input-field-input.is-empty")
    field.send_keys(code)

       
#handle_telegram(None, 1)