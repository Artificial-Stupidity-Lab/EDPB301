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


#Surveillance Mode
btn_gate1_open = Radiobutton(root, text="Surveillance", bg="lime", variable=mode, value=1)
btn_gate1_open['font'] = myFont1
btn_gate1_open.place(relx=0, rely=0, relwidth=0.5, relheight=0.2)
#Voice Control Mode
btn_gate1_close = Radiobutton(root, text="Voice Control", bg="yellow", variable=mode, value=2)
btn_gate1_close['font'] = myFont1
btn_gate1_close.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.2)

#Hand Control Mode
btn_gate2_open = Radiobutton(root, text="Hand Control", bg="orange", variable=mode, value=3)
btn_gate2_open['font'] = myFont1
btn_gate2_open.place(relx=0, rely=0.3, relwidth=0.5, relheight=0.2)
#Tracking Mode
btn_gate2_close = Radiobutton(root, text="Tracking", bg="#80c1ff",variable=mode, value=4)
btn_gate2_close['font'] = myFont1
btn_gate2_close.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.2)

#Battery
btn_available_parking = tk.Button(root, text="Get Battery", bg="violet")
btn_available_parking["font"] = myFont1
btn_available_parking.place(relx=0,rely=0.6,relwidth=1,relheight=0.15)

#EStop
btn_control_type = Radiobutton(root, text = "Emergency Stop", bg="red", variable=mode, value=0)
btn_control_type['font'] = myFont1
btn_control_type.place(relx=0, rely=0.85, relwidth=1, relheight=0.15)

root.geometry("500x500")
root.mainloop()