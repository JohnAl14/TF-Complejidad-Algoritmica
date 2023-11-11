import tkinter as tk
from tkinter import filedialog
import csv
import folium
from imprimirMapa import MapPrinter
from claseNodo import nodo
from claseGrafo import Graph
from astar import AStar
from directorios import ruta_completa, ruta_completa1

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI John/Free 1.2")
        
        self.root.geometry("600x180+300+100")
        # Establecer el fondo negro
        self.root.configure(bg='black')
        self.title_font = ('Helvetica', 24, 'bold')
        self.map_printer = MapPrinter()
        self.graph = Graph()

        self.create_widgets()

    def create_widgets(self):

        self.title_label = tk.Label(root, text="Rutas de New York", font=self.title_font, bg='black', fg='white', padx=20, pady=10)
        self.title_label.pack()

        load_button = tk.Button(self.root, text="Cargar Coordenadas", command=self.load_coordinates, bg='darkblue', fg='white', height=2, width=17)
        self.run_button = tk.Button(self.root, text="Ejecutar Ruta", command=self.run_astar, bg='darkgreen', fg='white', height= 2, width=11)
        
        # Centrar botones
        load_button.pack(pady=10)
        self.run_button.pack(pady=10)

        # Etiqueta para mostrar el resultado del algoritmo
        self.result_label = tk.Label(self.root, text="", bg='black', fg='white')
        self.result_label.pack(pady=10)

        # Lienzo para mostrar el mapa
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg='black')
        self.canvas.pack()

    def load_coordinates(self):
        file_path = filedialog.askopenfilename(title="Seleccionar archivo de coordenadas", filetypes=[("CSV files", "*.csv")])

        if file_path:
            self.graph = Graph()

            with open(file_path, 'r') as handle:
                archivo_coordenadas = csv.reader(handle)

                for linea in archivo_coordenadas:
                    nom = linea[0].split(';')
                    self.graph.add_node(nodo(float(nom[0]), float(nom[1]), nom[2]))

            print("Coordenadas cargadas correctamente.")

    def run_astar(self):
        if not self.graph.nodes:
            print("Error: Cargar coordenadas antes de ejecutar A*.")
            return

        self.graph.set_initial_weights()
        self.graph.nodes[0].agregar_salida(self.graph.nodes[1], [1, 1])
        self.graph.nodes[0].agregar_salida(self.graph.nodes[3], [1, 6])
        self.graph.nodes[1].agregar_salida(self.graph.nodes[2], [1, 1])
        self.graph.nodes[2].agregar_salida(self.graph.nodes[3], [1, 1])
        self.graph.nodes[4].agregar_salida(self.graph.nodes[5], [1, 1])
        self.graph.nodes[3].agregar_salida(self.graph.nodes[4], [1, 1])
        # Agregar más conexiones según tus necesidades

        result = AStar().find_path(self.graph.nodes[0], [], self.graph.nodes[3], [], 1)
        line = ""
    # Calcula el rectángulo que rodea todos los nodos del grafo
        min_x = min(node.x for node in self.graph.nodes)
        max_x = max(node.x for node in self.graph.nodes)
        min_y = min(node.y for node in self.graph.nodes)
        max_y = max(node.y for node in self.graph.nodes)

        # Calcula el centro del rectángulo
        center_x = (min_x + max_x) / 2
        center_y = (min_y + max_y) / 2

        shift_x = round(300 - center_x)  # 300 es la mitad del ancho del lienzo
        shift_y = round(200 - center_y)  # 200 es la mitad de la altura del lienzo

# Desplaza la vista del lienzo
        self.canvas.scan_dragto(shift_x, shift_y, gain=1)

        for nodo_actual in self.graph.nodes:
            for i, vecino in enumerate(nodo_actual.salientes):
                coordenadas = nodo_actual.pesos[i]
                x1, y1 = nodo_actual.x, nodo_actual.y
                x2, y2 = vecino.x, vecino.y
                self.canvas.create_line(x1, y1, x2, y2, fill="white")


        for dato in result:
            if line != "":
                line = "->" + line
            line = str(dato.idea) + line

        self.result_label.config(text=line)
        self.mapa = folium.Map(location=[37.0902, -95.7129], zoom_start=5)
        self.map_printer.print_map(self.graph, result)

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()


