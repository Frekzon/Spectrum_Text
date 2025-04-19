import pyowm
import asyncio
import random
import gigachat
import subprocess
from gigachat.models import Chat, Messages, MessagesRole
from gigachat import GigaChat
from plyer import notification
import os
import time
import subprocess
import logging
import webbrowser
import requests
import socket
import time
import smtplib
import subprocess
from win10toast import ToastNotifier




logging.basicConfig(level=logging.INFO, filename="spectrum_log.log")
logging.info("Запуск помощника")

while True:
################################################# SETTING #############################################
    hello_words = ['Чем могу служить?','Привет,чем могу помочь?','Здравствуйте','Ку,пользователь']
    error_text = ['Чувак,Ошибка.Повтори запрос','Ошибка','Проверь запрос, броу','Ошибочка']
    rw = random.choice(hello_words)
    ew = random.choice(error_text)
    help = []
    sto = 100
    sec = 0
    time.sleep(1)
    sec += 1    
    commands = 0
    from gigachat import GigaChat

    model = GigaChat(
        credentials="ZmFlM2E3ZWYtMjQ2YS00NTEwLThkZTgtYzE0M2RiZjRmMzIwOmZlNGU5MjhkLTNiZDktNDhkYS1iN2I5LTk3NDJlY2NkODU0Mg==",
        model="GigaChat",
    )


    

################################################# SETTING #############################################


################################################# DEF #################################################
    def imt(sto):
        print("Вес:")
        wes = input()
        print("Рост:")
        rost = input()
        t_rost = int(rost) / 100
        
        imt = int(wes) / float(t_rost*t_rost)
        print(str(imt))
        
    def gigachat():
        print("Задай запрос\n")
        input_request = input()
        response = model.chat(input_request)
        print(response.choices[0].message.content)
	
    def get_weather():
        print("Напишите город:")
        weather_input = input()
        city = weather_input
        url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=3456493edcef4076ece5155ecddda5f8'
        weather_data = requests.get(url).json()
        temperature = round(weather_data['main']['temp'])
        temperature_feels = round(weather_data['main']['feels_like'])
        print('Сейчас в городе', city, str(temperature), '°C')
        print('Ощущается как', str(temperature_feels), '°C')
        logging.info("Выдало погоду")
            

    
    def d20():
        d20_res = random.randint(1,20)
        print(d20_res)

    def note():
        print("Что вы хотите написать?")
        file = open('text.txt', 'a')
        request = input()
        file.write(str(request))
        file.close()
        
    def search_video(*args):
         webbrowser.open('https://www.youtube.com/results?search_query=' + request_video )
         
################################################# DEF #################################################
    print(rw + ".Ознакомтесь с функционалом при помощью команды - help")
    input_text = input()
    commands += 1
    file = open('stat_InputCommands.txt', 'a+')
    file.write(str(commands))
    file.close()
    
    
    if input_text == 'погода':
        
        get_weather()

    if input_text == 'уведомление':
        
        print("Что хотите чтобы я вывел?")
        response_title = input()
        print("Через сколько мне вывести таймер?(секунд)")
        time_sec = input()
        time.sleep(int(time_sec))

        toast = ToastNotifier()
        toast.show_toast("Spectrum", response_title, duration=10, icon_path="")
        logging.info("уведомление сработало")
        
        
    if input_text == 'help':
        print("погода - Спрашивает город и выдает погоду в этом городе")
        print("d20 - Бросает кубик d20")
        print("gigachat - ИИ от Сбербанка. Спросите что угодно")
        print("заметки - Пишите все идеи в заметки Spectrum")
        print("найти видео - Находит видео на YouTube")
        print("подбрось монету - Типичная Орел и Решка")
        print("Poweroff - Отключает компьютер")
        print("pinterest - Находит по вашему запросу в Pinterest")
        print("cmd - Командная строка")
        print("icon - найти иконку")

        
    if input_text == 'd20':
         d20()
         
         
    if input_text == 'gigachat':
        gigachat()
        
        
    if input_text == 'заметки':
        note()
        

    if input_text == 'cmd':
        subprocess.Popen('C:\\Windows\\system32\\cmd.exe')
        

    if input_text == 'найти видео':
        print("Что найти?")
        request_video = input()
        search_video()

    if input_text == 'посчитай ИМТ':
        imt(sto)
        
    if input_text == 'подбрось монету':
        print("Готовы?")
        ready = input()
        money = ['Решка','Орел']
        money_random = random.choice(money)
        print(money_random)

    if input_text == 'poweroff':
        os.system('shutdown -s')

    if input_text == 'pinterest':
        print("Напишите что хотите найти?")
        pin = input()
        webbrowser.open('https://ru.pinterest.com/search/pins/?q=' + pin + '&rs=typed')

    if input_text == 'icon':
        print("Напишите что хотите найти?")
        pin = input()
        webbrowser.open('https://www.flaticon.com/search?word=' + pin)

    pass
