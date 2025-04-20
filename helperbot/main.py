import telebot
import requests
import random

# Замени 'YOUR_TELEGRAM_BOT_TOKEN' на токен своего бота
bot = telebot.TeleBot('7846154698:AAHjHHkNXJ_WdTFE7OqmXWeDpiRtoBHN1Bk')
advics = ["экономь энергию,выключай свет когда не нужен", "покупай меньше одноразового пластика🛒", "Сортируй отходы и перерабатывай♻️ ", "Поддерживай глобальные и местные инициативы🌍"]
def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Привет! Я бот-помошник,который может тебе дать советы для сохранения природы и замедления процесса глобальное потепление,напиши команду /advice чтобы узнать как помочь природе")

@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде /duck возвращает фото утки'''
    image_url = get_duck_image_url()
    bot.send_message(message.chat.id, image_url)

@bot.message_handler(commands=['advice'])
def advices(message):
    bot.send_message(message.chat.id, random.choice(advics))
# Запускаем бота
bot.polling()