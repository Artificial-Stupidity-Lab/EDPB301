from djitellopy import tello
import time
from time import sleep
import random
import math
#tkinter(GUI) libraries
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
from tkinter import filedialog as fd
#Imaging libraries
import cv2
import cvzone as cvz
import numpy as np
import serial as serial
###########################################################
#drone Variable
global velocity
velocity = 50 #standard drone speed
mode = "standby"
###########################################################
#object surveiallnce variables
x_pos, y_pos, angle, x_home, y_home = 0,0,0,0,0
speedObjects = 117/10  #cm/s
angularSpeedObjects = 50 #degrees/s
interval = 0.25
distanceInterval = speedObjects*interval
angularInterval = angularSpeedObjects*interval
###########################################################
#drone communication libraries

drone = tello.Tello()  #creating an object for the drone
drone.connect() #communicating with the drone
#drone.streamon()

arduino_data=serial.Serial("com3",baudrate = 9600, timeout=1)

#communication function
def listen():
    while(arduino_data.inWaiting()==0):
        pass
    dataPacket = arduino_data.readline()
    dataPacket=str(dataPacket, "utf-8")
    dataPacket=(dataPacket.strip("\r\n"))
    return dataPacket
def move():
    if(drone.is_flying==False):
        drone.takeoff()

    moves = listen()
    print(f"Next move is {moves}")
    velocity = 25
    if (moves=="left"):
        drone.send_rc_control(-velocity,0,0,0)
    elif(moves=="right"):
        drone.send_rc_control(velocity,0,0,0)
    elif(moves=="antiClockwise"):
        drone.send_rc_control(0,0,0,-velocity)
    elif (moves=="clockwise"):
        drone.send_rc_control(0,0,0,velocity)
        #drone.rotate_clockwise(10)
    elif (moves=="back"):
        drone.send_rc_control(0,-velocity,0,0)
    elif(moves=="forward"):
        drone.send_rc_control(0,velocity,0,0)
    elif(moves=="down"):
        drone.send_rc_control(0,0,-velocity,0)
    elif(moves=="up"):
        drone.send_rc_control(0,0,velocity,0)
    elif(moves=="none"):
        pass
    elif(moves=="takePic"):
        cv2.imwrite(f"C:/Users/mpilo/OneDrive - Durban University of Technology/Year 3/EDPB/Drone Project/Drone Data/{time.time()}.jpg",img)

    elif(moves=="landTakeoff"):
        drone.land()
        mode="standby"
    else:
        pass

    sleep(0.05)
    #imagingNormal()

#battery function
def msg_box_battery():
    #create function that reads battery from tello drone
    battery = drone.get_battery()
    messagebox.showinfo("Battery Status", f"The Drone's Battery is {battery}% full")

while(mode=="standby"):
    drone.land()
    mode = input("What mode do you want?: ")
    
    if (mode=="flight"):
        while mode=="flight":
            #tello(drone) librar
            move()

    if(mode=="battery"):
        msg_box_battery()
        mode="standby"
