import time,random,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

time.sleep(3)
#x,y,z=mc.player.getPos()

def build_igloo(x,y,z):
    mc.setBlocks(x+1,y,z+1,x+6,y+7,z+8,80)
    mc.setBlocks(x+2,y,z+2,x+5,y+6,z+7,0)

build_igloo(0,0,20)
build_igloo(15,0,20)
build_igloo(30,0,20)
build_igloo(45,0,20)
build_igloo(60,0,20)
build_igloo(-15,0,20)
build_igloo(-30,0,20)
build_igloo(-45,0,20)
build_igloo(3,0,35)
build_igloo(18,0,35)
build_igloo(33,0,35)
build_igloo(48,0,35)
build_igloo(63,0,35)
build_igloo(-18,0,35)
build_igloo(-33,0,35)
build_igloo(-48,0,35)
