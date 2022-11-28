#####Codigo unicamnte jala horario y pastillero de cada paciente como strings
from datetime import datetime

from gtts import gTTS 
from playsound import playsound

#Aqui jalamos el codigo en donde se jala la info de la base de datos
from pruebas.subPastillero3 import *

#Jalamos la hora actual y la establecemos en formato hora:minuto
now = datetime.now()
tiempo = now.strftime("%H:%M")

playsound('BayTecBienvenida.mp3')

print(tiempo) # Impirmimos la hora actual

#if pastilleroLau == "4": print("holA WE") #Prueba para obetner varibale pastilleroLau

while(True):
#Recorremos la lista e imprimimos horario por horario dentro de la lista
    for horario in horarioLau:
        print(horario)
        if horario == tiempo: 
            print("A darle Lau") #Cuando la hora real coincida con una de las horas de la lista esto se ejecuta

    for horario in horarioAnth:
        print(horario)
        if horario == tiempo: 
            print("A darle Anthony") #Cuando la hora real coincida con una de las horas de la lista esto se ejecuta
        
    for horario in horarioAmad:
        print(horario)
        if horario == tiempo: 
            print("A darle Amadeo") #Cuando la hora real coincida con una de las horas de la lista esto se ejecuta

    for horario in horarioAlo:
        print(horario)
        if horario == tiempo: 
            print("A darle Alonso") #Cuando la hora real coincida con una de las horas de la lista esto se ejecuta                   