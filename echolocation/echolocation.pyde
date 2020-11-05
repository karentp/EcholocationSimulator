from math import sin, cos, radians
from random import randrange

class Sound_ray():
    def __init__(self, origin, main_angle , scenario, orientation= "derecha", length=0):
        self.origin = origin
        self.length = length
        self.main_angle = main_angle
        self.final_pos = [self.origin[0], self.origin[1]]
        self.orientation = orientation
        self.scenario = scenario
        
    def define_board_points(self, final_x,final_y):
        
        if(self.orientation=="derecha"):
        #Si el frente está viendo hacia la derecha
        #Si el angulo es positivo
            if(self.main_angle>=0):
                self.final_pos[0]=250+final_x
                self.final_pos[1]=250-final_y
            #Si el angulo es negativo
            else:
                #print("angulo negativo")
                self.final_pos[0]=250+final_x
                self.final_pos[1]=250+final_y
        
        elif(self.orientation=="arriba"):
            #Si el frente está viendo hacia arriba
            #Si el angulo es positivo
            if(self.main_angle>=0):
                self.final_pos[1]=250-final_x
                print("final y", final_y)
                self.final_pos[0]=250-final_y
            #Si el angulo es negativo
            else:
                #print("angulo negativo")
                self.final_pos[1]=250-final_x
                self.final_pos[0]=250+final_y
        
        elif(self.orientation=="izquierda"):
            #Si el frente está viendo hacia la izquierda
            #Si el angulo es positivo
                if(self.main_angle>=0):
                    self.final_pos[0]=250-final_x
                    self.final_pos[1]=250-final_y
                #Si el angulo es negativo
                else:
                    #print("angulo negativo")
                    self.final_pos[0]=250-final_x
                    self.final_pos[1]=250+final_y

        elif(self.orientation=="abajo"):
            #Si el frente está viendo hacia abajo
            #Si el angulo es positivo
            if(self.main_angle>=0):
                self.final_pos[1]=250+final_x #Este es Y
                self.final_pos[0]=250-final_y #Este es X
            #Si el angulo es negativo
            else:
                #print("angulo negativo")
                self.final_pos[1]=250+final_x #Este es Y
                self.final_pos[0]=250+final_y #Este es X
        
    
        #print(self.final_pos[0], self.final_pos[1])
        return(self.final_pos)
                
    def check_collision(self,final_pos):
        pass
    
        """x= final_pos[0]
        y= final_pos[1]
        
        for obj in scenario:
            if((x >=obj[0]+(obj[2]/2) and x<= obj[0]+(obj[2]/2)) and (y>= obj[1] and y<= obj[1]+(obj[3]))):

                print("COLISIIIOOOOOOOOOOOOOOOON en: ", x, y, "con ", obj, " con angulo ", self.main_angle )
                print("x", x, "y ",y)
                print(obj[0]-(obj[2]/2), obj[0]+(obj[2]/2),obj[1]-(obj[3]/2), obj[1]+(obj[3]/2))
                return True
        return False"""
        
        
        
        """if ()
         if (mouseX + mouseRectWidth > centerRectX && mouseX < centerRectX + centerRectWidth && mouseY + mouseRectHeight > centerRectY && mouseY < centerRectY + centerRectHeight) {
    fill(255, 0, 0);
  } """
        
    def move(self):
        final_x = 0
        final_y = 0
        for r in range(1,710):
            #print("r",r)
            if(self.main_angle ==0):
                y= self.origin[1]
                x= int(r*cos(radians(self.main_angle)))
                #print("cuando angulo es 0: x",x,"y",y)
            elif (self.main_angle == 90):
                x=0
                y= int(r*sin(radians(self.main_angle)))
                #print("cuando angulo es 90: x",x,"y",y)
            else:   
                y= round((r*sin(radians(self.main_angle))),0)
                x= round((r*cos(radians(self.main_angle))),0)
                #print("cuando angulo es otro: x",x,"y",y)
                #print("seno", sin(radians(self.main_angle)))
   
            
            #Si el x y el y siguen dentro de los bordes del board son una posición valida
            if(abs(x)<=250 and abs(x)>=0 and abs(y)<=250 and abs(y)>=0):
                #print("Sigue en el tablero")
                final_pos= self.define_board_points(abs(x),abs(y))
                if self.check_collision(final_pos) is True:
                    print("hubo colision")
                    break
                #print("real final y",final_y)
            else:
                #Caso en el que el rayo llega a alguno de los bordes
                #print("X tab",x,"Ytab",y)
                print("Fuera de tablero")
                final_pos= self.define_board_points(abs(x),abs(y))
                break
            
        return final_pos
        

class Sonar():
    def __init__(self, sonar_size, angle_scope, position,scenario):
        self.sonar_size = sonar_size
        self.angle_scope = angle_scope
        self.position = position
        self.scenario = scenario

        
    def emitir(self,target_angle):
        sound = Sound_ray(self.position,target_angle,self.scenario)
        pos_final=sound.move()
        return pos_final

#Creamos el sonar
scenario=[[400,250,20,70],[300,50,20,90],[350,450,90,100]]
sonar = Sonar(30,0,[250,250], scenario)
angle_scope=80
angles=[0]
MonteCarlo_tries=50
for i in range(MonteCarlo_tries/2):
    angle= randrange(angle_scope)
    if angle not in angles:
        if(i%2 !=0):
            angles.append(angle*-1)
        else:
            angles.append(angle)
    else:
        i-=1


    
"""Bx_pos=305  
By_pos=255  
Bspeed_x = 1  
Bspeed_y = 0  
Brect_w = 5  
Brect_h = 5  
radius = 5  
x=400  
y=250  
w=10  
h=70"""

size(500, 500)
fill(220,100,300) #morado
rect(250, 250, 40, 40)

fill(220,0,300) 
rect(400, 250, 10, 70)

fill(0,0,0)
rect(300, 50, 20, 90)

fill(220,100,0)
rect(350, 450, 90, 100)
            
for angle in angles:
    print(angle)
    finalpos=sonar.emitir(angle)
    #background(0)
    #noStroke()
    fill(250)
    rect(finalpos[0]-40, finalpos[1]-40, 10, 10)


"""if ((Bx_pos >= width-Brect_w)  and not(By_pos >= width-Brect_h)) :
        Bspeed_x = Bspeed_x * -1   
    #in down right area, going into down left
    if (not(Bx_pos >= width-Brect_w)  and (By_pos >= width-Brect_h))  :
        Bspeed_y = Bspeed_y * -1   
    #in down left, going into up left
    if ((Bx_pos <= 0)  and not(By_pos >= width-Brect_h))  :
        Bspeed_x = Bspeed_x * -1   
    #in up left, going into up right
    if (not(Bx_pos >= width-Brect_w)  and (By_pos <= 0))  :
        Bspeed_y = Bspeed_y * -1   
  
    Bx_pos = Bx_pos + Bspeed_x
    By_pos = By_pos + Bspeed_y
    fill (0,0,0,100)
    ellipse(Bx_pos,By_pos,Brect_w,Brect_h)
    
    
    
    colorMode(RGB)
    fill(255,230,255,10)
    rect(0,0,width,height)"""
#rect(finalpos[0]-40, finalpos[1]-40, 10, 10)
    
