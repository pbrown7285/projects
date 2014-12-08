name = ""
while name=="":
    name = input("What is your name?")
print("Good morning "+ name)

guess = ""
password = "QueenPippa"
while guess!=password:
    guess = input("What is the password?")
print("Well done!")


import time,picamera
opinion = "N"


with picamera.PiCamera() as camera:
    camera.resolution = (1024,768)
    while opinion.upper()=="N":
        camera.start_preview()
        time.sleep(2)
        camera.capture(name+".jpeg")
        camera.stop_preview()
        opinion = input("Do you like this photo? Y/N")

