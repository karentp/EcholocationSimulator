from math import sin, cos, radians

class Sound_ray():
    def __init__(self, origin, main_angle, orientation= 0, length=0):
        self.origin = origin
        self.length = length
        self.main_angle = main_angle
        self.final_pos = [self.origin[0], self.origin[1]]
        self.orientation = orientation
        
    def move(self):
        final_x = 0
        final_y = 0
        for r in range(0,200):
            y= r*sin(radians(self.main_angle))
            x= r*cos(radians(self.main_angle))
            
            if(x<500 and x>0 and y<500 and y>0):
                print("aqui")
                final_x = x
                final_y = y
                fill((color(random(30),random(50,255),random(200,255))), 150)
                noStroke()
                ellipse(final_x, final_y, 4*2, 4*2)
        
        #Si el frente está viendo hacia la derecha
        self.final_pos[0]=self.origin[0]+final_x
        self.final_pos[1]=self.origin[1]-final_y
        print(self.final_pos[0], self.final_pos[1])


class Sonar():
    def __init__(self, sonar_size, angle_scope, position):
        self.sonar_size = sonar_size
        self.angle_scope = angle_scope
        self.position = position
        
    def emitir(self):
        sound = Sound_ray(self.position,30)
        sound.move()


sonar = Sonar(30,0,[250,250])
sonar.emitir()
size(500, 500)
background(0)
noStroke()
rect(250, 250, 10, 10)
