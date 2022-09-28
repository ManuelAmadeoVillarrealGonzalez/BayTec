# Importamos las líbrerías
from gtts import gTTS 
from playsound import playsound

# Idioma
l = 'es'

### Audio de presentación ###
# Texto a convertir en audio 
txt_Walle = "Waaaaaaaaaaaaaaaaaaaaaaaaaaaaaallyyyyyyyyyyy....."
# Realizamos la conversión del texto a voz 
audio_Walle = gTTS(text = txt_Walle, lang = l, slow = True)
# Finalmente guardamos el archivo de Audio
audio_Walle.save('Walle.mp3') 
playsound('.\Walle.mp3')