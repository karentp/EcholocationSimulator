class SoundRay():
    def __init__(self, origin, main_angle , scenario, orientation= "derecha", length=0):
        self.origin = origin
        self.length = length
        self.main_angle = main_angle
        self.final_pos = [self.origin[0], self.origin[1]]
        self.orientation = orientation
        self.scenario = scenario
        
    def define_board_points(self, final_x,final_y):
        if(self.orientation=="derecha"):
            if(self.main_angle>=0):
                self.final_pos[0]=self.origin[0]+final_x
                self.final_pos[1]=self.origin[1]-final_y
            else:
                self.final_pos[0]=self.origin[0]+final_x
                self.final_pos[1]=self.origin[1]+final_y
                
        elif(self.orientation=="arriba"):
            if(self.main_angle>=0):
                self.final_pos[1]=self.origin[0]-final_x
                print("final y", final_y)
                self.final_pos[0]=self.origin[1]-final_y
            else:
                self.final_pos[1]=self.origin[0]-final_x
                self.final_pos[0]=self.origin[1]+final_y
                
        elif(self.orientation=="izquierda"):
                if(self.main_angle>=0):
                    self.final_pos[0]=self.origin[0]-final_x
                    self.final_pos[1]=self.origin[1]-final_y
                else:
                    self.final_pos[0]=self.origin[0]-final_x
                    self.final_pos[1]=self.origin[1]+final_y
                    
        elif(self.orientation=="abajo"):
            if(self.main_angle>=0):
                self.final_pos[1]=self.origin[0]+final_x 
                self.final_pos[0]=self.origin[1]-final_y 
            else:
                self.final_pos[1]=self.origin[0]+final_x 
                self.final_pos[0]=self.origin[1]+final_y 
                
        return(self.final_pos)

    def check_collision(self,final_pos):
        x= final_pos[0]
        y= final_pos[1]
        for wall in self.scenario:
            if(x >= wall.x and x<= wall.x + wall.w and y>= wall.y and y <= wall.y+wall.h):
                return True
        return False
        
    def move(self):
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
                
            if(abs(x)<=self.origin[0] and abs(x)>=0 and abs(y)<=self.origin[1] and abs(y)>=0):
                final_pos= self.define_board_points(abs(x),abs(y))
                if self.check_collision(final_pos) is True:
                    break
            else:
                #Caso en el que el rayo llega a alguno de los bordes
                final_pos= self.define_board_points(abs(x),abs(y))
                break
            
        return final_pos
