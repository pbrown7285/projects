import mcpi.minecraft as Minecraft,time as Time
mc = Minecraft.Minecraft.create()

black=7
red=14
orange=1
green=5

mc.setBlock(-10,0,9,35,black)
mc.setBlock(-10,1,9,35,black)
mc.setBlock(-10,2,9,35,black)
mc.setBlock(-10,2,9,35,black)
mc.setBlock(-10,3,9,35,black)
mc.setBlock(-10,4,9,35,black)
mc.setBlock(-10,5,9,35,black)
while True:
    mc.setBlock(-10,5,9,35,red)
    Time.sleep(2)
    mc.setBlock(-10,4,9,35,orange)
    Time.sleep(1)
    mc.setBlock(-10,5,9,35,black)
    mc.setBlock(-10,4,9,35,black)
    mc.setBlock(-10,3,9,35,green)
    Time.sleep(2)
    mc.setBlock(-10,3,9,35,black)
    mc.setBlock(-10,4,9,35,orange)
    Time.sleep(1)
    mc.setBlock(-10,4,9,35,black)
