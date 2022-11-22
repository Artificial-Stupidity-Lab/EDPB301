#tello(drone) libraries
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
velocity = 30 #standard drone speed
global mode
mode = "standby"
###########################################################
#object surveiallnce variables
x_pos, y_pos, x_home, y_home = 0,0,0,0
speedObjects = 30
angularSpeedObjects = 50 #degrees/s
interval = 0.25
rotate = 0
global angle
angle = 0
distanceInterval = speedObjects*interval
angularInterval = angularSpeedObjects*interval

frameWidth = 480
frameHeight = 360
frameCounter = 0
###########################################################
#drone communication libraries

drone = tello.Tello()  #creating an object for the drone
drone.connect() #communicating with the drone
drone.streamon()

arduino_data=serial.Serial("com3",baudrate = 9600, timeout=1)


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
                "Object | Time",
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
    mode1Win()
    #open data base

def tracking_mode(event):#mode2
    print("\nEntering tracking Mode")
    mode2Win()
    #create a list of objects to track

def defensive_mode(event):#mode3
    messagebox.showinfo("Defensive Mode", f'Pleas Wait while the drone defends itself')
    defend()
    messagebox.showinfo("Defensive Mode", f'Defensive Mode Completed')
    #mode3Win()
    #create mesage box

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
            move()
    mode="standby"
    drone.streamoff()
    
    
        
    #create mesage box
    
#general defesive mode function
def defend():
    
    '''pick random value from 1st list
    if value is from left to forward, pick a disntance
    from the second list, if value is a flip do it only once
    if spin, rotate 180 degrees
    '''
    randomflips = [
    "forward",
    "flipLeft",
    "flipRight",
    "flipBack",
    "flipForward"
    ]

    randomMoves = [
    "left", 
    "right",
    "up",
    "down",
    "back",
    ]

    randomDistance = [
        20,
        40,
        60,
        80,
        100,
        120,
        140,
        160,
        200
    ]
    randomReps = [
        1,
        2,
        3,
        4,
        5
    ]
    
    #random movements based on random choices
    y = random.choice(randomReps)
    i=0
    while(i<y):
        x = random.choice(randomflips)
        x = x[4:].lower()
        drone.flip(x.lower())
        y = random.choice(randomDistance)
        z = random.choice(randomMoves)
        drone.move(z,y)
        i+=1
    



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
        gui()

    else:
        pass

    #sleep(0.05)
    imagingNormal()

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
        gui()

    else:
        pass

    #sleep(0.05)
    imagingGreen()
    

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

    elif(moves=="landTakeoff"):
        if(drone.is_flying==False):
            drone.takeoff()
            
        else:
            drone.land()

    elif(moves=="standby"):
        drone.land()
        mode = "standby"
        gui()
    
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

    elif(moves=="landTakeoff"):
        if(drone.is_flying==False):
            drone.takeoff()
            
        else:
            drone.land()

    elif(moves=="standby"):
        drone.land()
        mode = "standby"
        gui()
    
    else:
        pass

   
    
def imagingNormal():
    img = drone.get_frame_read().frame
    img = cv2.resize(img,(720,480))
    cv2.imshow("Footage",img)
    cv2.waitKey(1)

def imagingGreen():
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (frameWidth, frameHeight))
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([29, 45, 0])
    upper = np.array([72, 255, 255])
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img, mask, result])
    cv2.imshow('Horizontal Stacking', hStack)
    cv2.waitKey(1)

'''

    img = drone.get_frame_read().frame
   
    img = cv2.resize(img,(720,480))
    hsv_frame = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #green mask
    low_green = np.array([25,52,72])
    high_green = np.array([102,255,255])
    green_mask = cv2.inRange(hsv_frame,low_green,high_green)
    green = cv2.bitwise_and(img,img,mask=green_mask)
    cv2.imshow("Footage",img)
    cv2.imshow("Green Mask",green)
    cv2.waitKey(1)  

    '''
def imagingBlack():
    
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




#functions for different modes
def mode0Win(): #surveillance
    root.destroy()
    global top_mod0
    top_mod0 = Toplevel()
    top_mod0.title("DJI TELLO DRONE Control Centre")
    #fucntion to destroy windows 
    def home():
        top_mod0.destroy()
    #styling the entire GUI
    canvastop = tk.Canvas(top_mod0, height=500, width=500)
    frametop = tk.Frame(top_mod0, bg="#1bcfa8")
    frametop.place(relwidth=1,relheight=1)
    myFont2 = font.Font(family='Helvetica', size=20, weight='bold')
    myFont1 = font.Font(family='Helvetica', size=20, weight='bold')
   #mde 0 buttons (surveillance mode)
    btn_object = tk.Button(top_mod0, text="Survey Objects", bg="lime", command= surveyObjects)
    btn_object['font'] = myFont2
    btn_object.place(relx=0, rely=0, relwidth=0.5, relheight=0.2)
    #btn_surveillance.bind("<Button-1>",surveyObjects)

    #Parking
    btn_parking = tk.Button(top_mod0, text="Survey Parking", bg="yellow")
    btn_parking['font'] = myFont2
    btn_parking.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.2)
    #btn_database.bind("<Button-1>",read_database)

    #Vegetation
    btn_vegetation = tk.Button(top_mod0, text="Survey Vegetation", bg="orange", command=surveyVegetation)
    btn_vegetation['font'] = myFont2
    btn_vegetation.place(relx=0, rely=0.3, relwidth=0.5, relheight=0.2)
    #btn_defensive.bind("<Button-1>",surveyVegetation)

    #Defensive
    btn_road = tk.Button(top_mod0, text="Survey Road", bg="#80c1ff", command=defend)
    btn_road['font'] = myFont2
    btn_road.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.2)
    #btn_tracking.bind("<Button-1>",tracking_mode)

    #home
    btn_home = tk.Button(top_mod0, text="Main Menu", bg="violet", command=home)
    btn_home["font"] = myFont2
    btn_home.place(relx=0,rely=0.6,relwidth=1,relheight=0.15)
    #btn_home.bind("<Button-1>",home)

    #EStop
    btn_halt = tk.Button(top_mod0, text = "HALT", bg="red")
    btn_halt['font'] = myFont2
    btn_halt.place(relx=0, rely=0.85, relwidth=1, relheight=0.15)
    #btn_halt.bind("<Button-1>",halt)

    top.attributes("-fullscreen", True)
    top.mainloop()

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
    top = Toplevel()
    top.title("Tracking Mode")
    obejectSet = []
    for i in objectsList:
        if i not in obejectSet:
            obejectSet.append(i)
    #fucntion to destroy windows 
    def home():
        top.destroy()
    #styling the entire GUI
    canvastop = tk.Canvas(top, height=500, width=500)
    frametop = tk.Frame(top, bg="#1bcfa8")
    frametop.place(relwidth=1,relheight=1)
   #select menu for objects to track
    global userObject
    userObject = StringVar()
    userObject.set("Please Select Object To Track")
    objectsMenu = tk.OptionMenu(top, userObject, *obejectSet)
    objectsMenu['font'] = myFont2
    objectsMenu.place(relx=0, rely=0, relwidth=0.5, relheight=0.2)
    #halt tracking function
    def haltTracking():
        userObject.set("Please Select Object To Track")
        messagebox.showinfo("Halt Tracking", f"Drone Is No loner Tracking Object Listed as PlaceHolder")

    #Parking
    btn_track = tk.Button(top, text="Click To Track", bg="yellow", command=track)
    btn_track['font'] = myFont2
    btn_track.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.2)
    #btn_database.bind("<Button-1>",read_database)

    #Defensive
    btn_defensive2 = tk.Button(top, text="Defensive", bg="#80c1ff", command=defend)
    btn_defensive2['font'] = myFont2
    btn_defensive2.place(relx=0, rely=0.3, relwidth=1, relheight=0.2)
    #btn_tracking.bind("<Button-1>",tracking_mode)

    #home
    btn_home = tk.Button(top, text="Main Menu", bg="violet", command=home)
    btn_home["font"] = myFont2
    btn_home.place(relx=0,rely=0.6,relwidth=1,relheight=0.15)
    #btn_home.bind("<Button-1>",home)

    #haltTracking
    btn_haltTracking = tk.Button(top, text = "HALT TRACKING", bg="red", command=haltTracking)
    btn_haltTracking['font'] = myFont2
    btn_haltTracking.place(relx=0, rely=0.85, relwidth=1, relheight=0.15)
    #btn_haltTracking.bind("<Button-1>",haltTracking)

    top.attributes("-fullscreen", True)
    top.mainloop()
def mode3Win(): #defensive mode
    top = Toplevel()
    lb3 = Label(top, text="Mode 3").pack()
def mode4Win(): #halt 
    mode = "standby"
    top = Toplevel()
    lb4 = Label(top, text="Mode 4").pack()
def mode5Win(): #flight mode
    '''
        top = Toplevel()
        lb5 = Label(top, text="Mode 5").pack()
        top.title("Tracking Mode")
        #styling the entire GUI
        #fucntion to destroy windows 
        def home():
            top.destroy()
        
        def haltFlight():
            drone.land()
            messagebox.showinfo("Halt Flight", f"Drone No longer in flight, and will land")
            home()
        
        canvastop = tk.Canvas(top, height=500, width=500)
        frametop = tk.Frame(top, bg="yellow")
        frametop.place(relwidth=1,relheight=1)
        mode = "flight"
    
        
    if(drone.is_flying==False):
        drone.takeoff()
    #haltflight
    
    
    btn_haltFlight = tk.Button(top, text = "HALT FLIGHT", bg="red", command=haltFlight)
    btn_haltFlight['font'] = myFont2
    btn_haltFlight.place(relx=0, rely=0.85, relwidth=1, relheight=0.15)
    #btn_haltTracking.bind("<Button-1>",haltTracking)
    #movement function
    
    
    
    #top.attributes("-fullscreen", True)
    #top.mainloop()
    #haltFlight()
    mode='flight'
    while(mode=='flight'):
        move()
    mode ="standby"
    '''
        
        

    

#tracking mode button(track)
def track():
    
    objectOfInterest = userObject.get()
    objectData = objectOfInterest.split("|") #this should split the objet into name, x, y,z,time, we need x,y,z
    object_x = int(float(objectData[1]))
    object_y = int(float(objectData[2]))
    object_z = int(float(objectData[3]))
    drone.go_xyz_speed(object_x,object_y,object_z,speedObjects)
    #split the string into the x, y, z components
    #tell drone to go there
    #when the drone finds its OOI
    messagebox.showinfo("Tracking Mode",f"Object Located")

#different types of sureveillance mode
def surveyObjects():
    top_mod0.destroy()
    
    
    #remember to save data in list as well
    threshold = 0.75
    nmsthreshold = 0.2
    mode = "surveyObjects"
    
    
    classNames = [] #use classID on excel
    classFile = "coco.names"
    with open(classFile,"rt") as f:
        classNames = f.read().split('\n')
    configPath = "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
    weightPath = "frozen_inference_graph.pb"
    net = cv2.dnn_DetectionModel(weightPath,configPath)
    net.setInputSize(320,320)
    net.setInputScale(1.0/127.5)
    net.setInputMean((127.5,127.5,127.5))
    net.setInputSwapRB(True)

    while mode == "surveyObjects":
    # success, img = cap.read()
        moveSurveyObjects()
        img = me.get_frame_read().frame
        classIds, confs, bbox = net.detect(img, confThreshold=thres, nmsThreshold=nmsThres)
        try:
            for classId, conf, box in zip(classIds.flatten(), confs.flatten(), bbox):
                cvzone.cornerRect(img, box)
                cv2.putText(img, f'{classNames[classId - 1].upper()} {round(conf * 100, 2)}',
                            (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                            1, (0, 255, 0), 2)
                objectsList.append(f"{classNames[classId-1].upper()} | {drone.get_flight_time()}")
        except:
            pass

    cv2.imshow("Image", img)
    cv2.waitKey(1)
        
        
def surveyParking():
    pass
def surveyVegetation():
    top_mod0.destroy()
    mode = "surveyVegetation"
    while (mode=="surveyVegetation"):
        moveVegetation()
    mode="standby"
    drone.streamoff()

def surveyRoad():
    pass
def halt_survey():
    mode = "standby"
    pass

#database functions
def clearDatabase():
    #function to clear database, clear the list as well
    del objectsList[2:]
    messagebox.showinfo("Database", f"All data in the database has been cleared")
#functions to write/read data file
def exportData():
    
    filename = "C:/Users/mpilo/OneDrive - Durban University of Technology/Year 3/EDPB/Drone Project/Drone Data/droneData.csv"
    # create a file handler 'fn'
    fh = open(filename, "w") # open filename in write mode
    fh.write(objectsList)
    # close the file
    fh.close()


def gui():
    #creating GUI
    global root
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
    btn_surveillance = tk.Button(root, text="Surveillance", bg="lime")
    btn_surveillance['font'] = myFont1
    btn_surveillance.place(relx=0, rely=0, relwidth=0.5, relheight=0.2)
    btn_surveillance.bind("<Button-1>",surveillance_mode)

    #Database Mode
    btn_database = tk.Button(root, text="Database", bg="yellow")
    btn_database['font'] = myFont1
    btn_database.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.2)
    btn_database.bind("<Button-1>",read_database)

    #Defensive Mode
    btn_defensive = tk.Button(root, text="Defensive", bg="orange")
    btn_defensive['font'] = myFont1
    btn_defensive.place(relx=0, rely=0.3, relwidth=0.5, relheight=0.2)
    btn_defensive.bind("<Button-1>",defensive_mode)

    #Tracking Mode
    btn_tracking = tk.Button(root, text="Tracking", bg="#80c1ff")
    btn_tracking['font'] = myFont1
    btn_tracking.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.2)
    btn_tracking.bind("<Button-1>",tracking_mode)

    #Battery
    btn_battery = tk.Button(root, text="Get Battery", bg="violet")
    btn_battery["font"] = myFont1
    btn_battery.place(relx=0,rely=0.6,relwidth=0.5,relheight=0.15)
    btn_battery.bind("<Button-1>",get_battery)

    #Standard Flight
    btn_flight = tk.Button(root, text="Flight", bg="blue",command=flight_mode)
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

#running the gui
gui()

