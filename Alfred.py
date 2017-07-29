import sys
import time
import telepot
from telepot.loop import MessageLoop
def checkTxtMsg(msg):
    calls = ['Alfred','alfred','Oi Alfred','oi alfred','Hey Alfred','hey alfred']
    for each in calls:
        if msg == each:
            return True

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text' and checkTxtMsg(msg['text']):
        bot.sendMessage(chat_id,'Ola Amo')

bot = telepot.Bot("354305351:AAFAAnzBnsE43UPScoGRXO-a_qjZpEIgZkM")
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
