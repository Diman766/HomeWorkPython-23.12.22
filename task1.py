import requests
import telebot


def handle_game_proc(message):
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    lst = list(res['Valute'])
    try:
        if lst.count(message.text) > 0:
            return True
        else:
            return False
    except KeyError:
        if lst.count(message.text) > 0:
            return True
        else:
            return False


bot = telebot.TeleBot("####################################")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    lst = list(res['Valute'])
    lst1 = []
    for i in lst:
        i += f" - {res['Valute'][i]['Name']}\n"
        lst1.append(i)
    x = ''.join(lst1)
    bot.reply_to(message, f"Выберите код валюты\n{x}")


@bot.message_handler(func=handle_game_proc)
def game_process(message):
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    res = res['Valute'][message.text]['Name'], res['Valute'][message.text]['Value']
    res = ' '.join(map(str, res))
    bot.reply_to(message, res)

bot.infinity_polling()
