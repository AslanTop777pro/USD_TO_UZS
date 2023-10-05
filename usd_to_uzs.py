import telebot
import requests

Token = '6604903869:AAF118M98kHD2LGOT0HB6KFBZngv1fh17Ms'
API_key = 'aadb12a34d5d4ea3898f7222030381b2'
bot = telebot.TeleBot(Token)


def usd_to_uzs(chat_id):
    url = f'https://openexchangerates.org/api/latest.json?app_id={API_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        currency_rate = data['rates']['UZS']
        currency_rate1 = data['rates']['RUB']
        rub_to_uzs = currency_rate/currency_rate1
        message = f"1 USD = {round(currency_rate, 2)} UZS\n " \
                   f"1 RUB = {round(rub_to_uzs, 2)} UZS"
        bot.send_message(chat_id, message)
    else:
        bot.send_message(chat_id, 'Извините, данные отсутствуют. Попробуйте позже')

@bot.message_handler(commands = ['start'])
def start(message):
    chat_id = message.chat.id
    usd_to_uzs(chat_id)

bot.polling()
