import time
import sys
import grovepi
from grove_rgb_lcd import *


rotaryPort = 0 #Grovepi potentiometer connected to analog port A0
ultrasonicPort = 4 #Grovepi ultrasonic ranger connected to port 4.
LCDPort = 3 #Grovepi LCD panel connected to port 5.

grovepi.pinMode(rotaryPort, "INPUT")
grovepi.pinMode(LCDPort, "OUTPUT")
        
if __name__ == '__main__':
  while (True):
    time.sleep(.1)
    
    # Set a threshold distance by turning the rotary angle sensor. 
    threshold = grovepi.analogRead(rotaryPort)
    
    # Measures the distance to an object using the ultrasonic ranger.
    distance = grovepi.ultrasonicRead(ultrasonicPort)    
    
    # Determines whether the object is within the threshold distance.
    if (threshold <= distance): # object not wihtin threshold; backlight green
        setText_norefresh(str(threshold)+ "          \n" + str(distance))
        setRGB(0, 255, 0)
    else: # object within threshold; backlight red
        setText_norefresh(str(threshold)+ " OBJ PRES\n" + str(distance))
        setRGB(255, 0, 0)
