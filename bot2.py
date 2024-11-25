import telebot
from telebot.types import InlineKeyboardMarkup
from telebot import types

bot = telebot.TeleBot('7721748157:AAH5NlI6XHxw2U5pJDywdlES1H41R9bF6J0')


@bot.message_handler(commands=['start'])
def start(message):
    main = Main(bot)
    main.start(message)


class Main:
    def __init__(self, bot):
        self.age = None
        self.height = None
        self.weight = None
        self.bot = bot
        print('Main started')

    def start(self, message):
        raw_height = self.bot.send_message(message.chat.id, 'Привет писька! Введи свой рост.')
        self.bot.register_next_step_handler(raw_height, self.height_handler)

    def height_handler(self, message):
        try:
            height = int(message.text)
            self.height = height

            raw_weight = self.bot.send_message(message.chat.id, f"Теперь введи свой вес")
            self.bot.register_next_step_handler(raw_weight, self.weight_handler)
        except ValueError:
            self.bot.send_message(message.chat.id, 'Вы ввели некорректное число!')

    def weight_handler(self, message):
        try:
            weight = int(message.text)
            self.weight = weight
            raw_age = self.bot.send_message(message.chat.id, f"Твой возраст")
            self.bot.register_next_step_handler(raw_age, self.age_handler)
        except ValueError:
            self.bot.send_message(message.chat.id, 'Вы ввели некорректное число!')

    def age_handler(self, message):
        try:
            age = int(message.text)
            self.age = age
            self.bot.send_message(message.chat.id,
                                  f"Твоя суточная норма калорий для набора массы {round((((10 * (float(self.weight))) + (6.25 * (float(self.height))) - (5 * (float(self.age))) - 161) * 1.55) + 250, None)}")
        except ValueError:
            self.bot.send_message(message.chat.id, 'Вы ввели некорректное число!')


bot.polling(none_stop=True, interval=0)
