import time,picamera

def getPicture(name):
    print("Get ready for your photo "+ name)

    opinion = "N"
    with picamera.PiCamera() as camera:
        camera.resolution = (1024,768)
        while opinion.upper()=="N":
            camera.start_preview()
            time.sleep(2)
            fn = name+".jpeg"
            camera.capture(fn)
            camera.stop_preview()
            opinion = input("Do you like this photo? Y/N")
    print("Photo has been saved as "+ fn)
    return fn

def getCharProfile():
    name = ""
    while name=="":
        name = input("What is your name?")
    filename = getPicture(name)
    hat = ""
    while hat=="":
        hat = input("Are you wearing a hat? Y/N")
    eyeColour = ""
    while eyeColour=="":
        eyeColour = input("What colour are your eyes?")
    hairColour = ""
    while hairColour=="":
        hairColour = input("What colour is your hair?")
    gender = ""
    while gender=="":
        gender = input("Are you female or male? F/M")
    facialHair = ""
    while facialHair=="":
        facialHair = input("Do you have any facial hair? Y/N")
    glasses = ""
    while glasses=="":
        glasses = input("Are you wearing any glasses? Y/N")
    characterProfile = [name,filename,hat,eyeColour,hairColour,gender,facialHair,glasses]
    return characterProfile
        
