import math
class Punto(object):
    x=0
    y=0
    x2=''
    y2=''
    def distancia(self):
        return math.sqrt(self.x2**2+self.y2**2)
    def muestra_punto(self):
        print(self.x2,self.y2)