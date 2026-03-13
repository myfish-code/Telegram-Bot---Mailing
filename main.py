import telebot
from telebot import types
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
#from appium import webdriver
import appium
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from database import get_mail, add_mail, remove_mail, search_mail
from telegram_handler import handle_telegram, input_code_telegram
from viber_handler import handle_viber, input_code_viber
from whatsapp_handler import handle_whatsapp

import os
from dotenv import load_dotenv

TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = telebot.TeleBot(TOKEN)


bot.set_my_commands([
    types.BotCommand("start", "Запустить бота"),
])

operation_state = None
app = None 

@bot.message_handler(commands=['start'])
def start_use(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    mailing = types.KeyboardButton('Начать рассылку')
    add_record = types.KeyboardButton('Управление записями в рассылке')
    change_count_group = types.KeyboardButton('Изменения количества чатов')

    markup.add(mailing, add_record, change_count_group)
    bot.send_message(
        message.chat.id,
        "Привет! Я готов к работе. 🚀\n\n"
        "Выбери, что ты хочешь сделать:\n",
        reply_markup=markup
        
    )

@bot.message_handler(content_types=['text'])
def text_reception(message):
    global operation_state, app, driver 

    if message.text == "Вернуться в начало":
        start_use(message)

    elif message.text == "Начать рассылку":
        start_mailing(message)

    elif message.text in ["Telegram", "Viber", "Whatsapp", "Все приложения"]:
        operation_state = "search"
        app = message.text
        records = get_mail()
        if not records:
            bot.send_message(message.chat.id, "Записей не найдено.")
        else:

            bot.send_message(message.chat.id, f"Введите номер записи (Просто число от {1} до {len(records)}) которую желаете отправить")
            for elem in records:
                bot.send_message(message.chat.id, f"№ {elem[1]} - {elem[2]}")

        
    elif message.text == "Управление записями в рассылке":
        manage_records(message)

    elif message.text == "Изменения количества чатов":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
        viber_group = types.KeyboardButton('Viber')
        ret_start = types.KeyboardButton('Вернуться в начало')
        markup.add(viber_group,ret_start)
        bot.send_message(message.chat.id, "Выберите месенджер для изменения количества чатов", reply_markup=markup)
        
    elif message.text == "Просмотр записей":
        records = get_mail()
        if not records:

            bot.send_message(message.chat.id, "Записей не найдено.")
        else:
            bot.send_message(message.chat.id, "Список записей: ")
            for elem in records:
                bot.send_message(message.chat.id, f"№ {elem[1]} - {elem[2]}")
    
    elif message.text == "Добавление записей":
        bot.send_message(message.chat.id, "Введи запись с припиской в начале 'Добавить запись'")
    
    elif "Добавить запись" in ' '.join(message.text.split()):
        text_save = ' '.join(message.text.split())[16:].strip()

        if text_save:
            add_mail(text_save)

            bot.send_message(message.chat.id, "Запись успешно добавлена!")
        else:
            bot.send_message(message.chat.id, "Пожалуйста введите корректную запись.")

    elif message.text == "Удаление записей":
        records = get_mail()
        operation_state = "delete"
        app = None
        
        if not records:
            bot.send_message(message.chat.id, "Записей не найдено.")
        else:
            bot.send_message(message.chat.id, f"Введите номер записи (Просто число от {1} до {len(records)}) которую желаете удалить")
            for elem in records:
                bot.send_message(message.chat.id, f"№ {elem[1]} - {elem[2]}")
                
    elif message.text.strip().isdigit() and len(message.text.strip()) >= 4 and len(message.text.strip()) <= 5:
        global driver, driver1
        if app == "Telegram" and len(message.text.strip()) == 5:
            try:
                input_code_telegram(driver, message.text.strip())
            except:
                bot.send_message(message.chat.id, "Некорректные данные отправки")
        elif app == "Viber" and len(message.text.strip()) == 4:
            try:
                input_code_viber(driver1, message.text.strip())
            except:
                bot.send_message(message.chat.id, "Некорректные данные отправки")
        
            
    elif message.text.strip().isdigit():
        number = int(message.text.strip())
        record = search_mail(number)
        if record:

            if operation_state == "delete":
                remove_mail(number)
                bot.send_message(message.chat.id, "Запись успешно удалена.")
                
            elif operation_state == "search":
                
                if app == "Telegram":
                    options = webdriver.ChromeOptions()
                    ua = UserAgent()
                    options.add_argument(f"user-agent={ua.random}")
                    driver = webdriver.Chrome(options=options)
                    handle_telegram(driver, bot, message, record)


                elif app == "Viber":
                    capabilities = dict(
                    platformName='Android',
                    automationName='uiautomator2',
                    deviceName='Android',
                    language='en',
                    locale='US',
                    dontStopAppOnReset=True,      
                    noReset=True,
                    )

                    capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
                    appium_server_url = 'http://localhost:4723'
                    try:
                        if driver1 is None:
                            driver1 = appium.webdriver.Remote(appium_server_url, options=capabilities_options)
                    except:
                        driver1 = appium.webdriver.Remote(appium_server_url, options=capabilities_options)

                    driver1.press_keycode(3)
                    handle_viber(bot, message, driver1, record)

                elif app == "Whatsapp":
                    options = webdriver.ChromeOptions()

                    #options.add_argument('user-data-dir=C:/Users/06361/AppData/Local/Google/Chrome/User Data/Profile 3')
                    options.add_argument("--no-sandbox")
                    options.add_argument("--disable-gpu")
    
                    driver2 = webdriver.Chrome(options=options)
                    
                    handle_whatsapp(driver2, bot, message, record)
                   
                    
                elif app == "Все приложения":
                    options = webdriver.ChromeOptions()
                    ua = UserAgent()
                    options.add_argument(f"user-agent={ua.random}")
                    driver = webdriver.Chrome(options=options)
                    handle_telegram(driver, bot, message, record)
                    

                    capabilities = dict(
                    platformName='Android',
                    automationName='uiautomator2',
                    deviceName='Android',
                    appPackage='com.viber.voip',  # Это package для Viber
                    appActivity='.WelcomeActivity',  # Это activity для Viber
                    language='en',
                    locale='US',
                    dontStopAppOnReset=True,
                    noReset=True
                    )
                    capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
                    appium_server_url = 'http://localhost:4723'
                    try:
                        if driver1 is None:
                            driver1 = appium.webdriver.Remote(appium_server_url, options=capabilities_options)
                    except:
                        driver1 = appium.webdriver.Remote(appium_server_url, options=capabilities_options)
                    driver1.press_keycode(3)
                    handle_viber(bot, message, driver1, record)
                   


                    options = webdriver.ChromeOptions()

                    options.add_argument('user-data-dir=C:/Users/06361/AppData/Local/Google/Chrome/User Data/Profile 3')
                    options.add_argument("--no-sandbox")
                    options.add_argument("--disable-gpu")
    
                    driver2 = webdriver.Chrome(options=options)
                    handle_whatsapp(driver2, bot, message, record)
                    
                    
            

            if not operation_state:
                bot.send_message(message.chat.id, "Пожалуйста, скажите что вы хотите сделать с номером.")
        else:
            bot.send_message(message.chat.id, "Данного номеро записи не существует.")
        
    else:
        bot.send_message(message.chat.id, "Пожалуйста введите корректное сообщение или начните заново командой /start")


def start_mailing(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=4)
    telegram = types.KeyboardButton('Telegram')
    viber = types.KeyboardButton('Viber')
    whatsapp = types.KeyboardButton('Whatsapp')
    all_apps = types.KeyboardButton('Все приложения')
    ret_start = types.KeyboardButton('Вернуться в начало')
    
    markup.add(telegram, viber, whatsapp, all_apps, ret_start)

    bot.send_message(message.chat.id, "Выбери, где ты хочешь сделать рассылку", reply_markup=markup)


def manage_records(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
    view_records = types.KeyboardButton('Просмотр записей')
    add_records = types.KeyboardButton('Добавление записей')
    delete_records = types.KeyboardButton('Удаление записей')
    ret_start = types.KeyboardButton('Вернуться в начало')
    markup.add(view_records, add_records, delete_records, ret_start)

    bot.send_message(message.chat.id, "Выбери, что ты хочешь сделать с записями", reply_markup=markup)

bot.polling()