from datetime import date
from datetime import datetime
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import webbrowser

def printar(texto):
    tts = gTTS(text=texto, lang='es')
    filename = "abc.mp3"
    tts.save(filename)
    playsound(filename)
    if os.path.exists("abc.mp3"):
        os.remove("abc.mp3")
    else:
        print("O arquivo não foi encontrado")

def bomdia(user): #This is just a function to greet you. She will ask you who's using Celebi to be aware how to call you whenever needed.
    hora_atual = datetime.now().strftime('%H')
    if 4 < int(hora_atual) < 13:
        printar ("Bom dia, senhor {}!".format(user))
    elif 12 < int(hora_atual) < 19:
        printar ("Boa tarde, senhor {}!".format(user))
    elif int(hora_atual) > 18:
        printar ("Boa noite, senhor {}!".format(user))
    else:
        printar ("Boa madrugada, senhor {}!".format(user))

## Desativados por enquanto.
#def interpretaFrase(frase):
    #if perguntaOuOrdem(frase) == 0:
        #return 0
#def perguntaOuOrdem(frase):
    #if "?" in frase:
        #printar("O senhor fez uma pergunta.")
        #return 1
    #elif "." in frase:
        #printar("O senhor deu uma ordem.")
        #return 1
    #else:
        #printar("Comando não reconhecido. Tente novamente.")
        #return 0


def faladia():
    data_atual = date.today()
    mes = transformaMes(data_atual)
    printar ("Hoje é {} de {} de {}!".format(data_atual.day, mes,data_atual.year))

def transformaMes(data_atual):
    if data_atual.month == 1:
        return "janeiro"
    if data_atual.month == 2:
        return "fevereiro"
    if data_atual.month == 3:
        return "março"
    if data_atual.month == 4:
        return "abril"
    if data_atual.month == 5:
        return "maio"
    if data_atual.month == 6:
        return "junho"
    if data_atual.month == 7:
        return "julho"
    if data_atual.month == 8:
        return "agosto"
    if data_atual.month == 9:
        return "setembro"
    if data_atual.month == 10:
        return "outubro"
    if data_atual.month == 11:
        return "novembro"
    if data_atual.month == 12:
        return "dezembro"

def ouvir_microfone():
    #Habilita o microfone do usuário
    
    while True:
        quebrar = 1
        microfone = sr.Recognizer()
        #usando o microfone
        with sr.Microphone() as source:
            #Chama um algoritmo de reducao de ruidos no som
              #microfone.adjust_for_ambient_noise(source)
            #Armazena o que foi dito numa variavel
            audio = microfone.listen(source)
        try:
            #Passa a variável para o algoritmo reconhecedor de padroes
            frase = microfone.recognize_google(audio,language='pt-BR')
            #Exibe o que a Celebi entendeu no terminal.
            print("Você disse: " + frase)
            if "desligar" in frase:
                exit()
        #Se nao reconhecer a fala.
        except sr.UnknownValueError:
            printar ("Não entendi, poderia repetir, por favor?")
            quebrar = 0
        if quebrar == 1:
            return frase

def defineUsuario():
    printar ("Quem está utilizando o sistema Célebi?")
    while (True):
        frase = ouvir_microfone()
        printar ("Seu nome é {}?".format(frase))
        confirmar = ouvir_microfone()
        if "sim" or "isso" or "é" or "confirma" or "certo" or "afirmativo" in confirmar:
            user = frase
            break
        else: printar ("Certo, repita seu nome para que eu possa entender.")
    return user

################################################################
if __name__ == '__main__':
    user = defineUsuario()
    bomdia(user)
    while True:
        printar("O senhor tem alguma ordem?\n")
        opcao = ouvir_microfone()
        if "dia" in opcao and "hoje" in opcao:
            faladia()
        if "spotify" in opcao or "Spotify" in opcao:
            os.system("Spotify")
        if "internet" in opcao:
            webbrowser.open("www.google.com")
        if "desligar" in opcao:
            break