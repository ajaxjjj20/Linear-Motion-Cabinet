import motor

#Variables
direction = 1
delay = 0.001
steps = 800

#Create motor
myMotor = motor.StepperMotor()

#Move motor
myMotor.Move(direction, delay, steps)
