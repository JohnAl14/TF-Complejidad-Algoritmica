import tkinter as tk

import csv
import folium
import random

from PIL import Image, ImageTk
from imprimirMapa import MapPrinter
from claseNodo import nodo
from claseGrafo import Graph



class MyApp:

    def __init__(self, root):
        self.root = root
        self.root.title("GUI John/Free 1.2")
        
        self.root.geometry("800x500+300+100")
       
        self.root.configure(bg='black')
        self.title_font = ('Helvetica', 24, 'bold')
        self.map_printer = MapPrinter()
        self.graph = Graph()

        self.create_widgets()
        self.map_printer.mapa= folium.Map(location=[40.77564193305398, -73.96262332073893], zoom_start=14)
        
                               
    def create_widgets(self):

        background_image = Image.open("C:\\Users\\USER\\Pictures\\Saved Pictures\\nw.jpg")
        background_photo = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(self.root, image=background_photo)
        background_label.image = background_photo
        background_label.place(relwidth=1, relheight=1)

        self.title_label = tk.Label(root, text="Rutas de New York", font=self.title_font, bg='white', fg='black', padx=20, pady=20)
        self.title_label.pack()

        load_button = tk.Button(self.root, text="Cargar Coordenadas", command=self.load_coordinates, bg='darkblue', fg='white', height=2, width=17)
        self.run_button2 = tk.Button(self.root, text="Mostrar Mapa", command=self.prueba, bg='darkred', fg='white', height= 2, width=11)
        self.run_button = tk.Button(self.root, text="Ejecutar Ruta", command=self.run, bg='darkgreen', fg='white', height= 2, width=11)


        load_button.pack(pady=10)
        self.run_button2.pack(pady=10)
        self.run_button.pack(pady=10)

        start_label = tk.Label(self.root, text="Ingrese coordenada de origen:", bg='black', fg='white')
        start_label.pack(pady=5)

        self.start_node_entry = tk.Entry(self.root, width=10)
        self.end_node_entry = tk.Entry(self.root, width=10)

        self.start_node_entry.pack(pady=5)

        end_label = tk.Label(self.root, text="Ingrese coordenada de destino:", bg='black', fg='white')
        end_label.pack(pady=5)

        self.end_node_entry.pack(pady=5)

        self.result_label = tk.Label(self.root, text="", bg='black', fg='white')
        self.result_label.pack(pady=10)

    def load_coordinates(self):
        file_path = 'archivos\\free.csv'

        if file_path:
            self.graph = Graph()

            with open(file_path, 'r') as handle:
                archivo_coordenadas = csv.reader(handle)

                for linea in archivo_coordenadas:
                    nom = linea[0].split(';')
                    nodo_actual = nodo(float(nom[0]), float(nom[1]), nom[2])
                    self.graph.add_node(nodo_actual)
                    custom_icon = folium.Icon(color='blue')
                    folium.Marker(location=[nodo_actual.x, nodo_actual.y],popup=nodo_actual.idea,icon=custom_icon).add_to(self.map_printer.mapa)
                    
            print("Coordenadas cargadas correctamente.")


    def run(self):
        if not self.graph.nodes:
            print("Error: Cargar coordenadas antes de ejecutar Ruta.")        
            return

        self.graph.cargar_conecciones(random.randint(1, 10))

        result=[]



       
        start_node = int(self.start_node_entry.get())
        end_node = int(self.end_node_entry.get())

    
        nodo_inicio = self.graph.nodes[start_node-1]
        nodo_fin = self.graph.nodes[end_node-1]
     
        result = self.graph.dijkstra( nodo_inicio, nodo_fin)

        line = ""
        for node in self.graph.nodes:
            print(f"Node {node.idea} Connections:", [neighbor.idea for neighbor in node.salientes])

        print(result)

        self.result_label.config(text=line)

        self.map_printer.print_map(self.graph, result)

    def prueba(self):

        if not self.graph.nodes:
            print("Error: Cargar coordenadas antes de ejecutar Ruta.")        
            return

        self.graph.cargar_conecciones(random.randint(1, 10))

        result=[]

        line = ""
        for node in self.graph.nodes:
            print(f"Node {node.idea} Connections:", [neighbor.idea for neighbor in node.salientes])

        print(result)

        self.result_label.config(text=line)

        self.map_printer.print_map(self.graph, result)

    
        
if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()


