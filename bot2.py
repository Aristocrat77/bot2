import telebot
from telebot.types import InlineKeyboardMarkup

bot = telebot.TeleBot('7721748157:AAH5NlI6XHxw2U5pJDywdlES1H41R9bF6J0')

from telebot import types


@bot.message_handler(content_types=['text'])
def welcome(pm):
    sent_msg = bot.send_message(pm.chat.id, "Чтобы узнать БЖУ введите свой вес")
    bot.register_next_step_handler(sent_msg, v_handler)


def v_handler(pm):
    try:
        v = int(pm.text)
        sent_msg = bot.send_message(pm.chat.id, f"Ваш вес {v}. Теперь введите свой рост")
        bot.register_next_step_handler(sent_msg, age_handler, v)
    except ValueError:
        bot.send_message(pm.chat.id, 'Вы ввели некорректное число!')


def age_handler(pm, v):
    try:
        age = int(pm.text)
        bot.send_message(pm.chat.id, f"Ваш вес {v}, ваш рост {age}.")
    except ValueError:
        bot.send_message(pm.chat.id, 'Вы ввели некорректное число!')


bot.polling(none_stop=True, interval=0)
