from datetime import datetime

#Aqui jalamos el codigo en donde se jala la info de la base de datos
from pruebas.subPastillero3 import *
#from cv2_face_recognition import * # Este programa se correra completo en el moemto en donde se ponga

#Jalamos la hora actual y la establecemos en formato hora:minuto
now = datetime.now()
tiempo = now.strftime("%H:%M")

print(tiempo) # Impirmimos la hora actual

#if tiempo == "16:30"  :print("Ya es hora perro") #Prueba para el tiempo actual

#if pastilleroLau == "4": print("holA WE") #Prueba para obetner varibale pastilleroLau

#Recorremos la lista e imprimimos horario por horario dentro de la lista
for horario in horarioLau:
  print(horario)
  if horario == tiempo: print("A darle canijo") #Cuando la hora real coincida con una de las horas de la lista esto se ejecuta
  


#if face_names == ['Alonso']: print("Hola ALonso") 