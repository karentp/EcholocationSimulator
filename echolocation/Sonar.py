from SoundRay import SoundRay
from Scenario import Scenario
import random

class Sonar():
    def __init__(self, sonar_size, angle_scope, position, scenario, orientation):
        self.sonar_size = sonar_size
        self.angle_scope = angle_scope
        self.position = position
        self.scenario = scenario
        self.orientation = orientation

    def cast_rays(self,target_angle):
        #sound = SoundRay(self.position,target_angle,self.scenario, self.orientation,[500,500])
        sound = SoundRay(self.position,target_angle,self.scenario, self.orientation,[500,500])
        pos_final=sound.generate(target_angle, self.orientation, [],self.position,0,3)
        print("distancias",pos_final)
        #pos_final=sound.move(target_angle, self.orientation)
        return pos_final
    
    def draw(self):
        fill(220,100,300) #morado
        rect(self.position[0], self.position[1], self.sonar_size, self.sonar_size)
        
    def scan(self, MonteCarlo_tries, angles=[]):
        for i in range(MonteCarlo_tries):
            angle = random.uniform(-self.angle_scope, self.angle_scope)
            angles.append(angle)
            distances=self.cast_rays(angle)
            #sound_ray = SoundRay(self.position,angle,self.scenario, self.orientation,[500,500])
            sound_ray = SoundRay(self.position,angle,self.scenario, self.orientation,[500,500])
            print("HOLIS")
            if(distances !=None):
                print("HOLIS2222")
                for i in range(len(distances)):
                    if(i == 0):
                        r = distances[0]
                        colorPixel = 250
                    else:
                        r = sum(distances[0:i+1])+ random.randrange(7)/random.randrange(1,2)
                        colorPixel = 100
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
                    print("FINAL POS", final_pos)
                    fill(colorPixel)
                    rect(final_pos[0], final_pos[1], 1, 1)
            #if sound_ray.check_collision(finalpos):
                #calculardistancia()
            #    fill(250)
            #    rect(finalpos[0], finalpos[1], 1, 1)
            
        
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
                
        return orientation
