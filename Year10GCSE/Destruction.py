import mcpi.minecraft as minecraft,time,random #Imports modules
mc = minecraft.Minecraft.create() #Connects to minecraft

mc.setBlocks(-30,-5,-30,30,30,30,0) #Clears everything around 0,0,0

for b in range(21,6,-7): #Changes the colours of the block
    mc.postToChat(b) #Posts to chat
    mc.setBlock(0,b,0,35,b) #Sets blocks at these points
    time.sleep(2) #Pauses for two seconds
