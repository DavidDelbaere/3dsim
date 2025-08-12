
import instance
camera = instance.instance(0,0,0)
points = []
def initRender(filename):
        
        lines = open(filename)

        i = 0
        for line in lines:
            coordinates = line.split()
            if coordinates[0] == "v":
                x = coordinates[1]
                y = coordinates[2]
                z = coordinates[3]

                points.append(instance.instance(x,y,z))
                



def calculatePlane():
    angles = camera.getAngle()