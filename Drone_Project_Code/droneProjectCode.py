#tello(drone) libraries
from djitellopy import tello
import time
from time import sleep


#tkinter(GUI) libraries
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
from tkinter import filedialog as fd
#Imaging libraries
import cv2
import numpy as np
#drone Variable
velocity = 50 #standard drone speed
droneState = 0 #drone state

#drone communication libraries
'''
drone = tello.Tello()  #creating an object for the drone
drone.connect() #communicating with the drone
arduino_data=serial.Serial("com3", baudrate = 115200, timeout = 1)

#communication function
def listen():
    while(arduino_data.inwaiting()==0):
        pass
    dataPacket = arduino_data.readline()
    dataPacket=str(dataPacket, "utf-8")
    dataPacket=int(dataPacket.strip("\r\n"))
    return dataPacket

def talk(data):
    userInput = data+"\r"
    arduino_data.write(userInput.encode())
  
'''
#creating GUI
root = Tk()
root.title("DJI TELLO DRONE Control Centre")
#styling the entire GUI
canvas = tk.Canvas(root, height=500, width=500)
frame = tk.Frame(root, bg="#1bcfa8")
frame.place(relwidth=1,relheight=1)
#button styles
myFont2 = font.Font(family='Helvetica', size=20, weight='bold')
myFont1 = font.Font(family='Helvetica', size=20, weight='bold')

#GUI variables
#objects list needs to be a tuple
objectsList = ("Please Select Object To Track",
                "a",
                "b",
                "a"
                )



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
    pass
    print("\nEntering Database Mode")
    mode1Win()
    #open data base

def tracking_mode(event):#mode2
    print("\nEntering tracking Mode")
    mode2Win()
    #create a list of objects to track

def defensive_mode(event):#mode3
    print("\nEntering defensive Mode")
    mode3Win()
    #create mesage box

def halt(event):#mode4
    print("\nEntering halt Mode")
    halt_msg()
    #create mesage box

#creating message box function
def msg_box_battery():
    pass
    #create function that reads battery from tello drone
    #battery = tello.get_battery()
    messagebox.showinfo("Battery Status", f"The Drone's Battery is Something% full")
def halt_msg():
    #land()
    messagebox.showinfo("Halt", f"Drone Operations have been halted")
    #tello.land()
    

#functions to write/read data file
def writeDataFile():
    pass
    global fn
    filename = "C:/Users/mpilo/OneDrive - Durban University of Technology/Year 3/EDPB/Drone Project/Drone Data/droneData.csv"
    # create a file handler 'fn'
    fn = open(filename, "a") # open filename in write mode
    # access the file
    fn.write()

def readDataFile():
    pass
    filename = "C:/Users/mpilo/OneDrive - Durban University of Technology/Year 3/EDPB/Drone Project/Drone Data/droneData.csv"
    fn.close()

#general defesive mode function
def defend():
    pass
    '''pick random value from 1st list
    if value is from left to forward, pick a disntance
    from the second list, if value is a flip do it only once
    if spin, rotate 180 degrees
    '''
    randomMoves = [
    "left", 
    "right",
    "up",
    "down",
    "back",
    "forward",
    "flipLeft",
    "flipRight",
    "flipBack",
    "flipForward"
    "spin"]
    randomTime = [
        20,
        40,
        60,
        80,
        100,
        120,
        140,
        160,
        200,
    ]

 #sureveillance function, how to survey   
def move():
    if(droneState==0):
        drone.takeoff()
        droneState = 1
    moves = listen()

    if (moves=="left"):
        drone.send_rc_control(-velocity,0,0,0)
    if(moves=="right"):
        drone.send_rc_control(velocity,0,0,0)
    if(moves=="antiClockwise"):
        drone.send_rc_control(0,0,0,-velocity)
    if (moves=="clockwise"):
        drone.send_rc_control(0,0,0,velocity)
    if(moves=="speedUp"):
        velocity+=2
    if(moves=="speedDown"):
        velocity-=2
    if (moves=="back"):
        drone.send_rc_control(0,-velocity,0,0)
    if(moves=="forward"):
        drone.send_rc_control(0,velocity,0,0)
    if(moves=="down"):
        drone.send_rc_control(0,0,-velocity,0)
    if(moves=="up"):
        drone.send_rc_control(0,0,velocity,0)
    if(moves=="takePic"):
        cv2.imwrite(f"C:/Users/mpilo/OneDrive - Durban University of Technology/Year 3/EDPB/Drone Project/Drone Data/{time.time()}.jpg",img)

    if(moves=="landTakeoff"):
        if(droneState==0):
            drone.takeoff()
            droneState = 1
        else:
            drone.land()
            droneState = 0

def imagingNormal():
    drone.stream_on()
    img = drone.get_frame_read().frame
    img = cv2.resize(img,(720,480))
    cv2.imshow("Footage",img)
    cv2.waitkey(1)

def imagingGreen():
    drone.stream_on()
    img = drone.get_frame_read().frame
    img = cv2.resize(img,(720,480))
    hsv_frame = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #green mask
    low_green = np.array([25,52,72])
    high_green = np.array([102,255,255])
    green_mask = cv2.inRange(hsv_frame,low_green,high_green)
    green = cv2.bitwise_and(frame,frame,mask=green_mask)
    cv2.imshow("Footage",img)
    cv2.imshow("Green",green)
    cv2.waitkey(1)  
def imagingBlack():
    drone.stream_on()
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
    cv2.waitkey(1)




#functions for different modes
def mode0Win(): #surveillance
 
    top = Toplevel()
    top.title("DJI TELLO DRONE Control Centre")
#fucntion to destroy windows 
    def home():
        top.destroy()
    #styling the entire GUI
    canvastop = tk.Canvas(top, height=500, width=500)
    frametop = tk.Frame(top, bg="#1bcfa8")
    frametop.place(relwidth=1,relheight=1)
   #mde 0 buttons (surveillance mode)
    btn_object = tk.Button(top, text="Survey Objects", bg="lime")
    btn_object['font'] = myFont2
    btn_object.place(relx=0, rely=0, relwidth=0.5, relheight=0.2)
    #btn_surveillance.bind("<Button-1>",surveillance_mode)

    #Parking
    btn_parking = tk.Button(top, text="Survey Parking", bg="yellow")
    btn_parking['font'] = myFont2
    btn_parking.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.2)
    #btn_database.bind("<Button-1>",read_database)

    #Vegetation
    btn_vegetation = tk.Button(top, text="Survey Vegetation", bg="orange")
    btn_vegetation['font'] = myFont2
    btn_vegetation.place(relx=0, rely=0.3, relwidth=0.5, relheight=0.2)
    #btn_defensive.bind("<Button-1>",defensive_mode)

    #Defensive
    btn_road = tk.Button(top, text="Survey Road", bg="#80c1ff")
    btn_road['font'] = myFont2
    btn_road.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.2)
    #btn_tracking.bind("<Button-1>",tracking_mode)

    #home
    btn_home = tk.Button(top, text="Main Menu", bg="violet", command=home)
    btn_home["font"] = myFont2
    btn_home.place(relx=0,rely=0.6,relwidth=1,relheight=0.15)
    #btn_home.bind("<Button-1>",home)

    #EStop
    btn_halt = tk.Button(top, text = "HALT", bg="red")
    btn_halt['font'] = myFont2
    btn_halt.place(relx=0, rely=0.85, relwidth=1, relheight=0.15)
    #btn_halt.bind("<Button-1>",halt)

    top.attributes("-fullscreen", True)
    top.mainloop()
def mode1Win(): #read database
    pass
    top = Toplevel()
    lb1 = Label(top, text="Mode 1").pack()
def mode2Win(): #tracking
    top = Toplevel()
    top.title("Tracking Mode")
    obejectSet = set(objectsList)
#fucntion to destroy windows 
    def home():
        top.destroy()
    #styling the entire GUI
    canvastop = tk.Canvas(top, height=500, width=500)
    frametop = tk.Frame(top, bg="#1bcfa8")
    frametop.place(relwidth=1,relheight=1)
   #select menu for objects to track
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
    btn_track = tk.Button(top, text="Click To Track", bg="yellow")
    btn_track['font'] = myFont2
    btn_track.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.2)
    #btn_database.bind("<Button-1>",read_database)

    #Defensive
    btn_defensive2 = tk.Button(top, text="Defensive", bg="#80c1ff")
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
    pass
    top = Toplevel()
    lb3 = Label(top, text="Mode 3").pack()
def mode4Win(): #halt
    pass
    top = Toplevel()
    lb4 = Label(top, text="Mode 4").pack()


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
#btn_database.bind("<Button-1>",read_database)

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
btn_battery.place(relx=0,rely=0.6,relwidth=1,relheight=0.15)
btn_battery.bind("<Button-1>",get_battery)

#EStop
btn_halt = tk.Button(root, text = "HALT", bg="red")
btn_halt['font'] = myFont1
btn_halt.place(relx=0, rely=0.85, relwidth=1, relheight=0.15)
btn_halt.bind("<Button-1>",halt)

root.attributes("-fullscreen", True)
root.mainloop()

