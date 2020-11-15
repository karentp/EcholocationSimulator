from SoundRay import SoundRay

class Sonar():
    def __init__(self, sonar_size, angle_scope, position,scenario):
        self.sonar_size = sonar_size
        self.angle_scope = angle_scope
        self.position = position
        self.scenario = scenario

    def emitir(self,target_angle):
        sound = SoundRay(self.position,target_angle,self.scenario)
        pos_final=sound.move()
        return pos_final
    
    def draw(self):
        fill(220,100,300) #morado
        rect(self.position[0], self.position[1], self.sonar_size, self.sonar_size)
