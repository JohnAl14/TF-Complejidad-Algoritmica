from math import sqrt

class nodo:

    def __init__(self, x, y, idea):
        self.salientes = []
        self.pesos = []
        self.x = x
        self.y = y
        self.peso = 999999999
        self.idea = idea
    
    def distance(self, x, y):
        return sqrt(((x - self.x) * (x - self.x)) + ((y - self.y) * (y - self.y)))
    
    def reset(self):
        self.peso = 999999999
    
    def agregar_salida(self, objective, durations):
        self.salientes.append(objective)
        self.pesos.append(durations)