#!/usr/bin/python3
import os
from dotenv import load_dotenv
import telebot
from telebot import types

load_dotenv(r"/etc/spectralvpn_data/secret.env")
TOKEN = os.getenv('SPECTRALVPN_TG_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message) :
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text="Зарегистрироватся"))
