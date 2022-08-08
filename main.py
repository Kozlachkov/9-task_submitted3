#телеграмм бот по выдаче погоды
import telebot
from telebot import types
from weather_request import get_weather
from logging1 import log1

bot  = telebot.TeleBot('5468074232:AAEyvcIoMhOzOoTVibu9cqQ382EkpFhd8x0')

@bot.message_handler(commands=['start'])
def start(message):
    mess= f'Привет <b>{message.from_user.first_name} </b>'
    bot.send_message(message.chat.id, mess)

@bot.message_handler(commands=['weather'])
def weather(message):
    text_mess_list= message.text.split()
    text_mess=''
    for i in range(1,len(text_mess_list)-1):
        text_mess+=text_mess_list[i]+" "
    text_mess+=text_mess_list[len(text_mess_list)-1]
    log1(message)
    res = get_weather(text_mess)    
    bot.send_message(message.chat.id, res)

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text=='Hello':       
        bot.send_message(message.chat.id, 'и тебе привет')
    elif message.text=='id':
        bot.send_message(message.chat.id, f'твой id: {message.from_user.id}', parse_mode='html')
    else:
        bot.send_message(message.chat.id, 'я не знаю таких команд')

bot.polling(none_stop=True)    