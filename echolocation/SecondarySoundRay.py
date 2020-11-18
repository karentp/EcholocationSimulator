import math
import random

class SecondarySoundRay():
    def __init__(self, origin, main_angle , scenario, orientation, board_size, position, length=0):
        self.origin = origin
        self.length = length
        self.main_angle = main_angle
        self.final_pos = [self.origin[0], self.origin[1]]
        self.orientation = orientation
        self.scenario = scenario
        self.board_size = board_size
        self.position = position
        self.vectorunitario = random.randrange(1,2)
        self.secondaryweight = 1 + ((random.randrange(1,6))*0.01)
        self.factor = random.randrange(0,2)
        
    def define_board_points(self, final_x,final_y, orientation, origin):
        if(orientation=="derecha"):
            if(self.main_angle>=0):
                self.final_pos[0]=origin[0]+final_x
                self.final_pos[1]=origin[1]-final_y
            else:
                self.final_pos[0]=origin[0]+final_x
                self.final_pos[1]=origin[1]+final_y
                
        elif(orientation=="arriba"):
            if(self.main_angle>=0):
                self.final_pos[1]=origin[1]-final_x
                self.final_pos[0]=origin[0]-final_y
            else:
                self.final_pos[1]=origin[1]-final_x
                self.final_pos[0]=origin[0]+final_y
                
        elif(orientation=="izquierda"):
                if(self.main_angle>=0):
                    self.final_pos[0]=origin[0]-final_x
                    self.final_pos[1]=origin[1]-final_y
                else:
                    self.final_pos[0]=origin[0]-final_x
                    self.final_pos[1]=origin[1]+final_y
                    
        elif(orientation=="abajo"):
            if(self.main_angle>=0):
                self.final_pos[1]=self.origin[1]+final_x 
                self.final_pos[0]=self.origin[0]-final_y 
                print("x",self.final_pos[0], "y", self.final_pos[1])
            else:
                self.final_pos[1]=self.origin[1]+final_x 
                self.final_pos[0]=self.origin[0]+final_y 
                
        return(self.final_pos)

    def check_collision(self,final_pos):
        x= final_pos[0]
        y= final_pos[1]
        for wall in self.scenario:
            if(x >= wall.x and x<= wall.x + wall.w and y>= wall.y and y <= wall.y+wall.h):
                return True
        return False
    
    def flip_orientation(self, orientation):
        if (orientation =="derecha"):
            orientation = "izquierda"
        elif (orientation =="izquierda"):
            orientation = "derecha"
        elif (orientation =="arriba"):
            orientation = "abajo"
        if (orientation =="abajo"):
            orientation = "arriba"
        return orientation
    
    def generate(self, main_angle, orientation,distances, origin, i, colisiones_max):
        #condicion de paro
        if (i>= colisiones_max):
            return distances
        
        final_x = 0
        final_y = 0
        for r in range(1,710):
            if(self.main_angle ==0):
                y= origin[1]
                x= int(r*cos(radians(main_angle)))
                
            elif (main_angle == 90):
                x=0
                y= int(r*sin(radians(main_angle)))
            else:   
                y= round((r*sin(radians(main_angle))),0)
                x= round((r*cos(radians(main_angle))),0)
                
            if(abs(x)<=self.board_size[0] and abs(x)>=0 and abs(y)<=self.board_size[1] and abs(y)>=0):
                final_pos= self.define_board_points(abs(x),abs(y), orientation, origin)
                if self.check_collision(final_pos) is True:
                    i +=1 #aumento las colisones
                    distances.append(r) #agrego la distancia recorrida por un rayo
                    orientation = self.flip_orientation(orientation)
                    self.generate(main_angle, orientation, distances, final_pos, i, colisiones_max )
                    break
            else:
                #Caso en el que el rayo llega a alguno de los bordes
                final_pos= self.define_board_points(abs(x),abs(y), orientation, origin)
                break 
            
        return distances
    
    
    def calculate_incidence_angle(self, pos_colision, pos_origen, angulo_emision, orientacion, distancia):
        if(orientacion == "derecha" or orientacion == "izquierda"):
            adyacente = abs(pos_origen[1]-pos_colision[1])
        else:
            adyacente = abs(pos_origen[0]-pos_colision[0])
                
        incidence_angle= 90-((acos(adyacente/distancia))*(180/math.pi))
        return incidence_angle
    
    def cast_rays(self,target_angle, bounces):
        sound = SecondarySoundRay(self.position,target_angle,self.scenario, self.orientation,[500,500], self.position)
        pos_final=sound.generate(target_angle, self.orientation, [],self.position,0,bounces)
        return pos_final
    
    def secondaryRays(self, MonteCarlo_tries,angle_scope, angles=[]):
        for i in range(MonteCarlo_tries/2):
            angle = random.uniform(-angle_scope, angle_scope)
            distances=self.cast_rays(angle, 1)
            sound_ray = SecondarySoundRay(self.position,angle,self.scenario, self.orientation,[500,500], self.position)
            if(distances !=None):
                for i in range(len(distances)):
                    if(i == 0):
                        r = distances[0] * random.randrange(1,2)
                        colorPixel = 70
                    else:
                        r = sum(distances[0:i+1]) + self.vectorunitario
                        colorPixel = 15
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
                    
                    rect(final_pos[0]/self.secondaryweight, final_pos[1]/self.secondaryweight, 0.5*self.factor, 0.5*self.factor)
