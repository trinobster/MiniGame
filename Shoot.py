# -*- coding: utf-8 -*-

from panda3d.bullet import BulletSphereShape
from panda3d.bullet import BulletWorld
from direct.showbase.ShowBase import ShowBase
from panda3d.bullet import BulletRigidBodyNode
from panda3d.core import *

imagePath = "./images/"

class Shoot( ) :
    
    def __init__(self, showbase) :
        
        self.showbase = showbase
        self.actor = showbase.actor
        
        print('Press "q" to shoot')
        showbase.accept('q', self.createBall)

    def createBall(self) :
        
        self.actor.play("launch")

        # Sphere
        self.shape = BulletSphereShape(0.15)
        self.node = BulletRigidBodyNode('Sphere')
        self.node.setMass(1)
        self.node.addShape(self.shape)
        self.np = self.showbase.render.attachNewNode(self.node)
        self.np.setPos(self.actor.getX(), self.actor.getY(), self.actor.getZ() + 2.5)

        # Smiley
        self.model = self.showbase.loader.loadModel("./models/smiley")
        self.model.setTexture(self.showbase.loader.loadTexture(imagePath + 'metal1.jpg'), 1)
        self.model.flattenLight()
        self.model.setScale(0.15, 0.15, 0.15)
        self.model.reparentTo(self.np)
        
        # Set speed
        h = self.actor.getH()
        if(h == 0) :
            x = 0
            y = 8
        if(h == 90) :
            x = -7
            y = 0
        if(h == 180) :
            x = 0
            y = -8
        if(h == -90) :
            x = 8
            y = 0
            
        self.node.setLinearVelocity(Vec3(x, y, 6.2)) #self.actor.getX()/3, 11, 6.2)
        self.showbase.world.attachRigidBody(self.node)