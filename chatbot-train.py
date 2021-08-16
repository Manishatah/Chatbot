from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('bot')
bot.set_trainer(ListTrainer)

for files in os.listdir('D:/demo projects/Chatbot_Project-master/data/'):   #put your own file path
         convoData = open('D:/demo projects/Chatbot_Project-master/data/' + files,'r').readlines()
         bot.train(convoData)

while True:
    message = input('you : ')
    if message.strip() != 'Bye':  
        reply = bot.get_response(message)
        print('chatbot :',reply)
    if message.strip() == 'Bye':
        print('Chatbot : Bye')
        break
