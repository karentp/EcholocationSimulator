from math import sin, cos, radians
import random
from Sonar import Sonar
from Scenario import Scenario

scenario = Scenario()

def setup():
    size(500, 500)
    noStroke()
    background(0)
    colorMode(HSB)
    global scenario
    scenario.draw()

def draw():
    global scenario
    sonar = Sonar(30,80,[250,250], scenario.walls)
    sonar.draw()
    angles=[0]
    
    MonteCarlo_tries=30
    for i in range(MonteCarlo_tries/2):
        angle= random.uniform(-sonar.angle_scope,sonar.angle_scope)
        if angle not in angles:
            if(i%2 !=0):
                angles.append(angle)
            else:
                angles.append(angle)
        else:
            i-=1
            
    for angle in angles:
        print(angle)
        finalpos=sonar.emitir(angle)
        fill(250)
        rect(finalpos[0], finalpos[1], 1, 1)

    
