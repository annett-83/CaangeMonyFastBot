import telebot
import requests
import json
from config import TOKEN,keys
#from extensions import ConverterException, Convertor
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start', 'help'])
def help (message: telebot.types.Message):
    text = 'Hallo! Ich kann dir helfen! ' \
           'Ich kann deinen gewünschten Betrag in die gewünschte Währung konvertieren.' \
           ' Lass uns starten, geben Sie die folgenden Werte ein:' \
           '\n<Währung><konvertierte Währung><Betrag>' \
           '\n Verfügbare Währung, klick hier: /values'
    bot.reply_to(message,text)

@bot.message_handler(commands=['values'])
def values(message:telebot.types.Message):
    text = 'Verfügbare Währung:'
    for key in keys.keys():
       text = '\n'.join((text,key,))
    bot.reply_to(message,text)
@bot.message_handler(content_types=['text', ])
def convert(message:telebot.types.Message):
    quote, base, amount = message.text.split(' ')
    r= requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
    bot.send_message(message.chat.id, text )
bot.polling()
