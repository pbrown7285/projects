import time,random,mcpi.minecraft as Minecraft
mc = Minecraft.Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

def Build_Initials():
    mc.setBlocks(x+2,y,z,x+2,y+7,z,35,6)
    mc.setBlocks(x+3,y+4,z,x+5,y+4,z,35,6)
    mc.setBlocks(x+6,y+6,z,x+6,y+5,z,35,6)
    mc.setBlocks(x+3,y+7,z,x+5,y+7,z,35,6)
    mc.setBlocks(x+8,y,z,x+8,y+7,z,35,6)
    mc.setBlocks(x+9,y+7,z,x+11,y+7,z,35,6)
    mc.setBlocks(x+12,y+6,z,x+12,y+5,z,35,6)
    mc.setBlocks(x+9,y+4,z,x+11,y+4,z,35,6)
    mc.setBlocks(x+12,y+3,z,x+12,y+1,z,35,6)
    mc.setBlocks(x+9,y,z,x+11,y,z,35,6)

def Build_S(x,y,z,colour):
    mc.setBlocks(x+2,y,z,x+5,y,z,35,colour)
    mc.setBlocks(x+6,y+1,z,x+6,y+2,z,35,colour)
    mc.setBlocks(x+3,y+3,z,x+5,y+3,z,35,colour)
    mc.setBlocks(x+2,y+4,z,x+2,y+5,z,35,colour)
    mc.setBlocks(x+3,y+6,z,x+6,y+6,z,35,colour)

Build_S(x,y,z,6)    
