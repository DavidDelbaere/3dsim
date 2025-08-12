class instance:
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
    
    def __init__(self,x):
        self.x = x
        self.y = 0
        self.z = 0

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.z = 0

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.angleX = 0
        self.angleY = 0
        self.angleZ = 0
        
    def setPOS(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    def setX(self, x):
        self.x = x

    def setY(self,y):
        self.y = y

    def setZ(self, z):
        self.z = z

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def getZ(self):
        return self.z
    
    def setAngle(self, x,y,z):
        self.angleX = x
        self.angleY = y
        self.angleZ = z
    def getAngle(self, x,y,z):
        return (self.angleX ,self.angleY, self.angleZ)
    
    def getPOS(self):
        return [self.x,self.y,self.z]