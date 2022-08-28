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
mode = IntVar()
mode.set(0)

#function for clicked button
def get_battery(event):
    pass
    #create mesage box


def modeSel():
    if(mode.get()==0):
        mode0Win()
    elif(mode.get()==1):
        mode1Win()
    elif(mode.get()==2):
        mode2Win()
    elif(mode.get()==3):
        mode3Win()
    elif(mode.get()==4):
        mode4Win()

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
btn_surveillance = Radiobutton(root, text="Surveillance", bg="lime", variable=mode, value=1, command=modeSel)
btn_surveillance['font'] = myFont1
btn_surveillance.place(relx=0, rely=0, relwidth=0.5, relheight=0.2)
#Voice Control Mode
btn_voice = Radiobutton(root, text="Voice Control", bg="yellow", variable=mode, value=2,command=modeSel)
btn_voice['font'] = myFont1
btn_voice.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.2)

#Hand Control Mode
btn_hand = Radiobutton(root, text="Hand Control", bg="orange", variable=mode, value=3,command=modeSel)
btn_hand['font'] = myFont1
btn_hand.place(relx=0, rely=0.3, relwidth=0.5, relheight=0.2)
#Tracking Mode
btn_tracking = Radiobutton(root, text="Tracking", bg="#80c1ff",variable=mode, value=4,command=modeSel)
btn_tracking['font'] = myFont1
btn_tracking.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.2)

#Battery
btn_battery = tk.Button(root, text="Get Battery", bg="violet")
btn_battery["font"] = myFont1
btn_battery.place(relx=0,rely=0.6,relwidth=1,relheight=0.15)
btn_battery.bind("<Button-1>",get_battery)

#EStop
btn_halt = Radiobutton(root, text = "HALT", bg="red", variable=mode, value=0)
btn_halt['font'] = myFont1
btn_halt.place(relx=0, rely=0.85, relwidth=1, relheight=0.15)

root.geometry("500x500")
root.mainloop()
