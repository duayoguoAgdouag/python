#import telebot

#bot = telebot.TeleBot('1562265923:AAE9dmWmFOIdSNEMewZXLB4pPQ1Y4gJHvyo')

#keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
#keyboard1.row('привет', 'пока')


#@bot.message_handler(commands=['start'])
#def start_message(message):
#    bot.send_message(message.chat.id, 'ты активировал меня', reply_markup=keyboard1)


#@bot.message_handler(content_types=['text'])

#def send_text(message):
#    if message.text.lower() == 'привет':
#        bot.send_message(message.chat.id, 'Привет,привет')
#    elif message.text.lower() == 'пока':
#        bot.send_message(message.chat.id, 'пока')
#    elif message.text.lower() == 'я тебя люблю':
#        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')

#bot.polling()
