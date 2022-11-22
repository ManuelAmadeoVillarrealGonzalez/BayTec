#testing connection with database

from datetime import datetime
from time import sleep
from gtts import gTTS
from playsound import playsound
import math
import time
from interbotix_xs_modules.locobot import InterbotixLocobotXS
from subPastillero import *
import socket

HOST = "192.168.211.15"  # The server's hostname or IP address
PORT = 65432  # The port used by the server




# This script uses the perception pipeline to pick up objects and place them in some virtual basket on the left side of the robot
# It also uses the AR tag on the arm to get a better idea of where the arm is relative to the camera (though the URDF is pretty accurate already).
#
# To get started, open a terminal and type...
#'roslaunch interbotix_xslocobot_nav xslocobot_nav.launch robot_model:=locobot_wx250s use_lidar:=true localization:=true use_nav:=true robot_name:=locobot'
# 'roslaunch interbotix_xslocobot_control xslocobot_python.launch robot_model:=locobot_wx250s use_perception:=true use_armtag:=true use_static_transform_pub:=true use_nav:=true localization:=true'
# include robot name in roslaunch if using base 
# Then change to this directory and type 'python pick_place_armtag.py'

def takeVitalSigns(bot,valor):
    #agregar sensores
    print("Taking vital signs")
    bot.camera.pan_tilt_move(0, -0.9)    
    bot.arm.set_ee_pose_components(x=0.2, z=0.6, pitch=-math.pi/6.0, moving_time=2)
    #topicopaciente=datos.elegirpaciente("Amadeo")
    #datos.medicionsensores(True,topicopaciente)
    bot.arm.set_ee_cartesian_trajectory(roll=-math.pi/2, moving_time=1)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
         s.connect((HOST, PORT))
         value = bytes(valor, encoding= 'utf-8')
         s.send(value)#1 Lau #2Anthony #3Amadeo #4Alonso
         data = s.recv(1024)
         sleep(5)
         bot.arm.set_ee_cartesian_trajectory(roll=math.pi, moving_time=1)
    
def roomTwo(bot,patient):
    playsound('Traslado.mp3')
    bot.base.move_to_pose(-1.4,2.15,0,True)
    bot.base.move(0,math.pi/2,2.7)
    bot.base.move(0.3,0,4.5)
    bot.base.move(0,-math.pi/2,0.7)
    givePills(bot,patient)
    bot.base.move(0,-math.pi/2,2.0)
    bot.base.move(0.3,0,4.2)
    bot.base.move_to_pose(-1.4,1,0,True)
    bot.base.move(0,-math.pi/2,1.42)

def givePills(bot,patient):
    #audio_ReconocimientoFacial.save('ReconocimientoFacial.mp3')
    #añadir face recognition en lugar de "Laura"
    if("Laura" == patient):
       bot.gripper.open()
       print("Patient matches")
       #agregar medicion de sensores
       takeVitalSigns(bot,"1")
    else:
       print("Wrong patient")
    print("Done attending patient ", patient," returning to table")
    bot.arm.set_ee_pose_components(x=0.2, z=0.2)
    bot.arm.go_to_sleep_pose()
   

def roomOne(locobot,patient):
    playsound('Traslado.mp3')
    locobot.base.move_to_pose(-1.4,2.35,0,True)
    #turning to enter room
    locobot.base.move(0.3,0,3.7)
    locobot.base.move(0,math.pi/2,0.7)
    givePills(locobot,patient)
    locobot.base.move(0,math.pi/2,2.2)
    locobot.base.move(0.3,0,3.7)
    #table position
    locobot.base.move_to_pose(-1.4,1,0,True)
    locobot.base.move(0,-math.pi/2,1.42)

def pickPills(pillNumber,bot,patient):
    
    okClusters=[] 
   
    print("Picking pill")

    if (pillNumber== "1"):
    	clusterNumber = 0
    elif (pillNumber == "2"):
    	clusterNumber = 1
    bot.arm.go_to_sleep_pose()
    time.sleep(1)
    bot.base.move(0.3,0,1.1)
    # move camera such that it's tilting down
    bot.camera.pan_tilt_move(0, 0.6)
    # position the arm such that the Apriltag is clearly visible to the camera
    bot.arm.set_ee_pose_components(x=0.2, z=0.3, pitch=-math.pi/8.0)
    # sleep half a second to give time for the arm to settle after moving
    time.sleep(0.5)
    # get the transform of the AR tag relative to the camera frame; based on that transform,
    # publish a new transform from the 'locobot/plate_link' to the 'locobot/arm_base_link'
    bot.armtag.find_ref_to_arm_base_transform(position_only=True)
    # move the arm out of the way of the camera
    bot.arm.go_to_sleep_pose()
    # get the positions of any clusters present w.r.t. the 'locobot/arm_base_link';
    # sort the clusters such that they appear from left-to-right w.r.t. the 'locobot/arm_base_link'
    time.sleep(0.5)
    #bot.pcl.set_z_filter_min(0.3)
    #bot.pcl.set_cluster_max_size(400)
    bot.camera.pan_tilt_move(0,0.4)
    time.sleep(0.5)
    success, clusters = bot.pcl.get_cluster_positions(ref_frame="locobot/arm_base_link", sort_axis="y", num_samples=5, reverse=True)
    # move the robot back so it's centered and open the gripper
    bot.arm.set_ee_pose_components(x=0.2, z=0.4, moving_time=1.5)
    bot.gripper.open()
    playsound('RecogePastillas.mp3')
   
    # pick up each object from left-to-right and drop it in a virtual basket on the left side of the robot
    for cluster in clusters:
        print(cluster)
        x, y, z = cluster["position"]
        print("Z is:",z)
        if (z>=0.27): 
            okClusters.append(cluster)
            
    for cluster in okClusters:
        print(cluster)
        print(okClusters.index(cluster))
        if (okClusters.index(cluster)== clusterNumber):
            x, y, z = cluster["position"]
            print("Cluster position:", cluster["position"])
            bot.arm.set_ee_pose_components(x=x-0.007, y=y+0.01, z=z+0.05,moving_time=2.0)
            bot.arm.set_ee_pose_components(x=x-0.007, y=y+0.01, z=z-0.025)
            bot.gripper.close()
            bot.arm.set_ee_pose_components(x=x, y=y, z=z+0.125,moving_time=2.0)
            bot.base.move(-0.3,0,0.5)
            bot.arm.set_ee_pose_components(x=0.25, z=z)
            #bot.arm.set_ee_cartesian_trajectory(z=-0.2)
            #bot.arm.set_ee_pose_components(x=x, z=0.2)
            #bot.gripper.open()
    bot.arm.set_ee_pose_components(x=0.2,z=0.2,moving_time =2.0)
    bot.camera.pan_tilt_move(0,0.2)
    bot.base.move(-0.3,0,1.0)
    if (pillNumber == "1"):
        roomOne(bot,patient)
    elif(pillNumber == "2"):
        roomTwo(bot,patient)

def main():
    playsound('Inicio.mp3')
    bot = InterbotixLocobotXS(robot_model="locobot_wx250s", arm_model="mobile_wx250s", use_move_base_action=True)
    sleep(10)
    #Jalamos la hora actual y la establecemos en formato hora:minuto
    now = datetime.now()
    tiempo = now.strftime("%H:%M")
    bot.gripper.open()
    print(tiempo) # Impirmimos la hora actual
    bot.arm.go_to_sleep_pose()
    #Modificamos la varibale horarioLau para que nos la de en formato de lista ya accesible 
    horarioLau, pastilleroL = pastilleroLau()
    print("Pastillero:", pastilleroL)
    bot.camera.pan_tilt_move(0,0.3)
    bot.base.move_to_pose(-1.4,1,0,True)
    bot.base.move(0,-math.pi/2,1.42)
    #Recorremos la lista e imprimimos horario por horario dentro de la lista
    flag=0
    while(flag==1):
        for horario in horarioLau:
            if horario == datetime.now().strftime("%H:%M"):
                time == horario
                print("its time")
                pickPills(pastilleroL,bot,"Laura")
                #while(time == datetime.now().strftime("%H:%M")):
                   # print("waiting")

    #bot.base.move(0.0,3.14,1.4)
    pickPills("1",bot,"Laura")
                
if __name__=='__main__':
    main()

