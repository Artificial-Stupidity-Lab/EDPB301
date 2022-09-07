#tello(drone) libraries
from djitellopy import tello
import time
from time import sleep
#tkinter(GUI) libraries
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
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
myFont1 = font.Font(family='Helvetica', size=20, weight='bold')
#GUI variables


#function for clicked button
def get_battery(event):
    print("\nEntering Battery Mode")
    #create mesage box

def surveillance_mode(event):
    print("\nEntering Surveillance Mode")
    #create mesage box

def read_database(event):
    print("\nEntering Database Mode")
    #create mesage box

def tracking_mode(event):
    print("\nEntering tracking Mode")
    #create mesage box

def defensive_mode(event):
    print("\nEntering defensive Mode")
    #create mesage box

def halt(event):
    print("\nEntering halt Mode")
    #create mesage box



#opening new windows for the each mode
def mode0Win():
    pass
def mode1Win():
    pass
def mode2Win():
    pass
def mode3Win():
    pass
def mode4Win():
    pass



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

root.geometry("500x500")
root.mainloop()
