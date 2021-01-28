from mcpi.minecraft import Minecraft
mc = Minecraft.create()
Line1 = []
Line2 = []
Line3 = []

for i in range(1,4):
    Line1.append(i*1)
for i in range(1,4):
    Line2.append(i*2)
for i in range(1,4):
    Line3.append(i*3)
    
#Print(Line1,"\n",Line2,"\n",Line3)
x,y,z = mc.player.getTilePos()
mc.setSign(x,y,z,63,0,str(Line1),str(Line2),str(Line3))