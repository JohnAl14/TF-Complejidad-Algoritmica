from imprimirMapa import MapPrinter
from claseNodo import nodo
from claseGrafo import Graph; import csv
from astar import AStar
from directorios import ruta_completa, ruta_completa1

def main():
    mapita = MapPrinter()
    graph = Graph()
    with open(ruta_completa, 'r') as handle:
        archivo_coordenadas = csv.reader(handle)

        for linea in archivo_coordenadas:
            nom = linea[0].split(';')
            graph.add_node(nodo(float(nom[0]), float(nom[1]), nom[2]))

    with open('archivo_aristas.csv', 'r') as handle:
        archivo_aristas = csv.reader(handle)
        
        for linea in archivo_aristas:
            nom = linea[0].split(';')
            pesin = list(map(int, nom[2:]))
            graph.nodes[int(nom[0])].agregar_salida(graph.nodes[int(nom[1])], pesin)

    graph.set_initial_weights()
    graph.nodes[0].agregar_salida(graph.nodes[1], [1, 1])
    graph.nodes[0].agregar_salida(graph.nodes[3], [1, 6])
    graph.nodes[1].agregar_salida(graph.nodes[2], [1, 1])
    graph.nodes[2].agregar_salida(graph.nodes[3], [1, 1])
    graph.nodes[4].agregar_salida(graph.nodes[5], [1, 1])
    graph.nodes[3].agregar_salida(graph.nodes[4], [1, 1])
    result = AStar().find_path(graph.nodes[0], [], graph.nodes[3], [], 1)
    line = ""

    for dato in result:
        if line != "":
            line = "->" + line
        line = str(dato.idea) + line

    print(line)
    print(graph.nodes[3].peso)
    mapita.print_map(graph, result)

if __name__ == "__main__":
    main()


