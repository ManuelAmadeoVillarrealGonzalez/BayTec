import paho.mqtt.publish as publish ## pip install paho-mqtt
from smbus2 import SMBus ## pip install smbus2
from mlx90614 import MLX90614 ## pip install pymlx90614
from time import sleep
import max30102
import hrcalc



## Define the variables for communicating with ThingSpeak. Edit the channel ID and MQTT device credentials.
# The ThingSpeak Channel ID.
# Replace <YOUR-CHANNEL-ID> with your channel ID.
channel_ID = "1859288" #Lau
channel_ID1 = "1860152" #Anthony
channel_ID2 = "1860153" #Amadeo
channel_ID3 = "1860154" #Alonso

#Declaramos el sensor de temperatura con sus respectivas variables
bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)
bandera=True
#declaramos el sensor de bpm y oxigenacion con sus respectivas variables
m = max30102.MAX30102()

# The hostname of the ThingSpeak MQTT broker.
mqtt_host = "mqtt3.thingspeak.com"

# Your MQTT credentials for the device
mqtt_client_ID = "KA00OAwDATsSFjcuBjQMCBk"
mqtt_username  = "KA00OAwDATsSFjcuBjQMCBk"
mqtt_password  = "M2lJDMOS31T6OEfrk8WRz9jD"

##Define the connection type as websockets, and set the port to 80.
t_transport = "websockets"
t_port = 80

# Create the topic string.
topic = "channels/" + channel_ID + "/publish"
topic1 = "channels/" + channel_ID1 + "/publish"
topic2 = "channels/" + channel_ID2 + "/publish"
topic3 = "channels/" + channel_ID3 + "/publish"

##Funciones a definir
def elegirpaciente(paciente):
    if paciente=='Laura':
        tmp=topic
        print("Se selecciono el paciente :"+str(paciente))
    elif paciente=='Anthony':
        tmp=topic1
        print("Se selecciono el paciente :"+str(paciente))
    elif paciente=='Amadeo':
        tmp=topic2
        print("Se selecciono el paciente :"+str(paciente))
    elif paciente=='Alonso':
        tmp=topic3
        print("Se selecciono el paciente :"+str(paciente))
    else:
        print("No existe ese paciente")
        
    return tmp    


def medicionsensores(bandera,topico):
    medicionestemp=0
    medicionesbpm=0
    hr2 = 0
    sp2 = 0
    while (bandera==True):
        
        while medicionestemp<=5 :
            temp=sensor.get_obj_temp()
            #print ("Object Temperature :", round(temp,2),"°C")
            payload1 = "field1=" + str(temp) #+ "&field2=" + str(2) + "&field3=" + str(1)
            sleep(1)
            medicionestemp=medicionestemp+1
            try:
                print ("Writing Payload = ", payload1," to host: ", mqtt_host, " clientID= ", mqtt_client_ID, " User ", mqtt_username, " PWD ", mqtt_password)
                publish.single(topico, payload1, hostname=mqtt_host, transport=t_transport, port=t_port, client_id=mqtt_client_ID, auth={'username':mqtt_username,'password':mqtt_password})
        
            except (keyboardInterrupt):
                break
            except Exception as e:
                print (e)
                
        print("Se tomaron las medidas de temperatura")
        bus.close()
        
        sleep(2)
        
        while medicionesbpm<=5 :
            red, ir = m.read_sequential()
            hr,hrb,sp,spb = hrcalc.calc_hr_and_spo2(ir, red)
            hr2 = float(hr)
            sp2 = float(sp)
            payload1 ="&field2=" + str(sp2) + "&field3=" + str(hr2)
            sleep(1)
            if(hrb == True and hr != -999 and spb==True and sp!=-999):
                if(hr>70 and sp>85):
                    try:
                        print ("Writing Payload = ", payload1," to host: ", mqtt_host, " clientID= ", mqtt_client_ID, " User ", mqtt_username, " PWD ", mqtt_password)
                        publish.single(topico, payload1, hostname=mqtt_host, transport=t_transport, port=t_port, client_id=mqtt_client_ID, auth={'username':mqtt_username,'password':mqtt_password})
                        medicionesbpm=medicionesbpm+1
                    except (keyboardInterrupt):
                        break
                    except Exception as e:
                        print (e)
                  
                
        print("Se tomaron las medidas de spo2")
        m.shutdown()
        
        bandera=False

#Programa Principal
topicopaciente=elegirpaciente("Alonso")
medicionsensores(bandera,topicopaciente)