import math

class SoundRay():
    def __init__(self, origin, main_angle , scenario, orientation, board_size, length=0):
        self.origin = origin
        self.length = length
        self.main_angle = main_angle
        self.final_pos = [self.origin[0], self.origin[1]]
        self.orientation = orientation
        self.scenario = scenario
        self.board_size = board_size
        
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
        
    """def move(self, main_angle, orientation):
        final_x = 0
        final_y = 0
        for r in range(1,710):
            if(self.main_angle ==0):
                y= self.origin[1]
                x= int(r*cos(radians(self.main_angle)))
                
            elif (self.main_angle == 90):
                x=0
                y= int(r*sin(radians(self.main_angle)))
            else:   
                y= round((r*sin(radians(self.main_angle))),0)
                x= round((r*cos(radians(self.main_angle))),0)
                
            if(abs(x)<=self.board_size[0] and abs(x)>=0 and abs(y)<=self.board_size[1] and abs(y)>=0):
                final_pos= self.define_board_points(abs(x),abs(y), self.orientation)
                if self.check_collision(final_pos) is True:
                    break
            else:
                #Caso en el que el rayo llega a alguno de los bordes
                final_pos= self.define_board_points(abs(x),abs(y), self.orientation)
                break 
            
        return final_pos"""
    
    def generate(self, main_angle, orientation,distances, origin, i, colisiones_max):
        print("orientacion",orientation)
        #condicion de paro
        if (i>= colisiones_max):
            print("COLISIONES MAXIMAS")
            print("distances en colision max", distances)
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
                    print("distances antes de llamar recursion", distances)
                    orientation = self.flip_orientation(orientation)
                    #rect(final_pos[0], final_pos[1], 1, 1)
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
        
