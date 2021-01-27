# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 11:47:46 2021

@author: USER
"""
from mcpi.minecraft import minecraft as mc
mcs=mc.create()
print(getTilePos())
x=50
y=50
z=50
x=60
mcs.player.setTilePos(x,y,z)