<br>
<br>
<br>

<p align="center">
  <img src="https://github.com/JohnAl14/TP-Complejidad-Algoritmica/blob/main/AlgComplexTF/archivos/upc.png" alt="UPC">
</p>

<br>

<p align="center"><strong>UNIVERSIDAD PERUANA DE CIENCIAS APLICADAS</strong></p>

<br>

<p align="center"><strong>TRABAJO FINAL </strong></p>

<br>

<p align="center"><strong>Curso: Complejidad Algorítmica</strong></p>

<br>

<p align="center"><strong>Sección: WS6B</strong></p>

<br>

<p align="center"><strong>Docente: Canaval Sánchez, Luis Martín</strong></p>

<br>

<p align="center"><strong>Integrantes:</strong></p>

<br>

<p align="center"><strong>Atencio Castillo, John Alexis – U202218229</strong></p>

<br>

<p align="center"><strong> Frisancho Levano, Sebastian Mathias Salomon – U202224392</strong></p>

<br>
<br>

<div style="text-align: center;">
<br>
<br>
<br>

## 1. Descripción del problema

### 1.1. Descripción

<div style="text-align: justify;">

El problema al que nos enfrentamos en este proyecto fue la optimización de rutas, un desafío fundamental en la gestión del transporte y la logística. El problema específico que estamos resolviendo se basa en una plataforma llamada Travel Salesman Problem (TSP), es considerado como un conjunto de grafos cuyas aristas son los posibles caminos que puede seguir una entidad para visitar todos los nodos (Öncan et al., 2009)

El objetivo principal de un proyecto de optimización de rutas con un modelo basado en  TSP es encontrar la ruta más corta y eficiente para que un agente de viajes visite un conjunto de ciudades o puntos de interés.  TSP es un problema clásico de optimización combinatoria que se ha  estudiado desde los inicios de la inteligencia artificial, y su aplicación puede ser en cualquier campo de investigación que tenga problemas de reflexión situacional que incluyan muchos destinos diferentes  con costos asociados a cada viaje.

<p align="center">
  <img src="https://github.com/JohnAl14/TP-Complejidad-Algoritmica/blob/main/AlgComplexTF/archivos/tsp-problema-del-agente-viajero.jpeg" alt="agente-viajero">
</p>

</div>

### 1.2. Fundamentación del problema

<div style="text-align: justify;">

Este problema es relevante para diversas aplicaciones prácticas, tales como:

  - **Logística y entrega**:
    Planifique rutas eficientes para camiones de reparto, mensajeros o vehículos de reparto para minimizar los costes y el tiempo de combustible  y maximizar el número de entregas realizadas.


  - **Sector servicios**:
    En negocios de servicios como reparación de equipos, inspecciones de seguridad, mantenimiento de infraestructuras, etc., es fundamental optimizar el recorrido del técnico para maximizar su productividad.


  - **Planificación de viaje**:
    En la industria de planificación de viajes y turismo, se utiliza para diseñar itinerarios que permitan a los turistas visitar múltiples lugares de interés en un tiempo limitado.


  - **Distribución de recursos**:
    En aplicaciones de distribución de recursos, como la recolección de residuos, la recolección de donaciones o la distribución de suministros, es importante optimizar las rutas para minimizar los recursos      utilizados.

</div>

#### 1.2.1. Teoría de grafos 


<div style="text-align: justify;">
  
En el ámbito de las matemáticas y la informática, se investiga la teoría de grafos (también conocida como teoría de gráficos), la cual se enfoca en analizar las características de las estructuras gráficas. Un grafo se define como un conjunto que no está vacío, compuesto por entidades denominadas vértices (también llamados nodos), junto con una colección de pares de vértices denominados aristas (edges en inglés), las cuales pueden o no tener una dirección específica. Comúnmente, se representa un grafo mediante una serie de puntos que representan los vértices, los cuales están interconectados por líneas que representan las aristas.

<p align="center">
  <img src="https://github.com/JohnAl14/TP-Complejidad-Algoritmica/blob/main/AlgComplexTF/archivos/400px-Connexe_et_pas_connexe.svg.png" alt="grafos-ejepmplo">
</p>

  - Clase grafo en nuestro código:
<p align="center">
  <img src="https://github.com/JohnAl14/TP-Complejidad-Algoritmica/blob/main/AlgComplexTF/archivos/clase-grafo.png" alt="grafos-cod">
</p>
<p align="center">
 (claseGrafo.py)
</p>

</div>

<br>
<br>
<br>
<br>
<br>

##### 1.2.1.1 Vértices y aristas 

<div style="text-align: justify;">

Los vértices son uno de los dos componentes esenciales en la composición de un grafo. En consonancia con las demás disciplinas matemáticas, la Teoría de Grafos no se enfoca en definir la naturaleza de los vértices en sí. En cambio, se centra en la capacidad de identificar situaciones diversas donde se puedan reconocer elementos y conexiones que cumplan con la definición de un grafo, permitiendo así la aplicación de la Teoría de Grafos en dichos contextos.
Mientras que las aristas son los segmentos que conectan los vértices (también llamados nodos) en la representación gráfica de una estructura. Las aristas son las relaciones o conexiones entre los elementos del grafo y representan cómo los vértices están vinculados entre sí. En un grafo, las aristas pueden tener diferentes propiedades, como ser dirigidas o dirigidas.  


- Clase nodo en nuestro código:
<p align="center">
  <img src="https://github.com/JohnAl14/TP-Complejidad-Algoritmica/blob/main/AlgComplexTF/archivos/clase-nodo.png" alt="nodos-cod">
</p>

<p align="center">
  (claseNodo.py)
</p>

Por ello hemos concluido que la mejor estructura de datos para este problema son los grafos. De esta manera, enlazaremos todas las cuadras de la ciudad elegida (New York) mediante el uso de sus coordenadas como nodos y las calles como aristas dirigidas. 



<p align="center">
  <img src="https://github.com/JohnAl14/TP-Complejidad-Algoritmica/blob/main/AlgComplexTF/archivos/image.png" alt="New-York">
</p>

</div>

<br>
<br>
<br>
<br>
<br>

## 2. Descripción y visualización del conjunto de datos

<div style="text-align: justify;">

Al proponer una estructura de datos tipo grafos, nuestra dataset es explícita. Por ello hemos recopilado más de 1000 coordenadas (latitud y longitud ) en las calles de New York:  

<p align="center";>
  <img src="https://github.com/JohnAl14/TP-Complejidad-Algoritmica/blob/main/AlgComplexTF/archivos/dataset.png" alt="Dataset">
  (archivo_coordenadas.csv)
</p>

Para la impresión del mapa de New york usamos las librerías folium  y Webbrowser en la clase Mapprinter. En esta clase, definimos dos tipos de líneas para conectar los nodos: verdes y rojas. Las primeras líneas representan las calles libres y las rojas donde hay interferencias.

<p align="center";>
  <img src="https://github.com/JohnAl14/TP-Complejidad-Algoritmica/blob/main/AlgComplexTF/archivos/algorito-impresion-mapa.png" alt="mapPrinter">
  (imprimirMapa.py)
</p>

- Ejemplo de un grafo en la ciudad:
<p align="center";>
  <img src="https://github.com/JohnAl14/TP-Complejidad-Algoritmica/blob/main/AlgComplexTF/archivos/grafo%20ejemplo.png" alt="ejemploOutput">
</p>

</div>

<br>
<br>
<br>
<br>
<br>

## 3. Propuesta

<div style="text-align: justify;">

- Proponemos un algoritmo sistemático que genere una estructura detallada de las calles de New York  a partir de la teoría de grafos dirigidos con el objetivo de solventar el problema planteado en la       
  descripción.
- Para la representación gráfica del mapa usaremos una api a la web de OpenStreetMap con el uso de la librería Folium.
- Para mejorar su eficiencia probaremos diferentes métodos de búsqueda de grafos y actualizaremos las calles conforme avance el proyecto. 
- Como metodología nos reunimos cada fin de semana para investigar y programar al menos 6 horas entre el Sábado y Domingo. 
</div>

<br>
<br>
<br>
<br>
<br>

## 4. Diseño de aplicación 

<div style="text-align: justify;">
La aplicación está dividida en 6 archivos principales ".py" conformados por:
  
- **claseGrafo.py**
- **astra.py**
- **claseNodo**
- **directorios.py**
- **imprimirMapa.py**
- **main.py**

En el archivo main cada una de estas clases se unen para crear el grafo, sus respectivos nodos, su mejor ruta y la impresión del mapa de New York desde un webbrowser. Además, el sistema está respaldado por un GUI sencillo creado desde la biblioteca Tkinter.

- Implementación de la librería Tkinter:
<p align="center";>
  <img src="https://github.com/JohnAl14/TP-Complejidad-Algoritmica/blob/main/AlgComplexTF/archivos/tkinter.png" alt="ejemploTkinter">
  (main.py)
</p>

Una vez ingresado al GUI visualizaremos 2 opciones "Cargar coordenadas" y "Ejecutar ruta".

- Ejemplo del GUI:
<p align="center";>
  <img src="https://github.com/JohnAl14/TP-Complejidad-Algoritmica/blob/main/AlgComplexTF/archivos/gui.png" alt="ejemploGUI"> 
</p>

En la primera opción buscaremos en nuestra máquina local el archivo ".csv" con todas las coordenadas de la ciudad y elegiremos los nodos para formar una ruta.

 - Ejemplo de Cargar coordenadas:
<p align="center";>
  <img src="https://github.com/JohnAl14/TP-Complejidad-Algoritmica/blob/main/AlgComplexTF/archivos/Cargar_Coordenadas.png"alt="ejemploCoordenadas"> 
</p>

Por último, tenemos la opción Ejecutar ruta en la cual visualizaremos la ruta que elegimos previamente en un mapa de Google maps.

- Ejemplo de ejecución de la ruta optima:
  
<p align="center";>
  <img src="https://github.com/JohnAl14/TP-Complejidad-Algoritmica/blob/main/AlgComplexTF/archivos/Ejemplo.png" alt="ejemploRuta"> 
</p>

</div>

## 5. Validación de resultados y pruebas
<div style="text-align: justify;">
- Ejemplo de imput de GUI completa:
  
Primero tenemos el Gui completado donde veremos 3 botones, el primero para cargar el data base, el segundo para observar los nodos a de interés y el ultimo para ejecutar la mejor ruta desde los nodos que deseamos dirigir.

<p align="center";>
  <img src="https://github.com/JohnAl14/TF-Complejidad-Algoritmica/blob/main/AlgComplexTF/archivos/newini.png"alt="NewGui"> 
</p>

- Ejemplo de output de mapa:
  
Aquí el usuario observará todos los puntos en los que podrá realizar una búsqueda de la ruta más corta en Central Park.
  
<p align="center";>
  <img src="https://github.com/JohnAl14/TF-Complejidad-Algoritmica/blob/main/AlgComplexTF/archivos/mapa%20con%20coordenadas.png"alt="MapaCompletado"> 
</p>

- Ejemplo de imput de nodos y output de ruta:

En el cuadro de dialogo el usuario podrá ingresar el nodo desde donde quiere partir y el nodo destino al que quiere llegar. Finalmente, recibirá un output de la ruta más optima graficada en el mapa en líneas rojas.
  
<p align="center";>
  <img src="https://github.com/JohnAl14/TF-Complejidad-Algoritmica/blob/main/AlgComplexTF/archivos/prueba1.png"alt="EjemploOutput"> 
</p>



</div>

<br>
<br>
<br>
<br>
<br>

## 6. Conclusiones 

- **Importancia de la Optimización de Rutas**: El proyecto aborda un problema crítico en la gestión del transporte y la logística: la optimización de rutas. Esta optimización tiene aplicaciones en una      variedad    de campos, desde la entrega de paquetes hasta la planificación de itinerarios turísticos y la distribución de recursos.
- **Amplio Espectro de Aplicaciones**: El problema de optimización de rutas es versátil y aplicable en una variedad de contextos, desde la logística hasta los servicios y la planificación de viajes. Esto demuestra la utilidad y la relevancia de abordar este tipo de desafíos.
- **Relevancia de la Teoría de Grafos**: La utilización de la teoría de grafos como marco conceptual es fundamental para modelar y abordar el problema del Viajante de Comercio (TSP). Esta teoría ofrece herramientas poderosas para representar relaciones y conexiones entre nodos, lo que resulta esencial en la optimización de rutas.
- **Importancia de los algoritmos de busqueda**: En este caso empezamos con un algoritmo de fuerza bruta sin embargo por la extensión del data set concluimos que un algoritmo dijskstra es mucho más eficiente en especial cuando se tratan de problemas de búsqueda de rutas. 

## 6. Bibliografía

<div style="text-align: justify;">

GraphEverywhere, E. (2019, octubre 20). Algoritmo de rutas más cortas - Algoritmos de grafos. GraphEverywhere; Graph Everywhere SL. https://www.grapheverywhere.com/algoritmo-de-rutas-mas-cortas/

López, B. S. (2019, junio 12). Algoritmo de la ruta más corta. Ingenieria Industrial Online. https://www.ingenieriaindustrialonline.com/investigacion-de-operaciones/algoritmo-de-la-ruta-mas-corta/

Öncan,T., Kuban A., Laporte, G. “A comparative analysis of several asymmetric traveling salesman problem formulations”. Computers and Operational Research. 36 Issue III. 2009. 637-65

Universidad Autónoma del Estado de Hidalgo. (s/f). Problema del agente viajero. Edu.Mx. Recuperado el 28 de septiembre de 2023, de https://www.uaeh.edu.mx/scige/boletin/tlahuelilpan/n3/e5.html


</div>


<br>
<br>
<br>
<br>
<br>

