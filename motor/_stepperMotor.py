import RPi.GPIO as GPIO
import time

class StepperMotor():
	#Set default values for the pins
	#Let's take out the stops from the motor class
	#And create a motor stop class that runs in the background
	def __init__(self, stp = 7, dirPin = 11, MS1 = 13, MS2 = 15, MS3 = 29, EN = 31, upperLimit = 0, lowerLimit = 0):
		self.stp = stp
		self.dirPin = dirPin
		self.MS1 = MS1
		self.MS2 = MS2
		self.MS3 = MS3
		self.EN = EN

		#We are setting it to BOARD mode to use actual numbers
		#Instead of using GPIO.BCM which corresponds to different numbering
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)


		#Setup IO pins appropriately
		GPIO.setup(self.stp, GPIO.OUT)
		GPIO.setup(self.dirPin, GPIO.OUT)
		GPIO.setup(self.MS1, GPIO.OUT)
		GPIO.setup(self.MS2, GPIO.OUT)
		GPIO.setup(self.MS3, GPIO.OUT)
		GPIO.setup(self.EN, GPIO.OUT)

		#Reset all pins to original state
		self.resetPins()

		#Pull enable pin low to set FETs active 
		#and allow motor control
		GPIO.output(EN, False)

		#Set MS1/2/3 to false so we go a full step
		GPIO.output(MS1, False)
		GPIO.output(MS2, False)
		GPIO.output(MS3, False)

		self.upperLimit = upperLimit
		self.lowerLimit = lowerLimit

	def resetPins(self):
		GPIO.output(self.stp, False)
		GPIO.output(self.dirPin, False)
		GPIO.output(self.MS1, False)
		GPIO.output(self.MS2, False)
		GPIO.output(self.MS3, False)
		GPIO.output(self.EN, True)

	def Move(self, direction, delay, steps = 0):
		#Pull direction pin low to move "forward"
		GPIO.output(self.dirPin, direction)
		#Move enough times so that it is visible

		if steps > 0:
			for i in range(steps):
				#If moving in the positive direction, check if we are past the upper limit
				if direction and self.getDistance() >= self.upperLimit and self.upperLimit:
					#Create an out of bounds exception
					raise Exception
				#If moving in the negative direction, check if we are past the lower limit
				elif not direction and self.getDistance() <= self.lowerLimit and self.lowerLimit:
					#Create an out of bounds exception
					raise Exception
				#If not past our limits, move to the appropriate steps
				else:
					self.moveStep(delay)
		elif not steps and (self.upperLimit and self.direction) or (self.lowerLimit and not direction):
			while not(direction and self.getDistance() >= self.upperLimit and self.upperLimit):
				self.moveStep(delay)
			while not(not direction and self.getDistance() <= self.lowerLimit and self.lowerLimit):
				self.moveStep(delay)

		#Make sure to reset the pins once we are done so it is ready for the next command
		self.resetPins()

	def moveStep(self, delay):
		GPIO.output(self.stp, True)
		time.sleep(delay)
		#Must set the stp pin to false
		#So it can be triggered again next time
		GPIO.output(self.stp, False)
		time.sleep(delay)

	def getDistance(self):
		#How are we going to do this??
		#Need to research the code for the distance board
		pass 










#print "Finished Imports"

#delay = 0.001
##delay = 0.0055
##delay = 0.05
#steps = 400

##We are setting it to BOARD mode to use actual numbers
##Instead of using GPIO.BCM which corresponds to different numbering
#GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)

#print "Finished GPIO set mode"

##Pin variables
##Pins are weird because of the layout that pi uses
#stp = 7
#dirPin = 11
#MS1 = 13
#MS2 = 15
#MS3 = 29
#EN = 31

#GPIO.setup(stp, GPIO.OUT)
#GPIO.setup(dirPin, GPIO.OUT)
#GPIO.setup(MS1, GPIO.OUT)
#GPIO.setup(MS2, GPIO.OUT)
#GPIO.setup(MS3, GPIO.OUT)
#GPIO.setup(EN, GPIO.OUT)

#print "Finished GPIO setup"

##Reset all pins to original state
#resetPins(stp, dirPin, MS1, MS2, MS3, EN)

##Pull enable pin low to set FETs active 
##and allow motor control
#GPIO.output(EN, False)

##Set MS1/2/3 to false so we go a full step
#GPIO.output(MS1, False)
#GPIO.output(MS2, False)
#GPIO.output(MS3, False)

#print "About to call step forward function"

#StepForwardDefault(steps, delay, dirPin, stp)

#resetPins(stp, dirPin, MS1, MS2, MS3, EN)

