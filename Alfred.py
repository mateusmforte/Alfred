import sys
import time
import telepot
from telepot.loop import MessageLoop

#Função para busca das frases de trocadilhos do arquivo
def trocadilho ():
    from random import randint
    trocadilhos = []
    num = randint(0,99)
    arquivo = open("trocadilhos.txt","r",encoding='UTF-8')
    texto = str(arquivo.read())
    linha_trocadilho = texto.split('\n')
    for linha in linha_trocadilho:
        trocadilhos.append(linha)
    return trocadilhos[num]

#Função para interpretar as formas de chamar o Alfred
def callAlfred(msg):
    calls = ['ALFRED','OI ALFRED','HEY ALFRED']
    for each in calls:
        if str.upper(msg) == each:
            return True

#Checagem do chamado do trocadilho
def checkCall(msg):
    if str.upper(msg) == "ALFRED CONTE-ME UM TROCADILHO":
        return "trocadilho"

#API fornecida para o tratamento de texto
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if content_type == 'text' and callAlfred(msg['text']):
        bot.sendMessage(chat_id,'Olá Amo')
    if content_type == 'text' and checkCall(msg['text']) == "trocadilho":
        bot.sendMessage(chat_id,trocadilho())

bot = telepot.Bot("354305351:AAFAAnzBnsE43UPScoGRXO-a_qjZpEIgZkM")
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
