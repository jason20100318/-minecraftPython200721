# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 11:14:04 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time,random


while True:
    x,y,z=mc.player.getTilePos()
    color=random.randrange(0,9)
    
    mc.setBlock(x,y,z-1,38)
    time.sleep(0.2)
   