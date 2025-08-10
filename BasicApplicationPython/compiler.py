import main

def compile(filename):
        
        lines = open(filename)
        for line in lines:
            coordinates = line.split()
            if coordinates[0] == "v":
                x = coordinates[1]
                y = coordinates[2]
                z = coordinates[3]
                
                print("x: "  + x+" y: " + y + " z: " + z)
                
def drawPoint(x,y):
     return 0