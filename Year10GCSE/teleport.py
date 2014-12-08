import time,mcpi.minecraft as minecraft #Imports the things to do with time
mc = minecraft.Minecraft.create() #Connects to an open/existing game

time.sleep(3)
mc.postToChat("Hello everyone.")
time.sleep(0.5)
mc.postToChat("Minecraft is actually annoying.")
time.sleep(0.5)

