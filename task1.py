import requests
import telebot
from telebot import types


def handle_game_proc():
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    lst = list(res['Valute'])
    return lst


bot = telebot.TeleBot("##############################")


@bot.message_handler(commands=handle_game_proc())
def game_process(message):
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    res = res['Valute'][message.text[1:]
                        ]['Name'], res['Valute'][message.text[1:]]['Value']
    res = ' '.join(map(str, res))
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton('Коды валют')
    markup.add(btn)
    bot.send_message(message.chat.id, res, reply_markup=markup)


@bot.message_handler(content_types=["text"])
def send_welcome(message):
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    lst = list(res['Valute'])
    lst1 = []
    for i in lst:
        i = f"/{i} - {res['Valute'][i]['Name']}\n"
        lst1.append(i)
    str = ''.join(lst1)
    bot.send_message(
        message.chat.id, f"Выберите код валюты\n\n\n{str}")


bot.infinity_polling()
