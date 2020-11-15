from Obstacles import Obstacle

class Scenario():
    def __init__(self):
        self.walls=[]
        self.walls.append(Obstacle(30,50,8,70,230,65,123))
        self.walls.append(Obstacle(0,100,80,34,230,65,123))
        self.walls.append(Obstacle(400,5,90,70,230,65,123))
        self.walls.append(Obstacle(150,200,20,30,230,65,123))
        
    def draw(self):
        self.draw_obstacles()
        
    def draw_obstacles(self):
        for wall in self.walls:
            wall.draw()       
    
