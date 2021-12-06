import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types
from helpers import *
bot = telebot.TeleBot("5043926452:AAFLpliMElJViSDo9bOZ-tGluKjmBJ4CCg0", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['menu'])
def echo_all(message):
    bot.send_message(message.chat.id, text)
@bot.message_handler(commands=['start'])
def echo_all(message):
    bot.send_message(message.chat.id, 'Hello. This bot will find you all kinds of templates. Press /menu to select.')

links = []
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text[0] == '/':
        text = message.text[0:]
        text = text.replace(' ','-')
    else:
        text = message.text
        text = text.replace(' ','-')
    sahifa = f"https://www.free-css.com/template-categories/{text}"
    r = requests.get(sahifa)
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        get_three = soup.select('ul[class="clear"] li ')[:4]
        media = []
        links.clear()
        for i in get_three:
            links.append(i.select('a')[0]['href'])
            media.append(types.InputMediaPhoto('https://www.free-css.com' +  i.select('img')[0]['src']))
        markup = types.InlineKeyboardMarkup(row_width=2)
        print(links)
        itembtna = types.InlineKeyboardButton('1', callback_data=links[0])
        itembtna1 = types.InlineKeyboardButton('2', callback_data=links[1])
        itembtna2 = types.InlineKeyboardButton('3', callback_data=links[2])
        itembtna3 = types.InlineKeyboardButton('4', callback_data=links[3])
        markup.add(itembtna,itembtna1,itembtna2,itembtna3)
        bot.send_media_group(message.chat.id, media)
        bot.send_message(message.chat.id, 'Choose one', reply_markup=markup)
    except:
        bot.send_message(message.chat.id, 'Not found')
    
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    # 'https://www.free-css.com' + 
    # print('https://www.free-css.com' + call.data)
    sahifa2 = 'https://www.free-css.com' + call.data
    # sahifa2 = links[int(call.data)]
    r2 = requests.get(sahifa2)
    soup = BeautifulSoup(r2.text, 'html.parser')
    zip = 'https://www.free-css.com' +  soup.select('ul[class="clear"] li[class="dld"] a')[0]["href"]
    bot.send_document(call.from_user.id, zip)

bot.infinity_polling()
