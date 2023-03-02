
import time
import sys
sys.path.append('../../Software/Python/grove_rgb_lcd')
import grovepi
from grove_rgb_lcd import *


rotaryPort = 0 #Grovepi potentiometer connected to analog port A0
UltrasonicPort = 4 #Grovepi ultrasonic ranger connected to port 4.
LCDPort = 5 #Grovepi LCD panel connected to port 5.

grovepi.pinMode(rotaryPort, "INPUT")
grovepi.pinMode(LCDPort, "OUTPUT")


# # Functions to print onto LCD. https://github.com/DexterInd/GrovePi/blob/master/Software/Python/grove_rgb_lcd/grove_rgb_lcd.py
# def textCommand(cmd):
#     bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,cmd)
      
# def setText_norefresh(text):
#     textCommand(0x02) # return home
#     time.sleep(.05)
#     textCommand(0x08 | 0x04) # display on, no cursor
#     textCommand(0x28) # 2 lines
#     time.sleep(.05)
#     count = 0
#     row = 0
#     while len(text) < 32: #clears the rest of the screen
#         text += ' '
#     for c in text:
#         if c == '\n' or count == 16:
#             count = 0
#             row += 1
#             if row == 2:
#                 break
#             textCommand(0xc0)
#             if c == '\n':
#                 continue
#         count += 1
#         bus.write_byte_data(DISPLAY_TEXT_ADDR,0x40,ord(c))

# # Function to change backlight color. 
# def setRGB(r,g,b):
#     bus.write_byte_data(DISPLAY_RGB_ADDR,0,0)
#     bus.write_byte_data(DISPLAY_RGB_ADDR,1,0)
#     bus.write_byte_data(DISPLAY_RGB_ADDR,0x08,0xaa)
#     bus.write_byte_data(DISPLAY_RGB_ADDR,4,r)
#     bus.write_byte_data(DISPLAY_RGB_ADDR,3,g)
#     bus.write_byte_data(DISPLAY_RGB_ADDR,2,b)
        
if __name__ == '__main__':
  while (True):
    time.sleep(0.25)
    
    # Set a threshold distance by turning the rotary angle sensor. 
    threshold = grovepi.analogRead(rotaryPort)
    
    # Measures the distance to an object using the ultrasonic ranger.
    distance = grovepi.ultrasonicRead(ultrasonicPort)    
    
    # Determines whether the object is within the threshold distance.
    if (threshold <= distance): # object not wihtin threshold; backlight green
        setText_norefresh(str(rotaryAngle)+ "\n" + str(distance))
        setRGB(0, 255, 0)
    else: # object within threshold; backlight red
        setText_norefresh(str(rotaryAngle)+ " OBJ PRES\n" + str(distance))
        setRGB(255, 0, 0)
