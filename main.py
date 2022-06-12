import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from OneClick import Hunter
from faker import Faker 
import json
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start'])
def boten(message):
	
    
    
    mas = types.InlineKeyboardMarkup(row_width=2)
    
    A = types.InlineKeyboardButton(text ="HUNTER", callback_data="F1")
    
    E = types.InlineKeyboardButton(text ="SOON", callback_data="F2") 
    
    M = types.InlineKeyboardButton('DEVLOPER', url='https://t.me/ONCLIK')
    
    mas.add(A,E,M)
    
    bot.send_message(message.chat.id, f"HUNTER CHECKER BY MOHAMMED ALMUSWI",reply_markup=mas)
    
    
@bot.callback_query_handler(func=lambda call: True)
def masg(call):
	
	
	global nam
	
	if call.data =="MohammedNajih":
		
		mas = types.InlineKeyboardMarkup(row_width=2)
		
		A = types.InlineKeyboardButton(text ="HUNTER", callback_data="F1")

		E = types.InlineKeyboardButton(text ="SOON", callback_data="F2") 

		M = types.InlineKeyboardButton('DEVLOPER', url='https://t.me/ONCLIK')
		
		M = types.InlineKeyboardButton('DEVLOPER', url='https://t.me/ONCLIK')
		
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="HUNTER CHECKER BY MOHAMMED ALMUSWI",reply_markup=mas)

	elif call.data =="F1":
		ho=0;gm=0;ins=0;ya=0;ma=0;ou=0;ao=0;bd=0
		while True:
			sets= ['@gmail.com','@aol.com','@yahoo.com','@mail.ru','@hotmail.com','@outlook.com']
			user1 = Faker().email().split("@")[0]
			us = random.choice(sets)
			user = user1+us
			if (user.split('@')[1])=='gmail.com':
					email= user 
					gmail = Hunter.Gmail(str(email))
					if str('[[["gf.wuar",1,[]]') in gmail:
						gm+=1
						Instagram = Hunter.Instagram(str(email))
						if (Instagram["status"]) == "Successful":
							ins+=1
							bot.send_message(message.chat.id,email)
			elif (user.split('@')[1])=='aol.com':
					email= user
					aol = Hunter.Aol(str(email))
					if (aol["status"]) == "Successful":
						ao+=1
						Instagram = Hunter.Instagram(str(email))
						if (Instagram["status"]) == "Successful":
							ins+=1
							bot.send_message(message.chat.id,email)
			elif (user.split('@')[1])=='mail.ru':
					email= user
					mailur = Hunter.Mailru(str(email))
					if (mailur["status"]) == "Successful":
						ma+=1
						Instagram = Hunter.Instagram(str(email))
						if (Instagram["status"]) == "Successful":
							ins+=1
							bot.send_message(message.chat.id,email)
			elif (user.split('@')[1])=='yahoo':
					email= user
					yahoo = Hunter.Yahoo(str(email))
					if (yahoo["status"]) == "Successful":
						ya+=1
						Instagram = Hunter.Instagram(str(email))
						if (Instagram["status"]) == "Successful":
							ins+=1
							bot.send_message(message.chat.id,email)
			elif (user.split('@')[1])=='hotmail.com':
					email = user
					hotmail = Hunter.Hotmail(str(email))
					if (hotmail["status"]) == "Successful":
						ho+=1
						Instagram = Hunter.Instagram(str(email))
						if (Instagram["status"]) == "Successful":
							ins+=1
							bot.send_message(message.chat.id,email)
			elif (user.split('@')[1])=='@outlook.com':
				email= user
				outlook = Hunter.Hotmail(str(email))
				if (outlook["status"]) == "Successful":
					ou+=1
					Instagram = Hunter.Instagram(str(email))
					if (Instagram["status"]) == "Successful":
						ins+=1
						bot.send_message(message.chat.id,email)
			else:
				bd+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				G = types.InlineKeyboardButton(f'GMAIL:{gm}',callback_data="1x")
				Y = types.InlineKeyboardButton(f'YAHOO:{ya}', callback_data="1x")
				I = types.InlineKeyboardButton(f'INSTAGRAM:{ins}', callback_data="1x")
				H = types.InlineKeyboardButton(f'HOTMAIL:{ho}', callback_data="1x")
				O = types.InlineKeyboardButton(f'OUTLOOK:{ou}', callback_data="1x")
				A = types.InlineKeyboardButton(f'AOL:{ao}', callback_data="1x")
				M = types.InlineKeyboardButton(f'MAIL.RU:{ma}', callback_data="1x")
				E = types.InlineKeyboardButton(f'EMAIL:{email}', callback_data="1x")
				S = types.InlineKeyboardButton(f'ERORR:{bd}', callback_data="1x")
				D = types.InlineKeyboardButton('المطور', url='https://t.me/t_4gi')
				mas.add(G,Y,I,H,O,S,A,M,E,D)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="FUCKED HUNTER",reply_markup=mas)
				
	elif call.data =="F2":
		os.system('rm -rf done.txt')
@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://hmody7.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
