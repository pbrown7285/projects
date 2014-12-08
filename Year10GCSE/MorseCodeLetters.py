#Importing GPIO for LEDs
import time,RPi.GPIO as GPIO

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

#Making Morse Code for Every Letter
def MorseLetter(letter):
	if letter == "A":
		Dot()
		Dash()
	elif letter == "B":
		Dash()
		Dot()
		Dot()
		Dot()
	elif letter == "C":
		Dash()
		Dot()
		Dash()
		Dot()
	elif letter == "D":
		Dash()
		Dot()
		Dot()
	elif letter == "E":
		Dot()
	elif letter == "F":
		Dot()
		Dot()
		Dash()
		Dot()
	elif letter == "G":
		Dash()
		Dash()
		Dot()
	elif letter == "H":
		Dot()
		Dot()
		Dot()
		Dot()
	elif letter == "I":
		Dot()
		Dot()
	elif letter == "J":
		Dot()
		Dash()
		Dash()
		Dash()
	elif letter == "K":
		Dash()
		Dot()
		Dash()
	elif letter == "L":
		Dot()
		Dash()
		Dot()
		Dot()
	elif letter == "M":
		Dash()
		Dash()
	elif letter == "N":
		Dash()
		Dot()
	elif letter == "O":
		Dash()
		Dash()
		Dash()
	elif letter == "P":
		Dot()
		Dash()
		Dash()
		Dot()
	elif letter == "Q":
		Dash()
		Dash()
		Dot()
		Dash()
	elif letter == "R":
		Dot()
		Dash()
		Dot()
	elif letter == "S":
		Dot()
		Dot()
		Dot()
	elif letter == "T":
		Dash()
	elif letter == "U":
		Dot()
		Dot()
		Dash()
	elif letter == "V":
		Dot()
		Dot()
		Dot()
		Dash()
	elif letter == "W":
		Dot()
		Dash()
		Dash()
	elif letter == "X":
		Dash()
		Dot()
		Dot()
		Dash()
	elif letter == "Y":
		Dash()
		Dot()
		Dash()
		Dash()
	elif letter == "Z":
		Dash()
		Dash()
		Dot()
		Dot()
	else:
		Print("Unknown Symbol - Space?")

letter = input("Please enter a capital letter.")
MorseLetter(letter)
