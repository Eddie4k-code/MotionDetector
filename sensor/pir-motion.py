import RPi.GPIO as GPIO
import time

motionPin = 12
GPIO.setmode(GPIO.BOARD)

GPIO.setup(motionPin, GPIO.IN)

#time.sleep(10)

print("Starting Motion Detector")

try:
    while True:
        motion = GPIO.input(motionPin)
        
        if motion == 1:
            print("Motion Detected")
        else:
            print("Looking for motion")
        
        time.sleep(.1)
    
    
except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO Cleanup done.")