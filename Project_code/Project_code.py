import serial
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import time

#variables
#arduino_data=serial.Serial("com3", baudrate = 115200, timeout = 1)

#creating GUI
root = tk.Tk()
root.title("Control Centre")
#styling the entire GUI
canvas = tk.Canvas(root, height=500, width=500)
#frame = tk.Frame(root, bg="#1bcfa8")
#frame.place(relwidth=1,relheight=1)
background_image = tk.PhotoImage(file="dut_logo.png")
background_label = tk.Label(root,image=background_image)
background_label.place(x=0,y=0,relheight=1,relwidth=1) 

#open entrance button
btn_gate1_open = tk.Button(root, text="Open Entrance", bg="lime")
btn_gate1_open.place(relx=0, rely=0, relwidth=0.5, relheight=0.2)
#close entrance button
btn_gate1_close = tk.Button(root, text="Close Entrance", bg="red")
btn_gate1_close.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.2)

#open exit button
btn_gate2_open = tk.Button(root, text="Open Exit", bg="lime")
btn_gate2_open.place(relx=0, rely=0.3, relwidth=0.5, relheight=0.2)
#close exit button
btn_gate2_close = tk.Button(root, text="Close Exit", bg="red")
btn_gate2_close.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.2)

#control type
control_type = IntVar()
btn_control_type = tk.Checkbutton(root, variable = control_type, text = "Automatic Control", bg="#80c1ff")
btn_control_type.place(relx=0, rely=0.5, relwidth=1, relheight=0.2)

root.geometry("500x500")
root.mainloop()