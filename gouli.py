import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
pos=mc.player.getTilePos()

f=open("gou.txt",'r')
nameList=f.readlines()
xCounter=0
for line in nameList:
    digitalList=line.split(",")
    zCounter=0
    for digitalSingle in digitalList:
        if digitalSingle=="1":
            mc.setBlock(pos.x+xCounter,pos.y-1,pos.z-zCounter,51)
        else:
            mc.setBlock(pos.x+xCounter,pos.y-1,pos.z-zCounter,46)
        zCounter+=1
    xCounter+=1
            
            
        
