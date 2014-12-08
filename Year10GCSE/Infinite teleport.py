import random,time,mcpi.minecraft as Minecraft #This imports the two necessary modules
mc = Minecraft.Minecraft.create() #Connects to Minecraft

def Coordinates():
    x = random.randint(0,256)
    y = random.randint(0,256)
    z = random.randint(0,256)
    return x,y,z

while True:
    time.sleep(3)
    mc.postToChat("Random teleportation in 3 seconds.")
    time.sleep(1)
    mc.postToChat("Random teleportation in 2 seconds.")
    time.sleep(1)
    mc.postToChat("Random teleportation in 1 second.")
    time.sleep(1)
    x,y,z = Coordinates()
    mc.player.setPos(x,y,z)
    time.sleep(1)
    mc.postToChat("You have teleported.")

