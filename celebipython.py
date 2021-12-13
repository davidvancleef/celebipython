from datetime import date
from datetime import datetime


def bomdia():
    usuario = input('Quem está a utilizar o sistema Celebi?\n')
    hora_atual = datetime.now().strftime('%H')
    if 4 < int(hora_atual) < 13:
        print ("Bom dia, senhor {}!".format(usuario))
    elif 12 < int(hora_atual) < 19:
        print ("Boa tarde, senhor {}!".format(usuario))
    elif int(hora_atual) > 18:
        print ("Boa noite, senhor {}!".format(usuario))
    else:
        print ("Boa madrugada, senhor {}!".format(usuario))


def interpretaFrase(frase):
    if perguntaOuOrdem(frase) == 0:
        return 0


def perguntaOuOrdem(frase):
    if "?" in frase:
        print("O senhor fez uma pergunta.")
        return 1
    elif "." in frase:
        print("O senhor deu uma ordem.")
        return 1
    else:
        print("Comando não reconhecido. Tente novamente.")
        return 0


def faladia():
    data_atual = date.today()
    print("Hm, hoje é", data_atual, ".")


################################################################
if __name__ == '__main__':
    bomdia()
    opcao = "a"
    while opcao != "0":
        opcao = input("O que faremos hoje?\n")
        interpretaFrase(opcao)
        if "dia" in opcao and "hoje" in opcao and "?" in opcao:
            faladia()
