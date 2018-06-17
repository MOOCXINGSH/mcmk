#coding=utf-8

import mcpi.minecraft as minecraft
import mcpi.block as block
import city
#mc.postToChat(str(pos.x))
def showRoof():
	dis=0
	for i in city.fileList:
		createRoof(i,dis)
		dis+=25
def createRoof(f,dis):
	mc=minecraft.Minecraft.create()
	pos=mc.player.getTilePos()
	#f=city.f2
	nameList=f.readlines()
	xCounter=0
	for line in nameList:
		digitalList=line.split(",")
		zCounter=0
		for digitalSingle in digitalList:
			if digitalSingle=='1':
				mc.setBlock(pos.x+xCounter+dis,pos.y-1,
				pos.z-zCounter,block.DIAMOND_BLOCK.id)
			else:
				mc.setBlock(pos.x+xCounter+dis,pos.y-1,
				pos.z-zCounter,block.WOOD.id)
			zCounter+=1
		xCounter+=1
showRoof()
	
	
	
	
	
	
	
	
	
	
