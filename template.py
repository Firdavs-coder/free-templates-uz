import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types
from helpers import *
# bot = telebot.TeleBot("5042865364:AAH4Tndi4n_vawDY9sXyEUlS4omPIePaVT4", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
bot = telebot.TeleBot("5043926452:AAFLpliMElJViSDo9bOZ-tGluKjmBJ4CCg0", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
start_Text = """
🇺🇿 Assalomu alaykum bu bot sizga minglab turdagi shablonlarni bepul topishingiz mumkin. Foydalanish uchun kanalga a'zo bo'ling.
🇺🇸 Hello. This bot will find you all kinds of templates. Please, subscribe for using.
"""
def alphabet():
    markup_reply = types.ReplyKeyboardMarkup(row_width=5)
    a = types.KeyboardButton('A')
    b = types.KeyboardButton ('B')
    c = types.KeyboardButton ('C')
    d = types.KeyboardButton ('D')
    e = types.KeyboardButton ('E')
    f = types.KeyboardButton ('F')
    g = types.KeyboardButton ('G')
    h = types.KeyboardButton ('H')
    i = types.KeyboardButton ('I')
    j = types.KeyboardButton ('J')
    k = types.KeyboardButton ('K')
    l = types.KeyboardButton ('L')
    m = types.KeyboardButton ('M')
    n = types.KeyboardButton ('N')
    o = types.KeyboardButton ('O')
    p = types.KeyboardButton ('P')
    q = types.KeyboardButton ('Q')
    r = types.KeyboardButton ('R')
    s = types.KeyboardButton ('S')
    t = types.KeyboardButton ('T')
    u = types.KeyboardButton ('U')
    v = types.KeyboardButton ('V')
    w = types.KeyboardButton ('W')
    x = types.KeyboardButton ('X')
    y = types.KeyboardButton ('Y')
    z = types.KeyboardButton ('Z')
    return markup_reply.add(
            a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z
            )
@bot.message_handler(commands=['start'])
def echo_all(message):
    add_file(message)
    markup = types.InlineKeyboardMarkup(row_width=1)
    itembtna = types.InlineKeyboardButton('View channel', url='https://t.me/python_flutter_uz')
    itembtnv = types.InlineKeyboardButton('Check', callback_data='check')
    markup.add(itembtna, itembtnv)
    bot.send_message(message.chat.id, start_Text,reply_markup=markup)

def add_file(message):
    with open('users.py','rt') as f:
        classNames = f.read().rstrip('\n').split('\n')
    if  not str(message.from_user.id) in classNames:
        classNames.append(message.from_user.id)
        id = """"""
        for i in classNames:
            id+=str(i)+'\n'
        print(id)
        with open('users.py','w') as fayl:
            fayl.write(id)     
@bot.message_handler(commands=['subs'])
def subs(message):
    with open('users.py','rt') as f:
        classNames = f.read().rstrip('\n').split('\n')
    bot.send_message(message.chat.id,'<b>'+str(len(classNames))+'</b>' +' obunachilar',parse_mode='HTML')
links = []
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    add_file(message)
    result_text2 = """"""
    if subs_to_channel(message.chat.id):  
        if len(message.text) == 1:
            for i in inf:
                if i.lower().startswith(str(message.text).lower()):
                    result_text2+='/'+str(i).lower().replace(' ','-') + '\n'
            if result_text2:
                bot.send_message(message.chat.id, result_text2)
            else:
                bot.send_message(message.chat.id,'Not Found')
        else:
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
                get_three = soup.select('ul[class="clear"] li ')[:10]
                result_text = """"""
                links.clear()
                for i in get_three:
                    links.append(str(i.select('a')[0]['href']).replace("/free-css-templates",''))
                    result_text += '✅ '+ str(i.select('span[class="name"]')[0].text) + '\n' 
                markup = types.InlineKeyboardMarkup(row_width=5)
                itembtna = types.InlineKeyboardButton('1', callback_data=links[0])
                itembtna1 = types.InlineKeyboardButton('2', callback_data=links[1])
                itembtna2 = types.InlineKeyboardButton('3', callback_data=links[2])
                itembtna3 = types.InlineKeyboardButton('4', callback_data=links[3])
                itembtna4 = types.InlineKeyboardButton('5', callback_data=links[4])
                itembtna5 = types.InlineKeyboardButton('6', callback_data=links[5])
                itembtna6 = types.InlineKeyboardButton('7', callback_data=links[6])
                itembtna7 = types.InlineKeyboardButton('8', callback_data=links[7])
                itembtna8 = types.InlineKeyboardButton('9', callback_data=links[8])
                itembtna9 = types.InlineKeyboardButton('10', callback_data=links[9])
                markup.add(itembtna,itembtna1,itembtna2,itembtna3,itembtna4,itembtna5,itembtna6,itembtna7,itembtna8,itembtna9,)
                bot.send_message(message.chat.id, result_text, reply_markup=markup)
            except:
                bot.send_message(message.chat.id, 'Not found')
    else:
        pass
def add_recline(message):
    with open('users.py','rt') as f:
        classNames = f.read().rstrip('\n').split('\n')
    if message.from_user.username == 'shavkatNor' and message.caption:
        for i in classNames:
            try:
                bot.forward_message(int(i),message.chat.id,message.message_id)
            except:
                classNames.remove(str(i))
                id = """"""
                for i in classNames:
                    id+=str(i)+'\n'
                with open('users.py','w') as fayl:
                    fayl.write(id) 
def subs_to_channel(id):
    subscribe = bot.get_chat_member(chat_id=-1001373178208, user_id=id).status
    if subscribe == 'creator' or subscribe == 'member' or subscribe == 'administrator':
        return True
    else:
        bot.send_message(id, "👉 Please subscribe to channel.\n@python_flutter_uz") 
        return False
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if subs_to_channel(call.from_user.id):
        if call.data =='check':
            subscribe = bot.get_chat_member(chat_id=-1001373178208, user_id=call.from_user.id).status
            if subscribe == 'creator' or subscribe == 'member' or subscribe == 'administrator':
                bot.send_message(call.from_user.id, "✅ Succesfuly checked.", reply_markup=alphabet())
            else:
                bot.send_message(call.from_user.id, "👉 Please subscribe to channel.\n@python_flutter_uz") 
        else:
            sahifa2 = 'https://www.free-css.com/free-css-templates' + call.data
            r2 = requests.get(sahifa2)
            soup = BeautifulSoup(r2.text, 'html.parser')
            zip = 'https://www.free-css.com' +  soup.select('ul[class="clear"] li[class="dld"] a')[0]["href"]
            bot.send_document(call.from_user.id, zip)
    else:
        pass
@bot.message_handler(content_types=['video'])
def video(message):
    add_file(message)
    if message.from_user.username == 'shavkatNor' and message.caption:
        bot.forward_message(-1001698572718, message.chat.id, message.message_id)
        add_recline(message)
@bot.message_handler(content_types=['photo'])
def photo(message):
    add_file(message)
    if message.from_user.username == 'shavkatNor' and message.caption:
        bot.forward_message(-1001698572718, message.chat.id, message.message_id)
        add_recline(message)
bot.infinity_polling()