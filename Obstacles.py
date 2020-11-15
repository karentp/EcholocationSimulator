class Obstacle():
    def __init__(self, x, y ,w, h, c1, c2, c3):
        self.x= x
        self.y = y
        self.w = w
        self.h = h
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        
    def draw(self):
        fill(self.c1,self.c2,self.c3)
        rect(self.x, self.y, self.w, self.h)
        
    
