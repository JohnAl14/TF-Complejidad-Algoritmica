import webbrowser
import folium

class MapPrinter:
    def __init__(self):
        self.mapa = folium.Map(location=[37.0902, -95.7129], zoom_start=5)

    def print_map(self, graph, result):
        for node1 in graph.nodes:
            for linea in node1.salientes:
                folium.PolyLine(
                    locations=[(node1.x, node1.y), (linea.x, linea.y)],
                    color='green',
                    weight=2.5,
                    opacity=1
                ).add_to(self.mapa)

                if node1 in result and linea in result and abs(result.index(node1) - result.index(linea)) == 1:
                    folium.PolyLine(
                        locations=[(node1.x, node1.y), (linea.x, linea.y)],
                        color='red',
                        weight=2.5,
                        opacity=1
                    ).add_to(self.mapa)
        
        self.mapa.save('nodos.html')
        webbrowser.open('nodos.html')