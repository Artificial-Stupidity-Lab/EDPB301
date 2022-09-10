
from djitellopy import tello
#import droneFunctions as tello
import time
from time import sleep
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
from tkinter import filedialog as fd
#Imaging libraries
import cv2

def surveillance_file():
    #tkinter(GUI) libraries
    
    #creating GUI
    root2 = Tk()
    root2.title("SURVEILLANCE MODE CENTRE")
    #styling the entire GUI
    canvas = tk.Canvas(root2, height=500, width=500)
    frame = tk.Frame(root2, bg="#1bcfa8")
    frame.place(relwidth=1,relheight=1)
    #button styles
    myFont2 = font.Font(family='Helvetica', size=20, weight='bold')


    #Objects
    btn_object = tk.Button(root2, text="Survey Objects", bg="lime")
    btn_object['font'] = myFont2
    btn_object.place(relx=0, rely=0, relwidth=0.5, relheight=0.2)
    #btn_surveillance.bind("<Button-1>",surveillance_mode)

    #Parking
    btn_parking = tk.Button(root2, text="Survey Parking", bg="yellow")
    btn_parking['font'] = myFont2
    btn_parking.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.2)
    #btn_database.bind("<Button-1>",read_database)

    #Vegetation
    btn_vegetation = tk.Button(root2, text="Survey Vegetation", bg="orange")
    btn_vegetation['font'] = myFont2
    btn_vegetation.place(relx=0, rely=0.3, relwidth=0.5, relheight=0.2)
    #btn_defensive.bind("<Button-1>",defensive_mode)

    #Defensive
    btn_defensive1 = tk.Button(root2, text="Defensive Mode", bg="#80c1ff")
    btn_defensive1['font'] = myFont2
    btn_defensive1.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.2)
    #btn_tracking.bind("<Button-1>",tracking_mode)

    #home
    btn_home = tk.Button(root2, text="Main Menu", bg="violet")
    btn_home["font"] = myFont2
    btn_home.place(relx=0,rely=0.6,relwidth=1,relheight=0.15)
    #btn_battery.bind("<Button-1>",get_battery)

    #EStop
    btn_halt = tk.Button(root2, text = "HALT", bg="red")
    btn_halt['font'] = myFont2
    btn_halt.place(relx=0, rely=0.85, relwidth=1, relheight=0.15)
    #btn_halt.bind("<Button-1>",halt)

    root2.geometry("500x500")
    root2.mainloop()