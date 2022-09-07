# Importamos las líbrerías
from gtts import gTTS 
from playsound import playsound

# Texto a convertir en audio 
txt_Bienvenida = "Hola, soy BayTec. Tu asistente médico personal uwu"
  
# Realizamos la conversión del texto a voz 
audio_Bienvenida = gTTS(text = txt_Bienvenida, lang = 'es', slow = True)
# Finalmente guardamos el archivo de Audio
audio_Bienvenida.save('BayTecBienvenida.mp3') 
playsound('.\BayTecBienvenida.mp3')

# Audio Petateado
txt_Petateado = "uuuuuuuu... ya te petateaste"
audio_Petateado = gTTS(text = txt_Petateado, lang = 'es', slow = False)
audio_Petateado.save('BayTecPetateado.mp3') 
playsound('.\BayTecPetateado.mp3')