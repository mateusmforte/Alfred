import sys
import time
import telepot
from telepot.loop import MessageLoop
from random import randint
def trocadilho ():
    trocadilhos = {
        1:"Eu sempre me preocupo com aquilo, ainda mais quando se trata de comida a quilo.",
        2:"Gata, você é Ágata? Sim por quê? Porque você é a gata.",
        3:"Meu bolso não é aquário, mas está cheio de peixe.",
        4:"Gata, você não é bebida alcoólica, mas Ice eu te pego.",
        5:"Encontrei com uma mina, pisei nela e explodiu.",
        6:"Não dê risada de tudo, porque quem acha tudo gozado é faxineira de motel.",
        7:"Seu nome é Tais? Não, por quê? Porque taistrovando!",
        8:"A enxada é de João, a foice é de Mané e o machado de Assis.",
        9:"Eu sou aquele cara que as minas tudo disputa, diz: puta que pariu que cara feio.",
        10:"É sempre bom contratar um demônio pra ser seu jardineiro, além de cortar, ele pentagrama."
    }
    num = randint(1,10)
    return(trocadilhos[num])
def checkTxtMsg(msg):
    calls = ['ALFRED','OI ALFRED','HEY ALFRED']
    for each in calls:
        if str.upper(msg) == each:
            return True


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)


    if content_type == 'text' and checkTxtMsg(msg['text']):
        bot.sendMessage(chat_id,trocadilho())

bot = telepot.Bot("354305351:AAFAAnzBnsE43UPScoGRXO-a_qjZpEIgZkM")
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
