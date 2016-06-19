# -*- coding: utf-8 -*-

from direct.showbase.ShowBase import ShowBase
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import *

class HandleCharacter() :
    
    def __init__(self, showbase, maxX, maxY, minX, minY) :
        
        self.maxX = maxX
        self.maxY = maxY
        self.minX = minX
        self.minY = minY
        self.showbase = showbase
        self.actor = showbase.actor
        
       # base.disableMouse()
        
        self.showbase.accept('d', self.move_right)
        self.showbase.accept('a', self.move_left)
        self.showbase.accept('w', self.move_up)
        self.showbase.accept('s', self.move_down)
        
    def intervalSequence(self) :
        self.pandaPace = Sequence(self.actorHprInterval1,
                                  self.actorPosInterval1,
                                  name="pandaPace")
        self.pandaPace.start()
    
    def move_up(self):
        self.actorHprInterval1 = self.actor.hprInterval(0.3,
                                                        Point3(0, 0, 0),
                                                        startHpr = Point3(self.actor.getH(), 0, 0))
                                                        
        if(self.actor.getX() < self.maxX) :
            self.actor.play("walk")
            self.actorPosInterval1 = self.actor.posInterval(1, 
                                                       Point3(self.actor.getX(), self.actor.getY() + 1, self.actor.getZ()), startPos = Point3(self.actor.getX(), self.actor.getY(), self.actor.getZ()))
            #self.actor.play("walk")
        self.intervalSequence()
            
    def move_right(self):
        self.actorHprInterval1 = self.actor.hprInterval(0.3,
                                                        Point3(-90, 0, 0),
                                                        startHpr = Point3(self.actor.getH(), 0, 0))
        if(self.actor.getX() < self.maxX) :
            self.actor.play("walk")
            self.actorPosInterval1 = self.actor.posInterval(1, 
                                                       Point3(self.actor.getX() + 1, self.actor.getY(), self.actor.getZ()), startPos = Point3(self.actor.getX(), self.actor.getY(), self.actor.getZ()))
            self.intervalSequence()
        
        
    def move_left(self):
        self.actorHprInterval1 = self.actor.hprInterval(0.3,
                                                        Point3(90, 0, 0),
                                                        startHpr = Point3(self.actor.getH(), 0, 0))
        if(self.actor.getX() < self.maxX) :
            self.actor.play("walk")
            self.actorPosInterval1 = self.actor.posInterval(1, 
                                                       Point3(self.actor.getX() - 1, self.actor.getY(), self.actor.getZ()), startPos = Point3(self.actor.getX(), self.actor.getY(), self.actor.getZ()))
            self.intervalSequence()
        
    def move_down(self):
        self.actorHprInterval1 = self.actor.hprInterval(0.3,
                                                        Point3(180, 0, 0),
                                                        startHpr = Point3(self.actor.getH(), 0, 0))
        if(self.actor.getX() < self.maxX) :
            self.actor.play("walk")
            self.actorPosInterval1 = self.actor.posInterval(1, 
                                                       Point3(self.actor.getX(), self.actor.getY() - 1, self.actor.getZ()), startPos = Point3(self.actor.getX(), self.actor.getY(), self.actor.getZ()))
            self.intervalSequence()