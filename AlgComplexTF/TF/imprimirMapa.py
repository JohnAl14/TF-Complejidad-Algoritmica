import webbrowser
import folium

class MapPrinter:
    def __init__(self):
        self.mapa = folium.Map(location=[40.725760164988955, -73.94288944812737], zoom_start=11)

    def print_map(self, graph, result):
        for node1 in graph.nodes:
            for linea in node1.salientes:
                folium.PolyLine(
                locations=[(node1.x, node1.y), (linea.x, linea.y)],
                color='green',
                weight=2.5,
                opacity=1
                ).add_to(self.mapa)
        
        for i in range(len(result) - 1):
            node1 = result[i]
            node2 = result[i + 1]

            folium.PolyLine(
                locations=[(node1.x, node1.y), (node2.x, node2.y)],
                color='red',
                weight=5,
                opacity=1
            ).add_to(self.mapa)
        
        self.mapa.save('nodos.html')
        webbrowser.open('nodos.html')