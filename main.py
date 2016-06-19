from HandleArrows import *
from Decoration import *
from Shoot import *
from Object import *
from HandleCharacter import *

from panda3d.bullet import BulletWorld
from panda3d.bullet import BulletPlaneShape
from panda3d.bullet import BulletRigidBodyNode
from panda3d.bullet import BulletCylinderShape
from panda3d.bullet import BulletBoxShape
from panda3d.bullet import BulletDebugNode
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence

imagePath = "./images/"
musicPath = "./music/"

class MyApp(ShowBase) :
    
    def __init__(self) :
        ShowBase.__init__(self)
        
        #--------------------- MUSIC
        mySound = base.loader.loadSfx(musicPath + "mus_reunited.ogg")
        mySound.play()
        
        
        #--------------------- WORLD
        self.world = BulletWorld()
        self.world.setGravity(Vec3(0, 0, -9.81))     
        
##         --------------------- DEBUG
#        debugNode = BulletDebugNode('Debug')
#        debugNode.showWireframe(True)
#        debugNode.showConstraints(True)
#        debugNode.showBoundingBoxes(False)
#        debugNode.showNormals(False)
#        debugNP = render.attachNewNode(debugNode)
#        debugNP.show()
#        
#        debugNode.showWireframe(True)
#        self.world.setDebugNode(debugNP.node())
        
        
        #--------------------- GRASS
        shape = BulletPlaneShape(Vec3(0, 0, 1), 0) # creo la forma geometrica (normale, distanza)
        node = BulletRigidBodyNode('Ground') # creo il rigidbody per il terreno
        node.addShape(shape) # link tra il rigidbody e la forma geometrica
        np = render.attachNewNode(node)
        np.setPos(0, 0, -0.5) #-1.5
        
        cm = CardMaker('card') # crea una carta bianca a cui appiccicare la texture
        cm.setFrame(-20, 20, -20, 20)
        grass = self.render.attachNewNode(cm.generate()) # attacca il nodo FLOOR
        pattern = self.loader.loadTexture(imagePath + 'grass3.jpg') # handler per la texture
        ts = TextureStage('ts')
        grass.setP(270)
        grass.setTexScale(ts, 3, 3)
        grass.setTexture(ts, pattern) # appiccica la texture al modello
        grass.reparentTo(np) # collega la texture dell'erba al nodo fisico
        
        self.world.attachRigidBody(node) # solo i nodi attaccati al world vengono considerati nella simulazione

        
        #--------------------- CRASH (MY MODEL)
        self.actor = Actor("models/MyCrash1/MyCrash1.egg", 
                           {"walk":"./models/MyCrash1/CrashWalk.egg","launch":"./models/MyCrash1/CrashLaunch.egg"})
        self.actor.reparentTo(np) # reparent the model to render
        self.actor.setScale(1, 1, 1) # apply scale to model
        self.actor.setPos(3, -10, 0) # apply position to model 
        
        #--------------------- CAMERA
        base.cam.setPos(self.actor.getX(), self.actor.getY() - 18, self.actor.getZ() + 4)
        base.cam.lookAt(self.actor.getX(), self.actor.getY(), self.actor.getZ() + 2)
        
        
        #--------------------- TABLE
        shape = BulletBoxShape(Vec3(4.8, 1.45, 0.15))
        node = BulletRigidBodyNode('Box')
        node.addShape(shape)
        np = render.attachNewNode(node)
        np.setPos(5, 3, 0.8 - 0.5)        
        
        self.table = Object(self, "CafeTableLong/CafeTableLong", 
                            0.01, 0.01, 0.01, 
                            0, 0, 0, 
                            0, 0, -0.15, np)
        
        self.world.attachRigidBody(node) 
                
        
        #--------------------- ARMCHAIR
        shape = BulletBoxShape(Vec3(1.35, 1.5, 2)) #2
        node = BulletRigidBodyNode('Box')
        node.addShape(shape) 
        node.setMass(5)
        np = render.attachNewNode(node)
        np.setPos(12, 3, 1.5)        
        
        self.chair = Object(self, "ArmChair/ArmChair", 
                            0.0013, 0.0013, 0.0013, 
                            100, 0, 0, 
                            0, 0, -1.5, np)
        
        self.world.attachRigidBody(node) 
        
        
        #--------------------- OBJECTS TO HIT
        # cake
        shape = BulletCylinderShape(0.56, 0.5, 2)
        node = BulletRigidBodyNode('Cylinder')
        node.setMass(2)
        node.addShape(shape)
        np = render.attachNewNode(node)
        np.setPos(5, 3, 0.62)
        
        self.cake = Object(self, "Cake/Cake", 
                           0.008, 0.008, 0.009, 
                           0, 0, 0, 
                           0, 0, -0.25, np)

        self.world.attachRigidBody(node)
        
        
        #teapot
        shape = BulletBoxShape(Vec3(0.65, 0.3, 0.8)) # creo la forma geometrica (normale, distanza)
        node = BulletRigidBodyNode('Box') # creo il rigidbody per il terreno
        node.setMass(2)
        node.addShape(shape) # link tra il rigidbody e la forma geometrica
        np = render.attachNewNode(node)
        np.setPos(3, 3, 1.2)   
        
        self.tea = Object(self, "Teapot/Teapot", 
                          1, 1, 1, 
                          90, 0, 0, 
                          0, 0, -0.83, np)

        self.world.attachRigidBody(node)
        
        
        #mug
        shape = BulletCylinderShape(0.2, 0.5, 2)
        node = BulletRigidBodyNode('Cylinder')
        node.setMass(2)
        node.addShape(shape)
        np = render.attachNewNode(node)
        np.setPos(6, 3, 1.2 - 0.54)        
        
        self.mug = Object(self, "cup/cup", 
                          0.02, 0.02, 0.02, 
                          0, 0, 0, 
                          0, 0.2, -0.1, np)

        self.world.attachRigidBody(node)
        
        
        #creamer
        shape = BulletBoxShape(Vec3(0.5, 0.3, 0.5)) 
        node = BulletRigidBodyNode('Box') 
        node.setMass(2)
        node.addShape(shape)
        np = render.attachNewNode(node)
        np.setPos(8, 3.2, 1.1 - 0.2)         
        
        self.creamer = Object(self, "creamer/creamer", 
                              1, 1, 1, 
                              -90, 0, 0, 
                              0.1, 0, -0.5, np)

        self.world.attachRigidBody(node)


        #mint
        shape = BulletCylinderShape(0.25, 0.2, 2)
        node = BulletRigidBodyNode('Cylinder')
        node.setMass(1)
        node.addShape(shape)
        np = render.attachNewNode(node)
        np.setPos(1.8, 3.2, 1.2 - 0.65)         
        
        self.mint = Object(self, "Mint/Mint", 
                           3, 3, 3, 
                           0, 0, 0, 
                           0, 0, 0, np)
        
        self.world.attachRigidBody(node)
        
        
        #--------------------- TASK and FUNCTIONS
        Decoration(self)
        self.lightUp()
        HandleArrows(self, 8, 12, -8, -31)
        Shoot(self)
        HandleCharacter(self, 8, 12, -8, -31)
        taskMgr.add(self.update, 'update')
        
        
    def lightUp(self): # L'oggetto che invoca la funzione viene SEMPRE passato IMPLICITAMENTE!        
       # Metodo che serve per creare e settare una luce ambientale ed una direzionale
        # Directional light
        dlight = DirectionalLight('dlight')
        dlight.setColor(VBase4(0.5, 0.5, 0.5, 1))
        dlnp = render.attachNewNode(dlight)
        dlnp.setHpr(0, -60, 0)
        render.setLight(dlnp)
        # Ambient light
        alight = AmbientLight('alight')
        alight.setColor(VBase4(0.8, 0.8, 0.8, 1))
        alnp = render.attachNewNode(alight)
        render.setLight(alnp)
        
    def update(self, task): 
       # Metodo che serve per attivare ad ogni frame la fisica della libreria Bullet
        dt = globalClock.getDt()
        self.world.doPhysics(dt)
        return task.cont
        
        
app = MyApp()
app.run() #ciclo base 

