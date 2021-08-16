from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('bot')
bot.set_trainer(ListTrainer)

while True:
    message = input('you : ')
    if message.strip() != 'Bye':  
        reply = bot.get_response(message)
        print('chatbot :',reply)
    if message.strip() == 'bye':
        print('Chatbot : Bye')
        break
