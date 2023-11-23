from math import sqrt

class nodo:

    def __init__(self, x, y, idea):
        self.salientes = []
        self.pesos = []
        self.x = x
        self.y = y
        self.peso = 999999999
        self.idea = idea
        self.previous = None
    
    def __hash__(self):
        return hash((self.x, self.y, self.idea))

    def distance(self, x, y):
        return sqrt(abs(((x - self.x) * (x - self.x)) + ((y - self.y) * (y - self.y))))
    
    
    def __lt__(self, other):
        return self.peso < other.peso

    def __eq__(self, other):
        return self.peso == other.peso  
      
    def reset(self):
        self.peso = 999999999
        self.previous = None
    
    def agregar_salida(self, objective, duration):
        self.salientes.append(objective)
        self.pesos.append(duration)

