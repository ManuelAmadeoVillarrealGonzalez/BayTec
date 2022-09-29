from smbus2 import SMBus
from mlx90614 import MLX90614
from time import sleep


bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)
mediciones=0
while mediciones<=10:
    temp=sensor.get_amb_temp()
    tempob=sensor.get_obj_temp()
    print ("Ambient Temperature :",round(temp,2),"°C")
    print ("Object Temperature :", round(tempob,2),"°C")
    sleep(0.5)
    mediciones=mediciones+1
bus.close() 