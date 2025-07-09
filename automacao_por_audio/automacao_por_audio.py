print("testando")

import speech_recognition as sr
import os

# Função para ouvir e reconhecer a fala
def ouvir_microfone():
    # Habilita o microfone
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        # Reduz ruído ambiente
        microfone.adjust_for_ambient_noise(source)

        print("Diga alguma coisa:")
        audio = microfone.listen(source)

    try:
        # Reconhece a fala com API do Google
        frase = microfone.recognize_google(audio, language='pt-BR')

        # Comandos personalizados por voz
        if "navegador" in frase:
            os.system("start chrome.exe")
        elif "Excel" in frase:
            os.system("start Excel.exe")
        elif "Word" in frase:
            os.system("start winword.exe")
        elif "Bloco de notas" in frase or "notas" in frase:
            
            os.system("start notepad.exe")
        elif "pasta downloads" in frase:
            os.startfile(r"C:\Users\CLIENTE\Downloads")
        elif "meu drive" in frase:
            os.startfile(r"C:\Users\CLIENTE\OneDrive")
        elif "site do Google" in frase:
            os.system("start https://www.google.com")
        elif "YouTube" in frase:
            os.system("start https://www.youtube.com")
        elif "abrir calculadora" in frase:
            os.system("start calc.exe")
        else:
            print("Comando não reconhecido.")

        print("Você disse: " + frase)

    except sr.UnknownValueError:
        print("Não entendi")

    return frase

# Chamada da função
ouvir_microfone()
