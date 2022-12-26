import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types


bot = telebot.TeleBot("##################################")


@bot.message_handler(content_types=["text"])
def exchange_rate(message):
    url = 'https://www.banki.ru/products/currency/cash/yaroslavl~/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    if message.text == 'Доллар США':
        string = str(soup.find_all(
            class_="table-flex__cell table-flex__cell--without-padding padding-left-default"))
        bot.send_message(message.chat.id, string[string.find(
            '>')+1:string.find('</div>'):].replace(',', '.'))
    elif message.text == 'Евро':
        string = str(soup.find_all(
            class_="table-flex__cell table-flex__cell--without-padding padding-left-default"))
        bot.send_message(message.chat.id, string[string.rfind(
            '>')-10:string.rfind('</div>'):].replace(',', '.'))
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Доллар США')
        btn2 = types.KeyboardButton("Евро")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, 'Нажми на кнопку!',
                         reply_markup=markup)


bot.infinity_polling()
