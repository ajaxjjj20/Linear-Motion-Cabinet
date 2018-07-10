import RPi.GPIO as GPIO
import time

def StepForwardDefault(steps, delay, dirPin = 11, stp = 7):
	#Pull direction pin low to move "forward"
	GPIO.output(dirPin, False)
	#Move enough times so that it is visible
	for i in range(steps):
		GPIO.output(stp, True)
		time.sleep(delay)
		#Must set the stp pin to false
		#So it can be triggered again next time
		GPIO.output(stp, False)
		time.sleep(delay)
		
def resetPins(stp, dirPin, MS1, MS2, MS3, EN):
	GPIO.output(stp, False)
	GPIO.output(dirPin, False)
	GPIO.output(MS1, False)
	GPIO.output(MS2, False)
	GPIO.output(MS3, False)
	GPIO.output(EN, True)


print "Finished Imports"

delay = 0.001
#delay = 0.0055
#delay = 0.05
steps = 400

#We are setting it to BOARD mode to use actual numbers
#Instead of using GPIO.BCM which corresponds to different numbering
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

print "Finished GPIO set mode"

#Pin variables
#Pins are weird because of the layout that pi uses
stp = 7
dirPin = 11
MS1 = 13
MS2 = 15
MS3 = 29
EN = 31

GPIO.setup(stp, GPIO.OUT)
GPIO.setup(dirPin, GPIO.OUT)
GPIO.setup(MS1, GPIO.OUT)
GPIO.setup(MS2, GPIO.OUT)
GPIO.setup(MS3, GPIO.OUT)
GPIO.setup(EN, GPIO.OUT)

print "Finished GPIO setup"

#Reset all pins to original state
resetPins(stp, dirPin, MS1, MS2, MS3, EN)

#Pull enable pin low to set FETs active 
#and allow motor control
GPIO.output(EN, False)

#Set MS1/2/3 to false so we go a full step
GPIO.output(MS1, False)
GPIO.output(MS2, False)
GPIO.output(MS3, False)

print "About to call step forward function"

StepForwardDefault(steps, delay, dirPin, stp)

resetPins(stp, dirPin, MS1, MS2, MS3, EN)

