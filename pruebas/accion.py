from datetime import datetime
from playsound import playsound



def Gen ():
  ##saluda
    playsound('Audios de interacción/EntregaPastillas.mp3') # Audio de pastillas
    #da pastillas
    playsound('Audios de interacción/TomaTemperatura.mp3')#audio temperatura
    #mueve el brazo
    #audio acercar dedo
    #instruccion al soc para sensores con nombre
    #delay
    #audio que diga ya ouedes quitar el dedo
    #vlteo de griper
    playsound('Audios de interacción/CambioDeSensor.mp3') #adio del seguiente sensor
    playsound('Audios de interacción/TomaBMPyOxi.mp3')#tomar del siguiente sensor
    playsound('Audios de interacción/Despedida.mp3') #audio de agradecimiento 
    #se regresa a casa


def Alonso():
  if face_names == ['Alonso']: 
    print("Hola ALonso") 
    playsound('Audios de interacción/Saludo.mp3')
    playsound('Audios de interacción/Paciente4.mp3')
    Gen ()
  else : 
    playsound('Audios de interacción/PacienteNoEncontrado.mp3')
  
    

def Amadeo():
  if face_names == ['Amadeo']: 
    print("Hola Amadeo") 
    playsound('Audios de interacción/Saludo.mp3')
    playsound('Audios de interacción/Paciente3.mp3')
    Gen ()
  else : 
    playsound('Audios de interacción/PacienteNoEncontrado.mp3')  

def Anthony():
  if face_names == ['Anthony']: 
    print("Hola Anthony") 
    playsound('Audios de interacción/Saludo.mp3')
    playsound('Audios de interacción/Paciente2.mp3')
    Gen ()
  else : 
    playsound('Audios de interacción/PacienteNoEncontrado.mp3')

def Laura ():
  if face_names == ['Laura']: 
    print("Hola Laura") 
    playsound('Audios de interacción/Saludo.mp3')
    playsound('Audios de interacción/Paciente1.mp3')
    Gen ()
  else : 
    playsound('Audios de interacción/PacienteNoEncontrado.mp3')


while(True):
  #Aqui jalamos el codigo en donde se jala la info de la base de datos
  from subPastillero import *
  #Jalamos la hora actual y la establecemos en formato hora:minuto
  now = datetime.now()
  tiempo = now.strftime("%H:%M")
  print(tiempo) # Impirmimos la hora actual
  #Recorremos la lista e imprimimos horario por horario dentro de la lista
  for horario in horarioLau:
    print(horario)
    if horario == tiempo: 
      print("A darle canijo") #Cuando la hora real coincida con una de las horas de la lista esto se ejecuta
      #ir del locobot
      playsound('Audios de interacción/ReconocimientoFacial.mp3')
      from cv2_face_recognition import * #funcion face
      Laura() 

  for horario in horarioAnth:
    print(horario)
    if horario == tiempo: 
      print("A darle Anthony") #Cuando la hora real coincida con una de las horas de la lista esto se ejecuta
      #ir del locobot
      playsound('Audios de interacción/ReconocimientoFacial.mp3')
      from cv2_face_recognition import * #funcion face
      Anthony() 
          
  for horario in horarioAmad:
      print(horario)
      if horario == tiempo: 
        print("A darle Amadeo") #Cuando la hora real coincida con una de las horas de la lista esto se ejecuta
        #ir del locobot
        playsound('Audios de interacción/ReconocimientoFacial.mp3')
        from cv2_face_recognition import * #funcion face
        Amadeo() 

  for horario in horarioAlo:
      print(horario)
      if horario == tiempo: 
        print("A darle Alonso") #Cuando la hora real coincida con una de las horas de la lista esto se ejecuta   
        #ir del locobot
        playsound('Audios de interacción/ReconocimientoFacial.mp3')
        from cv2_face_recognition import * #funcion face
        Alonso()       


