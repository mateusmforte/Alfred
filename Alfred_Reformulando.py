import sys
import time
import telepot
from telepot.loop import MessageLoop
import calls

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if content_type == 'text' and calls.callAlfred(msg['text']):
        if "trocadilho" in msg['text']: 
            if content_type == 'text' and calls.checkCall(msg['text']) == "trocadilho":
                bot.sendMessage(chat_id, calls.trocadilho())
        else:
            bot.sendMessage(chat_id,'Olá Amo')

bot = telepot.Bot("354305351:AAFAAnzBnsE43UPScoGRXO-a_qjZpEIgZkM")
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)