import cv2
import numpy as np
import time
from playsound import playsound

from cv2_acquire_visualize_module import *
from face_recognition_module import *


#################################################################
# SENSING - PERCEPTION
# Setup and initialization of perception
video_capture = init_camera()
# LONG TERM MEMORY
# Load database of known face and encode
known_faces_encodings, known_faces_names = load_known_faces_and_encode(KNOWN_FACES_DIR)
#################################################################


#################################################################
# COMMUNICATION - LANGUAGE - PROTOCOLS
# Defining some time scales for communications
lastPublication = 0.0
PUBLISH_TIME   = 5     # seconds
#################################################################


#################################################################
# Perception-action-loop
#################################################################
# While ALIVE DO
while (True):
    #############################################################
    # SENSING LAYER
    rgb_frame, scaled_rgb_frame = acquire_image(video_capture)
    # Percepts are obtained
    face_locations, face_encodings = extract_faces_and_encode(scaled_rgb_frame)
    # Recognition is performed - Short-Long term memory
    face_names = find_face_matches(face_encodings, known_faces_encodings, known_faces_names)
    #############################################################
    
    
    #############################################################
    # COMMUNICATION LAYER: messages to trigger actions
    # on the external world (SPATIAL-temporal SCALES)
    if np.abs(time.time()-lastPublication) > PUBLISH_TIME:
        try:
            print(face_names)
        except (keyboardInterrupt):
            break
        except Exception as e:
            print(e)
        lastPublication = time.time()
    #############################################################
    
    
    #############################################################
    # CONTROL LAYER - triggered actions to
    # the local/remote environment
    #draw_face_info_on_frame(rgb_frame, face_locations, face_names)
    #show_frame (rgb_frame) #####    ESTA ES LA LINEA QUE SE COMENTA PARA NO ABRIR EL CUADRO DE CAMARA
    #############################################################
    
    if face_names != [] and face_names != ['Unknown'] : break #Se agrega esta condicion para que en cuanto detecte a alguien conocido se cierre y proceda
    else: playsound('Audios de interacción/PacienteNoEncontrado.mp3')
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # END OF THE GAME/LIFE
        break

# LAST STUFF BEFORE BEING OFICIALLY DEAD
# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
