import telebot
import random

API_TOKEN = '7612094054:AAFT1_6qYhRnZql3Nw-2u2H4K-P7m9C6pIQ'
bot = telebot.TeleBot(API_TOKEN)

# Список цитат
quotes = [
    "Секрет успеха — это упорство.",
    "Время — самый ценный ресурс.",
    "Знание — это сила.",
    "Действие — ключ к успеху."
]

# Класс для машины
class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def info(self):
        return f"Машина марки {self.brand}, цвет {self.color}"

# Обработчик команды '/start' и '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет! Я бот EchoBot.
Напиши мне что-нибудь приятное, и я повторю это тебе!
""")

# Обработчик команды '/info'
@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, """\
Это команда /info.
Вы можете спросить у меня что-нибудь, и я постараюсь помочь. Также вы можете отправить мне фото, и я его приму!
""")

# Обработчик команды '/цитата'
@bot.message_handler(commands=['цитата'])
def send_quote(message):
    quote = random.choice(quotes)
    bot.reply_to(message, f"Вот мудрая цитата: \"{quote}\"")

# Обработчик команды '/car'
@bot.message_handler(commands=['car'])
def create_car(message):
    try:
        # Получение аргументов команды
        args = message.text.split()[1:]  # Пример команды: /car красная BMW
        if len(args) == 2:
            color = args[0]
            brand = args[1]
            # Создание экземпляра класса Car
            car = Car(color, brand)
            # Отправка информации о машине
            bot.reply_to(message, car.info())
        else:
            bot.reply_to(message, "Пожалуйста, введите цвет и марку машины. Пример: /car красная BMW")
    except Exception as e:
        bot.reply_to(message, "Произошла ошибка, попробуйте снова.")

# Обработчик всех других сообщений с текстом
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

# Обработчик сообщений с фото
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.reply_to(message, "Отличное фото! Я его получил.")

bot.infinity_polling()
