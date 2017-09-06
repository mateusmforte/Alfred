import sys
import time
import telepot
from telepot.loop import MessageLoop
from random import randint
def trocadilho ():
    trocadilhos = []
    num = randint(0,99)
    arquivo = open("C:/Users/m-for/Documents/GitHub/Alfred/Alfred/trocadilhos.txt","r",encoding='utf-8')
    texto = arquivo.read()
    trocadilho = texto.split('\n')
    for linha in trocadilho:
        l = linha.split(',')
        trocadilhos.append(l) 
    return trocadilhos[num]
def callAlfred(msg):
    calls = ['ALFRED','OI ALFRED','HEY ALFRED']
    for each in calls:
        if str.upper(msg) == each:
            return True
def checkCall(msg):
    if str.upper(msg) == "ALFRED CONTE-ME UM TROCADILHO":
        return True
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if content_type == 'text' and callAlfred(msg['text']):
        bot.sendMessage(chat_id,'Olá Amo')
    if content_type == 'text' and checkCall(msg['text']):
        bot.sendMessage(chat_id,trocadilho())
bot = telepot.Bot("354305351:AAFAAnzBnsE43UPScoGRXO-a_qjZpEIgZkM")
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
