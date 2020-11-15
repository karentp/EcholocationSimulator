from Obstacles import Obstacle

class Scenario():
    def __init__(self, wall_qty, width, height):
        self.walls=[]
        for i in range(wall_qty):
            self.walls.append(Obstacle(random(30,width), random(30, height),random(30,width)/4, random(30, height)/4,random(20,255),random(20,255),random(20,255)))
        
    def draw(self):
        self.draw_obstacles()
        
    def draw_obstacles(self):
        for wall in self.walls:
            wall.draw()       
    
