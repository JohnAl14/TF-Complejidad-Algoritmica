<br>
<br>
<br>

<p align="center">
  <img src="https://github.com/JohnAl14/TP-Complejidad-Algoritmica/blob/main/AlgComplexTF/archivos/upc.png" alt="UPC">
</p>

<br>

<p align="center"><strong>UNIVERSIDAD PERUANA DE CIENCIAS APLICADAS</strong></p>

<br>

<p align="center"><strong>TRABAJO PARCIAL</strong></p>

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

Por ello hemos concluido que la mejor estructura de datos para este problema son los grafos. De esta manera, enlazaremos todas las cuadras de la ciudad elegida (New York) mediante el uso de sus coordenadas como nodos y las calles como aristas dirigdas. 



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

Al proponer una estructura de datos tipo grafos, nuestra dataset es explícita. Por ello hemos recopilado más de 1000 coordenadas (latitud y longitud ) en las calles de Ney York:  

<p align="center";>
  <img src="https://github.com/JohnAl14/TP-Complejidad-Algoritmica/blob/main/AlgComplexTF/archivos/dataset.png" alt="Dataset">
  (archivo_coordenadas.csv)
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
- Como metodología nos reunimos cada fin de semana para investigar y programar al menos 6 horas entre el Sábado y Domingo. 

<br>
<br>
<br>
<br>
<br>

## 5. Bibliografía

<div style="text-align: justify;">

GraphEverywhere, E. (2019, octubre 20). Algoritmo de rutas más cortas - Algoritmos de grafos. GraphEverywhere; Graph Everywhere SL. https://www.grapheverywhere.com/algoritmo-de-rutas-mas-cortas/

López, B. S. (2019, junio 12). Algoritmo de la ruta más corta. Ingenieria Industrial Online. https://www.ingenieriaindustrialonline.com/investigacion-de-operaciones/algoritmo-de-la-ruta-mas-corta/

Öncan,T., Kuban A., Laporte, G. “A comparative analysis of several asymmetric traveling salesman problem formulations”. Computers and Operational Research. 36 Issue III. 2009. 637-65

Universidad Autónoma del Estado de Hidalgo. (s/f). Problema del agente viajero. Edu.Mx. Recuperado el 28 de septiembre de 2023, de https://www.uaeh.edu.mx/scige/boletin/tlahuelilpan/n3/e5.html


</div>

</div>

<br>
<br>
<br>
<br>
<br>

