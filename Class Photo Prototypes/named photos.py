import time,picamera

for run in range(5):
    name = input("What is your name?")
    with picamera.PiCamera() as camera:
        camera.resolution = (1024,768)
        camera.start_preview()
        time.sleep(2)
        camera.capture(name+".jpeg")
