# Importamos las líbrerías
from gtts import gTTS 
from playsound import playsound

idioma = 'es'
lento = True
rapido = False
paciente1 = 'Laura'
paciente2 = 'Anthony'
paciente3 = 'Amadeo'
paciente4 = 'Alonso'

audio_Inicio = gTTS(text = "Qué bonito día, hora de trabajar", lang = idioma, slow = rapido)
audio_Inicio.save('Inicio.mp3')
playsound('.\Inicio.mp3')

audio_BuscandoPastillas = gTTS(text = "Tuuututuuu laaalaralaaa... buscando pastillas, oh, aquí están", lang = idioma, slow = rapido)
audio_BuscandoPastillas.save('RecogePastillas.mp3')
playsound('.\RecogePastillas.mp3')

audio_Traslado = gTTS(text = "Abran paso perras, que no veo equisde, no ya al chile, no esquivo y tengo que entregar éstas pinches pastillas", lang = idioma, slow = rapido)
audio_Traslado.save('Traslado.mp3')
playsound('.\Traslado.mp3')

audio_Saludo = gTTS(text = "Hola soy BayTec, tu asistente médico personal", lang = idioma, slow = rapido)
audio_Saludo.save('Saludo.mp3')
playsound('.\Saludo.mp3')

audio_ReconocimientoFacial = gTTS(text = "Por favor, acerca tu rostro, veré si eres el paciente al que debo darle éstas pastillas", lang = idioma, slow = rapido)
audio_ReconocimientoFacial.save('ReconocimientoFacial.mp3')
playsound('.\ReconocimientoFacial.mp3')

audio_paciente1 = gTTS(text = "Hola" + paciente1 + ", ¡que guapa te ves hoy!", lang = idioma, slow = rapido)
audio_paciente1.save('Paciente1.mp3')
playsound('.\Paciente1.mp3')

audio_paciente2 = gTTS(text = "Hola" + paciente2 + ", ¡que guapo te ves hoy!", lang = idioma, slow = rapido)
audio_paciente2.save('Paciente2.mp3')
playsound('.\Paciente2.mp3')

audio_paciente3 = gTTS(text = "Hola" + paciente3 + ", ¡que guapo te ves hoy!", lang = idioma, slow = rapido)
audio_paciente3.save('Paciente3.mp3')
playsound('.\Paciente3.mp3')

audio_paciente4 = gTTS(text = "Hola" + paciente4 + ", ¡que guapo te ves hoy!", lang = idioma, slow = rapido)
audio_paciente4.save('Paciente4.mp3')
playsound('.\Paciente4.mp3')

audio_pacienteNoEncontrado = gTTS(text = "Chale, aquí no está el paciente, me voy a mimir", lang = idioma, slow = rapido)
audio_pacienteNoEncontrado.save('PacienteNoEncontrado.mp3')
playsound('.\PacienteNoEncontrado.mp3')

audio_EntregaPastillas = gTTS(text = "Toma, te entrego tus pastillas", lang = idioma, slow = rapido)
audio_EntregaPastillas.save('EntregaPastillas.mp3')
playsound('.\EntregaPastillas.mp3')

# Audio Toma de Temperatura
txt_Temperatura = "Ahora te voy a tomar la temperatura... acerca tu dedo no muerdo"
audio_Temperatura = gTTS(text = txt_Temperatura, lang = idioma, slow = rapido)
audio_Temperatura.save('TomaTemperatura.mp3') 
playsound('.\TomaTemperatura.mp3')


# Audio Cambio de Sensor
txt_CambioDeSensor = "Listo, puedes quitar tu dedo, dame un momento"
audio_CambioDeSensor = gTTS(text = txt_CambioDeSensor, lang = idioma, slow = rapido)
audio_CambioDeSensor.save('CambioDeSensor.mp3') 
playsound('.\CambioDeSensor.mp3')


# Audio Toma de Ritmo cardíaco y Oxígeno
txt_BMPyOxi = "Ahora te voy a tomar tu ritmo cardíaco y concentración de oxígeno, acerca tu dedo otra vez, por favor"
audio_BMPyOxi = gTTS(text = txt_BMPyOxi, lang = idioma, slow = rapido)
audio_BMPyOxi.save('TomaBMPyOxi.mp3') 
playsound('.\TomaBMPyOxi.mp3')

audio_Despedida = gTTS(text = "Listo, es todo por ahora. Puedes ver tus signos vitales en la App de ThinkSpeak, bye bye", lang = idioma, slow = rapido)
audio_Despedida.save('Despedida.mp3')
playsound('.\Despedida.mp3')

""" # Texto a convertir en audio 
txt_Bienvenida = "Hola, soy BayTec. Tu asistente médico personal uwu"
  
# Realizamos la conversión del texto a voz 
audio_Bienvenida = gTTS(text = txt_Bienvenida, lang = 'es', slow = True)
# Finalmente guardamos el archivo de Audio
audio_Bienvenida.save('BayTecBienvenida.mp3') 
playsound('.\BayTecBienvenida.mp3') """

""" # Audio Petateado
txt_Petateado = "uuuuuuuu... ya te petateaste"
audio_Petateado = gTTS(text = txt_Petateado, lang = 'es', slow = False)
audio_Petateado.save('BayTecPetateado.mp3') 
playsound('.\BayTecPetateado.mp3') """