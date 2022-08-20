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

drone = tello.Tello()  #creating an object for the drone
drone.connect() #communicating with the drone
drone.takeoff()