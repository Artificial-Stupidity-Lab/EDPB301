import serial
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
import time

#variables
#arduino_data=serial.Serial("com3", baudrate = 115200, timeout = 1)

#creating GUI
root = Tk()
root.title("Control Centre")
#styling the entire GUI
canvas = tk.Canvas(root, height=500, width=500)
frame = tk.Frame(root, bg="#1bcfa8")
frame.place(relwidth=1,relheight=1)
#button styles
myFont1 = font.Font(family='Helvetica', size=20, weight='bold')


#open entrance button
btn_gate1_open = tk.Button(root, text="Open Entrance", bg="lime")
btn_gate1_open['font'] = myFont1
btn_gate1_open.place(relx=0, rely=0, relwidth=0.5, relheight=0.2)
#close entrance button
btn_gate1_close = tk.Button(root, text="Close Entrance", bg="red")
btn_gate1_close['font'] = myFont1
btn_gate1_close.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.2)

#open exit button
btn_gate2_open = tk.Button(root, text="Open Exit", bg="lime")
btn_gate2_open['font'] = myFont1
btn_gate2_open.place(relx=0, rely=0.3, relwidth=0.5, relheight=0.2)
#close exit button
btn_gate2_close = tk.Button(root, text="Close Exit", bg="red")
btn_gate2_close['font'] = myFont1
btn_gate2_close.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.2)

#parking spots button
btn_available_parking = tk.Button(root, text="Parking Availabilty", bg="yellow")
btn_available_parking["font"] = myFont1
btn_available_parking.place(relx=0,rely=0.6,relwidth=1,relheight=0.15)

#control type
control_type = IntVar()
btn_control_type = tk.Checkbutton(root, variable = control_type, text = "Automatic Control", bg="#80c1ff")
btn_control_type['font'] = myFont1
btn_control_type.place(relx=0, rely=0.85, relwidth=1, relheight=0.15)

root.geometry("500x500")
root.mainloop()