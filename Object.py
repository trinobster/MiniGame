# -*- coding: utf-8 -*-

from panda3d.core import *

class Object( ) :
    
    def __init__(self, showbase, path, scaleX, scaleY, scaleZ, h, p, r, x, y, z, np) :
        
        modelPath = "./models/"
        
        showbase.object = showbase.loader.loadModel(modelPath + path) # load the model.
        # The return value is an object of the NODEPATH class, effectively a POINTER to the model. 
        showbase.object.reparentTo(np) # reparent the model to render
        showbase.object.setScale(scaleX, scaleY, scaleZ) # apply scale to model
        showbase.object.setHpr(h, p, r)
        showbase.object.setPos(x, y, z) # apply position to model 