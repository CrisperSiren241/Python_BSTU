import telebot
import json

bot = telebot.TeleBot('7165164543:AAG_Y2odqhmcTKuQkpg1J_Kq0x13eMITWbg')

with open('faq.json', 'r', encoding='utf-8') as faq_file:
    faq_data = json.load(faq_file)

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    text = message.text.lower()
    for question, keywords in faq_data.items():
        if any(keyword in text for keyword in keywords):
            bot.send_message(message.chat.id, question)
            return
    bot.send_message(message.chat.id, "Здравствуйте, я BookHubBot. Пожалуйста, уточните или напишите вопрос, чтобы я мог ответить на него!")
    
bot.polling(none_stop=True)