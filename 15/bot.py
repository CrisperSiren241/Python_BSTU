import telebot
from telebot import types

bot = telebot.TeleBot('7006580648:AAEUslP6hjRf7grCdAMHQQInuyAAsEAfHbQ')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("О чем игра")
    item2 = types.KeyboardButton("С помощью чего разрабатывалась игра")
    item3 = types.KeyboardButton("Правила игры")
    item4 = types.KeyboardButton("Кем разработана игра")

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный для игры.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Кнопка 1':
        bot.send_message(message.chat.id, 'Это игра об игре')
    elif message.text == 'Кнопка 2':
        bot.send_message(message.chat.id, 'С помощью библиотеки PyGame')
    elif message.text == 'Кнопка 3':
        bot.send_message(message.chat.id, 'Вы нажали на кнопку 3')
    elif message.text == 'Кнопка 4':
        bot.send_message(message.chat.id, 'Вы нажали на кнопку 4')
    else:
        bot.send_message(message.chat.id, 'Я не понимаю, что вы хотите сделать.')

bot.polling(none_stop=True)
