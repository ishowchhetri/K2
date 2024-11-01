import telebot,os
import re,json
import requests
import telebot,time,random
import random
import string
from telebot import types
from gates import *
from reg import reg
from datetime import datetime, timedelta
from faker import Faker
from multiprocessing import Process
import threading

import threading
import time
from telebot import types

stopuser = {}
token = "7608548081:AAEOnsjLSN_JH07fKVECU0mAkDSKwcOt9IM"
bot=telebot.TeleBot(token,parse_mode="HTML")


admin=6938095972

myid = ['6938095972']

admins = ['6938095972']

command_usage = {}
def reset_command_usage():
	for user_id in command_usage:
		command_usage[user_id] = {'count': 0, 'last_time': None}
@bot.message_handler(commands=["start"])
def start(message):
	def my_function():
		gate=''
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𓆩 𝐅𝐫𝐞𝐞 𓆪ꪾ'
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𓆩 𝐅𝐫𝐞𝐞 𓆪ꪾ",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
		if BL == '𓆩 𝐅𝐫𝐞𝐞 𓆪ꪾ':	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓 ❤‍🩹", url="https://t.me/iShowSandesheyyyyy")
			keyboard.add(contact_button)
			video_url = 'https://t.me/IShowCloud/5'
			bot.send_video(
    chat_id=message.chat.id,
    video=video_url,
    caption=f'''<b>♻️ 𝑨𝒉𝒉 𝑵𝒊𝒈𝒈𝒂 {name}!
━━━━━━━━━━━━━ 
🌟├𝒀𝒐𝒖𝒓 𝑹𝒂𝒏𝒌: 𓆩 𝑭𝒓𝒆𝒆 𓆪ꪾ 💔 
🌟├𝑩𝒖𝒚 𝑻𝒉𝒆 𝑷𝒓𝒆𝒎𝒊𝒖𝒎 𝑭𝒓𝒐𝒎 𝑴𝒚 𝑴𝒂𝒔𝒕𝒆𝒓
━━━━━━━━━━━━━ 
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [ 𝑴𝒂𝒔𝒕𝒆𝒓 ]</b>''',
    reply_markup=keyboard
)

			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="𝑷𝒐𝒘𝒆𝒓𝒆𝒅 𝑩𝒚 ❤‍🩹", url="https://t.me/TeamRedEye")
		keyboard.add(contact_button)
		username = message.from_user.first_name
		video_url = 'https://t.me/IShowCloud/5'
		bot.send_video(
    chat_id=message.chat.id,
    video=video_url,
    caption=f'''<strong>♻️ 𝑨𝒉𝒉 𝑵𝒊𝒈𝒈𝒂 {name} !
━━━━━━━━━━━━━
🌟├𝒀𝒐𝒖𝒓 𝑹𝒂𝒏𝒌 -> 𓆩 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𓆪ꪾ
🌟├𝑮𝒂𝒕𝒆𝒘𝒂𝒚𝒔 -> /cmds
🌟├𝑺𝒆𝒏𝒅 𝒀𝒐𝒖𝒓 𝑪𝒐𝒎𝒃𝒐 𝑭𝒐𝒓 𝑴𝒂𝒔𝒔 𝑪𝒉𝒆𝒄𝒌  
━━━━━━━━━━━━━
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</strong>''',
    reply_markup=keyboard
)
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["cmds"])
def start(message):
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	id=message.from_user.id
	try:BL=(json_data[str(id)]['plan'])
	except:
		BL='𓆩 𝐅𝐫𝐞𝐞 𓆪ꪾ'
	name = message.from_user.first_name
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text=f"𝐑𝐚𝐧𝐤 -> {BL} ",callback_data='plan')
	keyboard.add(contact_button)
	bot.send_message(chat_id=message.chat.id, text='''<b> 
♻️ 𝑴𝒚 𝑪𝒐𝒎𝒎𝒂𝒏𝒅𝒔 ━━━━━━━━━━━━━━━━━━━ 
🌟├ 𝑵𝒂𝒎𝒆: Braintree Auth 1
🌟├ 𝑭𝒐𝒓𝒎𝒂𝒕: /chk credit_card
🌟├ 𝑪𝒐𝒏𝒅𝒊𝒕𝒊𝒐𝒏: ON! ✅ 
🌟├ 𝑻𝒚𝒑𝒆: 𓆩 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𓆪ꪾ ━━━━━━━━━━━━━━━━━━━ 
🌟├ 𝑵𝒂𝒎𝒆: Stripe Auth 1
🌟├ 𝑭𝒐𝒓𝒎𝒂𝒕: /sa credit_card
🌟├ 𝑪𝒐𝒏𝒅𝒊𝒕𝒊𝒐𝒏: ON! ✅ 
🌟├ 𝑻𝒚𝒑𝒆: 𓆩 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𓆪ꪾ ━━━━━━━━━━━━━━━━━━━ 
🌟├ 𝑵𝒂𝒎𝒆: Braintree Auth 2
🌟├ 𝑭𝒐𝒓𝒎𝒂𝒕: /b3 credit_card
🌟├ 𝑪𝒐𝒏𝒅𝒊𝒕𝒊𝒐𝒏: ON! ✅ 
🌟├ 𝑻𝒚𝒑𝒆: 𓆩 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𓆪ꪾ ━━━━━━━━━━━━━━━━━━━ 
🌟├ 𝑵𝒂𝒎𝒆: Stripe Auth 2
🌟├ 𝑭𝒐𝒓𝒎𝒂𝒕: /cc credit_card
🌟├ 𝑪𝒐𝒏𝒅𝒊𝒕𝒊𝒐𝒏: ON! ✅ 
🌟├ 𝑻𝒚𝒑𝒆: 𓆩 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𓆪ꪾ ━━━━━━━━━━━━━━━━━━━ 
🌟├ 𝑵𝒂𝒎𝒆: BIN Info Lookup
🌟├ 𝑭𝒐𝒓𝒎𝒂𝒕: /bin BIN
🌟├ 𝑪𝒐𝒏𝒅𝒊𝒕𝒊𝒐𝒏: ON! ✅ 
🌟├ 𝑻𝒚𝒑𝒆: 𓆩 𝑭𝒓𝒆𝒆 𓆪ꪾ  ━━━━━━━━━━━━━━━━━━━ 
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>
''',reply_markup=keyboard)
@bot.message_handler(content_types=["document"])
def main(message):
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𓆩 𝐅𝐫𝐞𝐞 𓆪ꪾ'
		if BL == '𓆩 𝐅𝐫𝐞𝐞 𓆪ꪾ':
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𓆩 𝐅𝐫𝐞𝐞 𓆪ꪾ",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓 ❤‍🩹", url="https://t.me/iShowSandesheyyyyy")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>♻️ 𝑨𝒉𝒉 𝑵𝒊𝒈𝒈𝒂 {name}!
━━━━━━━━━━━━━ 
🌟├𝒀𝒐𝒖𝒓 𝑹𝒂𝒏𝒌: 𓆩 𝑭𝒓𝒆𝒆 𓆪ꪾ 💔 
🌟├𝑩𝒖𝒚 𝑻𝒉𝒆 𝑷𝒓𝒆𝒎𝒊𝒖𝒎 𝑭𝒓𝒐𝒎 𝑴𝒚 𝑴𝒂𝒔𝒕𝒆𝒓 ━━━━━━━━━━━━━ 
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [ 𝑴𝒂𝒔𝒕𝒆𝒓 ]</b>''',reply_markup=keyboard)
			return
		with open('data.json', 'r') as file:
			json_data = json.load(file)
			date_str=json_data[str(id)]['timer'].split('.')[0]
		try:
			provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
		except Exception as e:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓 ❤‍🩹", url="https://t.me/iShowSandesheyyyyy")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>♻️ 𝑨𝒉𝒉 𝑵𝒊𝒈𝒈𝒂 {name}!
━━━━━━━━━━━━━ 
🌟├𝒀𝒐𝒖𝒓 𝑹𝒂𝒏𝒌: 𓆩 𝑭𝒓𝒆𝒆 𓆪ꪾ 💔 
🌟├𝑩𝒖𝒚 𝑻𝒉𝒆 𝑷𝒓𝒆𝒎𝒊𝒖𝒎 𝑭𝒓𝒐𝒎 𝑴𝒚 𝑴𝒂𝒔𝒕𝒆𝒓 ━━━━━━━━━━━━━ 
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [ 𝑴𝒂𝒔𝒕𝒆𝒓 ]</b>''',reply_markup=keyboard)
			return
		current_time = datetime.now()
		required_duration = timedelta(hours=0)
		if current_time - provided_time > required_duration:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓 ❤‍🩹", url="https://t.me/iShowSandesheyyyyy")
			keyboard.add(contact_button)
			bot.send_message(
    chat_id=message.chat.id, 
    text='''<b>🥷 𝒀𝒐𝒖𝒓 𝑺𝒖𝒃𝒔𝒄𝒓𝒊𝒑𝒕𝒊𝒐𝒏 𝒉𝒂𝒔 𝑬𝒙𝒑𝒊𝒓𝒆𝒅 
━━━━━━━━━━━━━
- ❌ 𝒀𝒐𝒖 𝒄𝒂𝒏𝒏𝒐𝒕 𝒖𝒔𝒆 𝒕𝒉𝒆 𝒃𝒐𝒕 𝒃𝒆𝒄𝒂𝒖𝒔𝒆 𝒚𝒐𝒖𝒓 𝒔𝒖𝒃𝒔𝒄𝒓𝒊𝒑𝒕𝒊𝒐𝒏 𝒉𝒂𝒔 𝒆𝒙𝒑𝒊𝒓𝒆𝒅. 

- 𝑩𝒖𝒚 𝒕𝒉𝒆 𝒃𝒐𝒕 𝒔𝒖𝒃𝒔𝒄𝒓𝒊𝒑𝒕𝒊𝒐𝒏 𝒂𝒈𝒂𝒊𝒏 𝒃𝒚 𝒔𝒆𝒏𝒅𝒊𝒏𝒈 /buy
━━━━━━━━━━━━━
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>''', 
    parse_mode='HTML', 
    reply_markup=keyboard
)
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			json_data[str(id)]['timer'] = 'none'
			json_data[str(id)]['paln'] = '𓆩 𝐅𝐫𝐞𝐞 𓆪ꪾ'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text=f"✨ 𝑩𝒓𝒂𝒊𝒏𝒕𝒓𝒆𝒆 𝑨𝒖𝒕𝒉 1",callback_data='br')
		sw = types.InlineKeyboardButton(text=f"♻️ 𝑺𝒕𝒓𝒊𝒑𝒆 𝑨𝒖𝒕𝒉 2",callback_data='br2')
		b3 = types.InlineKeyboardButton(text=f"✨ 𝑩𝒓𝒂𝒊𝒏𝒕𝒓𝒆𝒆 𝑨𝒖𝒕𝒉 2",callback_data='br3')
		sa = types.InlineKeyboardButton(text=f"♻️ 𝑺𝒕𝒓𝒊𝒑𝒆 𝑨𝒖𝒕𝒉 1",callback_data='br4')
		#m = types.InlineKeyboardButton(text=f"ϟ Moneris Cahrge 0.10$ ϟ️",callback_data='br4')
		#d = types.InlineKeyboardButton(text=f"ϟ Moneris Cahrge 0.10$ ϟ️",callback_data='br4')
		keyboard.add(contact_button)
		keyboard.add(sw)
		keyboard.add(b3)
		keyboard.add(sa)
		#keyboard.add(m)
		#keyboard.add(d)
		bot.reply_to(
    message,
    text=(
        "<b>♻️ 𝑴𝒚 𝑮𝒂𝒕𝒆𝒘𝒂𝒚'𝒔.</b>\n"
        "━━━━━━━━━━━━━\n"
        "<b>🌟├ 𝑵𝒆𝒆𝒅 𝒄𝒐𝒎𝒃𝒐 𝒍𝒊𝒔𝒕.</b>\n"
        "<b>🌟├ 𝑴𝒂𝒔𝒔 𝑪𝒉𝒆𝒄𝒌𝒆𝒓 𝑾𝒊𝒕𝒉 𝑷𝒓𝒐𝒙𝒚.</b>\n"
        "<b>🌟├ 𝑺𝒆𝒍𝒆𝒄𝒕 𝒂 𝒈𝒂𝒕𝒆 𝒇𝒓𝒐𝒎 𝒃𝒆𝒍𝒐𝒘.</b>\n"
        "━━━━━━━━━━━━━\n"
        "<b>♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>"
    ),
    parse_mode='HTML',
    reply_markup=keyboard
)
		ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
		with open("combo.txt", "wb") as w:
			w.write(ee)
			
			
			
			

	
	
	
	
def dato(zh):
 
 

 
 
	try:
		api_url = requests.get("https://bins.antipublic.cc/bins/"+zh).json()
		brand=api_url["brand"]
		card_type=api_url["type"]
		level=api_url["level"]
		bank=api_url["bank"]
		country_name=api_url["country_name"]
		country_flag=api_url["country_flag"]
		mn = f'''𝗜𝗻𝗳𝗼 ⇾<code>{brand} - {card_type} - {level}</code>
𝐈𝐬𝐬𝐮𝐞𝐫 ⇾ <code>{bank}</code>
𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ⇾ <code>{country_name} [ {country_flag} ]</code>'''
		return mn
	except Exception as e:
		print(e)
		return '❌ 𝑼𝒏𝒂𝒃𝒍𝒆 𝒕𝒐 𝒈𝒆𝒕 𝒕𝒉𝒆 𝒊𝒏𝒇𝒐 𝒐𝒇 𝒕𝒉𝒆 𝒃𝒊𝒏.'
	
	
	







import threading
import time
from telebot import types

MAX_LINES = 1000
stopuser = {}  # To track the status of each user # Define variables to store the state of each gate # Define gate state variables
check_enabled_br1 = True
check_enabled_br2 = True
check_enabled_br3 = True
check_enabled_br4 = True



@bot.message_handler(commands=['on_B1'])
def enable_br1(message):
    global check_enabled_br1
    if str(message.from_user.id) in admins:
        check_enabled_br1 = True
        bot.reply_to(
            message,
            text=(
                "<b>♻️ 𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍.</b>\n"
                "━━━━━━━━━━━━━\n"
                "<b>🌟├ 𝑩𝒓𝒂𝒊𝒏𝒕𝒓𝒆𝒆 𝑨𝒖𝒕𝒉 1 𝑮𝒂𝒕𝒆 𝒘𝒂𝒔 𝒆𝒏𝒂𝒃𝒍𝒆𝒅.</b>\n"
                "━━━━━━━━━━━━━\n"
                "<b>♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>"
            ),
            parse_mode='HTML'
        )
    else:
        bot.reply_to(
            message,
            text="<b>𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌</b>",
            parse_mode="HTML"
        )

@bot.message_handler(commands=['off_B1'])
def disable_br1(message):
    global check_enabled_br1
    if str(message.from_user.id) in admins:
        check_enabled_br1 = False
        bot.reply_to(
            message,
            text=(
                "<b>♻️ 𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍.</b>\n"
                "━━━━━━━━━━━━━\n"
                "<b>🌟├ 𝑩𝒓𝒂𝒊𝒏𝒕𝒓𝒆𝒆 𝑨𝒖𝒕𝒉 1 𝑮𝒂𝒕𝒆 𝒘𝒂𝒔 𝒅𝒊𝒔𝒂𝒃𝒍𝒆.</b>\n"
                "━━━━━━━━━━━━━\n"
                "<b>♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>"
            ),
            parse_mode='HTML'
        )
    else:
        bot.reply_to(
            message,
            text="<b>𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌</b>",
            parse_mode="HTML"
        )

@bot.message_handler(commands=['on_S2'])
def enable_br2(message):
    global check_enabled_br2
    if str(message.from_user.id) in admins:
        check_enabled_br2 = True
        bot.reply_to(
            message,
            text=(
                "<b>♻️ 𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍.</b>\n"
                "━━━━━━━━━━━━━\n"
                "<b>🌟├ 𝑺𝒕𝒓𝒊𝒑𝒆 𝑨𝒖𝒕𝒉 2 𝑮𝒂𝒕𝒆 𝒘𝒂𝒔 𝒆𝒏𝒂𝒃𝒍𝒆𝒅.</b>\n"
                "━━━━━━━━━━━━━\n"
                "<b>♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>"
            ),
            parse_mode='HTML'
        )
    else:
        bot.reply_to(
            message,
            text="<b>𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌</b>",
            parse_mode="HTML"
        )

@bot.message_handler(commands=['off_S2'])
def disable_br2(message):
    global check_enabled_br2
    if str(message.from_user.id) in admins:
        check_enabled_br2 = False
        bot.reply_to(
            message,
            text=(
                "<b>♻️ 𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍.</b>\n"
                "━━━━━━━━━━━━━\n"
                "<b>🌟├ 𝑺𝒕𝒓𝒊𝒑𝒆 𝑨𝒖𝒕𝒉 2 𝑮𝒂𝒕𝒆 𝒘𝒂𝒔 𝒅𝒊𝒔𝒂𝒃𝒍𝒆.</b>\n"
                "━━━━━━━━━━━━━\n"
                "<b>♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>"
            ),
            parse_mode='HTML'
        )
    else:
        bot.reply_to(
            message,
            text="<b>𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌</b>",
            parse_mode="HTML"
        )

@bot.message_handler(commands=['on_B2'])
def enable_br3(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = True
        bot.reply_to(
            message,
            text=(
                "<b>♻️ 𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍.</b>\n"
                "━━━━━━━━━━━━━\n"
                "<b>🌟├ 𝑩𝒓𝒂𝒊𝒏𝒕𝒓𝒆𝒆 𝑨𝒖𝒕𝒉 2 𝑮𝒂𝒕𝒆 𝒘𝒂𝒔 𝒆𝒏𝒂𝒃𝒍𝒆𝒅.</b>\n"
                "━━━━━━━━━━━━━\n"
                "<b>♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>"
            ),
            parse_mode='HTML'
        )
    else:
        bot.reply_to(
            message,
            text="<b>𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌</b>",
            parse_mode="HTML"
        )

@bot.message_handler(commands=['off_B2'])
def disable_br3(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = False
        bot.reply_to(
            message,
            text=(
                "<b>♻️ 𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍.</b>\n"
                "━━━━━━━━━━━━━\n"
                "<b>🌟├ 𝑩𝒓𝒂𝒊𝒏𝒕𝒓𝒆𝒆 𝑨𝒖𝒕𝒉 2 𝑮𝒂𝒕𝒆 𝒘𝒂𝒔 𝒅𝒊𝒔𝒂𝒃𝒍𝒆.</b>\n"
                "━━━━━━━━━━━━━\n"
                "<b>♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>"
            ),
            parse_mode='HTML'
        )
    else:
        bot.reply_to(
            message,
            text="<b>𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌</b>",
            parse_mode="HTML"
        )

@bot.message_handler(commands=['on_S1'])
def enable_br4(message):
    global check_enabled_br4
    if str(message.from_user.id) in admins:
        check_enabled_br4 = True
        bot.reply_to(
            message,
            text=(
                "<b>♻️ 𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍.</b>\n"
                "━━━━━━━━━━━━━\n"
                "<b>🌟├ 𝑺𝒕𝒓𝒊𝒑𝒆 𝑨𝒖𝒕𝒉 1 𝑮𝒂𝒕𝒆 𝒘𝒂𝒔 𝒆𝒏𝒂𝒃𝒍𝒆𝒅.</b>\n"
                "━━━━━━━━━━━━━\n"
                "<b>♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>"
            ),
            parse_mode='HTML'
        )
    else:
        bot.reply_to(
            message,
            text="<b>𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌</b>",
            parse_mode="HTML"
        )

@bot.message_handler(commands=['off_S1'])
def disable_br4(message):
    global check_enabled_br4
    if str(message.from_user.id) in admins:
        check_enabled_br4 = False
        bot.reply_to(
            message,
            text=(
                "<b>♻️ 𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍.</b>\n"
                "━━━━━━━━━━━━━\n"
                "<b>🌟├ 𝑺𝒕𝒓𝒊𝒑𝒆 𝑨𝒖𝒕𝒉 1 𝑮𝒂𝒕𝒆 𝒘𝒂𝒔 𝒅𝒊𝒔𝒂𝒃𝒍𝒆.</b>\n"
                "━━━━━━━━━━━━━\n"
                "<b>♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>"
            ),
            parse_mode='HTML'
        )
    else:
        bot.reply_to(
            message,
            text="<b>𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌</b>",
            parse_mode="HTML"
        )




from telebot import types

# Define gate state variables
check_enabled_br1 = True
check_enabled_br2 = True
check_enabled_br3 = True
check_enabled_br4 = True

MAX_LINES = 1000

@bot.message_handler(commands=['loda'])
def show_menu(message):
    if str(message.from_user.id) in admins:
        markup = types.InlineKeyboardMarkup(row_width=1)
        toggle_br1 = 'Enable✅' if check_enabled_br1 else 'Disable❌'
        toggle_br2 = 'Enable✅' if check_enabled_br2 else 'Disable❌'
        toggle_br3 = 'Enable✅' if check_enabled_br3 else 'Disable❌'
        toggle_br4 = 'Enable✅' if check_enabled_br4 else 'Disable❌'
        toggle_ch1 = 'Enable✅' #if check_enabled_ch1 else 'Disable❌'
        
        br1_button = types.InlineKeyboardButton(f"Braintree Auth 1 ({toggle_br1})", callback_data='toggle_br1')
        br2_button = types.InlineKeyboardButton(f"Stripe Auth 2 ({toggle_br2})", callback_data='toggle_br2')
        br3_button = types.InlineKeyboardButton(f"Braintree Auth 2 ({toggle_br3})", callback_data='toggle_br3')
        br4_button = types.InlineKeyboardButton(f"Stripe Auth 1 ({toggle_br4})", callback_data='toggle_br4')
        limits_button = types.InlineKeyboardButton(f"Gate limits ({MAX_LINES})", callback_data='set_limits')
        
        markup.add(br1_button, br2_button, br3_button, br4_button, limits_button)
        bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)
    else:
        bot.send_message(
    chat_id=message.chat.id,
    text="<b>𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌</b>",
    parse_mode="HTML",
    reply_to_message_id=message.message_id
)


@bot.callback_query_handler(func=lambda call: call.data.startswith('toggle_') or call.data == 'set_limits')
def handle_toggle(call):
    global check_enabled_br1, check_enabled_br2, check_enabled_br3, check_enabled_br4, MAX_LINES
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    
    if call.data == 'toggle_br1':
        check_enabled_br1 = not check_enabled_br1
        status = 'Enable✅' if check_enabled_br1 else 'Disable❌'
        bot.answer_callback_query(call.id, f"Braintree Auth 1 is now {status}.")
    elif call.data == 'toggle_br2':
        check_enabled_br2 = not check_enabled_br2
        status = 'Enable✅' if check_enabled_br2 else 'Disable❌'
        bot.answer_callback_query(call.id, f"Stripe Auth 2 is now {status}.")
    elif call.data == 'toggle_br3':
        check_enabled_br3 = not check_enabled_br3
        status = 'Enable✅' if check_enabled_br3 else 'Disable❌'
        bot.answer_callback_query(call.id, f"Braintree Auth 2 is now {status}.")
    elif call.data == 'toggle_br4':
        check_enabled_br4 = not check_enabled_br4
        status = 'Enable✅' if check_enabled_br4 else 'Disable❌'
        bot.answer_callback_query(call.id, f"Stripe Auth 1 is now {status}.")
    elif call.data == 'set_limits':
        bot.send_message(chat_id, "Please enter the new limit value for Gate limits as /set_limit 1500")

    # Update the message to display the new status
    markup = types.InlineKeyboardMarkup(row_width=1)
    br1_button = types.InlineKeyboardButton(f"Braintree Auth 1 ({'Enable✅' if check_enabled_br1 else 'Disable❌'})", callback_data='toggle_br1')
    br2_button = types.InlineKeyboardButton(f"Stripe Auth 2 ({'Enable✅' if check_enabled_br2 else 'Disable❌'})", callback_data='toggle_br2')
    br3_button = types.InlineKeyboardButton(f"Braintree Auth 2 ({'Enable✅' if check_enabled_br3 else 'Disable❌'})", callback_data='toggle_br3')
    br4_button = types.InlineKeyboardButton(f"Stripe Auth 1 ({'Enable✅' if check_enabled_br4 else 'Disable❌'})", callback_data='toggle_br4')
   # ch1_button = types.InlineKeyboardButton(f"Braintree Charge 1 ({'Enable✅' if check_enabled_ch1 else 'Disable❌'})", callback_data='toggle_ch1')
    limits_button = types.InlineKeyboardButton(f"Gate limits ({MAX_LINES})", callback_data='set_limits')
    markup.add(br1_button, br2_button, br3_button, br4_button, limits_button)
    
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Choose an option:", reply_markup=markup)


@bot.message_handler(commands=['set_limit'])
def set_limit(message):
    global MAX_LINES
    
    if str(message.from_user.id) in admins:
        try:
            if len(message.text.split()) == 2 and message.text.split()[1].isdigit():
                new_limit = int(message.text.split()[1])
                MAX_LINES = new_limit
                bot.reply_to(message, f"Gate limit has been set to {MAX_LINES}.")
                show_menu(message)
            else:
                bot.reply_to(message, "Please use the correct format: /set_limit 1500.")
        except Exception as e:
            bot.reply_to(message, f"Error: {e}")
            print(f"Error: {e}")
    else:
        bot.reply_to(
            message,
            text="<b>𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌</b>",
            parse_mode="HTML"
        )



import threading
import time
from telebot import types

MAX_LINES = 1000
stopuser = {}
check_enabled = True

@bot.callback_query_handler(func=lambda call: call.data == 'br')
def menu_callback(call):
    id = str(call.from_user.id)

    if not check_enabled:
        bot.send_message(chat_id=call.message.chat.id, text="♻️ 𝑮𝒂𝒕𝒆𝒘𝒂𝒚 𝒊𝒔 𝒖𝒏𝒅𝒆𝒓 𝒎𝒂𝒊𝒏𝒕𝒆𝒏𝒂𝒏𝒄𝒆.. ")
        return

    if id not in stopuser:
        stopuser[id] = {'status': 'stopped'}

    if stopuser[id]['status'] == 'start':
        bot.send_message(
    chat_id=call.message.chat.id,
    text="""<b>❌ 𝑹𝒆𝒒𝒖𝒆𝒔𝒕 𝑭𝒂𝒊𝒍𝒆𝒅.</b>
━━━━━━━━━━━━━
<b>⚠️ 𝒀𝒐𝒖’𝒓𝒆 𝒂𝒍𝒓𝒆𝒂𝒅𝒚 𝒓𝒖𝒏𝒏𝒊𝒏𝒈 𝒂 𝒄𝒐𝒎𝒃𝒐 𝒄𝒉𝒆𝒄𝒌. 𝑷𝒍𝒆𝒂𝒔𝒆 𝒉𝒐𝒍𝒅 𝒕𝒊𝒈𝒉𝒕 𝒖𝒏𝒕𝒊𝒍 𝒊𝒕’𝒔 𝒄𝒐𝒎𝒑𝒍𝒆𝒕𝒆, 𝒐𝒓 𝒄𝒉𝒐𝒐𝒔𝒆 𝒕𝒐 𝒔𝒕𝒐𝒑 𝒕𝒉𝒆 𝒄𝒖𝒓𝒓𝒆𝒏𝒕 𝒔𝒆𝒔𝒔𝒊𝒐𝒏 𝒊𝒇 𝒏𝒆𝒆𝒅𝒆𝒅.</b>
━━━━━━━━━━━━━
<b>♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>""",
    parse_mode='HTML',
    reply_to_message_id=call.message.message_id
)

        return

    def my_function():
        gate = 'Braintree Auth 1'
        dd = 0
        live = 0
        cm = 0
        stopuser[id]['status'] = 'start'

        mes = types.InlineKeyboardMarkup(row_width=1)
        cm1 = types.InlineKeyboardButton("--------------", callback_data='u8')
        status = types.InlineKeyboardButton(f"--------------", callback_data='u8')
        cm3 = types.InlineKeyboardButton("--------------", callback_data='x')
        ccn = types.InlineKeyboardButton("--------------", callback_data='x')
        cm4 = types.InlineKeyboardButton("--------------", callback_data='x')
        cm5 = types.InlineKeyboardButton("--------------", callback_data='x')
        stop = types.InlineKeyboardButton("𝑺𝒕𝒐𝒑 𝑺𝒆𝒔𝒔𝒊𝒐𝒏 🔕", callback_data='stop')
        mes.add(cm1, status, cm3, ccn, cm4, cm5, stop)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="👁‍🗨 𝑪𝒐𝒏𝒇𝒊𝒈𝒖𝒓𝒊𝒏𝒈 𝒚𝒐𝒖𝒓 𝒄𝒐𝒎𝒃𝒐 𝒍𝒊𝒔𝒕, 𝑷𝒍𝒆𝒂𝒔𝒆 𝒘𝒂𝒊𝒕!\n━━━━━━━━━━━━━\n♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]", reply_markup=mes)

        try:
            with open("combo.txt", 'r') as file:
                lines = file.readlines()
                total_lines = len(lines)

                if total_lines > MAX_LINES:
                    bot.send_message(
                        chat_id=call.message.chat.id,
                        text=f"""<b>♻️ 𝑵𝒆𝒆𝒅 𝑪𝒐𝒓𝒓𝒆𝒄𝒕𝒊𝒐𝒏𝒔.</b>
━━━━━━━━━━━━━
<b>🌟├ 𝑩𝒂𝒅 𝑪𝒐𝒎𝒃𝒐.</b>
<b>🌟├ 𝑴𝒂𝒙 𝑪𝑪 𝑳𝒊𝒎𝒊𝒕 𝒊𝒔 {MAX_LINES} 💳</b>
<b>🌟├ 𝑬𝒅𝒊𝒕 𝒀𝒐𝒖𝒓 𝑭𝒊𝒍𝒆 & 𝑹𝒆𝒕𝒓𝒚.</b>
━━━━━━━━━━━━━
<b>♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>""",
                        parse_mode='HTML',
                        reply_to_message_id=call.message.message_id
                    )
                    stopuser[id]['status'] = 'stopped'
                    return

                for cc in lines:
                    if stopuser[id]['status'] == 'stop':
                        bot.send_message(
    chat_id=id,
    text="""<b>🔔 𝑵𝒐𝒕𝒊𝒇𝒊𝒄𝒂𝒕𝒊𝒐𝒏.</b>
━━━━━━━━━━━━━
<b>💳 𝑪𝒐𝒎𝒃𝒐 𝒄𝒉𝒆𝒄𝒌𝒊𝒏𝒈 𝒔𝒆𝒔𝒔𝒊𝒐𝒏𝒔 𝒔𝒕𝒐𝒑𝒑𝒆𝒅 𝒔𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍𝒚. ✅</b>
━━━━━━━━━━━━━
<b>♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>""",
    parse_mode='HTML'
)

                        stopuser[id]['status'] = 'stopped'
                        return
                    start_time = time.time()
                    try:
                        last = str(dexters(cc))
                        cm += 1
                    except Exception as e:
                        print(e)
                        last = "RISK: gateway_error"

                    mes = types.InlineKeyboardMarkup(row_width=1)
                    cm1 = types.InlineKeyboardButton(f" 𝘾𝘾 • {cc}", callback_data='u8')
                    status = types.InlineKeyboardButton(f" 𝙎𝙩𝙖𝙩𝙪𝙨 • {last}", callback_data='u8')
                    cm3 = types.InlineKeyboardButton(f" 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 !✅ • {live}", callback_data='x')
                    cm4 = types.InlineKeyboardButton(f" 𝗗𝗘𝗖𝗜𝗡𝗘𝗗 !❌ • {dd}", callback_data='x')
                    cm5 = types.InlineKeyboardButton(f"• {total_lines} / {cm} •", callback_data='x')
                    stop = types.InlineKeyboardButton("🔕 𝑺𝒕𝒐𝒑 𝑺𝒆𝒔𝒔𝒊𝒐𝒏", callback_data='stop')
                    mes.add(cm1, status, cm3, cm4, cm5, stop)

                    end_time = time.time()
                    execution_time = end_time - start_time
                    bot.edit_message_text(chat_id=call.message.chat.id, 
                        message_id=call.message.message_id, 
                        text=f'''
<b>♻️ 𝑷𝒓𝒐𝒄𝒆𝒔𝒔𝒊𝒏𝒈 𝒚𝒐𝒖𝒓 𝒓𝒆𝒒𝒖𝒆𝒔𝒕... 
━━━━━━━━━━━━━
🌟├ 𝑮𝒂𝒕𝒆 -> {gate}
━━━━━━━━━━━━━
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>''', 
                        reply_markup=mes)

                    msg = f'''<b>#Braintree_Auth 🔥 [/chk]
- - - - - - - - - - - - - - - - - - - - - - - -
𝐂𝐚𝐫𝐝: <code>{cc}</code>
𝐒𝐭𝐚𝐭𝐮𝐬: 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
{str(dato(cc[:6]))}
- - - - - - - - - - - - - - - - - - - - - - - -
𝐆𝐚𝐭𝐞: {gate}
𝐓𝐢𝐦𝐞: {"{:.1f}".format(execution_time)} 𝐒𝐞𝐜.
- - - - - - - - - - - - - - - - - - - - - - - -
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>'''

                    if "Insufficient Funds" in last or '1000: Approved' in last or 'avs' in last or 'Payment method successfully added.' in last or 'Duplicate' in last or 'Invalid postal code' in last or 'CVV' in last:
                        live += 1
                        bot.send_message(call.from_user.id, msg)
                    else:
                        dd += 1

                    time.sleep(15)

        except Exception as error:
            bot.send_message(admins[0], f'Error -> {error}')

        stopuser[id]['status'] = 'stopped'
        bot.send_message(
            chat_id=call.message.chat.id,
            text='<b>🔔 𝒀𝒐𝒖𝒓 𝑪𝒐𝒎𝒃𝒐 𝑪𝒉𝒆𝒄𝒌𝒊𝒏𝒈 𝑻𝒂𝒔𝒌 𝑾𝒂𝒔 𝑭𝒊𝒏𝒊𝒔𝒉𝒆𝒅...</b>',
            parse_mode='HTML'
        )

    my_thread = threading.Thread(target=my_function)
    my_thread.start()

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def stop_check(call):
    id = str(call.from_user.id)

    if id in stopuser and stopuser[id]['status'] == 'start':
        stopuser[id]['status'] = 'stop'
        bot.send_message(
    chat_id=call.message.chat.id,
    text="""<b>🚫 𝑷𝒍𝒆𝒂𝒔𝒆 𝒘𝒂𝒊𝒕 𝒑𝒓𝒐𝒄𝒆𝒔𝒔𝒊𝒏𝒈 𝒚𝒐𝒖𝒓 𝒔𝒆𝒔𝒔𝒊𝒐𝒏 𝒄𝒂𝒏𝒄𝒆𝒍𝒍𝒂𝒕𝒊𝒐𝒏 𝒓𝒆𝒒𝒖𝒆𝒔𝒕.</b>""",
    parse_mode='HTML',
    reply_to_message_id=call.message.message_id
)

    else:
        bot.send_message(
    chat_id=call.message.chat.id,
    text="""<b>🀄 𝑻𝒉𝒆𝒓𝒆 𝒊𝒔𝒏'𝒕 𝒂𝒏𝒚 𝒄𝒐𝒎𝒃𝒐 𝒄𝒉𝒆𝒄𝒌𝒊𝒏𝒈 𝒔𝒆𝒔𝒔𝒊𝒐𝒏 𝒓𝒖𝒏𝒏𝒊𝒏𝒈 𝒓𝒊𝒈𝒉𝒕 𝒏𝒐𝒘.</b>""",
    parse_mode='HTML',
    reply_to_message_id=call.message.message_id
)

	
	
	
	
	



	

	
	
	
	
	
	
	


import threading
import time
from telebot import types

MAX_LINES = 1000
stopuser = {} # To track the status of each user
check_enabled_br2 = True # To track whether Stripe Auth 2 checking is enabled or not

#@bot.message_handler(commands=['offb2'])
#def handle_admin_commands(message):
#    global check_enabled_br2
#    if str(message.from_user.id) in admins:
#        check_enabled_br2 = False
#        bot.send_message(chat_id=message.chat.id, text='- Stripe Auth 2 Check has been disabled. 🔒 No users can start the check until it is re-enabled.')
#    else:
#        bot.send_message(chat_id=message.chat.id, text='𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌')

#@bot.message_handler(commands=['onb2'])
#def handle_admin_commands(message):
#    global check_enabled_br2
#    if str(message.from_user.id) in admins:
#        check_enabled_br2 = True
#        bot.send_message(chat_id=message.chat.id, text='- Stripe Auth 2 Check has been re-enabled. ✅ Users can now start the check.')
#    else:
#        bot.send_message(chat_id=message.chat.id, text='𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌')

@bot.callback_query_handler(func=lambda call: call.data == 'br2')
def menu_callback(call):
    id = str(call.from_user.id)

    if not check_enabled_br2:
        bot.send_message(chat_id=call.message.chat.id, text="♻️ 𝑮𝒂𝒕𝒆𝒘𝒂𝒚 𝒊𝒔 𝒖𝒏𝒅𝒆𝒓 𝒎𝒂𝒊𝒏𝒕𝒆𝒏𝒂𝒏𝒄𝒆.. ")
        return

    # Check if the user has a scan running
    if id in stopuser and stopuser[id]['status'] == 'start':
        bot.send_message(
    chat_id=call.message.chat.id,
    text="""<b>❌ 𝑹𝒆𝒒𝒖𝒆𝒔𝒕 𝑭𝒂𝒊𝒍𝒆𝒅.</b>
━━━━━━━━━━━━━
<b>⚠️ 𝒀𝒐𝒖’𝒓𝒆 𝒂𝒍𝒓𝒆𝒂𝒅𝒚 𝒓𝒖𝒏𝒏𝒊𝒏𝒈 𝒂 𝒄𝒐𝒎𝒃𝒐 𝒄𝒉𝒆𝒄𝒌. 𝑷𝒍𝒆𝒂𝒔𝒆 𝒉𝒐𝒍𝒅 𝒕𝒊𝒈𝒉𝒕 𝒖𝒏𝒕𝒊𝒍 𝒊𝒕’𝒔 𝒄𝒐𝒎𝒑𝒍𝒆𝒕𝒆, 𝒐𝒓 𝒄𝒉𝒐𝒐𝒔𝒆 𝒕𝒐 𝒔𝒕𝒐𝒑 𝒕𝒉𝒆 𝒄𝒖𝒓𝒓𝒆𝒏𝒕 𝒔𝒆𝒔𝒔𝒊𝒐𝒏 𝒊𝒇 𝒏𝒆𝒆𝒅𝒆𝒅.</b>
━━━━━━━━━━━━━
<b>♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>""",
    parse_mode='HTML',
    reply_to_message_id=call.message.message_id
)

        return  # If there is a scan running, we exit the function and do not start a new scan

    def my_function():
        gate = 'Stripe Auth 2'
        dd = 0
        live = 0
        cm = 0
        mes = types.InlineKeyboardMarkup(row_width=1)
        cm1 = types.InlineKeyboardButton("--------------", callback_data='u8')
        status = types.InlineKeyboardButton(f"--------------", callback_data='u8')
        cm3 = types.InlineKeyboardButton("--------------", callback_data='x')
        ccn = types.InlineKeyboardButton("--------------", callback_data='x')
        cm4 = types.InlineKeyboardButton("--------------", callback_data='x')
        cm5 = types.InlineKeyboardButton("--------------", callback_data='x')
        stop = types.InlineKeyboardButton("𝑺𝒕𝒐𝒑 𝑺𝒆𝒔𝒔𝒊𝒐𝒏 🔕", callback_data='stop')
        mes.add(cm1, status, cm3, ccn, cm4, cm5, stop)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="👁‍🗨 𝑪𝒐𝒏𝒇𝒊𝒈𝒖𝒓𝒊𝒏𝒈 𝒚𝒐𝒖𝒓 𝒄𝒐𝒎𝒃𝒐 𝒍𝒊𝒔𝒕, 𝑷𝒍𝒆𝒂𝒔𝒆 𝒘𝒂𝒊𝒕!\n━━━━━━━━━━━━━\n♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]", reply_markup=mes)

        try:
            with open("combo.txt", 'r') as file:
                lines = file.readlines()
                total_lines = len(lines)

                # Check the number of lines
                if total_lines > MAX_LINES:
                    bot.send_message(
    chat_id=call.message.chat.id,
    text=f"""<b>♻️ 𝑵𝒆𝒆𝒅 𝑪𝒐𝒓𝒓𝒆𝒄𝒕𝒊𝒐𝒏𝒔.</b>
━━━━━━━━━━━━━
<b>🌟├ 𝑩𝒂𝒅 𝑪𝒐𝒎𝒃𝒐.</b>
<b>🌟├ 𝑴𝒂𝒙 𝑪𝑪 𝑳𝒊𝒎𝒊𝒕 𝒊𝒔 {MAX_LINES} 💳</b>
<b>🌟├ 𝑬𝒅𝒊𝒕 𝒀𝒐𝒖𝒓 𝑭𝒊𝒍𝒆 & 𝑹𝒆𝒕𝒓𝒚.</b>
━━━━━━━━━━━━━
<b>♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>""",
    parse_mode='HTML',
    reply_to_message_id=call.message.message_id
)
                    stopuser[id]['status'] = 'stopped'  # Edit scan status
                    return

                stopuser[id] = {'status': 'start'}

                for cc in lines:
                    if stopuser[id]['status'] == 'stop':
                        bot.send_message(
    chat_id=id,
    text="""<b>🔔 𝑵𝒐𝒕𝒊𝒇𝒊𝒄𝒂𝒕𝒊𝒐𝒏.</b>
━━━━━━━━━━━━━
<b>💳 𝑪𝒐𝒎𝒃𝒐 𝒄𝒉𝒆𝒄𝒌𝒊𝒏𝒈 𝒔𝒆𝒔𝒔𝒊𝒐𝒏𝒔 𝒔𝒕𝒐𝒑𝒑𝒆𝒅 𝒔𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍𝒚. ✅</b>
━━━━━━━━━━━━━
<b>♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>""",
    parse_mode='HTML'
)

                        stopuser[id]['status'] = 'stopped'  # Edit scan status
                        return
                    start_time = time.time()
                    try:
                        last = str(stripem2(cc))
                        cm += 1
                    except Exception as e:
                        print(e)
                        last = "RISK: gateway_error"

                    print(last)
                    mes = types.InlineKeyboardMarkup(row_width=1)
                    cm1 = types.InlineKeyboardButton(f"- 𝘾𝘾 • {cc}", callback_data='u8')
                    status = types.InlineKeyboardButton(f" 𝙎𝙩𝙖𝙩𝙪𝙨 • {last}", callback_data='u8')
                    cm3 = types.InlineKeyboardButton(f" 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 !✅ • {live}", callback_data='x')
                    cm4 = types.InlineKeyboardButton(f" 𝗗𝗘𝗖𝗜𝗡𝗘𝗗 !❌ • {dd}", callback_data='x')
                    cm5 = types.InlineKeyboardButton(f"• {total_lines} / {cm} •", callback_data='x')
                    stop = types.InlineKeyboardButton("🔕 𝑺𝒕𝒐𝒑 𝑺𝒆𝒔𝒔𝒊𝒐𝒏", callback_data='stop')
                    mes.add(cm1, status, cm3, cm4, cm5, stop)

                    end_time = time.time()
                    execution_time = end_time - start_time
                    bot.edit_message_text(chat_id=call.message.chat.id, 
                        message_id=call.message.message_id, 
                        text=f'''
<b>♻️ 𝑷𝒓𝒐𝒄𝒆𝒔𝒔𝒊𝒏𝒈 𝒚𝒐𝒖𝒓 𝒓𝒆𝒒𝒖𝒆𝒔𝒕... 
━━━━━━━━━━━━━
🌟├ 𝑮𝒂𝒕𝒆 -> {gate}
━━━━━━━━━━━━━
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>''', 
                        reply_markup=mes)

                    msg = f'''<b>#Stripe_Auth 🇮🇹
- - - - - - - - - - - - - - - - - - - - - - - -
𝐂𝐚𝐫𝐝: <code>{cc}</code>
𝐒𝐭𝐚𝐭𝐮𝐬: 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
{str(dato(cc[:6]))}
- - - - - - - - - - - - - - - - - - - - - - - -
𝐆𝐚𝐭𝐞: {gate}
𝐓𝐢𝐦𝐞: {"{:.1f}".format(execution_time)} 𝐒𝐞𝐜.
- - - - - - - - - - - - - - - - - - - - - - - -
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>'''

                    if "Nice! New payment method added." in last or 'Insufficient Funds' in last or 'Invalid Billing Address: Avs' in last:
                        live += 1
                        bot.send_message(call.from_user.id, msg)
                    else:
                        dd += 1

                    time.sleep(15)

        except Exception as error:
            bot.send_message(admins[0], f'Error -> {error}')

        stopuser[id]['status'] = 'stopped'  # Edit the scan status after completion
        bot.send_message(
    chat_id=call.message.chat.id,
    text='<b>🔔 𝒀𝒐𝒖𝒓 𝑪𝒐𝒎𝒃𝒐 𝑪𝒉𝒆𝒄𝒌𝒊𝒏𝒈 𝑻𝒂𝒔𝒌 𝑾𝒂𝒔 𝑭𝒊𝒏𝒊𝒔𝒉𝒆𝒅...n━━━━━━━━━━━━━n♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>',
    parse_mode='HTML'
)

    my_thread = threading.Thread(target=my_function)
    my_thread.start()

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def stop_check(call):
    id = str(call.from_user.id)
    if id in stopuser and stopuser[id]['status'] == 'start':
        stopuser[id]['status'] = 'stop'
        bot.send_message(
    chat_id=call.message.chat.id,
    text="""<b>🚫 𝑷𝒍𝒆𝒂𝒔𝒆 𝒘𝒂𝒊𝒕 𝒑𝒓𝒐𝒄𝒆𝒔𝒔𝒊𝒏𝒈 𝒚𝒐𝒖𝒓 𝒔𝒆𝒔𝒔𝒊𝒐𝒏 𝒄𝒂𝒏𝒄𝒆𝒍𝒍𝒂𝒕𝒊𝒐𝒏 𝒓𝒆𝒒𝒖𝒆𝒔𝒕.</b>""",
    parse_mode='HTML',
    reply_to_message_id=call.message.message_id
)

    else:
        bot.send_message(
    chat_id=call.message.chat.id,
    text="""<b>🀄 𝑻𝒉𝒆𝒓𝒆 𝒊𝒔𝒏'𝒕 𝒂𝒏𝒚 𝒄𝒐𝒎𝒃𝒐 𝒄𝒉𝒆𝒄𝒌𝒊𝒏𝒈 𝒔𝒆𝒔𝒔𝒊𝒐𝒏 𝒓𝒖𝒏𝒏𝒊𝒏𝒈 𝒓𝒊𝒈𝒉𝒕 𝒏𝒐𝒘.</b>""",
    parse_mode='HTML',
    reply_to_message_id=call.message.message_id
)

	
	
	












	






















import threading
import time
from telebot import types

MAX_LINES = 1000
stopuser = {} # To track the status of each user
check_enabled_br3 = True # To track whether Braintree Auth 2 checking is enabled or not

#@bot.message_handler(commands=['offb3'])
#def handle_admin_commands(message):
#    global check_enabled_br3
#    if str(message.from_user.id) in admins:
#        check_enabled_br3 = False
#        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 2 Check has been disabled. 🔒 No users can start the check until it is re-enabled.')
#    else:
#        bot.send_message(chat_id=message.chat.id, text='𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌')

#@bot.message_handler(commands=['onb3'])
#def handle_admin_commands(message):
#    global check_enabled_br3
#    if str(message.from_user.id) in admins:
#        check_enabled_br3 = True
#        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 2 Check has been re-enabled. ✅ Users can now start the check.')
#    else:
#        bot.send_message(chat_id=message.chat.id, text='𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌')

@bot.callback_query_handler(func=lambda call: call.data == 'br3')
def menu_callback(call):
    id = str(call.from_user.id)

    if not check_enabled_br3:
        bot.send_message(chat_id=call.message.chat.id, text="♻️ 𝑮𝒂𝒕𝒆𝒘𝒂𝒚 𝒊𝒔 𝒖𝒏𝒅𝒆𝒓 𝒎𝒂𝒊𝒏𝒕𝒆𝒏𝒂𝒏𝒄𝒆.. ")
        return

    # Check if the user has a scan running
    if id in stopuser and stopuser[id]['status'] == 'start':
        bot.send_message(
    chat_id=call.message.chat.id,
    text="""<b>❌ 𝑹𝒆𝒒𝒖𝒆𝒔𝒕 𝑭𝒂𝒊𝒍𝒆𝒅.</b>
━━━━━━━━━━━━━
<b>⚠️ 𝒀𝒐𝒖’𝒓𝒆 𝒂𝒍𝒓𝒆𝒂𝒅𝒚 𝒓𝒖𝒏𝒏𝒊𝒏𝒈 𝒂 𝒄𝒐𝒎𝒃𝒐 𝒄𝒉𝒆𝒄𝒌. 𝑷𝒍𝒆𝒂𝒔𝒆 𝒉𝒐𝒍𝒅 𝒕𝒊𝒈𝒉𝒕 𝒖𝒏𝒕𝒊𝒍 𝒊𝒕’𝒔 𝒄𝒐𝒎𝒑𝒍𝒆𝒕𝒆, 𝒐𝒓 𝒄𝒉𝒐𝒐𝒔𝒆 𝒕𝒐 𝒔𝒕𝒐𝒑 𝒕𝒉𝒆 𝒄𝒖𝒓𝒓𝒆𝒏𝒕 𝒔𝒆𝒔𝒔𝒊𝒐𝒏 𝒊𝒇 𝒏𝒆𝒆𝒅𝒆𝒅.</b>
━━━━━━━━━━━━━
<b>♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>""",
    parse_mode='HTML',
    reply_to_message_id=call.message.message_id
)

        return  # If there is a scan running, we exit the function and do not start a new scan

    def my_function():
        gate = 'Braintree Auth 2'
        dd = 0
        live = 0
        cm = 0
        mes = types.InlineKeyboardMarkup(row_width=1)
        cm1 = types.InlineKeyboardButton("--------------", callback_data='u8')
        status = types.InlineKeyboardButton(f"--------------", callback_data='u8')
        cm3 = types.InlineKeyboardButton("--------------", callback_data='x')
        ccn = types.InlineKeyboardButton("--------------", callback_data='x')
        cm4 = types.InlineKeyboardButton("--------------", callback_data='x')
        cm5 = types.InlineKeyboardButton("--------------", callback_data='x')
        stop = types.InlineKeyboardButton("𝑺𝒕𝒐𝒑 𝑺𝒆𝒔𝒔𝒊𝒐𝒏 🔕", callback_data='stop')
        mes.add(cm1, status, cm3, ccn, cm4, cm5, stop)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="👁‍🗨 𝑪𝒐𝒏𝒇𝒊𝒈𝒖𝒓𝒊𝒏𝒈 𝒚𝒐𝒖𝒓 𝒄𝒐𝒎𝒃𝒐 𝒍𝒊𝒔𝒕, 𝑷𝒍𝒆𝒂𝒔𝒆 𝒘𝒂𝒊𝒕! \n━━━━━━━━━━━━━\n♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]", reply_markup=mes)

        try:
            with open("combo.txt", 'r') as file:
                lines = file.readlines()
                total_lines = len(lines)

                # Check the number of lines
                if total_lines > MAX_LINES:
                    bot.send_message(
    chat_id=call.message.chat.id,
    text=f"""<b>♻️ 𝑵𝒆𝒆𝒅 𝑪𝒐𝒓𝒓𝒆𝒄𝒕𝒊𝒐𝒏𝒔.</b>
━━━━━━━━━━━━━
<b>🌟├ 𝑩𝒂𝒅 𝑪𝒐𝒎𝒃𝒐.</b>
<b>🌟├ 𝑴𝒂𝒙 𝑪𝑪 𝑳𝒊𝒎𝒊𝒕 𝒊𝒔 {MAX_LINES} 💳</b>
<b>🌟├ 𝑬𝒅𝒊𝒕 𝒀𝒐𝒖𝒓 𝑭𝒊𝒍𝒆 & 𝑹𝒆𝒕𝒓𝒚.</b>
━━━━━━━━━━━━━
<b>♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>""",
    parse_mode='HTML',
    reply_to_message_id=call.message.message_id
)
                    stopuser[id]['status'] = 'stopped'  # Edit scan status
                    return

                stopuser[id] = {'status': 'start'}

                for cc in lines:
                    if stopuser[id]['status'] == 'stop':
                        bot.send_message(
    chat_id=id,
    text="""<b>🔔 𝑵𝒐𝒕𝒊𝒇𝒊𝒄𝒂𝒕𝒊𝒐𝒏.</b>
━━━━━━━━━━━━━
<b>💳 𝑪𝒐𝒎𝒃𝒐 𝒄𝒉𝒆𝒄𝒌𝒊𝒏𝒈 𝒔𝒆𝒔𝒔𝒊𝒐𝒏𝒔 𝒔𝒕𝒐𝒑𝒑𝒆𝒅 𝒔𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍𝒚. ✅</b>
━━━━━━━━━━━━━
<b>♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>""",
    parse_mode='HTML'
)

                        stopuser[id]['status'] = 'stopped'  # Edit scan status
                        return
                    start_time = time.time()
                    try:
                        last = str(b3m(cc))
                        cm += 1
                    except Exception as e:
                        print(e)
                        last = "RISK: gateway_error"

                    print(last)
                    mes = types.InlineKeyboardMarkup(row_width=1)
                    cm1 = types.InlineKeyboardButton(f" 𝘾𝘾 • {cc}", callback_data='u8')
                    status = types.InlineKeyboardButton(f" 𝙎𝙩𝙖𝙩𝙪𝙨 • {last}", callback_data='u8')
                    cm3 = types.InlineKeyboardButton(f" 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 !✅ • {live}", callback_data='x')
                    cm4 = types.InlineKeyboardButton(f" 𝗗𝗘𝗖𝗜𝗡𝗘𝗗 !❌ • {dd}", callback_data='x')
                    cm5 = types.InlineKeyboardButton(f"• {total_lines} / {cm} •", callback_data='x')
                    stop = types.InlineKeyboardButton("🔕 𝑺𝒕𝒐𝒑 𝑺𝒆𝒔𝒔𝒊𝒐𝒏", callback_data='stop')
                    mes.add(cm1, status, cm3, cm4, cm5, stop)

                    end_time = time.time()
                    execution_time = end_time - start_time
                    bot.edit_message_text(chat_id=call.message.chat.id, 
                        message_id=call.message.message_id, 
                        text=f'''
<b>♻️ 𝑷𝒓𝒐𝒄𝒆𝒔𝒔𝒊𝒏𝒈 𝒚𝒐𝒖𝒓 𝒓𝒆𝒒𝒖𝒆𝒔𝒕... 
━━━━━━━━━━━━━
🌟├ 𝑮𝒂𝒕𝒆 -> {gate}
━━━━━━━━━━━━━
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>''', 
                        reply_markup=mes)

                    msg = f'''<b>#Braintree_Auth2  🇷🇺
- - - - - - - - - - - - - - - - - - - - - - - -
𝐂𝐚𝐫𝐝: <code>{cc}</code>
𝐒𝐭𝐚𝐭𝐮𝐬: 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
{str(dato(cc[:6]))}
- - - - - - - - - - - - - - - - - - - - - - - -
𝐆𝐚𝐭𝐞: {gate}
𝐓𝐢𝐦𝐞: {"{:.1f}".format(execution_time)} 𝐒𝐞𝐜.
- - - - - - - - - - - - - - - - - - - - - - - -
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>'''

                    if "Insufficient Funds" in last or 'Invalid postal code' in last or '81724: Duplicate card exists in the vault.' in last or 'Nice! New payment method added.' in last or 'avs: Gateway Rejected: avs' in last:
                        live += 1
                        bot.send_message(call.from_user.id, msg)
                    else:
                        dd += 1

                    time.sleep(15)

        except Exception as error:
            bot.send_message(admins[0], f'Error -> {error}')

        stopuser[id]['status'] = 'stopped'  # Edit the scan status after completion
        bot.send_message(
    chat_id=call.message.chat.id,
    text='<b>🔔 𝒀𝒐𝒖𝒓 𝑪𝒐𝒎𝒃𝒐 𝑪𝒉𝒆𝒄𝒌𝒊𝒏𝒈 𝑻𝒂𝒔𝒌 𝑾𝒂𝒔 𝑭𝒊𝒏𝒊𝒔𝒉𝒆𝒅...n━━━━━━━━━━━━━n♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>',
    parse_mode='HTML'
)

    my_thread = threading.Thread(target=my_function)
    my_thread.start()

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def stop_check(call):
    id = str(call.from_user.id)
    if id in stopuser and stopuser[id]['status'] == 'start':
        stopuser[id]['status'] = 'stop'
        bot.send_message(
    chat_id=call.message.chat.id,
    text="""<b>🚫 𝑷𝒍𝒆𝒂𝒔𝒆 𝒘𝒂𝒊𝒕 𝒑𝒓𝒐𝒄𝒆𝒔𝒔𝒊𝒏𝒈 𝒚𝒐𝒖𝒓 𝒔𝒆𝒔𝒔𝒊𝒐𝒏 𝒄𝒂𝒏𝒄𝒆𝒍𝒍𝒂𝒕𝒊𝒐𝒏 𝒓𝒆𝒒𝒖𝒆𝒔𝒕.</b>""",
    parse_mode='HTML',
    reply_to_message_id=call.message.message_id
)

    else:
        bot.send_message(
    chat_id=call.message.chat.id,
    text="""<b>🀄 𝑻𝒉𝒆𝒓𝒆 𝒊𝒔𝒏'𝒕 𝒂𝒏𝒚 𝒄𝒐𝒎𝒃𝒐 𝒄𝒉𝒆𝒄𝒌𝒊𝒏𝒈 𝒔𝒆𝒔𝒔𝒊𝒐𝒏 𝒓𝒖𝒏𝒏𝒊𝒏𝒈 𝒓𝒊𝒈𝒉𝒕 𝒏𝒐𝒘.</b>""",
    parse_mode='HTML',
    reply_to_message_id=call.message.message_id
)

    







	
	
	
	
	
	
	
	
	
	
	
import threading
import time
from telebot import types

MAX_LINES = 1000
stopuser = {} # To track the status of each user 
check_enabled_br4 = True # To track whether Stripe Auth 1 checking is enabled or not

#@bot.message_handler(commands=['offb4'])
#def handle_admin_commands(message):
#    global check_enabled_br4
#    if str(message.from_user.id) in admins:
#        check_enabled_br4 = False
#        bot.send_message(chat_id=message.chat.id, text='- Stripe Auth 1 Check has been disabled. 🔒 No users can start the check until it is re-enabled.')
#    else:
#        bot.send_message(chat_id=message.chat.id, text='𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌')

#@bot.message_handler(commands=['onb4'])
#def handle_admin_commands(message):
#    global check_enabled_br4
#    if str(message.from_user.id) in admins:
#        check_enabled_br4 = True
#        bot.send_message(chat_id=message.chat.id, text='- Stripe Auth 1 Check has been re-enabled. ✅ Users can now start the check.')
#    else:
#        bot.send_message(chat_id=message.chat.id, text='𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌')

@bot.callback_query_handler(func=lambda call: call.data == 'br4')
def menu_callbactok(call):
    id = str(call.from_user.id)

    if not check_enabled_br4:
        bot.send_message(chat_id=call.message.chat.id, text="♻️ 𝑮𝒂𝒕𝒆𝒘𝒂𝒚 𝒊𝒔 𝒖𝒏𝒅𝒆𝒓 𝒎𝒂𝒊𝒏𝒕𝒆𝒏𝒂𝒏𝒄𝒆.. ")
        return

    # Check if the user has a scan running
    if id in stopuser and stopuser[id]['status'] == 'start':
        bot.send_message(
    chat_id=call.message.chat.id,
    text="""<b>❌ 𝑹𝒆𝒒𝒖𝒆𝒔𝒕 𝑭𝒂𝒊𝒍𝒆𝒅.</b>
━━━━━━━━━━━━━
<b>⚠️ 𝒀𝒐𝒖’𝒓𝒆 𝒂𝒍𝒓𝒆𝒂𝒅𝒚 𝒓𝒖𝒏𝒏𝒊𝒏𝒈 𝒂 𝒄𝒐𝒎𝒃𝒐 𝒄𝒉𝒆𝒄𝒌. 𝑷𝒍𝒆𝒂𝒔𝒆 𝒉𝒐𝒍𝒅 𝒕𝒊𝒈𝒉𝒕 𝒖𝒏𝒕𝒊𝒍 𝒊𝒕’𝒔 𝒄𝒐𝒎𝒑𝒍𝒆𝒕𝒆, 𝒐𝒓 𝒄𝒉𝒐𝒐𝒔𝒆 𝒕𝒐 𝒔𝒕𝒐𝒑 𝒕𝒉𝒆 𝒄𝒖𝒓𝒓𝒆𝒏𝒕 𝒔𝒆𝒔𝒔𝒊𝒐𝒏 𝒊𝒇 𝒏𝒆𝒆𝒅𝒆𝒅.</b>
━━━━━━━━━━━━━
<b>♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>""",
    parse_mode='HTML',
    reply_to_message_id=call.message.message_id
)

        return  # If there is a scan running, we exit the function and do not start a new scan

    def my_function():
        gate = 'Stripe Auth 1'
        dd = 0
        live = 0
        cm = 0
        mes = types.InlineKeyboardMarkup(row_width=1)
        cm1 = types.InlineKeyboardButton("--------------", callback_data='u8')
        status = types.InlineKeyboardButton(f"--------------", callback_data='u8')
        cm3 = types.InlineKeyboardButton("--------------", callback_data='x')
        ccn = types.InlineKeyboardButton("--------------", callback_data='x')
        cm4 = types.InlineKeyboardButton("--------------", callback_data='x')
        cm5 = types.InlineKeyboardButton("--------------", callback_data='x')
        stop = types.InlineKeyboardButton("𝑺𝒕𝒐𝒑 𝑺𝒆𝒔𝒔𝒊𝒐𝒏 🔕", callback_data='stop')
        mes.add(cm1, status, cm3, ccn, cm4, cm5, stop)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="👁‍🗨 𝑪𝒐𝒏𝒇𝒊𝒈𝒖𝒓𝒊𝒏𝒈 𝒚𝒐𝒖𝒓 𝒄𝒐𝒎𝒃𝒐 𝒍𝒊𝒔𝒕, 𝑷𝒍𝒆𝒂𝒔𝒆 𝒘𝒂𝒊𝒕!\n━━━━━━━━━━━━━\n♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]", reply_markup=mes)
        
        try:
            with open("combo.txt", 'r') as file:
                lines = file.readlines()
                total_lines = len(lines)
                
                # Check the number of lines
                if total_lines > MAX_LINES:
                    bot.send_message(
    chat_id=call.message.chat.id,
    text=f"""<b>♻️ 𝑵𝒆𝒆𝒅 𝑪𝒐𝒓𝒓𝒆𝒄𝒕𝒊𝒐𝒏𝒔.</b>
━━━━━━━━━━━━━
<b>🌟├ 𝑩𝒂𝒅 𝑪𝒐𝒎𝒃𝒐.</b>
<b>🌟├ 𝑴𝒂𝒙 𝑪𝑪 𝑳𝒊𝒎𝒊𝒕 𝒊𝒔 {MAX_LINES} 💳</b>
<b>🌟├ 𝑬𝒅𝒊𝒕 𝒀𝒐𝒖𝒓 𝑭𝒊𝒍𝒆 & 𝑹𝒆𝒕𝒓𝒚.</b>
━━━━━━━━━━━━━
<b>♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>""",
    parse_mode='HTML',
    reply_to_message_id=call.message.message_id
)
                    stopuser[id]['status'] = 'stopped'  # Edit scan status
                    return
                
                stopuser[id] = {'status': 'start'}
                
                for cc in lines:
                    if stopuser[id]['status'] == 'stop':
                        bot.send_message(
    chat_id=id,
    text="""<b>🔔 𝑵𝒐𝒕𝒊𝒇𝒊𝒄𝒂𝒕𝒊𝒐𝒏.</b>
━━━━━━━━━━━━━
<b>💳 𝑪𝒐𝒎𝒃𝒐 𝒄𝒉𝒆𝒄𝒌𝒊𝒏𝒈 𝒔𝒆𝒔𝒔𝒊𝒐𝒏𝒔 𝒔𝒕𝒐𝒑𝒑𝒆𝒅 𝒔𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍𝒚. ✅</b>
━━━━━━━━━━━━━
<b>♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>""",
    parse_mode='HTML'
)

                        stopuser[id]['status'] = 'stopped'  # Edit scan status
                        return
                    start_time = time.time()
                    try:
                        last = str(stripem1(cc))
                        cm += 1
                    except Exception as e:
                        print(e)
                        last = "RISK: gateway_error"
                    
                    print(last)
                    mes = types.InlineKeyboardMarkup(row_width=1)
                    cm1 = types.InlineKeyboardButton(f" 𝘾𝘾 • {cc}", callback_data='u8')
                    status = types.InlineKeyboardButton(f" 𝙎𝙩𝙖𝙩𝙪𝙨 • {last}", callback_data='u8')
                    cm3 = types.InlineKeyboardButton(f" 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 !✅ • {live}", callback_data='x')
                    cm4 = types.InlineKeyboardButton(f" 𝗗𝗘𝗖𝗜𝗡𝗘𝗗 !❌ • {dd}", callback_data='x')
                    cm5 = types.InlineKeyboardButton(f"• {total_lines} / {cm} •", callback_data='x')
                    stop = types.InlineKeyboardButton("🔕 𝑺𝒕𝒐𝒑 𝑺𝒆𝒔𝒔𝒊𝒐𝒏", callback_data='stop')
                    mes.add(cm1, status, cm3, cm4, cm5, stop)
                    
                    end_time = time.time()
                    execution_time = end_time - start_time
                    bot.edit_message_text(chat_id=call.message.chat.id, 
                        message_id=call.message.message_id, 
                        text=f'''
<b>♻️ 𝑷𝒓𝒐𝒄𝒆𝒔𝒔𝒊𝒏𝒈 𝒚𝒐𝒖𝒓 𝒓𝒆𝒒𝒖𝒆𝒔𝒕... 
━━━━━━━━━━━━━
🌟├ 𝑮𝒂𝒕𝒆 -> {gate}
━━━━━━━━━━━━━
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>''', 
                        reply_markup=mes)
                    
                    msg = f'''<b>#Stripe_Auth 🇺🇸 
- - - - - - - - - - - - - - - - - - - - - - - -
𝐂𝐚𝐫𝐝: <code>{cc}</code>
𝐒𝐭𝐚𝐭𝐮𝐬: 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
{str(dato(cc[:6]))}
- - - - - - - - - - - - - - - - - - - - - - - -
𝐆𝐚𝐭𝐞: {gate}
𝐓𝐢𝐦𝐞: {"{:.1f}".format(execution_time)} 𝐒𝐞𝐜.
- - - - - - - - - - - - - - - - - - - - - - - -
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>'''
                    
                    if "Thankyou For Your Purchase!" in last:
                        live += 1
                        bot.send_message(call.from_user.id, msg)
                    else:
                        dd += 1
                    
                    time.sleep(15)
        except Exception as error:
            bot.send_message(admins[0], f'Error -> {error}')
        
        stopuser[id]['status'] = 'stopped'  # Edit the scan status after completion
        bot.send_message(
    chat_id=call.message.chat.id,
    text='<b>🔔 𝒀𝒐𝒖𝒓 𝑪𝒐𝒎𝒃𝒐 𝑪𝒉𝒆𝒄𝒌𝒊𝒏𝒈 𝑻𝒂𝒔𝒌 𝑾𝒂𝒔 𝑭𝒊𝒏𝒊𝒔𝒉𝒆𝒅...n━━━━━━━━━━━━━n♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>',
    parse_mode='HTML'
)

    my_thread = threading.Thread(target=my_function)
    my_thread.start()

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def stop_check(call):
    id = str(call.from_user.id)
    if id in stopuser and stopuser[id]['status'] == 'start':
        stopuser[id]['status'] = 'stop'
        bot.send_message(
    chat_id=call.message.chat.id,
    text="""<b>🚫 𝑷𝒍𝒆𝒂𝒔𝒆 𝒘𝒂𝒊𝒕 𝒑𝒓𝒐𝒄𝒆𝒔𝒔𝒊𝒏𝒈 𝒚𝒐𝒖𝒓 𝒔𝒆𝒔𝒔𝒊𝒐𝒏 𝒄𝒂𝒏𝒄𝒆𝒍𝒍𝒂𝒕𝒊𝒐𝒏 𝒓𝒆𝒒𝒖𝒆𝒔𝒕.</b>""",
    parse_mode='HTML',
    reply_to_message_id=call.message.message_id
)

    else:
        bot.send_message(
    chat_id=call.message.chat.id,
    text="""<b>🀄 𝑻𝒉𝒆𝒓𝒆 𝒊𝒔𝒏'𝒕 𝒂𝒏𝒚 𝒄𝒐𝒎𝒃𝒐 𝒄𝒉𝒆𝒄𝒌𝒊𝒏𝒈 𝒔𝒆𝒔𝒔𝒊𝒐𝒏 𝒓𝒖𝒏𝒏𝒊𝒏𝒈 𝒓𝒊𝒈𝒉𝒕 𝒏𝒐𝒘.</b>""",
    parse_mode='HTML',
    reply_to_message_id=call.message.message_id
)

    


	






























import json
from datetime import datetime, timedelta

# User plan verification function
def check_user_plan(user_id):
    with open('data.json', 'r') as file:
        json_data = json.load(file)
    if str(user_id) in json_data:
        user_plan = json_data[str(user_id)]['plan']
        timer = json_data[str(user_id)]['timer']
        if user_plan != '𓆩 𝐅𝐫𝐞𝐞 𓆪ꪾ':
            date_str = timer.split('.')[0]
            try:
                provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                current_time = datetime.now()
                if current_time - provided_time <= timedelta(hours=0):  # Modify the subscription period as needed
                    return True
            except Exception as e:
                return False
    return False










import time
from datetime import datetime, timedelta

# Define a dictionary to store the time of the last request for each user
command_usage = {}

# Default status of Gate 1 (activated)
check_enabled_br1 = True

#@bot.message_handler(commands=['offb1'])
#def handle_admin_commands(message):
#    global check_enabled_br1
#    if str(message.from_user.id) in admins:
#        check_enabled_br1 = False
#        bot.send_message(chat_id=message.chat.id, text='- Focusing Check has been disabled. 🔒 No users can start the check until it is re-enabled.')
#    else:
#        bot.send_message(chat_id=message.chat.id, text='𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌')

#@bot.message_handler(commands=['onb1'])
#def handle_admin_commands(message):
#    global check_enabled_br1
#    if str(message.from_user.id) in admins:
#        check_enabled_br1 = True
#        bot.send_message(chat_id=message.chat.id, text='- Focusing Check has been re-enabled. ✅ Users can now start the check.')
#    else:
#        bot.send_message(chat_id=message.chat.id, text='𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌')

@bot.message_handler(func=lambda message: message.text.lower().startswith('.chk') or message.text.lower().startswith('/chk'))
def respond_to_vhk(message):
    global check_enabled_br1
    user_id = message.chat.id
    current_time = datetime.now()

    # Check the status of gateway 1
    if not check_enabled_br1:
        bot.reply_to(message, "<b>♻️ 𝑮𝒂𝒕𝒆𝒘𝒂𝒚 𝒊𝒔 𝒖𝒏𝒅𝒆𝒓 𝒎𝒂𝒊𝒏𝒕𝒆𝒏𝒂𝒏𝒄𝒆.. </b>", parse_mode="HTML")
        return

    # Check if the user has the last usage time of the command
    if user_id in command_usage:
        last_time = command_usage[user_id]['last_time']
        time_diff = (current_time - last_time).seconds
        # Check if the interval time is less than 30 seconds
        if time_diff < 30:
            bot.reply_to(message, f"<b>♻️ 𝑻𝒓𝒚 𝒂𝒈𝒂𝒊𝒏 𝒂𝒇𝒕𝒆𝒓 {30 - time_diff} 𝒔𝒆𝒄𝒐𝒏𝒅𝒔.</b>", parse_mode="HTML")
            return
    
    # Update the time of the last request
    command_usage[user_id] = {'last_time': current_time}

    if check_user_plan(user_id):
        cc = message.text.replace('.chk ', '').replace('/chk ', '')
        gate='Braintree Auth 1'
        ko = bot.reply_to(message, '𝑷𝒓𝒐𝒄𝒆𝒔𝒔𝒊𝒏𝒈 𝒚𝒐𝒖𝒓 𝒓𝒆𝒒𝒖𝒆𝒔𝒕...').message_id
        start_time = time.time()
        try:
            last = str(dexter(cc))
        except:
            last = '𝑭𝒂𝒊𝒍𝒆𝒅 𝒕𝒐 𝒍𝒐𝒂𝒅 𝒕𝒉𝒆 𝒈𝒂𝒕𝒆. ❌'
        end_time = time.time()
        execution_time = end_time - start_time

        dec = f'''<b>#Braintree_Auth 🔥 [/chk]
- - - - - - - - - - - - - - - - - - - - - - - -
𝐂𝐚𝐫𝐝: <code>{cc}</code>
𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
{str(dato(cc[:6]))}
- - - - - - - - - - - - - - - - - - - - - - - -
𝐆𝐚𝐭𝐞: Braintree Auth 1
𝐓𝐢𝐦𝐞: {"{:.1f}".format(execution_time)} 𝐒𝐞𝐜.
- - - - - - - - - - - - - - - - - - - - - - - -
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>'''

        ok = f'''<b>#Braintree_Auth 🔥 [/chk]
- - - - - - - - - - - - - - - - - - - - - - - -
𝐂𝐚𝐫𝐝: <code>{cc}</code>
𝐒𝐭𝐚𝐭𝐮𝐬: 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
{str(dato(cc[:6]))}
- - - - - - - - - - - - - - - - - - - - - - - -
𝐆𝐚𝐭𝐞: Braintree Auth 1
𝐓𝐢𝐦𝐞: {"{:.1f}".format(execution_time)} 𝐒𝐞𝐜.
- - - - - - - - - - - - - - - - - - - - - - - -
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>'''

        insf = f'''<b>#Braintree_Auth 🔥 [/chk]
- - - - - - - - - - - - - - - - - - - - - - - -
𝐂𝐚𝐫𝐝: <code>{cc}</code>
𝐒𝐭𝐚𝐭𝐮𝐬: 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
{str(dato(cc[:6]))}
- - - - - - - - - - - - - - - - - - - - - - - -
𝐆𝐚𝐭𝐞: Braintree Auth 1
𝐓𝐢𝐦𝐞: {"{:.1f}".format(execution_time)} 𝐒𝐞𝐜.
- - - - - - - - - - - - - - - - - - - - - - - -
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>'''

        if 'Insufficient Funds' in last:
            bot.edit_message_text(text=insf, chat_id=message.chat.id, message_id=ko)
        elif "avs" in last or "1000: Approved" in last or "Invalid postal code" in last or "Duplicate" in last or "Payment method successfully added." in last:
            bot.edit_message_text(text=ok, chat_id=message.chat.id, message_id=ko)
        else:
            bot.edit_message_text(text=dec, chat_id=message.chat.id, message_id=ko)
    else:
        bot.reply_to(message, f'''<b>♻️ 𝑨𝒉𝒉 𝑵𝒊𝒈𝒈𝒂 {message.from_user.first_name}!
━━━━━━━━━━━━━ 
🌟├𝒀𝒐𝒖𝒓 𝑹𝒂𝒏𝒌: 𓆩 𝑭𝒓𝒆𝒆 𓆪ꪾ 💔 
🌟├𝑩𝒖𝒚 𝑻𝒉𝒆 𝑷𝒓𝒆𝒎𝒊𝒖𝒎 𝑭𝒓𝒐𝒎 𝑴𝒚 𝑴𝒂𝒔𝒕𝒆𝒓 ━━━━━━━━━━━━━ 
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [ 𝑴𝒂𝒔𝒕𝒆𝒓 ]</b>''')



#####₹₹-₹+₹(₹(₹(₹)₹))₹



import time
from datetime import datetime, timedelta

# Define a dictionary to store the time of the last request for each user
command_usage = {}

# Default status of Gate 2 (activated)
check_enabled_br2 = True

#@bot.message_handler(commands=['offb2'])
#def handle_admin_commands(message):
#    global check_enabled_br2
#    if str(message.from_user.id) in admins:
#        check_enabled_br2 = False
#        bot.send_message(chat_id=message.chat.id, text='- Focusing Check for Gateway 2 has been disabled. 🔒 No users can start the check until it is re-enabled.')
#    else:
#        bot.send_message(chat_id=message.chat.id, text='𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌')

#@bot.message_handler(commands=['on_B2'])
#def handle_admin_commands(message):
#    global check_enabled_br2
#    if str(message.from_user.id) in admins:
#        check_enabled_br2 = True
#        bot.send_message(chat_id=message.chat.id, text='- Focusing Check for Gateway 2 has been re-enabled. ✅ Users can now start the check.')
#    else:
#        bot.send_message(chat_id=message.chat.id, text='𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌')

@bot.message_handler(func=lambda message: message.text.lower().startswith('.cc') or message.text.lower().startswith('/cc'))
def respond_to_vhk(message):
    global check_enabled_br2
    user_id = message.chat.id
    current_time = datetime.now()

    # Check the status of gateway 2
    if not check_enabled_br2:
        bot.reply_to(message, "<b>♻️ 𝑮𝒂𝒕𝒆𝒘𝒂𝒚 𝒊𝒔 𝒖𝒏𝒅𝒆𝒓 𝒎𝒂𝒊𝒏𝒕𝒆𝒏𝒂𝒏𝒄𝒆.. </b>", parse_mode="HTML")
        return

    # Check if the user has the last usage time of the command
    if user_id in command_usage:
        last_time = command_usage[user_id]['last_time']
        time_diff = (current_time - last_time).seconds
        # Check if the interval time is less than 30 seconds
        if time_diff < 30:
            bot.reply_to(message, f"<b>♻️ 𝑻𝒓𝒚 𝒂𝒈𝒂𝒊𝒏 𝒂𝒇𝒕𝒆𝒓 {30 - time_diff} 𝒔𝒆𝒄𝒐𝒏𝒅𝒔.</b>", parse_mode="HTML")
            return
    
    # Update the time of the last request
    command_usage[user_id] = {'last_time': current_time}

    if check_user_plan(user_id):
        cc = message.text.replace('.cc ', '').replace('/cc ', '')
        gate = 'Stripe Auth 2'
        ko = bot.reply_to(message, '𝑷𝒓𝒐𝒄𝒆𝒔𝒔𝒊𝒏𝒈 𝒚𝒐𝒖𝒓 𝒓𝒆𝒒𝒖𝒆𝒔𝒕...').message_id
        start_time = time.time()
        try:
            last = str(stripea2(cc))
        except:
            last = '𝑭𝒂𝒊𝒍𝒆𝒅 𝒕𝒐 𝒍𝒐𝒂𝒅 𝒕𝒉𝒆 𝒈𝒂𝒕𝒆. ❌'
        end_time = time.time()
        execution_time = end_time - start_time

        dec = f'''<b>#Stripe_Auth 🇮🇹 [/cc]
- - - - - - - - - - - - - - - - - - - - - - - -
𝐂𝐚𝐫𝐝: <code>{cc}</code>
𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
{str(dato(cc[:6]))}
- - - - - - - - - - - - - - - - - - - - - - - -
𝐆𝐚𝐭𝐞: {gate}
𝐓𝐢𝐦𝐞: {"{:.1f}".format(execution_time)} 𝐒𝐞𝐜.
- - - - - - - - - - - - - - - - - - - - - - - -
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>'''

        ok = f'''<b>#Stripe_Auth 🇮🇹 [/cc]
- - - - - - - - - - - - - - - - - - - - - - - -
𝐂𝐚𝐫𝐝: <code>{cc}</code>
𝐒𝐭𝐚𝐭𝐮𝐬: 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
{str(dato(cc[:6]))}
- - - - - - - - - - - - - - - - - - - - - - - -
𝐆𝐚𝐭𝐞: {gate}
𝐓𝐢𝐦𝐞: {"{:.1f}".format(execution_time)} 𝐒𝐞𝐜.
- - - - - - - - - - - - - - - - - - - - - - - -
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>'''

        if "Nice! New payment method added." in last or 'Insufficient Funds' in last or 'Invalid Billing Address: Avs' in last:
            bot.edit_message_text(text=ok, chat_id=message.chat.id, message_id=ko)
        else:
            bot.edit_message_text(text=dec, chat_id=message.chat.id, message_id=ko)
    else:
        bot.reply_to(message, f'''<b>♻️ 𝑨𝒉𝒉 𝑵𝒊𝒈𝒈𝒂 {message.from_user.first_name}!
━━━━━━━━━━━━━ 
🌟├𝒀𝒐𝒖𝒓 𝑹𝒂𝒏𝒌: 𓆩 𝑭𝒓𝒆𝒆 𓆪ꪾ 💔 
🌟├𝑩𝒖𝒚 𝑻𝒉𝒆 𝑷𝒓𝒆𝒎𝒊𝒖𝒎 𝑭𝒓𝒐𝒎 𝑴𝒚 𝑴𝒂𝒔𝒕𝒆𝒓 ━━━━━━━━━━━━━ 
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [ 𝑴𝒂𝒔𝒕𝒆𝒓 ]</b>''')










import time
from datetime import datetime, timedelta

# Define a dictionary to store the time of the last request for each user 
command_usage = {} # Default status of Gate 3 (activated) 
check_enabled_br3 = True

#@bot.message_handler(commands=['offb3'])
#def handle_admin_commands(message):
#    global check_enabled_br3
#    if str(message.from_user.id) in admins:
#        check_enabled_br3 = False
#        bot.send_message(chat_id=message.chat.id, text='- Focusing Check for Gateway 3 has been disabled. 🔒 No users can start the check until it is re-enabled.')
#    else:
#        bot.send_message(chat_id=message.chat.id, text='𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌')

#@bot.message_handler(commands=['onb3'])
#def handle_admin_commands(message):
#    global check_enabled_br3
#    if str(message.from_user.id) in admins:
#        check_enabled_br3 = True
#        bot.send_message(chat_id=message.chat.id, text='- Focusing Check for Gateway 3 has been re-enabled. ✅ Users can now start the check.')
#    else:
#        bot.send_message(chat_id=message.chat.id, text='𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌')

@bot.message_handler(func=lambda message: message.text.lower().startswith('.b3') or message.text.lower().startswith('/b3'))
def respond_to_vhk(message):
    global check_enabled_br3
    user_id = message.chat.id
    current_time = datetime.now()

    # Check the status of gateway 3
    if not check_enabled_br3:
        bot.reply_to(message, "<b> ♻️ 𝑮𝒂𝒕𝒆𝒘𝒂𝒚 𝒊𝒔 𝒖𝒏𝒅𝒆𝒓 𝒎𝒂𝒊𝒏𝒕𝒆𝒏𝒂𝒏𝒄𝒆.. </b>", parse_mode="HTML")
        return

    # Check if the user has the last usage time of the command
    if user_id in command_usage:
        last_time = command_usage[user_id]['last_time']
        time_diff = (current_time - last_time).seconds
        # Check if the interval time is less than 30 seconds
        if time_diff < 30:
            bot.reply_to(message, f"<b>♻️ 𝑻𝒓𝒚 𝒂𝒈𝒂𝒊𝒏 𝒂𝒇𝒕𝒆𝒓 {30 - time_diff} 𝒔𝒆𝒄𝒐𝒏𝒅𝒔.</b>", parse_mode="HTML")
            return
    
    # Update the time of the last request
    command_usage[user_id] = {'last_time': current_time}

    if check_user_plan(user_id):
        cc = message.text.replace('.b3 ', '').replace('/b3 ', '')
        gate='Braintree Auth 2'
        ko = bot.reply_to(message, '𝑷𝒓𝒐𝒄𝒆𝒔𝒔𝒊𝒏𝒈 𝒚𝒐𝒖𝒓 𝒓𝒆𝒒𝒖𝒆𝒔𝒕...').message_id
        start_time = time.time()
        try:
            last = str(b3s(cc))
        except:
            last = '𝑭𝒂𝒊𝒍𝒆𝒅 𝒕𝒐 𝒍𝒐𝒂𝒅 𝒕𝒉𝒆 𝒈𝒂𝒕𝒆. ❌'
        end_time = time.time()
        execution_time = end_time - start_time

        dec = f'''<b>#Braintree_Auth2  🇷🇺 [/b3]
- - - - - - - - - - - - - - - - - - - - - - - -
𝐂𝐚𝐫𝐝: <code>{cc}</code>
𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
{str(dato(cc[:6]))}
- - - - - - - - - - - - - - - - - - - - - - - -
𝐆𝐚𝐭𝐞: {gate}
𝐓𝐢𝐦𝐞: {"{:.1f}".format(execution_time)} 𝐒𝐞𝐜.
- - - - - - - - - - - - - - - - - - - - - - - -
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>'''

        ok = f'''<b>#Braintree_Auth2  🇷🇺 [/b3]
- - - - - - - - - - - - - - - - - - - - - - - -
𝐂𝐚𝐫𝐝: <code>{cc}</code>
𝐒𝐭𝐚𝐭𝐮𝐬: 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
{str(dato(cc[:6]))}
- - - - - - - - - - - - - - - - - - - - - - - -
𝐆𝐚𝐭𝐞: {gate}
𝐓𝐢𝐦𝐞: {"{:.1f}".format(execution_time)} 𝐒𝐞𝐜.
- - - - - - - - - - - - - - - - - - - - - - - -
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>'''

        if "Insufficient Funds" in last or 'Invalid postal code' in last or '81724: Duplicate card exists in the vault.' in last or 'Nice! New payment method added.' in last or 'avs: Gateway Rejected: avs' in last:
            bot.edit_message_text(text=ok, chat_id=message.chat.id, message_id=ko)
        else:
            bot.edit_message_text(text=dec, chat_id=message.chat.id, message_id=ko)
    else:
        bot.reply_to(message, f'''<b>♻️ 𝑨𝒉𝒉 𝑵𝒊𝒈𝒈𝒂 {message.from_user.first_name}!
━━━━━━━━━━━━━ 
🌟├𝒀𝒐𝒖𝒓 𝑹𝒂𝒏𝒌: 𓆩 𝑭𝒓𝒆𝒆 𓆪ꪾ 💔 
🌟├𝑩𝒖𝒚 𝑻𝒉𝒆 𝑷𝒓𝒆𝒎𝒊𝒖𝒎 𝑭𝒓𝒐𝒎 𝑴𝒚 𝑴𝒂𝒔𝒕𝒆𝒓 ━━━━━━━━━━━━━ 
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [ 𝑴𝒂𝒔𝒕𝒆𝒓 ]</b>''')












import time
from datetime import datetime, timedelta

# Define a dictionary to store the time of the last request for each user
command_usage = {}

# Default state of gate 4 (activated)
check_enabled_br4 = True

#@bot.message_handler(commands=['offb4'])
#def handle_admin_commands(message):
#    global check_enabled_br4
#    if str(message.from_user.id) in admins:
#        check_enabled_br4 = False
#        bot.send_message(chat_id=message.chat.id, text='- Focusing Check for Gateway 4 has been disabled. 🔒 No users can start the check until it is re-enabled.')
#    else:
#        bot.send_message(chat_id=message.chat.id, text='𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌')

#@bot.message_handler(commands=['onb4'])
#def handle_admin_commands(message):
#    global check_enabled_br4
#    if str(message.from_user.id) in admins:
#        check_enabled_br4 = True
#        bot.send_message(chat_id=message.chat.id, text='- Focusing Check for Gateway 4 has been re-enabled. ✅ Users can now start the check.')
#    else:
#        bot.send_message(chat_id=message.chat.id, text='𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌')

@bot.message_handler(func=lambda message: message.text.lower().startswith('.sa') or message.text.lower().startswith('/sa'))
def respond_to_vhk(message):
    global check_enabled_br4
    user_id = message.chat.id
    current_time = datetime.now()
    
    # Check the status of gateway 4
    if not check_enabled_br4:
        bot.reply_to(message, "<b>♻️ 𝑮𝒂𝒕𝒆𝒘𝒂𝒚 𝒊𝒔 𝒖𝒏𝒅𝒆𝒓 𝒎𝒂𝒊𝒏𝒕𝒆𝒏𝒂𝒏𝒄𝒆.. </b>", parse_mode="HTML")
        return

    # Check if the user has the last usage time of the command
    if user_id in command_usage:
        last_time = command_usage[user_id]['last_time']
        time_diff = (current_time - last_time).seconds
        # Check if the interval time is less than 30 seconds
        if time_diff < 30:
            bot.reply_to(message, f"<b>♻️ 𝑻𝒓𝒚 𝒂𝒈𝒂𝒊𝒏 𝒂𝒇𝒕𝒆𝒓 {30 - time_diff} 𝒔𝒆𝒄𝒐𝒏𝒅𝒔.</b>", parse_mode="HTML")
            return
    
    # Update the time of the last request
    command_usage[user_id] = {'last_time': current_time}

    if check_user_plan(user_id):
        cc = message.text.replace('.sa ', '').replace('/sa ', '')
        gate='Stripe Auth 1'
        ko = bot.reply_to(message, '𝑷𝒓𝒐𝒄𝒆𝒔𝒔𝒊𝒏𝒈 𝒚𝒐𝒖𝒓 𝒓𝒆𝒒𝒖𝒆𝒔𝒕...').message_id
        start_time = time.time()
        try:
            last = str(stripea1(cc))
        except:
            last = '𝑭𝒂𝒊𝒍𝒆𝒅 𝒕𝒐 𝒍𝒐𝒂𝒅 𝒕𝒉𝒆 𝒈𝒂𝒕𝒆. ❌'
        end_time = time.time()
        execution_time = end_time - start_time

        dec = f'''<b>#Stripe_Auth 🇺🇸 [/sa]
- - - - - - - - - - - - - - - - - - - - - - - -
𝐂𝐚𝐫𝐝: <code>{cc}</code>
𝐒𝐭𝐚𝐭𝐮𝐬: 𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
{str(dato(cc[:6]))}
- - - - - - - - - - - - - - - - - - - - - - - -
𝐆𝐚𝐭𝐞: Stripe Auth 1
𝐓𝐢𝐦𝐞: {"{:.1f}".format(execution_time)} 𝐒𝐞𝐜.
- - - - - - - - - - - - - - - - - - - - - - - -
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>'''

        ok = f'''<b>#Stripe_Auth 🇺🇸 [/sa]
- - - - - - - - - - - - - - - - - - - - - - - -
𝐂𝐚𝐫𝐝: <code>{cc}</code>
𝐒𝐭𝐚𝐭𝐮𝐬: 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
{str(dato(cc[:6]))}
- - - - - - - - - - - - - - - - - - - - - - - -
𝐆𝐚𝐭𝐞: Stripe Auth 1
𝐓𝐢𝐦𝐞: {"{:.1f}".format(execution_time)} 𝐒𝐞𝐜.
- - - - - - - - - - - - - - - - - - - - - - - -
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>'''

        if "Thank you for your purchase!" in last:
            bot.edit_message_text(text=ok, chat_id=message.chat.id, message_id=ko)
        else:
            bot.edit_message_text(text=dec, chat_id=message.chat.id, message_id=ko)
    else:
        bot.reply_to(message, f'''<b>♻️ 𝑨𝒉𝒉 𝑵𝒊𝒈𝒈𝒂 {message.from_user.first_name}!
━━━━━━━━━━━━━ 
🌟├𝒀𝒐𝒖𝒓 𝑹𝒂𝒏𝒌: 𓆩 𝑭𝒓𝒆𝒆 𓆪ꪾ 💔 
🌟├𝑩𝒖𝒚 𝑻𝒉𝒆 𝑷𝒓𝒆𝒎𝒊𝒖𝒎 𝑭𝒓𝒐𝒎 𝑴𝒚 𝑴𝒂𝒔𝒕𝒆𝒓 ━━━━━━━━━━━━━ 
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [ 𝑴𝒂𝒔𝒕𝒆𝒓 ]</b>''')


################


#from datetime import datetime, timedelta

# Create a dictionary to track the last time each user used the command
#last_command_usage = {}

# Default status of Gate 1 (activated)
#check_enabled_ch1 = True

#@bot.message_handler(commands=['offch1'])
#def handle_admin_commands(message):
#    global check_enabled_ch1
#    if str(message.from_user.id) in admins:
#        check_enabled_ch1 = False
#        bot.send_message(chat_id=message.chat.id, text='- Charge Check for Gateway 1 has been disabled. 🔒 No users can start the check until it is re-enabled.')
#    else:
#        bot.send_message(chat_id=message.chat.id, text='- You are not the owner 🤍')

#@bot.message_handler(commands=['onch1'])
#def handle_admin_commands(message):
#    global check_enabled_ch1
#    if str(message.from_user.id) in admins:
#        check_enabled_ch1 = True
#        bot.send_message(chat_id=message.chat.id, text='- Charge Check for Gateway 1 has been re-enabled. ✅ Users can now start the check.')
#    else:
#        bot.send_message(chat_id=message.chat.id, text='- You are not the owner 🤍')

#@bot.message_handler(func=lambda message: message.text.lower().startswith('.ba') or message.text.lower().startswith('/ba'))
#def respond_to_vhk(message):
#    global check_enabled_ch1
#    user_id = message.chat.id
#    current_time = datetime.now()

#    # Check the status of gateway 1
#    if not check_enabled_ch1:
#        bot.reply_to(message, "<b>♻️ 𝑮𝒂𝒕𝒆𝒘𝒂𝒚 𝒊𝒔 𝒖𝒏𝒅𝒆𝒓 𝒎𝒂𝒊𝒏𝒕𝒆𝒏𝒂𝒏𝒄𝒆.. </b>", parse_mode="HTML")
#        return

#    # Check when the user last used the command
#    if user_id in last_command_usage:
#        time_diff = (current_time - last_command_usage[user_id]).seconds
#        if time_diff < 30:  # If the duration is less than 30 seconds
#            bot.reply_to(message, f"<b>♻️ 𝑻𝒓𝒚 𝒂𝒈𝒂𝒊𝒏 𝒂𝒇𝒕𝒆𝒓 {30 - time_diff} 𝒔𝒆𝒄𝒐𝒏𝒅𝒔.</b>", parse_mode="HTML")
#            return

#    # Update last usage time
#    last_command_usage[user_id] = current_time

#    if check_user_plan(user_id):
#        cc = message.text.replace('.ba ', '').replace('/ba ', '')
#        gate = 'ʙʀᴀɪɴᴛʀᴇᴇ ᴄʜᴀʀɢᴇ 𝟶.𝟻𝟶'
#        ko = bot.reply_to(message, '𝑷𝒓𝒐𝒄𝒆𝒔𝒔𝒊𝒏𝒈 𝒚𝒐𝒖𝒓 𝒓𝒆𝒒𝒖𝒆𝒔𝒕...').message_id
#        start_time = time.time()
#        try:
#            last = str(Tele4(cc))
#        except:
#            last = '𝑭𝒂𝒊𝒍𝒆𝒅 𝒕𝒐 𝒍𝒐𝒂𝒅 𝒕𝒉𝒆 𝒈𝒂𝒕𝒆. ❌'
#        end_time = time.time()
#        execution_time = end_time - start_time

#        dec = f'''<b>• Declined ❌

#ϟ Card ->  <code>{cc}</code>
#ϟ Status -> {last}
#ϟ Gate ->  ʙʀᴀɪɴᴛʀᴇᴇ ᴄʜᴀʀɢᴇ 𝟶.𝟻𝟶

#{str(dato(cc[:6]))}

#ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
#ϟ - Programmer -> @Ishowsandeshyyyyy⚡</b>'''

#        ok = f'''<b>• Approved ✅

#ϟ Card ->  <code>{cc}</code>
#ϟ Status -> {last}
#ϟ Gate -> ʙʀᴀɪɴᴛʀᴇᴇ ᴄʜᴀʀɢᴇ 𝟶.𝟻𝟶 $

#{str(dato(cc[:6]))}

#ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
#ϟ - Programmer -> @Ishowsandeshyyyyy⚡</b>'''

#        cvc = f'''<b>• Cvv Card ☑️        
#--------------------------------------------
#- Card -> <code>{cc}</code>
#- Message -> {last}
#- GateWay -> {gate}
#--------------------------------------------
#{str(dato(cc[:6]))}
#- Process Time -> {"{:.1f}".format(execution_time)} Seconds. 
#--------------------------------------------
#- Programmer • @Ishowsandeshyyyyy</b>'''

#        if 'CVV' in last or 'CCN' in last:
#            bot.edit_message_text(text=cvc, chat_id=message.chat.id, message_id=ko)
#        elif "Funds" in last or 'Invalid postal' in last or 'Charge 0.50$ ✅' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
#            bot.edit_message_text(text=ok, chat_id=message.chat.id, message_id=ko)
#        else:
#            bot.edit_message_text(text=dec, chat_id=message.chat.id, message_id=ko)
#    else:
#        bot.reply_to(message, f'''<b>♻️ 𝑨𝒉𝒉 𝑵𝒊𝒈𝒈𝒂 {message.from_user.first_name}!
#━━━━━━━━━━━━━ 
#🌟├𝒀𝒐𝒖𝒓 𝑹𝒂𝒏𝒌: 𓆩 𝑭𝒓𝒆𝒆 𓆪ꪾ 💔 
#🌟├𝑩𝒖𝒚 𝑻𝒉𝒆 𝑷𝒓𝒆𝒎𝒊𝒖𝒎 𝑭𝒓𝒐𝒎 𝑴𝒚 𝑴𝒂𝒔𝒕𝒆𝒓 ━━━━━━━━━━━━━ 
#♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [ 𝑴𝒂𝒔𝒕𝒆𝒓 ]</b>''')


###############

@bot.message_handler(func=lambda message: message.text.lower().startswith('.bin') or message.text.lower().startswith('/bin'))
def resgpond_to_vhk(message):
	cc = message.text.replace('.bin ', '').replace('/bin ', '')
	bot.reply_to(message,f'''<b>𝗕𝗜𝗡 𝗟𝗼𝗼𝗸𝘂𝗽 𝗥𝗲𝘀𝘂𝗹𝘁 🔍
	
𝗕𝗜𝗡 ⇾</b> <code>{cc}</code>

<b>{str(dato(cc[:6]))}</b>''')










import json
import threading
from datetime import datetime
import time




def get_user_info(user_id):
    try:
        chat = bot.get_chat(user_id)
        user_name = chat.first_name
        user_username = chat.username
        return user_name, user_username
    except Exception as e:
        m = (f"Error retrieving user info for ID {user_id}: {e}")
        return '-----------', '-----------'

def notify_admins(user_id, user_data):
    user_name, user_username = get_user_info(user_id)
    message = f'''⌛️ 𝑺𝒖𝒃𝒔𝒄𝒓𝒊𝒑𝒕𝒊𝒐𝒏 𝑬𝒙𝒑𝒊𝒓𝒆𝒅 𝑵𝒐𝒕𝒊𝒇𝒊𝒄𝒂𝒕𝒊𝒐𝒏. 
━━━━━━━━━━━━━ 
🌟├𝑼𝒔𝒆𝒓 𝑰𝑫: {user_id}
🌟├𝑼𝒔𝒆𝒓 𝑵𝒂𝒎𝒆: {user_name} 
🌟├𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆: @{user_username} 
🌟├𝑷𝒍𝒂𝒏: {user_data.get('plan', '𓆩 𝐅𝐫𝐞𝐞 𓆪ꪾ')}
🌟├𝑬𝒙𝒑𝒊𝒓𝒂𝒕𝒊𝒐𝒏 𝑫𝒂𝒕𝒆: {user_data.get('timer', 'N/A')}
━━━━━━━━━━━━━ 
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [ 🇳🇵 ]'''
    for admin_id in myid:
        bot.send_message(admin_id, message)

def notify_user(user_id):
    try:
        bot.send_message(
    user_id,
    '''<b>🔔 𝑵𝒆𝒘 𝑵𝒐𝒕𝒊𝒇𝒊𝒄𝒂𝒕𝒊𝒐𝒏. 
━━━━━━━━━━━━━ 
🌟├ 𝑺𝒖𝒃𝒔𝒄𝒓𝒊𝒑𝒕𝒊𝒐𝒏 𝑾𝒂𝒔 𝑬𝒙𝒑𝒊𝒓𝒆𝒅 𝑩𝒖𝒚 𝑨𝒈𝒂𝒊𝒏 𝑭𝒓𝒐𝒎 𝑴𝒚 𝑴𝒂𝒔𝒕𝒆𝒓. 
━━━━━━━━━━━━━ 
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [ 𝑴𝒂𝒔𝒕𝒆𝒓 ]</b>''',
    parse_mode='HTML'
)
    except Exception as e:
        m = (f"Error notifying user {user_id}: {e}")

def update_subscription_status():
    try:
        # Read users' data from data.json file
        with open('data.json', 'r') as file:
            json_data = json.load(file)
        
        current_time = datetime.now()
        updated = False  # Let us know if there are updates

        for user_id, user_data in json_data.items():
            timer_str = user_data.get('timer', None)
            if timer_str:
                try:
                    expiration_time = datetime.strptime(timer_str, "%Y-%m-%d %H:%M")
                    
                    if current_time > expiration_time:
                        user_data['plan'] = '𓆩 𝐅𝐫𝐞𝐞 𓆪ꪾ'
                        del user_data['timer']  # Delete time after update
                        updated = True
                        # Send a notification to the admin
                        notify_admins(user_id, user_data)
                        # Send notification to the user
                        notify_user(user_id)
                except ValueError:
                    m = (f"Date format error for user {user_id} with date {timer_str}")
        
        if updated:
            with open('data.json', 'w') as file:
                json.dump(json_data, file, indent=2, ensure_ascii=False)
            p = ("Subscription status updated.")
    
    except Exception as e:
        mm = (f"Error updating subscription status: {e}")

def schedule_check():
    while True:
        update_subscription_status()
        time.sleep(1)  # Check every minute 
        
        # Start the subscription verification process in a separate thread
check_thread = threading.Thread(target=schedule_check)
check_thread.start()















import json
from datetime import datetime, timedelta

# User plan verification function
def check_user_plan(user_id):
    with open('data.json', 'r') as file:
        json_data = json.load(file)
    if str(user_id) in json_data:
        user_plan = json_data[str(user_id)].get('plan', '𓆩 𝐅𝐫𝐞𝐞 𓆪ꪾ')
        timer = json_data[str(user_id)].get('timer', None)
        if user_plan != '𓆩 𝐅𝐫𝐞𝐞 𓆪ꪾ' and timer:
            date_str = timer.split('.')[0]
            try:
                provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                current_time = datetime.now()
                if current_time - provided_time <= timedelta(hours=0):  # Modify the subscription period as needed
                    return True
            except Exception as e:
                print(f"Error parsing date for user {user_id}: {e}")
                return False
    return False
    
    
    



@bot.message_handler(commands=['broadcast'])
def qwwe(message):
    if str(message.from_user.id) in myid:
        mp, erop = 0, 0
        try:
            idd = message.from_user.id
            mes = message.text.replace("/broadcast ", "")
            bot.send_message(idd, mes)

            # Send messages to subscribers from data.json
            with open('data.json', 'r') as file:
                json_data = json.load(file)

            for user_id, details in json_data.items():
                if check_user_plan(user_id):
                    try:
                        mp += 1
                        bot.send_message(user_id, text=mes)
                    except Exception as e:
                        erop += 1
                        print(f"Error sending message to user {user_id}: {e}")

            bot.reply_to(message, f'''♻️ 𝑩𝒓𝒐𝒂𝒅𝒄𝒂𝒔𝒕 𝑾𝒂𝒔 𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍. 
━━━━━━━━━━━━━ 
🌟├𝑺𝒖𝒄𝒄𝒆𝒔𝒔 𝑼𝒔𝒆𝒓'𝒔 ✅ -> {mp}
🌟├𝑭𝒂𝒊𝒍𝒆𝒅 𝑼𝒔𝒆𝒓'𝒔 ❌-> {erop}
━━━━━━━━━━━━━ 
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]''')
        except Exception as err:
            bot.reply_to(message, f'❌ 𝑭𝒂𝒊𝒍𝒆𝒅 : {err}')
    else:
        bot.reply_to(message, "𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌")












@bot.message_handler(commands=["total_users"])
def adode(message):
    if str(message.from_user.id) in myid:
        with open('data.json', 'r') as file:
            json_data = json.load(file)
        
        vip_count = 0
        for user_id, details in json_data.items():
            user_plan = details.get('plan', '𓆩 𝐅𝐫𝐞𝐞 𓆪ꪾ')
            timer = details.get('timer', None)
            if user_plan != '𓆩 𝐅𝐫𝐞𝐞 𓆪ꪾ' and timer:
                try:
                    date_str = timer.split('.')[0]
                    provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                    current_time = datetime.now()
                    if current_time - provided_time <= timedelta(hours=0):  # Modify the subscription period as needed
                        vip_count += 1
                except Exception as e:
                    print(f"Error parsing date for user {user_id}: {e}")

        bot.reply_to(message, f'👁‍🗨 𝑻𝒐𝒕𝒂𝒍 𓆩 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𓆪ꪾ 𝑼𝒔𝒆𝒓𝒔: {vip_count}')
    else:
        bot.reply_to(message, "𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌")











import json
from datetime import datetime

@bot.message_handler(commands=['showp'])
def show_vip_subscribers(message):
    if str(message.chat.id) in myid:
        try:
            with open('data.json', 'r') as file:
                json_data = json.load(file)
        except Exception as e:
            bot.send_message(message.chat.id, f'- Error reading data file: {e}')
            return

        total_subscribers = 0
        subscriber_details = []

        for user_id, user_data in json_data.items():
            plan = user_data.get('plan', 'NO PLAN')
            if plan == '𓆩 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𓆪ꪾ':
                timer = user_data.get('timer', 'NO EXPIRATION DATE')
                if timer != 'NO EXPIRATION DATE':
                    try:
                        expiration_date = datetime.strptime(timer, "%Y-%m-%d %H:%M")
                        expiration_date_str = expiration_date.strftime("%Y-%m-%d %H:%M")
                    except ValueError:
                        expiration_date_str = 'INVALID DATE FORMAT'
                else:
                    expiration_date_str = 'NO EXPIRATION DATE'
                
                # Get user details
                try:
                    chat = bot.get_chat(user_id)
                    user_name = chat.first_name
                    user_username = chat.username
                    if user_name:
                        user_display = f"Name: {user_name}\nUsername: @{user_username}" if user_username else f"Name: {user_name}\nUsername: Not Available"
                    else:
                        # Skip users with no valid name
                        continue
                except Exception as e:
                    # Skip users with errors retrieving data
                    continue
                
                subscriber_details.append(f'''🌟 𝑼𝒔𝒆𝒓 𝑰𝑫: {user_id}
{user_display}
🌟 𝑷𝒍𝒂𝒏: {plan}
🌟 𝑬𝒙𝒑𝒊𝒓𝒂𝒕𝒊𝒐𝒏 𝑫𝒂𝒕𝒆: {expiration_date_str}
━━━━━━━━━━━━━━━━━━━━━━
''')

                total_subscribers += 1

        if subscriber_details:
            details_message = "\n".join(subscriber_details)
            bot.send_message(message.chat.id, f'''𓆩 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𓆪ꪾ  𝑼𝒔𝒆𝒓 𝑫𝒆𝒕𝒂𝒊𝒍𝒔 🎅 


{details_message} - 𝑻𝒐𝒕𝒂𝒍 𓆩 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𓆪ꪾ 𝑼𝒔𝒆𝒓𝒔 -> {total_subscribers} 🥷''')
        else:
            bot.send_message(message.chat.id, '❌ 𝑵𝒐,𓆩 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𓆪ꪾ 𝑼𝒔𝒆𝒓𝒔 𝒇𝒐𝒖𝒏𝒅.')











import json
from datetime import datetime

def remove_subscription(user_id):
    try:
        # Read users' data from data.json file
        with open('data.json', 'r') as file:
            json_data = json.load(file)
        
        if user_id in json_data:
            # Convert plan to FREE
            json_data[user_id]['plan'] = '𓆩 𝐅𝐫𝐞𝐞 𓆪ꪾ'
            del json_data[user_id]['timer']  # Delete time if any 
            # Write the modified data to data.json
            with open('data.json', 'w') as file:
                json.dump(json_data, file, indent=2, ensure_ascii=False)
            p = (f"Subscription for user {user_id} has been set to FREE.")
        else:
            mm= (f"User ID {user_id} not found in data.json.")
    
    except Exception as e:
        m = (f"Error removing subscription for user {user_id}: {e}")

@bot.message_handler(commands=['remove'])
def qwwem(message):
    if str(message.chat.id) in admins:
        user_id = message.text.replace("/remove ", "")
        
        # Convert user subscription to FREE
        remove_subscription(user_id)
        
        try:
            chat = bot.get_chat(user_id)
            frs = chat.first_name
            use = chat.username
            bot.send_message(message.chat.id, f'''𝑫𝒐𝒏𝒆 ✅   

🌟 𝑵𝒂𝒎𝒆 𝑺𝒖𝒃𝒔𝒄𝒓𝒊𝒃𝒆𝒓 -> <code>{frs}</code>
🌟 𝑼𝒔𝒆𝒓 𝑺𝒖𝒃𝒔𝒄𝒓𝒊𝒃𝒆𝒓 -> @{use}
🌟 𝑰𝑺 𝑹𝒆𝒎𝒐𝒗𝒆𝒅 𝑭𝒓𝒐𝒎 𝑺𝒖𝒃𝒔𝒄𝒓𝒊𝒃𝒆𝒓𝒔 ✅''')
        except Exception as e:
            bot.send_message(message.chat.id, f'''𝑼𝒏𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍 𝑹𝒆𝒎𝒐𝒗𝒂𝒍 ❌  


🌟 𝑼𝒔𝒆𝒓 𝒎𝒊𝒈𝒉𝒕 𝒏𝒐𝒕 𝒉𝒂𝒗𝒆 𝒐𝒑𝒆𝒏𝒆𝒅 𝒚𝒐𝒖𝒓 𝒃𝒐𝒕.  - 𝑬𝒓𝒓𝒐𝒓 -> {e}''')
    else:
        bot.send_message(message.chat.id, "𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌")















@bot.message_handler(commands=['id'])
def send_user_info(message):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_username = message.from_user.username or '------------------'  # Handle the case of no username
    
    response_message = f'''🆔 𝑰𝑫 » <code>{user_id}</code>
📛 𝑵𝒂𝒎𝒆 » {user_first_name}
🧑 𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆 » @{user_username}'''
    
    bot.reply_to(message, response_message, parse_mode='HTML')






@bot.message_handler(commands=["admin"])
def adodre(message):
	if str(message.chat.id) in myid:
		bot.reply_to(message,'''<b>♻️𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝑻𝒐 𝑨𝒅𝒎𝒊𝒏 𝑷𝒂𝒏𝒆𝒍.. ━━━━━━━━━━━━━━━━━━━  
🌟├ 𝑫𝒆𝒔𝒄𝒓𝒊𝒑𝒕𝒊𝒐𝒏: 𝑺𝒕𝒂𝒓𝒕 𝑪𝒉𝒆𝒄𝒌 𝑩𝒐𝒕  
🌟├ 𝑼𝒔𝒂𝒈𝒆: /start 
━━━━━━━━━━━━━━━━━━━ 
🌟├ 𝑫𝒆𝒔𝒄𝒓𝒊𝒑𝒕𝒊𝒐𝒏: 𝑨𝒅𝒅 𝑵𝒆𝒘 𝑺𝒖𝒃𝒔𝒄𝒓𝒊𝒃𝒆𝒓 
🌟├ 𝑼𝒔𝒂𝒈𝒆: /add telegram_id ━━━━━━━━━━━━━━━━━━━ 
🌟├ 𝑫𝒆𝒔𝒄𝒓𝒊𝒑𝒕𝒊𝒐𝒏: 𝑻𝒐𝒕𝒂𝒍 𝑩𝒐𝒕 𝑼𝒔𝒆𝒓𝒔 
🌟├ 𝑼𝒔𝒂𝒈𝒆: /total_users ━━━━━━━━━━━━━━━━━━━ 
🌟├ 𝑫𝒆𝒔𝒄𝒓𝒊𝒑𝒕𝒊𝒐𝒏: 𝑩𝒓𝒐𝒂𝒅𝒄𝒂𝒔𝒕 𝑻𝒐 𝑼𝒔𝒆𝒓'𝒔. 
🌟├ 𝑼𝒔𝒂𝒈𝒆: /broadcast message ━━━━━━━━━━━━━━━━━━━ 
🌟├ 𝑫𝒆𝒔𝒄𝒓𝒊𝒑𝒕𝒊𝒐𝒏: 𝑹𝒆𝒎𝒐𝒗𝒆 𝑨 𝑷𝒓𝒆𝒎𝒊𝒖𝒎 𝑼𝒔𝒆𝒓. 
🌟├ 𝑼𝒔𝒂𝒈𝒆: /remove telegram_id ━━━━━━━━━━━━━━━━━━━ 
🌟├ 𝑫𝒆𝒔𝒄𝒓𝒊𝒑𝒕𝒊𝒐𝒏: 𝑺𝒉𝒐𝒘 𝑷𝒓𝒆𝒎𝒊𝒖𝒎 𝑼𝒔𝒆𝒓'𝒔. 
🌟├ 𝑼𝒔𝒂𝒈𝒆: /showp ━━━━━━━━━━━━━━━━━━━ 
🌟├ 𝑫𝒆𝒔𝒄𝒓𝒊𝒑𝒕𝒊𝒐𝒏: 𝑺𝒕𝒐𝒑 𝑨𝒏𝒅 𝑺𝒕𝒂𝒓𝒕 𝑻𝒉𝒆 𝑮𝒂𝒕𝒆𝒔 
🌟├ 𝑼𝒔𝒂𝒈𝒆: /loda
━━━━━━━━━━━━━━━━━━━ 
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>''')
	
@bot.message_handler(func=lambda message: message.text.lower().startswith('.buy') or message.text.lower().startswith('/buy'))
def respondn_to_vhk(message):
 bot.reply_to(message, '''<b>⚡️𝔎𝔦𝔯𝔱𝔦 𝔓𝔯𝔦𝔠𝔦𝔫𝔤 :</b>
━━━━━━━━━━━━━━━━━━
<b>𝔅𝓮𝓷𝓮𝓯𝓲𝓽𝓼 :</b>
<b>- <i>Combo Checker.</i></b>
<b>- <i>Manual Checker.</i></b>
━━━━━━━━━━━━━━━━━━
● <b>Starter</b> - Premium Access For 1 Week at <b>$2</b>

● <b>Silver</b> - Premium Access For 15 Days at <b>$5</b>

● <b>Gold</b> - Premium Access For 1 Month at <b>$10</b>
━━━━━━━━━━━━━━━━━━
<i><b>🥷 Note: All plans are available for 7, 15, or 30 days. Once your plan expires, you will need to purchase a new one to continue using our services. Please note that all purchases are non-refundable, and you cannot transfer plans to another account.</b></i>
━━━━━━━━━━━━━━━━━━
<b>𝔉𝓸𝓻 𝔅𝓾𝔶𝓲𝓷𝓰 :
- @iShowSandesheyyyyy [ 𝔒𝔴𝓷𝓮𝓻 ]</b>
''', parse_mode='HTML')

import json
import threading
from datetime import datetime, timedelta
import random
import string

# Code generation function
@bot.message_handler(commands=["code"])
def generate_code(message):
    def my_function():
        id = message.from_user.id
        if not str(id) in myid:
            return
        try:
            h = float(message.text.split(' ')[1])
            with open('data.json', 'r') as json_file:
                existing_data = json.load(json_file)
            
            characters = string.ascii_uppercase + string.digits
            pas = 'Kirti-' + '2024' +'-' + ''.join(random.choices(characters, k=4))
            current_time = datetime.now()
            expiration_time = current_time + timedelta(hours=h)
            plan = '𓆩 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𓆪ꪾ'
            expiration_time_str = expiration_time.strftime("%Y-%m-%d %H:%M")
            
            new_data = {
                pas: {
                    "plan": plan,
                    "timer": expiration_time_str
                }
            }
            
            existing_data.update(new_data)
            
            with open('data.json', 'w') as json_file:
                json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
            
            msg = f'''<b>𝑲𝒆𝒚 𝑪𝒓𝒆𝒂𝒕𝒆𝒅 🔑
━━━━━━━━━━━━━━━━━━            
🌟├𝑻𝒉𝒆 𝒌𝒆𝒚 𝒆𝒙𝒑𝒊𝒓𝒆𝒔 -> {expiration_time_str}
🌟├𝑲𝒆𝒚 -> <code>{pas}</code>
🌟├𝑼𝒔𝒂𝒈𝒆 ->  /redeem key
🌟├𝑹𝒂𝒏𝒌 -> 𓆩 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𓆪ꪾ
━━━━━━━━━━━━━
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>'''
            bot.reply_to(message, msg, parse_mode="HTML")
        except Exception as e:
            print('ERROR : ', e)
            bot.reply_to(message, f'<b>ERROR : {e}</b>', parse_mode="HTML")

    my_thread = threading.Thread(target=my_function)
    my_thread.start()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# Code recovery function
@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def respond_to_vbv(message):
    def my_function():
        try:
            # Extract the code from the message
            re = message.text.split(' ')[1]
            
            # Read data from data.json
            with open('data.json', 'r') as file:
                json_data = json.load(file)
            
            # Check if the code exists in the data
            if re in json_data:
                timer = json_data[re].get('timer', 'Unknown')
                typ = json_data[re].get('plan', '𓆩 𝐅𝐫𝐞𝐞 𓆪ꪾ')

                # Update current user data
                json_data[str(message.from_user.id)] = {
                    'timer': timer,
                    'plan': typ
                }
                
                # Delete old code
                del json_data[re]
                
                # Write the modified data to data.json
                with open('data.json', 'w') as file:
                    json.dump(json_data, file, indent=2, ensure_ascii=False)

                msg = f'''<b>𝑹𝒆𝒅𝒆𝒎𝒑𝒕𝒊𝒐𝒏 𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍 ♻️
━━━━━━━━━━━━━
🌟├𝒀𝒐𝒖𝒓 𝑹𝒂𝒏𝒌 -> 𓆩 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𓆪ꪾ
🌟├𝑬𝒙𝒑𝒊𝒓𝒊𝒏𝒈 𝒕𝒊𝒎𝒆 -> {timer}
━━━━━━━━━━━━━
♻️ 𝑩𝒐𝒕 𝑩𝒚 -> @iShowSandesheyyyyy [🇳🇵]</b>'''
                bot.reply_to(message, msg, parse_mode="HTML")
            else:
                bot.reply_to(message, '❌ <b>𝑰𝒏𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒄𝒐𝒅𝒆 𝒐𝒓 𝒊𝒕 𝒉𝒂𝒔 𝒂𝒍𝒓𝒆𝒂𝒅𝒚 𝒃𝒆𝒆𝒏 𝒓𝒆𝒅𝒆𝒆𝒎𝒆𝒅.</b>', parse_mode="HTML")

        except KeyError as e:
            print(f'KeyError: {e}')
            bot.reply_to(message, '❌ <b>𝑰𝒏𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒄𝒐𝒅𝒆 𝒐𝒓 𝒊𝒕 𝒉𝒂𝒔 𝒂𝒍𝒓𝒆𝒂𝒅𝒚 𝒃𝒆𝒆𝒏 𝒓𝒆𝒅𝒆𝒆𝒎𝒆𝒅.</b>', parse_mode="HTML")
        except Exception as e:
            print('ERROR : ', e)
            bot.reply_to(message, '⚙ <b>𝑻𝒉𝒆𝒓𝒆 𝒘𝒂𝒔 𝒂𝒏 𝒆𝒓𝒓𝒐𝒓 𝒑𝒓𝒐𝒄𝒆𝒔𝒔𝒊𝒏𝒈 𝒚𝒐𝒖𝒓 𝒓𝒆𝒒𝒖𝒆𝒔𝒕. 𝑷𝒍𝒆𝒂𝒔𝒆 𝒕𝒓𝒚 𝒂𝒈𝒂𝒊𝒏 𝒍𝒂𝒕𝒆𝒓.</b>', parse_mode="HTML")

    my_thread = threading.Thread(target=my_function)
    my_thread.start()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# Function of adding new user to VIP plan
@bot.message_handler(commands=['add'])
def add_subscription(message):
    def my_function():
        try:
            chid = message.chat.id
            command_text = message.text.replace('/add ', '')
            user_id, duration_hours = command_text.split()
            duration_hours = int(duration_hours)
            
            if str(message.chat.id) in myid:
                current_time = datetime.now()
                expiration_time = current_time + timedelta(hours=duration_hours)
                expiration_time_str = expiration_time.strftime("%Y-%m-%d %H:%M")
                plan = '𓆩 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𓆪ꪾ'
                
                with open('data.json', 'r') as json_file:
                    existing_data = json.load(json_file)
              
                existing_data[user_id] = {
                    'timer': expiration_time_str,
                    'plan': plan
                }
                
                with open('data.json', 'w') as json_file:
                    json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
                    
                try:
                    chat = bot.get_chat(user_id)
                    frs = chat.first_name
                    use = chat.username
                    user_display = f"𝑵𝒂𝒎𝒆: {frs}\n𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆: @{use}" if use else f"𝑵𝒂𝒎𝒆: {frs}\n𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆: 𝑵𝒐𝒕 𝑨𝒗𝒂𝒊𝒍𝒂𝒃𝒍𝒆"
                except Exception as e:
                    user_display = f"𝑵𝒂𝒎𝒆: 𝑼𝒏𝒌𝒏𝒐𝒘𝒏\n𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆: 𝑼𝒏𝒌𝒏𝒐𝒘𝒏"
                
                bot.send_message(chid, f'''✅ 𝑫𝒐𝒏𝒆 𝑨𝒅𝒅 -> <code>{user_id}</code> 

 🌟 𝑺𝒖𝒃𝒔𝒄𝒓𝒊𝒑𝒕𝒊𝒐𝒏 𝑫𝒖𝒓𝒂𝒕𝒊𝒐𝒏 -> {duration_hours} 𝒉𝒐𝒖𝒓𝒔 

🌟 {user_display} - 𝑨𝒅𝒅𝒆𝒅 𝒕𝒐 𝑺𝒖𝒃𝒔𝒄𝒓𝒊𝒃𝒆𝒓𝒔 𝑳𝒊𝒔𝒕 ✅''')
            else:
                bot.send_message(chid, ' 𝑳𝒐𝒐𝒌𝒔 𝒍𝒊𝒌𝒆 𝒚𝒐𝒖’𝒓𝒆 𝒏𝒐𝒕 𝒂𝒖𝒕𝒉𝒐𝒓𝒊𝒛𝒆𝒅 𝒂𝒔 𝒕𝒉𝒆 𝒐𝒘𝒏𝒆𝒓. ❌')
        except Exception as e:
            bot.reply_to(message, f'𝑭𝒂𝒊𝒍𝒆𝒅. -> {e}')

    my_thread = threading.Thread(target=my_function)
    my_thread.start()



def menu_callback(call):
	id=call.from_user.id
	stopuser[f'{id}']['status'] = 'stop'
print("The bot has been launched")
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print(f"An error occurred: {e}")
		continue