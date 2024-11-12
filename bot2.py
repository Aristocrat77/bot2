import telebot
from telebot.types import InlineKeyboardMarkup

bot = telebot.TeleBot('7721748157:AAH5NlI6XHxw2U5pJDywdlES1H41R9bF6J0')

from telebot import types


@bot.message_handler(content_types=['text'])
def welcome(massage):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Мужчина", callback_data="1")
    btn2 = types.InlineKeyboardButton("Женщина", callback_data="2")
    markup.add(btn1, btn2)
    sd = bot.send_message(massage.chat.id, 'Чтобы узнать БЖУ укажите свой пол',
                     reply_markup=markup, parse_mode='html')
    print(sd)
    bot.register_next_step_handler(sd, v_handler)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call, self=None):
    try:
        if call.data == '1':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Вы мужчина теперь введите свой рост")
        elif call.data == '2':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Вы женщина теперь введите свой рост")
        else:
            bot.answer_callback_query(callback_query_id=call.id, text="Неизвестная команда")
    except Exception as e:
        print(repr(e))

def v_handler(pm):
    try:
        v = int(pm.text)
        sent_msg = bot.send_message(pm.chat.id, f"Ваш рост {v}. Теперь введите свой вес")
        print(v)
        bot.register_next_step_handler(sent_msg, weight_handler, v)
    except ValueError:
        bot.send_message(pm.chat.id, 'Вы ввели некорректное число!')


def weight_handler(pm, v):
    try:
        weight = int(pm.text)
        sent_msg2 = bot.send_message(pm.chat.id, f"Ваш вес {weight}. Введите возраст")
        print(weight)
        bot.register_next_step_handler(sent_msg2, age_handler, v)
    except ValueError:
        bot.send_message(pm.chat.id, 'Вы ввели некорректное число!')


def age_handler(pm, q):
    try:
        age = int(pm.text)
        bot.send_message(pm.chat.id, f"Ваш возраст {age}.")
        bot.send_message(pm.chat.id, f" ????7 ")
        print(age)
    except ValueError:
        bot.send_message(pm.chat.id, 'Вы ввели некорректное число!')




bot.polling(none_stop=True, interval=0)
