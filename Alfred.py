import telepot
from pprint import pprint
from telepot.loop import MessageLoop
bot = telepot.Bot('354305351:AAEWwnWaZo_Dnn1hOr_PuVCQtuH_WwzAy5A')
bot.getMe()

response = bot.getUpdates()
pprint(response)
def handle(msg):
    pprint(msg)
MessageLoop(bot,handle).run_as_thread()
bot.sendMessage(131404726,'Olá!')
