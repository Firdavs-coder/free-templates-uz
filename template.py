import requests
from bs4 import BeautifulSoup
import telebot
import random
from telebot import types
from helpers import *
from data import *
import random
# bot = telebot.TeleBot("5042865364:AAH4Tndi4n_vawDY9sXyEUlS4omPIePaVT4", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
bot = telebot.TeleBot("5043926452:AAFLpliMElJViSDo9bOZ-tGluKjmBJ4CCg0", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

all_data1 = []

# start matni
start_Text = """
🇺🇿 Assalomu alaykum bu bot sizga minglab turdagi shablonlarni bepul topishingiz mumkin. Foydalanish uchun kanalga a'zo bo'ling.
🇺🇸 Hello. This bot will find you all kinds of templates. Please, subscribe for using.
"""

# templatelar alfabeti
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
    l = types.KeyboardButton ('L')
    m = types.KeyboardButton ('M')
    n = types.KeyboardButton ('N')
    o = types.KeyboardButton ('O')
    p = types.KeyboardButton ('P')
    r = types.KeyboardButton ('R')
    s = types.KeyboardButton ('S')
    t = types.KeyboardButton ('T')
    w = types.KeyboardButton ('W')
    a48 = types.KeyboardButton ('🔙 Back')
    return markup_reply.add(a,b,c,d,e,f,g,h,i,j,l,m,n,o,p,r,s,t,w,a48)

# asosiy ReplyKeyboardMarkup tugmalari
def home():
    markup_reply = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    a = types.KeyboardButton('Templates')
    b = types.KeyboardButton ('API')
    return markup_reply.add(a,b)


# start buyrug'i handleri
@bot.message_handler(commands=['start'])
def echo_all(message):
    save_users(message)
    markup = types.InlineKeyboardMarkup(row_width=1)
    itembtna = types.InlineKeyboardButton('View channel', url='https://t.me/python_flutter_uz')
    itembtnv = types.InlineKeyboardButton('Check', callback_data='check')
    markup.add(itembtna, itembtnv)
    bot.send_message(message.chat.id, start_Text,reply_markup=markup)

# subs buyrug'i handleri 
@bot.message_handler(commands=['subs'])
def start(message):
    save_users(message)
    if message.from_user.username == 'shavkatNor':
        res = requests.get("https://telegrambotbazasi.pythonanywhere.com//view_fr_users")
        subs = res.json()['subscribes_count']
        bot.send_message(message.chat.id, f"Obunachilaringiz <b>{subs}</b> ta", parse_mode='HTML')

# matnni ushlash (assosiy funksiya)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    save_users(message)
    result_text2 = """"""
    if subs_to_channel(message.chat.id):  
        if len(message.text) == 1:
            for i in inf:
                if i.lower().startswith(str(message.text).lower()):
                    result_text2+='/'+str(i).lower().replace(' ','-').replace('-','_') + '\n'
            if result_text2:
                bot.send_message(message.chat.id, result_text2)
            else:
                bot.send_message(message.chat.id,'🇺🇿 Topilmadi 😌\n🇺🇸 Not found 😌')
        elif message.text == '🔙 Back':
            bot.send_message(message.chat.id,"Choose", reply_markup=home())
        elif message.text == 'Templates':
            bot.send_message(message.chat.id,"Choose", reply_markup=alphabet())
        elif message.text == "API":
            markup_reply = types.ReplyKeyboardMarkup(row_width=2)
            a1 = types.KeyboardButton ('Animals')
            a2 = types.KeyboardButton ('Anime')
            a3 = types.KeyboardButton ('Anti-Malware')
            a4 = types.KeyboardButton ('Art & Design')
            a5 = types.KeyboardButton ('Authentication & Authorization')
            a6 = types.KeyboardButton ('Blockchain')
            a7 = types.KeyboardButton ('Books')
            a8 = types.KeyboardButton ('Business')
            a9 = types.KeyboardButton ('Calendar')
            a10 = types.KeyboardButton ('Cloud Storage & File Sharing')
            a11 = types.KeyboardButton ('Continuous Integration')
            a12 = types.KeyboardButton ('Cryptocurrency')
            a13 = types.KeyboardButton ('Currency Exchange')
            a14 = types.KeyboardButton ('Data Validation')
            a15 = types.KeyboardButton ('Development')
            a16 = types.KeyboardButton ('Dictionaries')
            a17 = types.KeyboardButton ('Documents & Productivity')
            a18 = types.KeyboardButton ('Email')
            a19 = types.KeyboardButton ('Entertainment')
            a20 = types.KeyboardButton ('Events')
            a21 = types.KeyboardButton ('Finance')
            a22 = types.KeyboardButton ('Food & Drink')
            a23 = types.KeyboardButton ('Games & Comics')
            a24 = types.KeyboardButton ('Geocoding')
            a25 = types.KeyboardButton ('Government')
            a26 = types.KeyboardButton ('Health')
            a27 = types.KeyboardButton ('Jobs')
            a28 = types.KeyboardButton ('Machine Learning')
            a29 = types.KeyboardButton ('Music')
            a30 = types.KeyboardButton ('News')
            a31 = types.KeyboardButton ('Personality')
            a32 = types.KeyboardButton ('Phone')
            a33 = types.KeyboardButton ('Photography')
            a34 = types.KeyboardButton ('Programming')
            a35 = types.KeyboardButton ('Science & Math')
            a36 = types.KeyboardButton ('Security')
            a37 = types.KeyboardButton ('Shopping')
            a38 = types.KeyboardButton ('Social')
            a39 = types.KeyboardButton ('Sports & Fitness')
            a40 = types.KeyboardButton ('Test Data')
            a41 = types.KeyboardButton ('Text Analysis')
            a42 = types.KeyboardButton ('Tracking')
            a43 = types.KeyboardButton ('Transportation')
            a44 = types.KeyboardButton ('URL Shorteners')
            a45 = types.KeyboardButton ('Vehicle')
            a46 = types.KeyboardButton ('Video')
            a47 = types.KeyboardButton ('Weather')
            a48 = types.KeyboardButton ('🔙 Back')
            markup_reply.add(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37,a38,a39,a40,a41,a42,a43,a44,a45,a46,a47,a48)
            bot.send_message(message.chat.id,"🇺🇸 Choose one category\n🇺🇿 Bitta kategoriya tanlang", reply_markup=markup_reply)
        
        try:
            if apis[str(message.text).replace(" ","_")]:
                one_api = random.choice(apis[(message.text).replace(" ","_")])
                full_one_api_data = f"""🔗 <b>API</b>: {one_api['API']}\n🗒 <b>Description</b>: {one_api['Description']}\n🙎 <b>Auth</b>: {one_api['Auth']}\n⛓ <b>HTTPS</b>: {one_api['HTTPS']}\n✅ <b>Cors</b>: {one_api['Cors']}\n👉 <b>Link</b>: {one_api['Link']}\n📂 <b>Category</b>: {one_api['Category']}"""
                markup = types.InlineKeyboardMarkup(row_width=1)
                itembtna = types.InlineKeyboardButton('Random else', callback_data=f'{(message.text).replace(" ","_")}')
                markup.add(itembtna)
                bot.send_message(message.chat.id,full_one_api_data,reply_markup=markup, parse_mode='HTML')
        except:
            if message.text[0] == '/':
                text = message.text[0:]
                text = text.replace(' ','-').replace('_','-')
                sahifa = f"https://www.free-css.com/template-categories/{text}"
                r = requests.get(sahifa)
                soup = BeautifulSoup(r.text, 'html.parser')
                try:
                    get_three = soup.select('ul[class="clear"] li ')[:10]
                    result_text = """"""
                    all_data1.clear()
                    for i in get_three:
                        all_data1.append(list((str(i.select('a')[0]['href']).replace("/free-css-templates",''),str(i.select('span[class="name"]')[0].text))))
                    random.shuffle(all_data1)
                    all_data2 = all_data1[:10]
                    for i in all_data2:
                        result_text += '✅ '+ i[1] + '\n' 
                    markup = types.InlineKeyboardMarkup(row_width=5)
                    itembtna = types.InlineKeyboardButton('1', callback_data=all_data2[0][0])
                    itembtna1 = types.InlineKeyboardButton('2', callback_data=all_data2[1][0])
                    itembtna2 = types.InlineKeyboardButton('3', callback_data=all_data2[2][0])
                    itembtna3 = types.InlineKeyboardButton('4', callback_data=all_data2[3][0])
                    itembtna4 = types.InlineKeyboardButton('5', callback_data=all_data2[4][0])
                    itembtna5 = types.InlineKeyboardButton('6', callback_data=all_data2[5][0])
                    itembtna6 = types.InlineKeyboardButton('7', callback_data=all_data2[6][0])
                    itembtna7 = types.InlineKeyboardButton('8', callback_data=all_data2[7][0])
                    itembtna8 = types.InlineKeyboardButton('9', callback_data=all_data2[8][0])
                    itembtna9 = types.InlineKeyboardButton('10', callback_data=all_data2[9][0])
                    markup.add(itembtna,itembtna1,itembtna2,itembtna3,itembtna4,itembtna5,itembtna6,itembtna7,itembtna8,itembtna9,)
                    bot.send_message(message.chat.id, result_text, reply_markup=markup)
                except:
                    bot.send_message(message.chat.id, '🇺🇿 Topilmadi 😌\n🇺🇸 Not found 😌')
    
    else:
        pass

# reklama tarqatish funksiyasi
def add_recline(message):
    if message.from_user.username == 'shavkatNor' and message.caption:
        res = requests.get("https://telegrambotbazasi.pythonanywhere.com/view_fr_users")
        users = res.json()['data']
        for i in users:
            id = i['name']
            try:
                bot.forward_message(int(id),message.chat.id,message.message_id)
            except:
                res = requests.get(f"https://telegrambotbazasi.pythonanywhere.com/templates/delete/{id}")

# userlarni saqlash funksiyasi
def save_users(message):
    id = message.from_user.id
    ok = requests.get(f"https://telegrambotbazasi.pythonanywhere.com/templates/add/{id}")

# kanalga azo bolganligini tekshirish funksiyasi
def subs_to_channel(id):
    subscribe = bot.get_chat_member(chat_id=-1001373178208, user_id=id).status
    if subscribe == 'creator' or subscribe == 'member' or subscribe == 'administrator':
        return True
    else:
        bot.send_message(id, "🇺🇿 Kanalga a'zo bo'ling. 👉 @python_flutter_uz.\n🇺🇸 Please subscribe to channel. 👉 @python_flutter_uz") 
        return False

# call back querylarni ushlash funksiyasi
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if subs_to_channel(call.from_user.id):
        try:
            if apis[(call.data).replace(" ","_")]:
                bot.delete_message(call.from_user.id,call.message.id)
                one_api = random.choice(apis[(call.data).replace(" ","_")])
                full_one_api_data = f"""🔗 <b>API</b>: {one_api['API']}\n🗒 <b>Description</b>: {one_api['Description']}\n🙎 <b>Auth</b>: {one_api['Auth']}\n⛓ <b>HTTPS</b>: {one_api['HTTPS']}\n✅ <b>Cors</b>: {one_api['Cors']}\n👉 <b>Link</b>: {one_api['Link']}\n📂 <b>Category</b>: {one_api['Category']}"""
                markup = types.InlineKeyboardMarkup(row_width=1)
                itembtna = types.InlineKeyboardButton('Random else', callback_data=f'{(call.data).replace(" ","_")}')
                markup.add(itembtna)
                bot.send_message(call.from_user.id,full_one_api_data,reply_markup=markup, parse_mode='HTML')
        except:
            pass
        if call.data =='check':
            subscribe = bot.get_chat_member(chat_id=-1001373178208, user_id=call.from_user.id).status
            if subscribe == 'creator' or subscribe == 'member' or subscribe == 'administrator':
                bot.send_message(call.from_user.id, "🇺🇿 Botdan bemalol foydalanishingiz mumkin ✅.\n🇺🇸 Succesfuly checked ✅.", reply_markup=home())
            else:
                bot.send_message(call.from_user.id, "🇺🇿 Kanalga a'zo bo'ling. 👉 @python_flutter_uz.\n🇺🇸 Please subscribe to channel. 👉 @python_flutter_uz") 
        else:
            sahifa2 = 'https://www.free-css.com/free-css-templates' + call.data
            r2 = requests.get(sahifa2)
            soup = BeautifulSoup(r2.text, 'html.parser')
            zip = 'https://www.free-css.com' +  soup.select('ul[class="clear"] li[class="dld"] a')[0]["href"]
            bot.send_document(call.from_user.id, zip)
    else:
        pass

# video larni ushlash handleri
@bot.message_handler(content_types=['video'])
def video(message):
    if message.from_user.username == 'shavkatNor' and message.caption:
        add_recline(message)

# rasmlarni ushlash handleri
@bot.message_handler(content_types=['photo'])
def photo(message):
    if message.from_user.username == 'shavkatNor' and message.caption:
        add_recline(message)

# cheksizlik funksiyasi
bot.infinity_polling()

