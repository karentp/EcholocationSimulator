from math import sin, cos, radians
import random
from Sonar import Sonar
from Scenario import Scenario
import time

w = h = 500
sonarX = sonarY = 250
walls = 7
scenario = Scenario(walls, w, h)
angle_for_rays = 80
montecarlo_tries = 15
orientation = "derecha"
sonar_size = 10

def settings():
    size(w, h)
    
def mousePressed():
    global scenario
    global sonarX
    global sonarY
    global sonar
    
    sonarX = mouseX
    sonarY = mouseY
    background(0)
    scenario.draw()
    sonar = Sonar(sonar_size,angle_for_rays,[sonarX,sonarY], scenario.walls, orientation)

def setup():
    noStroke()
    background(0)
    colorMode(HSB)
    global scenario
    scenario.draw()

def draw():
    global scenario
    global angle_for_rays
    global montecarlo_tries
    global orientation
    global sonar_size
    global w
    global h
    
    sonar = Sonar(sonar_size,angle_for_rays,[sonarX,sonarY], scenario.walls, orientation)
    sonar.draw()
    sonar.scan(montecarlo_tries)
    orientation = sonar.change_orientation(orientation, scenario)
    time.sleep(0)

    
