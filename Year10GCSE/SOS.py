#SOS Flasher by Pippa

import RPi.GPIO as GPIO,time

GPIO.setmode(GPIO.BOARD) #Set the pin numbering system

GPIO.setup(11,GPIO.OUT)

#Function Definition for Morse Code Dot
def Dot():
	GPIO.output(11,False)
	time.sleep(0.5)
	GPIO.output(11,True)
	time.sleep(0.5)

#Function Definition for Morse Code Dash
def Dash():
	GPIO.output(11,False)
	time.sleep(1.5)
	GPIO.output(11,True)
	time.sleep(0.5)

#Morse Code for SOS
Dot()
Dot()
Dot()
Dash()
Dash()
Dash()
Dot()
Dot()
Dot()





