from SoundRay import SoundRay
from SecondarySoundRay import SecondarySoundRay
from Scenario import Scenario
import random

class Sonar():
    def __init__(self, sonar_size, angle_scope, position, scenario, orientation):
        self.sonar_size = sonar_size
        self.angle_scope = angle_scope
        self.position = position
        self.scenario = scenario
        self.orientation = orientation
        self.vectorunitario = random.randrange(1,7) ** random.randrange(2,4)

    def cast_rays(self,target_angle, bounces):
        sound = SoundRay(self.position,target_angle,self.scenario, self.orientation,[500,500])
        pos_final=sound.generate(target_angle, self.orientation, [],self.position,0,bounces)
        return pos_final
    
    def draw(self):
        fill(220,100,300) #morado
        rect(self.position[0], self.position[1], self.sonar_size, self.sonar_size)
        
    def scan(self, MonteCarlo_tries, angles=[]):
        for i in range(MonteCarlo_tries):
            angle = random.uniform(-self.angle_scope, self.angle_scope)
            angles.append(angle)
            secondary = SecondarySoundRay(self.position,angle,self.scenario, self.orientation,[500,500], self.position)
            angles = []
            angle = random.uniform(-self.angle_scope, self.angle_scope)
            angles.append(angle)
            distances=self.cast_rays(angle, 3)
            secondary.secondaryRays(MonteCarlo_tries, self.angle_scope)
            sound_ray = SoundRay(self.position,angle,self.scenario, self.orientation,[500,500])
            if(distances !=None):
                for i in range(len(distances)):
                    if(i == 0):
                        r = distances[0]
                        colorPixel = 250
                    else:
                        r = sum(distances[0:i+1]) + self.vectorunitario
                        colorPixel = 70
                    if(angle ==0):
                        y= origin[1]
                        x= int(r*cos(radians(angle)))
                        
                    elif (angle == 90):
                        x=0
                        y= int(r*sin(radians(angle)))
                    else:   
                        y= round((r*sin(radians(angle))),0)
                        x= round((r*cos(radians(angle))),0)
                    final_pos= sound_ray.define_board_points(abs(x),abs(y), self.orientation, self.position)
                    fill(colorPixel)
                    rect(final_pos[0], final_pos[1], 1, 1)
            
        
    def change_orientation(self, orientation, scenario):
        if(keyPressed):
            if(key == 'w'):
                orientation = "arriba"
                background(0)
            if(key == 'a'):
                orientation = "izquierda"
                background(0)
            if(key == 's'):
                orientation = "abajo"
                background(0)
            if(key == 'd'):
                orientation = "derecha"
                background(0)
            if(key == 'r'):
                scenario.draw()
            if(key == 'f'):
                noLoop()
            if(key == 'p'):
                saveFrame()
            if(key == 'z'):
                background(0)
                
        return orientation
