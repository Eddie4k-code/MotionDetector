import RPi.GPIO as GPIO
import time

class MotionSensor:
    def __init__(self, motionPin):
        self.motionPin = motionPin

    def runDetector(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.motionPin, GPIO.IN)

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


    
