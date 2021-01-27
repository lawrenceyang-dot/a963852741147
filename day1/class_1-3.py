from mcpi.minecraft import Minecraft as mc
import time
mcs=mc.create()
print(mcs.player.getPos())
x=50
y=100
z=100
x=100
mcs.player.setPos(x,y,z)
time.sleep(2.5)
y=y-10
mcs.player.setPos(x,y,z) 
time.sleep(2.5)         
y=y-10
mcs.player.setPos(x,y,z)
time.sleep(2.5)
y=y-10
mcs.player.setPos(x,y,z)