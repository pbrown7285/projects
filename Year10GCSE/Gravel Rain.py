import time,random,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

while True: #This loops the progam infinitely
    pos = mc.player.getPos() #This gets the player's position
    x = pos.x #Gets the x coordinate
    y = pos.y #Gets the y coordinate
    z = pos.z #Gets the z coordinate

    a = random.randint(-10,+10) #Randomising
    b = random.randint(-10,+10) #Randomising

    mc.setBlock(x+a,50,z+b,13) #Sets the gravel to a random location

    time.sleep(0.2) #Pauses for 0.2 seconds
