import telebot
import random
from telebot import types

TOKEN = '6198116251:AAFLdJffE_aWcsNsa2YNwn6foyC24vbe2AA'


bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Как вступить в ваш канал?")
    item2 = types.KeyboardButton("Как получить промокод?")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ − <b>{1.first_name}</b>. \nЧем могу быть вам полезен?".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Как вступить в ваш канал?':
            markup = types.InlineKeyboardMarkup()
            item = types.InlineKeyboardButton("Перейти", url = 'https://t.me/+HkACG1aipp44NDA6')
            markup.add(item)
            bot.send_message(message.chat.id, "Для того чтобы вступить в наш закрытый телеграмм-канал перейдите по ссылке:".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)
        elif message.text == 'Как получить промокод?':
            bot.send_message(message.chat.id,"Один или несколько раз в день в нашем телеграмм канале появляются посты с сылками(которые можно активировать только <strong>ОДИН</strong> раз). \nПерейдя по ссылке вас автоматически перекинет в бравл старс и вы сможете забрать свою награду.".format(message.from_user,bot.get_me()),parse_mode='html')
        else:
            bot.send_message(message.chat.id,"Извините, я не могу ответить на ваш запрос.".format(message.from_user, bot.get_me()),parse_mode='html')


bot.polling(none_stop=True)