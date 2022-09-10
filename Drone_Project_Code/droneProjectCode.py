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

#drone communication libraries
#drone = tello.Tello()  #creating an object for the drone
#drone.connect() #communicating with the drone

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



#function for clicked button
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
    #create mesage box

def tracking_mode(event):#mode2
    print("\nEntering tracking Mode")
    mode2Win()
    #create mesage box

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
    battery = tello.get_battery()
    messagebox.showinfo("Battery Status", f"The Drone's Battery is {battery}% full")
def halt_msg():
    #land()
    pass
    messagebox.showinfo("Halt", f"Drone Operations have been halted")
    tello.land()
    

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





#opening new windows for the each mode
def mode0Win():
 
    top = Toplevel()
    top.title("DJI TELLO DRONE Control Centre")
#fucntion to destroy windows 
    def home():
        top.destroy()
    #styling the entire GUI
    canvastop = tk.Canvas(top, height=500, width=500)
    frametop = tk.Frame(top, bg="#1bcfa8")
    frametop.place(relwidth=1,relheight=1)
   #Objects
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
def mode1Win():
    pass
    top = Toplevel()
    lb1 = Label(top, text="Mode 1").pack()
def mode2Win():
    pass
    top = Toplevel()
    lb2 = Label(top, text="Mode 2").pack()
def mode3Win():
    pass
    top = Toplevel()
    lb3 = Label(top, text="Mode 3").pack()
def mode4Win():
    pass
    top = Toplevel()
    lb4 = Label(top, text="Mode 4").pack()



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
btn_battery.place(relx=0,rely=0.6,relwidth=1,relheight=0.15)
btn_battery.bind("<Button-1>",get_battery)

#EStop
btn_halt = tk.Button(root, text = "HALT", bg="red")
btn_halt['font'] = myFont1
btn_halt.place(relx=0, rely=0.85, relwidth=1, relheight=0.15)
btn_halt.bind("<Button-1>",halt)

root.attributes("-fullscreen", True)
root.mainloop()

