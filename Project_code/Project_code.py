import serial
from tkinter import *
import tkinter as tkinter
from tkinter import messagebox
import time

#variables
arduino_data=serial.Serial("com3", baudrate = 115200, timeout = 1)

#creating GUI