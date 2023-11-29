import telebot
bot = telebot.TeleBot('6644995464:AAE3u9XafF8l66uEZaEv2JTFp0xdyIeG-rQ')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Сообщение')

@bot.message_handler(commands=['play'])
def main(message):
    bot.send_message(message.chat.id, 'игры \nигры')

@bot.message_handler(commands=['subscribe'])
def main(message):
    bot.send_message(message.chat.id, '_Подпишись на канал_[ссылка](https://t.me/+7VEOklx7yDcxNzcy)')

bot.infinity_polling()