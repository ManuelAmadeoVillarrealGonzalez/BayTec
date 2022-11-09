# Importamos las líbrerías
from gtts import gTTS 
from playsound import playsound

# Idioma
l = 'es'

### Audio de presentación ###
# Texto a convertir en audio 
txt_Presentacion = "Hola, soy BayTec.Tu asistente médico personal"
# Realizamos la conversión del texto a voz 
audio_Presentacion = gTTS(text = txt_Presentacion, lang = l, slow = True)
# Finalmente guardamos el archivo de Audio
audio_Presentacion.save('BayTecBienvenida.mp3') 
playsound('.\BayTecBienvenida.mp3')


# Audio Entrega de medicamento
txt_Entrega = "Te entrego tu medicamento"
audio_Entrega = gTTS(text = txt_Entrega, lang = l, slow = False)
audio_Entrega.save('BayTecEntrega.mp3') 
playsound('.\BayTecEntrega.mp3')

# Audio Toma de Oxigeno
txt_Oxigeno1 = "Te tomaré tu concentración de oxígeno, acerca tu dedo no muerdo"
audio_Oxigeno1 = gTTS(text = txt_Oxigeno1, lang = l, slow = False)
audio_Oxigeno1.save('BayTecOxigeno1.mp3') 
playsound('.\BayTecOxigeno1.mp3')

# Audio Tomó de Oxigeno
txt_Oxigeno2 = "Listo, puedes quitar tu dedo, dame un momento"
audio_Oxigeno2 = gTTS(text = txt_Oxigeno2, lang = l, slow = False)
audio_Oxigeno2.save('BayTecOxigeno2.mp3') 
playsound('.\BayTecOxigeno2.mp3')

# Audio Toma de Temperatura
txt_Temperatura1 = "Ahora te voy a tomar la temperatura..."
audio_Temperatura1 = gTTS(text = txt_Temperatura1, lang = l, slow = False)
audio_Temperatura1.save('BayTecTemperatura1.mp3') 
playsound('.\BayTecTemperatura1.mp3')

# Audio Tomó de Temperatura
txt_Temperatura2 = "Listo, ya te tomé la temperatura"
audio_Temperatura2 = gTTS(text = txt_Temperatura2, lang = l, slow = False)
audio_Temperatura2.save('BayTecTemperatura2.mp3') 
playsound('.\BayTecTemperatura2.mp3')

# Audio Petateado
txt_Petateado = "uuuuuuuu... ya te petateaste"
audio_Petateado = gTTS(text = txt_Petateado, lang = l, slow = False)
audio_Petateado.save('BayTecPetateado.mp3') 
playsound('.\BayTecPetateado.mp3')