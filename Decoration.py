# -*- coding: utf-8 -*-

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import *
from Object import *

class Decoration() :
    
    def __init__(self, showbase) :
        
        #--------------------- SKY
        
        showbase.scene = Object(showbase, "ForestSky/ForestSky", 
                           0.10, 0.10, 0.10, 
                           0, 0, 0, 
                           0, 0, 8.8, showbase.render)               
        
        #--------------------- DECORATIONS

        showbase.dec = Object(showbase, "Shrubbery2/Shrubbery2", 
                          0.01, 0.01, 0.01, 
                          0, 0, 0, 
                          7, 8, -0.5, showbase.render)             
                          
        
        for i in range(0, 4) :   
            showbase.dec = Object(showbase, "MushroomStalk/MushroomStalk", 
                          0.3 * i, 0.3 * i, 0.9, 
                          0, 0, 0, 
                          4 - i * 3, 10 - i * 3, 0, showbase.render)            

        
        for i in range(1, 3) :
            showbase.dec = Object(showbase, "Tulip/Tulip", 
                          8, 8, 8, 
                          90, 0, 0, 
                          10 + i * i, 8 - i * i, -0.5, showbase.render) 
        
        
        for i in range(1, 4) :
            showbase.dec = Object(showbase, "Sunflower/Sunflower", 
                          2.3 * i, 2.2 * i, 2.5 * i, 
                          180, 0, 0, 
                          7.5 + i, 8 + i, -1.5, showbase.render)