import time
import telepot
from telepot.loop import MessageLoop
WEATHER_BASE_URL = 'api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}'

WEATHER_CITY_NAME = 'q='

WEATHER_CITY_LAT = 'lat='

WEATHER_CITY_LNG = 'lon='

WEATHER_UNIT = 'metric'

WEATHER_DAY_CNT = 1
def previsaoTempo(chat_id):
    return str(bot.sendLocation(chat_id,WEATHER_CITY_LAT,WEATHER_CITY_LNG))
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
    msg = str.upper(msg)
    call = msg.find("ALFRED")
    if call != -1:
        return True

#Checagem do chamado do trocadilho
def checkCall(msg):
    msg = str.upper(msg)
    call = msg.find("TROCADILHO")
    if call != -1:
        return "trocadilho"

#API fornecida para o tratamento de texto
>>>>>>> master
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if content_type == 'text' and callAlfred(msg['text']):
        bot.sendMessage(chat_id,'Olá Amo')
    if content_type == 'text' and checkCall(msg['text']) == "trocadilho":
        bot.sendMessage(chat_id,trocadilho())
    if content_type == 'text' and checkCall(msg['text']) == "previsao":
        bot.sendMessage(chat_id,trocadilho())
bot = telepot.Bot("354305351:AAFAAnzBnsE43UPScoGRXO-a_qjZpEIgZkM")
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
