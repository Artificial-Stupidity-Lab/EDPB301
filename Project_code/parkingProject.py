import serial
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
import time

#variables
#arduino_data=serial.Serial("com3", baudrate = 115200, timeout = 1)

#communication function
def listen():
    while(arduino_data.inwaiting()==0):
        pass
    dataPacket = arduino_data.readline()
    dataPacket=str(dataPacket, "utf-8")
    dataPacket=int(dataPacket.strip("\r\n"))
    return dataPacket

def talk(data: str):
    userInput = data+"\r"
    arduino_data.write(userInput.encode())
 

#functions
#parking spaces availabilty
def parkingSpaces():
    talk("parkingSpaces")
    parkingSpaces = listen()
    messagebox.showinfo("Parking Availabilty", f"There are {parkingSpaces} spaces available")


#halting the system
def halt():
    #tell arduino we are stopping all processing
    talk("halt")
    control_type.set("manualMode")
    messagebox.showinfo("HALT","THE SYSTEM IS SHUTTING DOWN")
    messagebox.showinfo("MODE","System is now in Manual mode")
    

def automaticMode():
    #tell arduino we are going to automatic mode
    if(control_type.get()=="automaticMode"):
        talk("automaticMode")
        messagebox.showinfo("MODE","System is now in automatic mode")
    else:
        talk("manualMode")
        messagebox.showinfo("MODE","System is now in Manual Mode")


#opening the gates
def openEntranceManual():
    talk("openEntrance")
    messagebox.showinfo("Entrance State",f"Entrance is now open")
def openExitManual():
    #tell arduino to open entrance
    talk("openExit")
    messagebox.showinfo("Exit State", f"Exit is now open")

#closing the gates
def closeEntranceManual():
    talk("closeEntrance")
    messagebox.showinfo("Entrance State",f"Entrance is now closed")
def closeExitManual():
    talk("closeExit")
    messagebox.showinfo("Entrance State", f"Exit is now closed")


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
btn_gate1_open = tk.Button(root, text="Open Entrance", bg="lime",command=openEntranceManual)
btn_gate1_open['font'] = myFont1
btn_gate1_open.place(relx=0, rely=0, relwidth=0.5, relheight=0.15)
#close entrance button
btn_gate1_close = tk.Button(root, text="Close Entrance", bg="red",command=closeEntranceManual)
btn_gate1_close['font'] = myFont1
btn_gate1_close.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.15)

#open exit button
btn_gate2_open = tk.Button(root, text="Open Exit", bg="lime", command=openExitManual)
btn_gate2_open['font'] = myFont1
btn_gate2_open.place(relx=0, rely=0.25, relwidth=0.5, relheight=0.15)
#close exit button
btn_gate2_close = tk.Button(root, text="Close Exit", bg="red", command=closeExitManual)
btn_gate2_close['font'] = myFont1
btn_gate2_close.place(relx=0.5, rely=0.25, relwidth=0.5, relheight=0.15)

#parking spots button
btn_available_parking = tk.Button(root, text="Parking Availability", bg="yellow",command=parkingSpaces)
btn_available_parking["font"] = myFont1
btn_available_parking.place(relx=0,rely=0.45,relwidth=1,relheight=0.15)

#ESTOP
btn_estop = tk.Button(root, text="HALT SYSTEM", bg="red", command=halt)
btn_estop["font"] = myFont1
btn_estop.place(relx=0,rely=0.85,relwidth=1,relheight=0.15)

#control type
control_type = StringVar()
control_type.set("manualMode")
btn_control_type = tk.Checkbutton(root, variable = control_type, onvalue="automaticMode", offvalue="manualMode", text = "Automatic Control", bg="purple", command=automaticMode)
btn_control_type['font'] = myFont1
btn_control_type.place(relx=0, rely=0.65, relwidth=1, relheight=0.15)

root.attributes("-fullscreen",True)
root.mainloop()


