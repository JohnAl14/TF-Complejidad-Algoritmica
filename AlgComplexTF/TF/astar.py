class AStar:
    def __init__(self):
        pass
    
    def find_path(self, actual, ruta, objective, libres, hora):
        ruta = list()
        libres = list()

        if actual == objective: return [actual]

        ruta.append(actual)

        for punto in actual.salientes:
            dis = actual.pesos[actual.salientes.index(punto)][hora] + actual.peso
            if dis < punto.peso:
                punto.peso = dis
                if punto not in libres:
                    libres.append(punto)

        men = None

        for punto in libres:
            if men is None:
                if punto not in ruta:
                    men = punto
            else:
                if (punto.peso + punto.distance(objective.x, objective.y) < men.peso and
                        punto not in ruta):
                    men = punto

        if men is None: return list()

        auxi = self.find_path(men, ruta, objective, libres, hora)
    
        if len(auxi) == 0: return list()

        if men in actual.salientes:
            auxi.append(actual)

        return auxi
