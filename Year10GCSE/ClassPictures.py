import time,picamera #Imports the necessary modules

with picamera.PiCamera() as camera: #Renaming the module and using it
    camera.resolution = (1024,768) #Sets the resolution
    camera.start_preview() #Shows us what we will take a photo of

    time.sleep(2) #Waits for two seconds
    camera.capture("classpicture.jpeg") #Captures the photo and names it
    
