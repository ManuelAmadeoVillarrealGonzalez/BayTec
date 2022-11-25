from datetime import datetime

#Aqui jalamos el codigo en donde se jala la info de la base de datos
from subPastillero import *

#Jalamos la hora actual y la establecemos en formato hora:minuto
now = datetime.now()
tiempo = now.strftime("%H:%M")

print(tiempo) # Impirmimos la hora actual

if tiempo == "16:30"  :print("Ya es hora perro") #Prueba para el tiempo actual

if pastilleroLau == "4": print("holA WE") #Prueba para obetner varibale pastilleroLau

#Modificamos la varibale horarioLau para que nos la de en formato de lista ya accesible 
horarioLau = horarioLau.translate({ord('['):None, ord(']'):None, ord('"'):None}) 
horarioLau = horarioLau.split(',')

#Recorremos la lista e imprimimos horario por horario dentro de la lista
for horario in horarioLau:
  print(horario)
  if horario == tiempo: print("A darle canijo") #Cuando la hora real coincida con una de las horas de la lista esto se ejecuta
  if horario == "23:45": print("Hora inventada") #Este se ejecuta al ser la misma hora que esta dentro de la lista
