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