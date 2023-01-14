import os
import requests
import telebot

os.system('cls')

bot = telebot.TeleBot('XXXXXX') # https://t.me/d_slider_bot

def request(data):
    currency = ''
    if data == 1:
        req_data = 'USD'
    elif data == 2:
        req_data = 'EUR'
    elif data == 3:
        req_data = 'GBP'
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    currency = res['Valute'][req_data]['Name'] + ' = ' + str(res['Valute'][req_data]['Value'])
    return currency

@bot.message_handler(commands=['menu'])
def start_message(message):
    bot.send_message(message.chat.id, 'Выберите валюту:\n'+
    '=======================================\n'+
    '1 - $ Доллар США\n'+
    '2 - € Евро\n'+
    '3 - £ Фунт стерлингов\n'+
    '=======================================')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == '1' or message.text == '2' or message.text == '3':
        bot.send_message(message.chat.id, f'{request(int(message.text))}')
    else:
        bot.send_message(message.chat.id, 'Некорректный ввод')

bot.infinity_polling()