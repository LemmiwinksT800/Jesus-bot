import sqlite3
import TOKEN
import os
from aiogram import Bot,types
connection = sqlite3.connect('sources.db')
b=connection.cursor()
message = types.Message
bot = Bot(token=TOKEN.TOKEN)
for i in os.listdir('music'):
    f = open('music/'+i,'rb')
    g=bot.send_audio(f)
