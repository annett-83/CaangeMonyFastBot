import telebot
from config import TOKEN,keys
from extensions import ConverterException, Convertor
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
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConverterException('Falscher Wertenanzahl!')
        quote, base, amount = values
        total_base = Convertor.convert(quote, base, amount)
    except ConverterException as e:
        bot.reply_to(message, f'Benutzerfehler!\n{e}')
    except Exception as e:
        bot.reply_to(message, f'der Befehl konnte nicht verarbeiten werden!')
    else:
     text = f'Price {amount} {quote} in {base} - {total_base}'
     bot.send_message(message.chat.id,text)

bot.polling()