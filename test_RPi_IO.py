import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
#the 6th pin in the right
GPIO.setup(18, GPIO.OUT)        
GPIO.output(18, GPIO.LOW)
#the 8th pin in the right
GPIO.setup(23, GPIO.IN)

while True:
    print(GPIO.input(23))
    GPIO.output(18, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(18, GPIO.LOW)