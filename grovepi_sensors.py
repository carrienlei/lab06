
import time
import grovepi

rotaryPort = 0 #Grovepi potentiometer connected to analog port A0
UltrasonicPort = 4 #Grovepi ultrasonic ranger connected to port 4.

if __name__ == '__main__':
  while (True):
    time.sleep(0.1)
    
    # Set a threshold distance by turning the rotary angle sensor.
    rotaryAngle = grovepi.analogRead(rotaryPort)
    
    # Measures the distance to an object using the ultrasonic ranger.
    distance = grovepi.ultrasonicRead(ultrasonicPort)
    
    # Determines whether the object is within the threshold distance.
    if (rotaryAngle <= distance):
        print("wrong")
    elif (rotaryAngle > distance):
        print('"blah")
    
