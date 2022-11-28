#tello(drone) libraries
from djitellopy import tello
import time
from time import sleep
import csv
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
import pandas as pd
import serial as serial
global img
###########################################################
#drone Variable
global velocity
velocity = 30 #standard drone speed
global angularSpeedObjects
angularSpeedObjects = 30
global mode
mode = "standby"
###########################################################
#object surveiallnce variables
flight_time = []
real_time = []
picture_path = []
speedObjects = 30
frameWidth = 480
frameHeight = 360
frameCounter = 0
thres = 0.60
nmsThres = 0.2
mode = "surveyObjects"
global classNames
classNames = [] #use classID on excel
classFile = "Drone_Project_Code/coco.names"
with open(classFile,"rt") as f:
    classNames = f.read().split('\n')
configPath = "Drone_Project_Code/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightPath = "Drone_Project_Code/frozen_inference_graph.pb"
net = cv2.dnn_DetectionModel(weightPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5,127.5,127.5))
net.setInputSwapRB(True)
###########################################################
#drone communication libraries

'''
drone = tello.Tello()  #creating an object for the drone
drone.connect() #communicating with the drone
drone.streamon()
arduino_data=serial.Serial("com5",baudrate = 9600, timeout=1)
'''

#communication function
def listen():
    while(arduino_data.inWaiting()==0):
        pass
    dataPacket = arduino_data.readline()
    dataPacket=str(dataPacket, "utf-8")
    dataPacket=(dataPacket.strip("\r\n"))
    return dataPacket
'''
def talk(data):
    userInput = data+"\r"
    arduino_data.write(userInput.encode())
'''

###########################################################
#GUI variables
#objects list needs to be a tuple
objectsList = ["Please Select Object To Track",
                "Object | flight Time | Real Time",
                "b",
                "a",
                "a",
                "c"
]
###########################################################


#function for each button
def get_battery(event): 
    print("\nEntering Battery Mode")
    #create mesage box
    msg_box_battery()

def surveillance_mode(event): #mode0
    print("\nEntering Surveillance Mode")
    mode0Win()
    #create mesage box

def read_database(event):#mod1
    print("\nEntering Database Mode")
    root.destroy()
    database = pd.read_csv("C:/Users/mpilo/OneDrive - Durban University of Technology/Year 3/EDPB/Drone Project/Drone Data/droneData.csv")
    print("Here is the Database :\n")
    print(database)
    #open data base

def tracking_mode(event):#mode2
    print("\nEntering tracking Mode")
    mode2Win()
    #create a list of objects to track

def halt(event):#mode4
    print("\nEntering halt Mode")
    mode = "standby"
    halt_msg()
    #create mesage box

#creating message box function
def msg_box_battery():
    #create function that reads battery from tello drone
    battery = drone.get_battery()
    messagebox.showinfo("Battery Status", f"The Drone's Battery is {battery}% full")
def halt_msg():
    #land()
    drone.land()
    messagebox.showinfo("Halt", f"Drone Operations have been halted")
    

def flight_mode(): #mode5
    print("\nEntering Flight Mode")
    root.destroy()
    mode="flight"
    if (mode=="flight"):
        while mode=="flight":
            #tello(drone) librar
            imagingNormal()
            move()
            if mode=="standby":
                break
    mode="standby"
    
    
        
    #create mesage box

 #sureveillance function, how to survey   
def move():
    moves = listen()
    print(f"Next move is {moves}")
    velocity = 30
    if (moves=="left" and drone.is_flying==True):
        drone.send_rc_control(-velocity,0,0,0)
    elif(moves=="right" and drone.is_flying==True):
        drone.send_rc_control(velocity,0,0,0)
    elif(moves=="antiClockwise" and drone.is_flying==True):
        drone.send_rc_control(0,0,0,-velocity)
    elif (moves=="clockwise" and drone.is_flying==True):
        drone.send_rc_control(0,0,0,velocity)
        #drone.rotate_clockwise(10)
    elif (moves=="back" and drone.is_flying==True):
        drone.send_rc_control(0,-velocity,0,0)
    elif(moves=="forward" and drone.is_flying==True):
        drone.send_rc_control(0,velocity,0,0)
    elif(moves=="down" and drone.is_flying==True):
        drone.send_rc_control(0,0,-velocity,0)
    elif(moves=="up" and drone.is_flying==True):
        drone.send_rc_control(0,0,velocity,0)
    elif(moves=="none"):
        drone.send_rc_control(0, 0, 0, 0)
    elif(moves=="takePic"):
        cv2.imwrite(f"C:/Users/mpilo/OneDrive - Durban University of Technology/Year 3/EDPB/Drone Project/Drone Data/{time.time()}.jpg",img)
        time.sleep(1)

    elif(moves=="landTakeoff"):
        if(drone.is_flying==False):
            drone.takeoff()
            #mode=="flight"
        else:
            drone.land()
            #mode="standby"
    
    elif(moves=="standby"):
        drone.land()
        mode = "standby"
        

    else:
        pass

    #sleep(0.05)
    

def moveVegetation():
    moves = listen()
    print(f"Next move is {moves}")
    velocity = 30
    if (moves=="left" and drone.is_flying==True):
        drone.send_rc_control(-velocity,0,0,0)
    elif(moves=="right" and drone.is_flying==True):
        drone.send_rc_control(velocity,0,0,0)
    elif(moves=="antiClockwise" and drone.is_flying==True):
        drone.send_rc_control(0,0,0,-velocity)
    elif (moves=="clockwise" and drone.is_flying==True):
        drone.send_rc_control(0,0,0,velocity)
        #drone.rotate_clockwise(10)
    elif (moves=="back" and drone.is_flying==True):
        drone.send_rc_control(0,-velocity,0,0)
    elif(moves=="forward" and drone.is_flying==True):
        drone.send_rc_control(0,velocity,0,0)
    elif(moves=="down" and drone.is_flying==True):
        drone.send_rc_control(0,0,-velocity,0)
    elif(moves=="up" and drone.is_flying==True):
        drone.send_rc_control(0,0,velocity,0)
    elif(moves=="none"):
        drone.send_rc_control(0, 0, 0, 0)
    elif(moves=="takePic"):
        cv2.imwrite(f"C:/Users/mpilo/OneDrive - Durban University of Technology/Year 3/EDPB/Drone Project/Drone Data/{time.time()}.jpg",img)
        time.sleep(1)

    elif(moves=="landTakeoff"):
        if(drone.is_flying==False):
            drone.takeoff()
            #mode=="flight"
        else:
            drone.land()
            #mode="standby"
    
    elif(moves=="standby"):
        drone.land()
        mode = "standby"

    else:
        pass

    #sleep(0.05)
    
    

def moveSurveyObjects():

    moves = listen()

    if (moves=="left" and drone.is_flying==True):
        drone.send_rc_control(-speedObjects,0,0,0)

    elif(moves=="right" and drone.is_flying==True):
        drone.send_rc_control(speedObjects,0,0,0)
        
    elif(moves=="antiClockwise" and drone.is_flying==True):
        drone.send_rc_control(0,0,0,-angularSpeedObjects)
       
    elif(moves=="clockwise" and drone.is_flying==True):
        drone.send_rc_control(0,0,0,angularSpeedObjects)
        
    elif (moves=="back" and drone.is_flying==True):
        drone.send_rc_control(0,-speedObjects,0,0)

    elif(moves=="forward" and drone.is_flying==True):
        drone.send_rc_control(0,speedObjects,0,0)
    
    elif(moves=="down" and drone.is_flying==True):
        drone.send_rc_control(0,0,-speedObjects,0)

    elif(moves=="up" and drone.is_flying==True):
        drone.send_rc_control(0,0,speedObjects,0)

    elif(moves=="takePic"):
        cv2.imwrite(f"C:/Users/mpilo/OneDrive - Durban University of Technology/Year 3/EDPB/Drone Project/Drone Data/{time.time()}.jpg",img)
        time.sleep(1)
    

    elif(moves=="landTakeoff"):
        if(drone.is_flying==False):
            drone.takeoff()
            
        else:
            drone.land()
            add_data()

    elif(moves=="standby"):
        drone.land()
        add_data()
        mode = "standby"
    
    else:
        pass

def move_track():

    moves = listen()

    if (moves=="left" and drone.is_flying==True):
        drone.send_rc_control(-speedObjects,0,0,0)

    elif(moves=="right" and drone.is_flying==True):
        drone.send_rc_control(speedObjects,0,0,0)
        
    elif(moves=="antiClockwise" and drone.is_flying==True):
        drone.send_rc_control(0,0,0,-angularSpeedObjects)
       
    elif(moves=="clockwise" and drone.is_flying==True):
        drone.send_rc_control(0,0,0,angularSpeedObjects)
        
    elif (moves=="back" and drone.is_flying==True):
        drone.send_rc_control(0,-speedObjects,0,0)

    elif(moves=="forward" and drone.is_flying==True):
        drone.send_rc_control(0,speedObjects,0,0)
    
    elif(moves=="down" and drone.is_flying==True):
        drone.send_rc_control(0,0,-speedObjects,0)

    elif(moves=="up" and drone.is_flying==True):
        drone.send_rc_control(0,0,speedObjects,0)

    elif(moves=="takePic"):
        cv2.imwrite(f"C:/Users/mpilo/OneDrive - Durban University of Technology/Year 3/EDPB/Drone Project/Drone Data/{time.time()}.jpg",img)
        time.sleep(1)

    elif(moves=="landTakeoff"):
        if(drone.is_flying==False):
            drone.takeoff()
            
        else:
            drone.land()

    elif(moves=="standby"):
        drone.land()
        mode = "standby"
    
    else:
        pass

   
    
def imagingNormal():
    global img
    img = drone.get_frame_read().frame
    img = cv2.resize(img,(720,480))
    cv2.imshow("Footage",img)
    cv2.waitKey(1)

def imagingGreen():
    global img
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (frameWidth, frameHeight))
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([29, 116, 64])
    upper = np.array([92, 255, 231])
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img, mask, result])
    cv2.imshow('Horizontal Stacking', hStack)
    cv2.waitKey(1)

def imagingBlack():
    global img
    img = drone.get_frame_read().frame
    img = cv2.resize(img,(720,480))
    hsv_frame = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #black mask
    low_black = np.array([45,7,71])
    high_black = np.array([45,5,11])
    black_mask = cv2.inRange(hsv_frame,low_black,high_black)
    black = cv2.bitwise_and(frame,frame,mask=black_mask)
    cv2.imshow("Footage",img)
    cv2.imshow("black",black)
    cv2.waitKey(1)

def mode1Win(): #read database
    top = Toplevel()
    top.title("DJI TELLO DRONE Control Centre")
    #fucntion to destroy windows 
    def home():
        top.destroy()
    #styling the entire GUI
    canvastop = tk.Canvas(top, height=500, width=500)
    frametop = tk.Frame(top, bg="#1bcfa8")
    frametop.place(relwidth=1,relheight=1)
    #read database
    btn_viewDatabase = tk.Button(top, text="Export Database To Excel", bg="lime", command=exportData)
    btn_viewDatabase['font'] = myFont2
    btn_viewDatabase.place(relx=0, rely=0, relwidth=1, relheight=0.2)
    #btn_surveillance.bind("<Button-1>",surveillance_mode)

    #clear database
    btn_clearDatabase = tk.Button(top, text="Clear Database", bg="red", command=clearDatabase)
    btn_clearDatabase['font'] = myFont2
    btn_clearDatabase.place(relx=0, rely=0.4, relwidth=1, relheight=0.2)
    

    #home
    btn_home = tk.Button(top, text="Main Menu", bg="violet", command=home)
    btn_home["font"] = myFont2
    btn_home.place(relx=0,rely=0.8,relwidth=1,relheight=0.2)
    #btn_home.bind("<Button-1>",home)    

    top.attributes("-fullscreen", True)
    top.mainloop() 

def mode2Win(): #tracking
    root.destroy()
    global top_tracking
    top_tracking = Toplevel()
    top_tracking.title("Tracking Mode")
    #styling the entire GUI
    canvastop = tk.Canvas(top_tracking, height=500, width=500)
    frametop = tk.Frame(top_tracking, bg="#1bcfa8")
    frametop.place(relwidth=1,relheight=1)
    #fonts
    myFont2 = font.Font(family='Helvetica', size=20, weight='bold')
    myFont1 = font.Font(family='Helvetica', size=20, weight='bold')
    #red car
    btn_redcar = tk.Button(top_tracking, text="Red Car", bg="red", command=RedCar)
    btn_redcar['font'] = myFont2
    btn_redcar.place(relx=0, rely=0, relwidth=0.5, relheight=0.2)
    #Orange car
    btn_OrangeCar = tk.Button(top_tracking, text="Orange Car", bg="yellow", command=OrangeCar)
    btn_OrangeCar['font'] = myFont2
    btn_OrangeCar.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.2)
    #white car
    btn_whiteCar = tk.Button(top_tracking, text="White Car", bg="green", command=WhiteCar)
    btn_whiteCar["font"] = myFont2
    btn_whiteCar.place(relx=0,rely=0.4,relwidth=0.5,relheight=0.2)
    #btn_home.bind("<Button-1>",home)

    #blue car
    btn_blueCar = tk.Button(top_tracking, text = "Blue Car", bg="blue", command=BlueCar)
    btn_blueCar['font'] = myFont2
    btn_blueCar.place(relx=0.5, rely=0.4, relwidth=0.5, relheight=0.2)
    #btn_haltTracking.bind("<Button-1>",haltTracking)

    #main menu
    btn_haltTracking = tk.Button(top_tracking, text = "HALT", bg="red", command=halt_tracking)
    btn_haltTracking['font'] = myFont1
    btn_haltTracking.place(relx=0, rely=0.85, relwidth=1, relheight=0.15)
    #btn_halt.bind("<Button-1>",halt_tracking)

    top_tracking.attributes("-fullscreen", True)
    top_tracking.mainloop()

#tracking mode functions
def RedCar():
    mode = 'RedCar'
    top_tracking.destroy()
    while mode == "RedCar":
        imagingRed()
        move()
        if mode=="standby":
            break
    #leaving while loop
    
def YellowCar():
    mode = 'YellowCar'
    top_tracking.destroy()
    while mode == "YellowCar":
        imagingYellow()
        move()
        if mode=="standby":
            break
    #leaving while loop

    
def GreenCar():
    mode = 'GreenCar'
    top_tracking.destroy()
    while mode == "GreenCar":
        imagingGreen()
        move()
        if mode=="standby":
            break
    #leaving while loop
    
def BlueCar():
    mode = 'BlueCar'
    top_tracking.destroy()
    while mode == "BlueCar":
        imagingBlue()
        move()
        if mode=="standby":
            break
    #leaving while loop

def WhiteCar():
    mode = 'WhiteCar'
    top_tracking.destroy()
    while mode == "WhiteCar":
        imagingWhite()
        move()
        if mode=="standby":
            break
    #leaving while loop

def OrangeCar():
    mode = 'OrangeCar'
    top_tracking.destroy()
    while mode == "OrangeCar":
        imagingOrange()
        move()
        if mode=="standby":
            break
    #leaving while loop

    
def Vegetation():
    mode = 'Vegetation'
    top_tracking.destroy()
    while mode == "Vegetation":
        imagingVegetation()
        move()
    #leaving while loop

def surveyVegetation(event):
    root.destroy()
    mode = "surveyVegetation"
    while (mode=="surveyVegetation"):
        imagingVegetation()
        move()
        if mode=="standby":
            break
    mode="standby"

def halt_tracking():
    top_tracking.destroy()
    mode = "standby"
    
#functions for imaging the above

def imagingRed():
    global img
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (frameWidth, frameHeight))
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 156, 99])
    upper = np.array([6, 255, 229])
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img, mask, result])
    cv2.imshow('Horizontal Stacking', hStack)
    cv2.waitKey(1)

def imagingYellow():
    global img
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (frameWidth, frameHeight))
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([15, 145, 144])
    upper = np.array([27, 255, 255])
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img, mask, result])
    cv2.imshow('Horizontal Stacking', hStack)
    cv2.waitKey(1)
    
def imagingWhite():
    global img
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (frameWidth, frameHeight))
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 0, 117])
    upper = np.array([179, 22, 219])
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img, mask, result])
    cv2.imshow('Horizontal Stacking', hStack)
    cv2.waitKey(1)
    
    
def imagingBlue():
    global img
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (frameWidth, frameHeight))
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([52, 48, 10])
    upper = np.array([149, 255, 255])
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img, mask, result])
    cv2.imshow('Horizontal Stacking', hStack)
    cv2.waitKey(1)
    
def imagingVegetation():
    global img
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (frameWidth, frameHeight))
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([29, 116, 64])
    upper = np.array([92, 255, 231])
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img, mask, result])
    cv2.imshow('Horizontal Stacking', hStack)
    cv2.waitKey(1)

def imagingOrange():
    global img
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (frameWidth, frameHeight))
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([11, 213, 90])
    upper = np.array([18, 255, 255])
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img, mask, result])
    cv2.imshow('Horizontal Stacking', hStack)
    cv2.waitKey(1)

#different types of sureveillance mode
def surveyObjects(event):
    root.destroy()
    #top_mod0.destroy()
    mode = "surveyObjects"
    #remember to save data in list as well
    while(mode == "surveyObjects"):
    # success, img = cap.read()
        global img
        img = drone.get_frame_read().frame
        classIds, confs, bbox = net.detect(img, confThreshold=thres, nmsThreshold=nmsThres)
        try:
            for classId, conf, box in zip(classIds.flatten(), confs.flatten(), bbox):
                if (classNames[classId - 1] == "person"):
                    cvz.cornerRect(img, box)
                    cv2.putText(img, f'Person {round(conf * 100, 2)}%',
                                (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                1, (0, 255, 0), 2)
                    global clock
                    clock = time.time()
                    print(f"Object Of Interest Captured at {clock}")
                    cv2.imwrite(f"C:/Users/mpilo/OneDrive - Durban University of Technology/Year 3/EDPB/Drone Project/Drone Data/{clock}.jpg",img)
                    flight_time.append(drone.get_flight_time())
                    real_time.append(clock)
                    picture_path.append(f"C:/Users/mpilo/OneDrive - Durban University of Technology/Year 3/EDPB/Drone Project/Drone Data/{clock}.jpg")
                    time.sleep(2)
                else:
                    pass
        except:
            pass
        
        cv2.imshow("Image", img)
        cv2.waitKey(1)
        moveSurveyObjects()
        if mode=="standby":
            break
        
    mode = "standby"

def add_data():
    dict = {"flight_time": flight_time, "real_time": real_time,
        "picture_path": picture_path}
    df = pd.DataFrame(dict)
    df.to_csv("C:/Users/mpilo/OneDrive - Durban University of Technology/Year 3/EDPB/Drone Project/Drone Data/droneData.csv")
    print("Data appended successfully.")




root = Tk()
root.title("DJI TELLO DRONE Control Centre")
#styling the entire GUI
canvas = tk.Canvas(root, height=500, width=500)
frame = tk.Frame(root, bg="#1bcfa8")
frame.place(relwidth=1,relheight=1)
#button styles
global myFont2
global myFont1
myFont2 = font.Font(family='Helvetica', size=20, weight='bold')
myFont1 = font.Font(family='Helvetica', size=20, weight='bold')

#buttons for different modes
#Surveillance Mode
btn_surveillance = tk.Button(root, text="Surveillance Mode", bg="lime")
btn_surveillance['font'] = myFont1
btn_surveillance.place(relx=0, rely=0, relwidth=0.5, relheight=0.2)
btn_surveillance.bind("<Button-1>",surveyObjects)

#Database Mode
btn_database = tk.Button(root, text="View Database", bg="yellow")
btn_database['font'] = myFont1
btn_database.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.2)
btn_database.bind("<Button-1>",read_database)

#Survey Veg Mode
btn_surveyVeg = tk.Button(root, text="Survey Vegetation", bg="orange")
btn_surveyVeg['font'] = myFont1
btn_surveyVeg.place(relx=0, rely=0.3, relwidth=0.5, relheight=0.2)
btn_surveyVeg.bind("<Button-1>",surveyVegetation)

#Tracking Mode
btn_trackingV = tk.Button(root, text="Track Vehicles", bg="#80c1ff")
btn_trackingV['font'] = myFont1
btn_trackingV.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.2)
btn_trackingV.bind("<Button-1>",tracking_mode)

#Battery
btn_battery = tk.Button(root, text="Get Battery", bg="violet")
btn_battery["font"] = myFont1
btn_battery.place(relx=0,rely=0.6,relwidth=0.5,relheight=0.15)
btn_battery.bind("<Button-1>",get_battery)

#Standard Flight
btn_flight = tk.Button(root, text="Flight Mode", bg="blue",command=flight_mode)
btn_flight["font"] = myFont1
btn_flight.place(relx=0.5,rely=0.6,relwidth=0.5,relheight=0.15)
#btn_flight.bind("<Button-1>",flight_mode)

#EStop
btn_halt = tk.Button(root, text = "HALT", bg="red")
btn_halt['font'] = myFont1
btn_halt.place(relx=0, rely=0.85, relwidth=1, relheight=0.15)
btn_halt.bind("<Button-1>",halt)

#drone.send_keepalive()
#root.geometry("350x350")
root.attributes("-fullscreen", True)
root.mainloop()


