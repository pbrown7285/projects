import time,picamera,json #imports the needed modules

def getPicture(name):
    print("Get ready for your photo "+ name) #informs the user that their picture will be taken

    opinion = "N"
    with picamera.PiCamera() as camera:
        camera.resolution = (1024,768)
        while opinion.upper()=="N":
            camera.start_preview()
            time.sleep(2)
            fn = name+".jpeg"
            camera.capture(fn)
            camera.stop_preview()
            opinion = input("Do you like this photo? Y/N") #asks the user if they like the photo
    print("Photo has been saved as "+ fn)
    return fn #returns the filename

def getCharProfile(): #defines the 'get character profile' function
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
    return characterProfile #returns the character profile information to the user
        
def saveProfile(profileList):
    profile = getCharProfile()
    profileList.append(profile)
    with open("Files.txt",mode="w") as file:
        json.dump(profileList,file)

def loadProfile():
    profiles = []
    try:
        with open("Files.txt",mode="r") as file:
            json.load(profiles,file)
    except IOError:
        print("Error")
        saveProfile(profiles)
