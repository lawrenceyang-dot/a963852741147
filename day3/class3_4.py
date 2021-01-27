from mcpi.minecraft import Minecraft 
mc = Minecraft.create()
x,y,z = mc.player.getPos()
def planttree(x,y,z,mc,c,t):
    mc.setBlocks(x-1,y+4,z-1,x+1,y+7,z+1,c,5)
    mc.setBlocks(x,y,z,x,y+4,z,t)
"""for i in range(0,40,5):
    for j in range(5):
        planttree(x+i,y,z+j*5,mc,11,11)"""
        
for i in range(0,40,5):
    for j in range(5):
        for q in range(5):
            planttree(x+i,y+j*i,z+q*i,mc,11,11)
    