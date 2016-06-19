# -*- coding: utf-8 -*-

from direct.showbase.ShowBase import ShowBase
from panda3d.core import *

class HandleArrows() :
    
    def __init__(self, showbase, maxX, maxY, minX, minY) :
        
        self.maxX = maxX
        self.maxY = maxY
        self.minX = minX
        self.minY = minY
        
       # base.disableMouse()
        
        showbase.accept('arrow_right', self.move_right)
        showbase.accept('arrow_left', self.move_left)
        showbase.accept('arrow_up', self.move_up)
        showbase.accept('arrow_down', self.move_down)
        
    
    def move_right(self):
        camera = base.cam
        if(camera.getX() < self.maxX) :
            camera.setX(camera.getX() + 1)
        #print('x = ', camera.getX())
        
        
    def move_left(self):
        camera = base.cam
        if(camera.getX() > self.minX) :
            camera.setX(camera.getX() - 1)
        
    def move_down(self):
        camera = base.cam
        if(camera.getY() > self.minY) :
            camera.setY(camera.getY() - 1)
        #print('y = ', camera.getY())
        
    def move_up(self):
        camera = base.cam
        if(camera.getY() < self.maxY) :
            camera.setY(camera.getY() + 1)