import heapq  
import random
class Graph:
    def __init__(self):
        self.nodes = []
        

    def add_node(self, node):
        self.nodes.append(node)

    def set_initial_weights(self):
        self.nodes[0].peso = 0

    def construir_camino(self,nodo):
        camino = []
        while nodo is not None:
            camino.append(nodo)
            nodo = nodo.previous
        camino.reverse()
        return camino
    
    def dijkstra(self, inicio, fin):
        inicio.peso = 0
        heap = [(0, inicio)]
        while heap:
            (peso, nodo) = heapq.heappop(heap)
            if nodo == fin:
                return self.construir_camino(fin)
            for i in range(len(nodo.salientes)):
                vecino = nodo.salientes[i]
                nuevo_peso = nodo.pesos[i] + peso
                if nuevo_peso < vecino.peso:
                    vecino.peso = nuevo_peso
                    vecino.previous = nodo
                    heapq.heappush(heap, (vecino.peso, vecino))
        return None

    def RandDijkstra(self, inicio, fin):
        inicio.peso = 0
        heap = [(0, inicio)]
        while heap:
            (peso, nodo) = heap.pop()
            if nodo == fin:
                return self.construir_camino(fin)
            for i in range(len(nodo.salientes)):
                vecino = nodo.salientes[i]
                nuevo_peso = nodo.pesos[i] + peso
                if nuevo_peso < vecino.peso:
                    vecino.peso = nuevo_peso
                    vecino.previous = nodo
                    heap.append((vecino.peso, vecino))
                    random.shuffle(heap)
        return None


    def cargar_conecciones(self): 
        
    
        for i in range(1013):
            if i!=168:
                self.nodes[i].agregar_salida(self.nodes[i+1],random.randint(1,10))

        for i in range(1000, 0, -1):
            if i!=169:
                self.nodes[i].agregar_salida(self.nodes[i-1],random.randint(1,10))


        self.nodes[0].agregar_salida(self.nodes[486], random.randint(1,10))
        self.nodes[0].agregar_salida(self.nodes[487], random.randint(1,10))

        self.nodes[486].agregar_salida(self.nodes[0], random.randint(1,10))
        self.nodes[487].agregar_salida(self.nodes[0], random.randint(1,10))

        self.nodes[1].agregar_salida(self.nodes[169], random.randint(1,10))
        self.nodes[1].agregar_salida(self.nodes[488], random.randint(1,10))

        self.nodes[2].agregar_salida(self.nodes[170], random.randint(1,10))
        self.nodes[2].agregar_salida(self.nodes[489], random.randint(1,10))

        self.nodes[3].agregar_salida(self.nodes[171], random.randint(1,10))
        self.nodes[31].agregar_salida(self.nodes[585], random.randint(1,10))

        self.nodes[4].agregar_salida(self.nodes[172], random.randint(1,10))
        self.nodes[4].agregar_salida(self.nodes[491], random.randint(1,10))

        self.nodes[5].agregar_salida(self.nodes[173], random.randint(1,10))

        self.nodes[6].agregar_salida(self.nodes[174], random.randint(1,10))
        self.nodes[6].agregar_salida(self.nodes[493], random.randint(1,10))

        self.nodes[7].agregar_salida(self.nodes[175], random.randint(1,10))
        
        self.nodes[8].agregar_salida(self.nodes[177], random.randint(1,10))
        self.nodes[8].agregar_salida(self.nodes[495], random.randint(1,10))

        self.nodes[9].agregar_salida(self.nodes[178], random.randint(1,10))
        
        self.nodes[10].agregar_salida(self.nodes[498], random.randint(1,10))

        self.nodes[11].agregar_salida(self.nodes[179], random.randint(1,10))
        self.nodes[11].agregar_salida(self.nodes[499], random.randint(1,10))

        self.nodes[12].agregar_salida(self.nodes[180], random.randint(1,10))
        self.nodes[12].agregar_salida(self.nodes[500], random.randint(1,10))

        self.nodes[13].agregar_salida(self.nodes[181], random.randint(1,10))
        self.nodes[13].agregar_salida(self.nodes[501], random.randint(1,10))

        self.nodes[14].agregar_salida(self.nodes[182], random.randint(1,10))
        self.nodes[14].agregar_salida(self.nodes[502], random.randint(1,10))

        self.nodes[15].agregar_salida(self.nodes[183], random.randint(1,10))
        self.nodes[15].agregar_salida(self.nodes[503], random.randint(1,10))

        self.nodes[16].agregar_salida(self.nodes[504], random.randint(1,10))

        self.nodes[17].agregar_salida(self.nodes[184], random.randint(1,10))
        self.nodes[17].agregar_salida(self.nodes[506], random.randint(1,10))

        self.nodes[18].agregar_salida(self.nodes[185], random.randint(1,10))
        self.nodes[18].agregar_salida(self.nodes[507], random.randint(1,10))

        self.nodes[19].agregar_salida(self.nodes[186], random.randint(1,10))
        self.nodes[19].agregar_salida(self.nodes[508], random.randint(1,10))

        self.nodes[20].agregar_salida(self.nodes[187], random.randint(1,10))
        self.nodes[20].agregar_salida(self.nodes[509], random.randint(1,10))

        self.nodes[21].agregar_salida(self.nodes[188], random.randint(1,10))
        self.nodes[21].agregar_salida(self.nodes[510], random.randint(1,10))

        self.nodes[22].agregar_salida(self.nodes[189], random.randint(1,10))
        self.nodes[22].agregar_salida(self.nodes[511], random.randint(1,10))

        self.nodes[23].agregar_salida(self.nodes[191], random.randint(1,10))
        self.nodes[23].agregar_salida(self.nodes[512], random.randint(1,10))

        self.nodes[24].agregar_salida(self.nodes[192], random.randint(1,10))
        self.nodes[24].agregar_salida(self.nodes[513], random.randint(1,10))

        self.nodes[25].agregar_salida(self.nodes[193], random.randint(1,10))
        self.nodes[25].agregar_salida(self.nodes[514], random.randint(1,10))

        self.nodes[26].agregar_salida(self.nodes[194], random.randint(1,10))
        self.nodes[26].agregar_salida(self.nodes[515], random.randint(1,10))

        self.nodes[27].agregar_salida(self.nodes[195], random.randint(1,10))
        self.nodes[27].agregar_salida(self.nodes[516], random.randint(1,10))

        self.nodes[28].agregar_salida(self.nodes[197], random.randint(1,10))
        self.nodes[28].agregar_salida(self.nodes[517], random.randint(1,10))

        self.nodes[29].agregar_salida(self.nodes[198], random.randint(1,10))
        self.nodes[29].agregar_salida(self.nodes[518], random.randint(1,10))

        self.nodes[30].agregar_salida(self.nodes[199], random.randint(1,10))
        self.nodes[30].agregar_salida(self.nodes[519], random.randint(1,10))

        self.nodes[31].agregar_salida(self.nodes[200], random.randint(1,10))
        

        self.nodes[32].agregar_salida(self.nodes[201], random.randint(1,10))
        self.nodes[32].agregar_salida(self.nodes[520], random.randint(1,10))
        
        self.nodes[33].agregar_salida(self.nodes[202], random.randint(1,10))
        self.nodes[33].agregar_salida(self.nodes[521], random.randint(1,10))

        self.nodes[34].agregar_salida(self.nodes[203], random.randint(1,10))
        self.nodes[34].agregar_salida(self.nodes[522], random.randint(1,10))

        self.nodes[35].agregar_salida(self.nodes[204], random.randint(1,10))
        self.nodes[35].agregar_salida(self.nodes[523], random.randint(1,10))

        self.nodes[36].agregar_salida(self.nodes[205], random.randint(1,10))
        self.nodes[36].agregar_salida(self.nodes[524], random.randint(1,10))

        self.nodes[37].agregar_salida(self.nodes[206], random.randint(1,10))
        self.nodes[37].agregar_salida(self.nodes[525], random.randint(1,10))

        self.nodes[38].agregar_salida(self.nodes[207], random.randint(1,10))
        self.nodes[38].agregar_salida(self.nodes[526], random.randint(1,10))

        self.nodes[39].agregar_salida(self.nodes[208], random.randint(1,10))
        self.nodes[39].agregar_salida(self.nodes[527], random.randint(1,10))

        self.nodes[40].agregar_salida(self.nodes[209], random.randint(1,10))
        self.nodes[40].agregar_salida(self.nodes[528], random.randint(1,10))

        self.nodes[41].agregar_salida(self.nodes[210], random.randint(1,10))
        self.nodes[41].agregar_salida(self.nodes[529], random.randint(1,10))

        self.nodes[42].agregar_salida(self.nodes[211], random.randint(1,10))
        self.nodes[42].agregar_salida(self.nodes[530], random.randint(1,10))

        self.nodes[43].agregar_salida(self.nodes[212], random.randint(1,10))
        self.nodes[43].agregar_salida(self.nodes[531], random.randint(1,10))

        self.nodes[44].agregar_salida(self.nodes[213], random.randint(1,10))
        self.nodes[44].agregar_salida(self.nodes[532], random.randint(1,10))

        self.nodes[45].agregar_salida(self.nodes[214], random.randint(1,10))
        self.nodes[45].agregar_salida(self.nodes[533], random.randint(1,10))

        self.nodes[46].agregar_salida(self.nodes[215], random.randint(1,10))
        self.nodes[46].agregar_salida(self.nodes[534], random.randint(1,10))

        self.nodes[47].agregar_salida(self.nodes[216], random.randint(1,10))
        self.nodes[47].agregar_salida(self.nodes[535], random.randint(1,10))

        self.nodes[48].agregar_salida(self.nodes[218], random.randint(1,10))
        self.nodes[48].agregar_salida(self.nodes[538], random.randint(1,10))

        self.nodes[217].agregar_salida(self.nodes[536], random.randint(1,10))

        self.nodes[49].agregar_salida(self.nodes[219], random.randint(1,10))
        self.nodes[49].agregar_salida(self.nodes[539], random.randint(1,10))

        self.nodes[50].agregar_salida(self.nodes[220], random.randint(1,10))
        self.nodes[50].agregar_salida(self.nodes[540], random.randint(1,10))

        self.nodes[51].agregar_salida(self.nodes[221], random.randint(1,10))
        self.nodes[51].agregar_salida(self.nodes[541], random.randint(1,10))

        self.nodes[52].agregar_salida(self.nodes[222], random.randint(1,10))
        self.nodes[52].agregar_salida(self.nodes[542], random.randint(1,10))

        self.nodes[53].agregar_salida(self.nodes[223], random.randint(1,10))
        self.nodes[53].agregar_salida(self.nodes[543], random.randint(1,10))

        self.nodes[54].agregar_salida(self.nodes[224], random.randint(1,10))
        self.nodes[54].agregar_salida(self.nodes[544], random.randint(1,10))

        self.nodes[55].agregar_salida(self.nodes[225], random.randint(1,10))
        self.nodes[55].agregar_salida(self.nodes[545], random.randint(1,10))

        self.nodes[56].agregar_salida(self.nodes[226], random.randint(1,10))
        self.nodes[56].agregar_salida(self.nodes[546], random.randint(1,10))

        self.nodes[57].agregar_salida(self.nodes[227], random.randint(1,10))
        self.nodes[57].agregar_salida(self.nodes[547], random.randint(1,10))

        self.nodes[58].agregar_salida(self.nodes[228], random.randint(1,10))
        self.nodes[58].agregar_salida(self.nodes[548], random.randint(1,10))

        self.nodes[59].agregar_salida(self.nodes[229], random.randint(1,10))
        self.nodes[59].agregar_salida(self.nodes[549], random.randint(1,10))

        self.nodes[61].agregar_salida(self.nodes[230], random.randint(1,10))
        self.nodes[61].agregar_salida(self.nodes[550], random.randint(1,10))

        self.nodes[62].agregar_salida(self.nodes[231], random.randint(1,10))
        self.nodes[62].agregar_salida(self.nodes[551], random.randint(1,10))

        self.nodes[63].agregar_salida(self.nodes[232], random.randint(1,10))
        self.nodes[63].agregar_salida(self.nodes[857], random.randint(1,10))

        self.nodes[857].agregar_salida(self.nodes[858], random.randint(1,10))

        self.nodes[64].agregar_salida(self.nodes[233], random.randint(1,10))
        self.nodes[64].agregar_salida(self.nodes[856], random.randint(1,10))

        self.nodes[65].agregar_salida(self.nodes[234], random.randint(1,10))
        self.nodes[65].agregar_salida(self.nodes[855], random.randint(1,10))

        self.nodes[235].agregar_salida(self.nodes[854], random.randint(1,10))

        self.nodes[66].agregar_salida(self.nodes[236], random.randint(1,10))
        self.nodes[66].agregar_salida(self.nodes[853], random.randint(1,10))
        self.nodes[853].agregar_salida(self.nodes[852], random.randint(1,10))

        self.nodes[68].agregar_salida(self.nodes[238], random.randint(1,10))
        self.nodes[68].agregar_salida(self.nodes[851], random.randint(1,10))

        self.nodes[69].agregar_salida(self.nodes[239], random.randint(1,10))
        self.nodes[69].agregar_salida(self.nodes[850], random.randint(1,10))

        self.nodes[70].agregar_salida(self.nodes[240], random.randint(1,10))
        self.nodes[70].agregar_salida(self.nodes[849], random.randint(1,10))

        self.nodes[71].agregar_salida(self.nodes[241], random.randint(1,10))
        self.nodes[71].agregar_salida(self.nodes[848], random.randint(1,10))

        self.nodes[72].agregar_salida(self.nodes[242], random.randint(1,10))
        self.nodes[72].agregar_salida(self.nodes[847], random.randint(1,10))

        self.nodes[73].agregar_salida(self.nodes[243], random.randint(1,10))
        self.nodes[73].agregar_salida(self.nodes[846], random.randint(1,10))

        self.nodes[74].agregar_salida(self.nodes[244], random.randint(1,10))
        self.nodes[74].agregar_salida(self.nodes[845], random.randint(1,10))

        self.nodes[78].agregar_salida(self.nodes[245], random.randint(1,10))
        self.nodes[78].agregar_salida(self.nodes[844], random.randint(1,10))

        self.nodes[79].agregar_salida(self.nodes[247], random.randint(1,10))
        self.nodes[79].agregar_salida(self.nodes[843], random.randint(1,10))

        self.nodes[80].agregar_salida(self.nodes[248], random.randint(1,10))
        self.nodes[80].agregar_salida(self.nodes[842], random.randint(1,10))

        self.nodes[81].agregar_salida(self.nodes[250], random.randint(1,10))
        self.nodes[81].agregar_salida(self.nodes[841], random.randint(1,10))

        self.nodes[82].agregar_salida(self.nodes[251], random.randint(1,10))
        self.nodes[82].agregar_salida(self.nodes[840], random.randint(1,10))

        self.nodes[83].agregar_salida(self.nodes[839], random.randint(1,10))

        self.nodes[84].agregar_salida(self.nodes[253], random.randint(1,10))
        self.nodes[84].agregar_salida(self.nodes[838], random.randint(1,10))

        self.nodes[85].agregar_salida(self.nodes[254], random.randint(1,10))
        self.nodes[85].agregar_salida(self.nodes[837], random.randint(1,10))

        self.nodes[86].agregar_salida(self.nodes[255], random.randint(1,10))
        self.nodes[86].agregar_salida(self.nodes[836], random.randint(1,10))

        self.nodes[87].agregar_salida(self.nodes[835], random.randint(1,10))
        
        self.nodes[88].agregar_salida(self.nodes[834], random.randint(1,10))

        self.nodes[89].agregar_salida(self.nodes[833], random.randint(1,10))

        self.nodes[90].agregar_salida(self.nodes[257], random.randint(1,10))

        self.nodes[617].agregar_salida(self.nodes[487], random.randint(1,10))

        self.nodes[616].agregar_salida(self.nodes[488], random.randint(1,10))
        self.nodes[616].agregar_salida(self.nodes[619], random.randint(1,10))

        self.nodes[615].agregar_salida(self.nodes[489], random.randint(1,10))
        self.nodes[615].agregar_salida(self.nodes[620], random.randint(1,10))

        self.nodes[614].agregar_salida(self.nodes[621], random.randint(1,10))
        self.nodes[614].agregar_salida(self.nodes[490], random.randint(1,10))

        self.nodes[613].agregar_salida(self.nodes[622], random.randint(1,10))
        self.nodes[613].agregar_salida(self.nodes[491], random.randint(1,10))

        self.nodes[612].agregar_salida(self.nodes[624], random.randint(1,10))
        self.nodes[612].agregar_salida(self.nodes[492], random.randint(1,10))

        self.nodes[611].agregar_salida(self.nodes[625], random.randint(1,10))
        self.nodes[611].agregar_salida(self.nodes[493], random.randint(1,10))

        self.nodes[610].agregar_salida(self.nodes[626], random.randint(1,10))
        self.nodes[610].agregar_salida(self.nodes[494], random.randint(1,10))

        self.nodes[609].agregar_salida(self.nodes[627], random.randint(1,10))
        self.nodes[609].agregar_salida(self.nodes[495], random.randint(1,10))

        self.nodes[608].agregar_salida(self.nodes[628], random.randint(1,10))
        self.nodes[608].agregar_salida(self.nodes[496], random.randint(1,10))

        self.nodes[607].agregar_salida(self.nodes[629], random.randint(1,10))
        self.nodes[607].agregar_salida(self.nodes[497], random.randint(1,10))

        self.nodes[606].agregar_salida(self.nodes[630], random.randint(1,10))
        self.nodes[606].agregar_salida(self.nodes[498], random.randint(1,10))

        self.nodes[605].agregar_salida(self.nodes[632], random.randint(1,10))
        self.nodes[605].agregar_salida(self.nodes[499], random.randint(1,10))

        self.nodes[604].agregar_salida(self.nodes[633], random.randint(1,10))
        self.nodes[604].agregar_salida(self.nodes[500], random.randint(1,10))

        self.nodes[603].agregar_salida(self.nodes[634], random.randint(1,10))
        self.nodes[603].agregar_salida(self.nodes[501], random.randint(1,10))

        self.nodes[602].agregar_salida(self.nodes[635], random.randint(1,10))
        self.nodes[602].agregar_salida(self.nodes[502], random.randint(1,10))

        self.nodes[601].agregar_salida(self.nodes[636], random.randint(1,10))
        self.nodes[601].agregar_salida(self.nodes[503], random.randint(1,10))

        self.nodes[600].agregar_salida(self.nodes[637], random.randint(1,10))
        self.nodes[600].agregar_salida(self.nodes[504], random.randint(1,10))

        self.nodes[599].agregar_salida(self.nodes[638], random.randint(1,10))
        self.nodes[599].agregar_salida(self.nodes[506], random.randint(1,10))

        self.nodes[598].agregar_salida(self.nodes[639], random.randint(1,10))
        self.nodes[598].agregar_salida(self.nodes[507], random.randint(1,10))

        self.nodes[597].agregar_salida(self.nodes[641], random.randint(1,10))
        self.nodes[597].agregar_salida(self.nodes[508], random.randint(1,10))

        self.nodes[596].agregar_salida(self.nodes[642], random.randint(1,10))
        self.nodes[596].agregar_salida(self.nodes[509], random.randint(1,10))

        self.nodes[595].agregar_salida(self.nodes[643], random.randint(1,10))
        self.nodes[595].agregar_salida(self.nodes[510], random.randint(1,10))

        self.nodes[594].agregar_salida(self.nodes[644], random.randint(1,10))
        self.nodes[594].agregar_salida(self.nodes[511], random.randint(1,10))

        self.nodes[593].agregar_salida(self.nodes[645], random.randint(1,10))
        self.nodes[593].agregar_salida(self.nodes[512], random.randint(1,10))

        self.nodes[592].agregar_salida(self.nodes[646], random.randint(1,10))
        self.nodes[592].agregar_salida(self.nodes[513], random.randint(1,10))

        self.nodes[591].agregar_salida(self.nodes[647], random.randint(1,10))
        self.nodes[591].agregar_salida(self.nodes[514], random.randint(1,10))

        self.nodes[590].agregar_salida(self.nodes[648], random.randint(1,10))
        self.nodes[590].agregar_salida(self.nodes[515], random.randint(1,10))

        self.nodes[589].agregar_salida(self.nodes[649], random.randint(1,10))
        self.nodes[589].agregar_salida(self.nodes[516], random.randint(1,10))

        self.nodes[588].agregar_salida(self.nodes[650], random.randint(1,10))
        self.nodes[588].agregar_salida(self.nodes[517], random.randint(1,10))

        self.nodes[587].agregar_salida(self.nodes[651], random.randint(1,10))
        self.nodes[587].agregar_salida(self.nodes[518], random.randint(1,10))

        self.nodes[586].agregar_salida(self.nodes[653], random.randint(1,10))
        self.nodes[586].agregar_salida(self.nodes[519], random.randint(1,10))

        self.nodes[585].agregar_salida(self.nodes[654], random.randint(1,10))

        self.nodes[584].agregar_salida(self.nodes[655], random.randint(1,10))
        self.nodes[584].agregar_salida(self.nodes[520], random.randint(1,10))

        self.nodes[583].agregar_salida(self.nodes[656], random.randint(1,10))
        self.nodes[583].agregar_salida(self.nodes[521], random.randint(1,10))

        self.nodes[582].agregar_salida(self.nodes[657], random.randint(1,10))
        self.nodes[582].agregar_salida(self.nodes[522], random.randint(1,10))

        self.nodes[581].agregar_salida(self.nodes[658], random.randint(1,10))
        self.nodes[581].agregar_salida(self.nodes[523], random.randint(1,10))

        self.nodes[580].agregar_salida(self.nodes[659], random.randint(1,10))
        self.nodes[580].agregar_salida(self.nodes[524], random.randint(1,10))

        self.nodes[579].agregar_salida(self.nodes[660], random.randint(1,10))
        self.nodes[579].agregar_salida(self.nodes[525], random.randint(1,10))

        self.nodes[578].agregar_salida(self.nodes[661], random.randint(1,10))
        self.nodes[578].agregar_salida(self.nodes[526], random.randint(1,10))

        self.nodes[577].agregar_salida(self.nodes[662], random.randint(1,10))
        self.nodes[577].agregar_salida(self.nodes[527], random.randint(1,10))

        self.nodes[576].agregar_salida(self.nodes[663], random.randint(1,10))
        self.nodes[576].agregar_salida(self.nodes[528], random.randint(1,10))

        self.nodes[575].agregar_salida(self.nodes[664], random.randint(1,10))
        self.nodes[575].agregar_salida(self.nodes[529], random.randint(1,10))

        self.nodes[574].agregar_salida(self.nodes[665], random.randint(1,10))
        self.nodes[574].agregar_salida(self.nodes[530], random.randint(1,10))

        self.nodes[573].agregar_salida(self.nodes[666], random.randint(1,10))
        self.nodes[573].agregar_salida(self.nodes[531], random.randint(1,10))

        self.nodes[572].agregar_salida(self.nodes[667], random.randint(1,10))
        self.nodes[572].agregar_salida(self.nodes[532], random.randint(1,10))

        self.nodes[571].agregar_salida(self.nodes[668], random.randint(1,10))
        self.nodes[571].agregar_salida(self.nodes[533], random.randint(1,10))

        self.nodes[570].agregar_salida(self.nodes[669], random.randint(1,10))
        self.nodes[570].agregar_salida(self.nodes[534], random.randint(1,10))

        self.nodes[569].agregar_salida(self.nodes[670], random.randint(1,10))
        self.nodes[569].agregar_salida(self.nodes[535], random.randint(1,10))

        self.nodes[568].agregar_salida(self.nodes[671], random.randint(1,10))
        self.nodes[568].agregar_salida(self.nodes[536], random.randint(1,10))

        self.nodes[567].agregar_salida(self.nodes[672], random.randint(1,10))
        self.nodes[567].agregar_salida(self.nodes[538], random.randint(1,10))

        self.nodes[566].agregar_salida(self.nodes[673], random.randint(1,10))
        self.nodes[566].agregar_salida(self.nodes[539], random.randint(1,10))

        self.nodes[565].agregar_salida(self.nodes[674], random.randint(1,10))
        self.nodes[565].agregar_salida(self.nodes[540], random.randint(1,10))

        self.nodes[564].agregar_salida(self.nodes[675], random.randint(1,10))
        self.nodes[564].agregar_salida(self.nodes[541], random.randint(1,10))

        self.nodes[563].agregar_salida(self.nodes[676], random.randint(1,10))
        self.nodes[563].agregar_salida(self.nodes[542], random.randint(1,10))

        self.nodes[562].agregar_salida(self.nodes[677], random.randint(1,10))
        self.nodes[562].agregar_salida(self.nodes[543], random.randint(1,10))

        self.nodes[561].agregar_salida(self.nodes[678], random.randint(1,10))
        self.nodes[561].agregar_salida(self.nodes[544], random.randint(1,10))

        self.nodes[560].agregar_salida(self.nodes[679], random.randint(1,10))
        self.nodes[560].agregar_salida(self.nodes[545], random.randint(1,10))

        self.nodes[559].agregar_salida(self.nodes[680], random.randint(1,10))
        self.nodes[559].agregar_salida(self.nodes[546], random.randint(1,10))

        self.nodes[558].agregar_salida(self.nodes[681], random.randint(1,10))
        self.nodes[558].agregar_salida(self.nodes[547], random.randint(1,10))

        self.nodes[557].agregar_salida(self.nodes[682], random.randint(1,10))
        self.nodes[557].agregar_salida(self.nodes[548], random.randint(1,10))

        self.nodes[556].agregar_salida(self.nodes[683], random.randint(1,10))
        self.nodes[556].agregar_salida(self.nodes[549], random.randint(1,10))

        self.nodes[555].agregar_salida(self.nodes[684], random.randint(1,10))
        self.nodes[555].agregar_salida(self.nodes[550], random.randint(1,10))

        self.nodes[554].agregar_salida(self.nodes[685], random.randint(1,10))
        self.nodes[554].agregar_salida(self.nodes[551], random.randint(1,10))

        self.nodes[553].agregar_salida(self.nodes[686], random.randint(1,10))

        self.nodes[748].agregar_salida(self.nodes[618], random.randint(1,10))

        self.nodes[747].agregar_salida(self.nodes[619], random.randint(1,10))
        self.nodes[747].agregar_salida(self.nodes[750], random.randint(1,10))

        self.nodes[746].agregar_salida(self.nodes[751], random.randint(1,10))

        self.nodes[745].agregar_salida(self.nodes[623], random.randint(1,10))
        self.nodes[745].agregar_salida(self.nodes[753], random.randint(1,10))

        self.nodes[744].agregar_salida(self.nodes[754], random.randint(1,10))
        self.nodes[744].agregar_salida(self.nodes[624], random.randint(1,10))

        self.nodes[743].agregar_salida(self.nodes[755], random.randint(1,10))
        self.nodes[743].agregar_salida(self.nodes[625], random.randint(1,10))

        self.nodes[742].agregar_salida(self.nodes[756], random.randint(1,10))

        self.nodes[741].agregar_salida(self.nodes[757], random.randint(1,10))
        self.nodes[741].agregar_salida(self.nodes[627], random.randint(1,10))

        self.nodes[740].agregar_salida(self.nodes[758], random.randint(1,10))

        self.nodes[739].agregar_salida(self.nodes[759], random.randint(1,10))

        self.nodes[738].agregar_salida(self.nodes[760], random.randint(1,10))
        self.nodes[738].agregar_salida(self.nodes[630], random.randint(1,10))

        self.nodes[737].agregar_salida(self.nodes[761], random.randint(1,10))
        self.nodes[737].agregar_salida(self.nodes[633], random.randint(1,10))

        self.nodes[736].agregar_salida(self.nodes[762], random.randint(1,10))
        self.nodes[736].agregar_salida(self.nodes[634], random.randint(1,10))

        self.nodes[735].agregar_salida(self.nodes[764], random.randint(1,10))
        self.nodes[735].agregar_salida(self.nodes[636], random.randint(1,10))

        self.nodes[734].agregar_salida(self.nodes[765], random.randint(1,10))
        self.nodes[734].agregar_salida(self.nodes[637], random.randint(1,10))

        self.nodes[763].agregar_salida(self.nodes[635], random.randint(1,10))

        self.nodes[733].agregar_salida(self.nodes[766], random.randint(1,10))
        self.nodes[733].agregar_salida(self.nodes[638], random.randint(1,10))

        self.nodes[732].agregar_salida(self.nodes[767], random.randint(1,10))
        self.nodes[732].agregar_salida(self.nodes[639], random.randint(1,10))

        self.nodes[731].agregar_salida(self.nodes[768], random.randint(1,10))
        self.nodes[731].agregar_salida(self.nodes[641], random.randint(1,10))

        self.nodes[730].agregar_salida(self.nodes[769], random.randint(1,10))
        self.nodes[730].agregar_salida(self.nodes[642], random.randint(1,10))

        self.nodes[729].agregar_salida(self.nodes[770], random.randint(1,10))
        self.nodes[729].agregar_salida(self.nodes[643], random.randint(1,10))

        self.nodes[728].agregar_salida(self.nodes[771], random.randint(1,10))
        self.nodes[728].agregar_salida(self.nodes[644], random.randint(1,10))

        self.nodes[727].agregar_salida(self.nodes[772], random.randint(1,10))
        self.nodes[727].agregar_salida(self.nodes[645], random.randint(1,10))

        self.nodes[726].agregar_salida(self.nodes[773], random.randint(1,10))
        self.nodes[726].agregar_salida(self.nodes[646], random.randint(1,10))

        self.nodes[725].agregar_salida(self.nodes[774], random.randint(1,10))
        self.nodes[725].agregar_salida(self.nodes[647], random.randint(1,10))

        self.nodes[724].agregar_salida(self.nodes[775], random.randint(1,10))
        self.nodes[724].agregar_salida(self.nodes[648], random.randint(1,10))

        self.nodes[723].agregar_salida(self.nodes[776], random.randint(1,10))
        self.nodes[723].agregar_salida(self.nodes[649], random.randint(1,10))

        self.nodes[722].agregar_salida(self.nodes[778], random.randint(1,10))
        self.nodes[722].agregar_salida(self.nodes[650], random.randint(1,10))

        self.nodes[721].agregar_salida(self.nodes[779], random.randint(1,10))
        self.nodes[721].agregar_salida(self.nodes[651], random.randint(1,10))

        self.nodes[720].agregar_salida(self.nodes[780], random.randint(1,10))
        self.nodes[720].agregar_salida(self.nodes[653], random.randint(1,10))

        self.nodes[719].agregar_salida(self.nodes[781], random.randint(1,10))
        self.nodes[719].agregar_salida(self.nodes[654], random.randint(1,10))

        self.nodes[718].agregar_salida(self.nodes[782], random.randint(1,10))
        self.nodes[718].agregar_salida(self.nodes[655], random.randint(1,10))

        self.nodes[717].agregar_salida(self.nodes[783], random.randint(1,10))
        self.nodes[717].agregar_salida(self.nodes[656], random.randint(1,10))

        self.nodes[716].agregar_salida(self.nodes[784], random.randint(1,10))
        self.nodes[716].agregar_salida(self.nodes[657], random.randint(1,10))

        self.nodes[715].agregar_salida(self.nodes[785], random.randint(1,10))
        self.nodes[715].agregar_salida(self.nodes[658], random.randint(1,10))

        self.nodes[714].agregar_salida(self.nodes[786], random.randint(1,10))
        self.nodes[714].agregar_salida(self.nodes[659], random.randint(1,10))

        self.nodes[713].agregar_salida(self.nodes[787], random.randint(1,10))
        self.nodes[713].agregar_salida(self.nodes[660], random.randint(1,10))

        self.nodes[712].agregar_salida(self.nodes[788], random.randint(1,10))
        self.nodes[712].agregar_salida(self.nodes[661], random.randint(1,10))

        self.nodes[711].agregar_salida(self.nodes[789], random.randint(1,10))
        self.nodes[711].agregar_salida(self.nodes[662], random.randint(1,10))

        self.nodes[710].agregar_salida(self.nodes[790], random.randint(1,10))
        self.nodes[710].agregar_salida(self.nodes[663], random.randint(1,10))

        self.nodes[709].agregar_salida(self.nodes[791], random.randint(1,10))
        self.nodes[709].agregar_salida(self.nodes[664], random.randint(1,10))

        self.nodes[708].agregar_salida(self.nodes[792], random.randint(1,10))
        self.nodes[708].agregar_salida(self.nodes[665], random.randint(1,10))

        self.nodes[707].agregar_salida(self.nodes[793], random.randint(1,10))
        self.nodes[707].agregar_salida(self.nodes[666], random.randint(1,10))

        self.nodes[706].agregar_salida(self.nodes[794], random.randint(1,10))
        self.nodes[706].agregar_salida(self.nodes[667], random.randint(1,10))

        self.nodes[705].agregar_salida(self.nodes[795], random.randint(1,10))
        self.nodes[705].agregar_salida(self.nodes[668], random.randint(1,10))

        self.nodes[704].agregar_salida(self.nodes[796], random.randint(1,10))
        self.nodes[704].agregar_salida(self.nodes[669], random.randint(1,10))

        self.nodes[703].agregar_salida(self.nodes[797], random.randint(1,10))
        self.nodes[703].agregar_salida(self.nodes[670], random.randint(1,10))

        self.nodes[702].agregar_salida(self.nodes[798], random.randint(1,10))
        self.nodes[702].agregar_salida(self.nodes[671], random.randint(1,10))

        self.nodes[701].agregar_salida(self.nodes[799], random.randint(1,10))
        self.nodes[701].agregar_salida(self.nodes[672], random.randint(1,10))

        self.nodes[700].agregar_salida(self.nodes[800], random.randint(1,10))
        self.nodes[700].agregar_salida(self.nodes[673], random.randint(1,10))

        self.nodes[699].agregar_salida(self.nodes[801], random.randint(1,10))
        self.nodes[699].agregar_salida(self.nodes[674], random.randint(1,10))

        self.nodes[698].agregar_salida(self.nodes[802], random.randint(1,10))
        self.nodes[698].agregar_salida(self.nodes[675], random.randint(1,10))

        self.nodes[697].agregar_salida(self.nodes[803], random.randint(1,10))
        self.nodes[697].agregar_salida(self.nodes[676], random.randint(1,10))

        self.nodes[696].agregar_salida(self.nodes[804], random.randint(1,10))
        self.nodes[696].agregar_salida(self.nodes[677], random.randint(1,10))

        self.nodes[695].agregar_salida(self.nodes[805], random.randint(1,10))
        self.nodes[695].agregar_salida(self.nodes[678], random.randint(1,10))

        self.nodes[694].agregar_salida(self.nodes[806], random.randint(1,10))
        self.nodes[694].agregar_salida(self.nodes[679], random.randint(1,10))

        self.nodes[693].agregar_salida(self.nodes[807], random.randint(1,10))
        self.nodes[693].agregar_salida(self.nodes[680], random.randint(1,10))

        self.nodes[692].agregar_salida(self.nodes[808], random.randint(1,10))
        self.nodes[692].agregar_salida(self.nodes[681], random.randint(1,10))

        self.nodes[691].agregar_salida(self.nodes[809], random.randint(1,10))
        self.nodes[691].agregar_salida(self.nodes[682], random.randint(1,10))

        self.nodes[690].agregar_salida(self.nodes[810], random.randint(1,10))
        self.nodes[690].agregar_salida(self.nodes[683], random.randint(1,10))

        self.nodes[689].agregar_salida(self.nodes[684], random.randint(1,10))

        self.nodes[688].agregar_salida(self.nodes[685], random.randint(1,10))

        self.nodes[687].agregar_salida(self.nodes[686], random.randint(1,10))
        self.nodes[687].agregar_salida(self.nodes[811], random.randint(1,10))

        self.nodes[885].agregar_salida(self.nodes[834], random.randint(1,10))
        self.nodes[885].agregar_salida(self.nodes[884], random.randint(1,10))

        self.nodes[886].agregar_salida(self.nodes[835], random.randint(1,10))
        self.nodes[886].agregar_salida(self.nodes[1006], random.randint(1,10))

        self.nodes[887].agregar_salida(self.nodes[836], random.randint(1,10))
        self.nodes[887].agregar_salida(self.nodes[1005], random.randint(1,10))

        self.nodes[888].agregar_salida(self.nodes[837], random.randint(1,10))
        self.nodes[888].agregar_salida(self.nodes[1004], random.randint(1,10))

        self.nodes[889].agregar_salida(self.nodes[838], random.randint(1,10))
        self.nodes[889].agregar_salida(self.nodes[1003], random.randint(1,10))

        self.nodes[890].agregar_salida(self.nodes[839], random.randint(1,10))
        self.nodes[890].agregar_salida(self.nodes[1002], random.randint(1,10))

        self.nodes[891].agregar_salida(self.nodes[840], random.randint(1,10))
        self.nodes[891].agregar_salida(self.nodes[1001], random.randint(1,10))

        self.nodes[892].agregar_salida(self.nodes[841], random.randint(1,10))
        self.nodes[892].agregar_salida(self.nodes[1000], random.randint(1,10))

        self.nodes[893].agregar_salida(self.nodes[842], random.randint(1,10))
        self.nodes[893].agregar_salida(self.nodes[999], random.randint(1,10))

        self.nodes[894].agregar_salida(self.nodes[843], random.randint(1,10))
        self.nodes[894].agregar_salida(self.nodes[998], random.randint(1,10))

        self.nodes[895].agregar_salida(self.nodes[844], random.randint(1,10))
        self.nodes[895].agregar_salida(self.nodes[997], random.randint(1,10))

        self.nodes[896].agregar_salida(self.nodes[845], random.randint(1,10))
        self.nodes[896].agregar_salida(self.nodes[996], random.randint(1,10))

        self.nodes[897].agregar_salida(self.nodes[846], random.randint(1,10))
        self.nodes[897].agregar_salida(self.nodes[995], random.randint(1,10))

        self.nodes[898].agregar_salida(self.nodes[847], random.randint(1,10))
        self.nodes[898].agregar_salida(self.nodes[994], random.randint(1,10))

        self.nodes[870].agregar_salida(self.nodes[994], random.randint(1,10))
        self.nodes[870].agregar_salida(self.nodes[819], random.randint(1,10))

        self.nodes[871].agregar_salida(self.nodes[995], random.randint(1,10))
        self.nodes[871].agregar_salida(self.nodes[820], random.randint(1,10))

        self.nodes[872].agregar_salida(self.nodes[996], random.randint(1,10))
        self.nodes[872].agregar_salida(self.nodes[821], random.randint(1,10))

        self.nodes[873].agregar_salida(self.nodes[997], random.randint(1,10))
        self.nodes[873].agregar_salida(self.nodes[822], random.randint(1,10))

        self.nodes[874].agregar_salida(self.nodes[998], random.randint(1,10))
        self.nodes[874].agregar_salida(self.nodes[823], random.randint(1,10))

        self.nodes[875].agregar_salida(self.nodes[999], random.randint(1,10))

        self.nodes[876].agregar_salida(self.nodes[1000], random.randint(1,10))

        self.nodes[877].agregar_salida(self.nodes[1001], random.randint(1,10))
        self.nodes[877].agregar_salida(self.nodes[824], random.randint(1,10))

        self.nodes[878].agregar_salida(self.nodes[1002], random.randint(1,10))
        self.nodes[878].agregar_salida(self.nodes[825], random.randint(1,10))

        self.nodes[879].agregar_salida(self.nodes[1003], random.randint(1,10))
        self.nodes[879].agregar_salida(self.nodes[826], random.randint(1,10))

        self.nodes[880].agregar_salida(self.nodes[1004], random.randint(1,10))

        self.nodes[881].agregar_salida(self.nodes[1005], random.randint(1,10))
        self.nodes[881].agregar_salida(self.nodes[827], random.randint(1,10))

        self.nodes[882].agregar_salida(self.nodes[1006], random.randint(1,10))
        self.nodes[882].agregar_salida(self.nodes[828], random.randint(1,10))

        self.nodes[883].agregar_salida(self.nodes[884], random.randint(1,10))

        self.nodes[885].agregar_salida(self.nodes[886], random.randint(1,10))
        self.nodes[885].agregar_salida(self.nodes[832], random.randint(1,10))

        self.nodes[887].agregar_salida(self.nodes[888], random.randint(1,10))
        self.nodes[887].agregar_salida(self.nodes[886], random.randint(1,10))

        self.nodes[889].agregar_salida(self.nodes[890], random.randint(1,10))
        self.nodes[889].agregar_salida(self.nodes[888], random.randint(1,10))

        self.nodes[891].agregar_salida(self.nodes[892], random.randint(1,10))
        self.nodes[891].agregar_salida(self.nodes[890], random.randint(1,10))

        self.nodes[893].agregar_salida(self.nodes[894], random.randint(1,10))
        self.nodes[893].agregar_salida(self.nodes[892], random.randint(1,10))

        self.nodes[895].agregar_salida(self.nodes[896], random.randint(1,10))
        self.nodes[895].agregar_salida(self.nodes[894], random.randint(1,10))

        self.nodes[897].agregar_salida(self.nodes[898], random.randint(1,10))
        self.nodes[897].agregar_salida(self.nodes[896], random.randint(1,10))

        self.nodes[884].agregar_salida(self.nodes[831], random.randint(1,10))
        self.nodes[884].agregar_salida(self.nodes[1006], random.randint(1,10))

        self.nodes[883].agregar_salida(self.nodes[830], random.randint(1,10))
        self.nodes[883].agregar_salida(self.nodes[882], random.randint(1,10))

        self.nodes[880].agregar_salida(self.nodes[881], random.randint(1,10))
        self.nodes[880].agregar_salida(self.nodes[879], random.randint(1,10))

        self.nodes[878].agregar_salida(self.nodes[879], random.randint(1,10))
        self.nodes[878].agregar_salida(self.nodes[877], random.randint(1,10))

        self.nodes[876].agregar_salida(self.nodes[877], random.randint(1,10))
        self.nodes[876].agregar_salida(self.nodes[875], random.randint(1,10))

        self.nodes[874].agregar_salida(self.nodes[875], random.randint(1,10))
        self.nodes[874].agregar_salida(self.nodes[873], random.randint(1,10))

        self.nodes[872].agregar_salida(self.nodes[873], random.randint(1,10))
        self.nodes[872].agregar_salida(self.nodes[871], random.randint(1,10))

        self.nodes[870].agregar_salida(self.nodes[871], random.randint(1,10))
        self.nodes[870].agregar_salida(self.nodes[869], random.randint(1,10))

        self.nodes[868].agregar_salida(self.nodes[869], random.randint(1,10))
        self.nodes[868].agregar_salida(self.nodes[867], random.randint(1,10))

        self.nodes[866].agregar_salida(self.nodes[867], random.randint(1,10))
        self.nodes[866].agregar_salida(self.nodes[865], random.randint(1,10))

        self.nodes[864].agregar_salida(self.nodes[865], random.randint(1,10))
        self.nodes[864].agregar_salida(self.nodes[863], random.randint(1,10))

        self.nodes[862].agregar_salida(self.nodes[863], random.randint(1,10))
        self.nodes[862].agregar_salida(self.nodes[687], random.randint(1,10))
        
        self.nodes[985].agregar_salida(self.nodes[686], random.randint(1,10))
        self.nodes[985].agregar_salida(self.nodes[986], random.randint(1,10))

        self.nodes[987].agregar_salida(self.nodes[986], random.randint(1,10))
        self.nodes[987].agregar_salida(self.nodes[989], random.randint(1,10))

        self.nodes[990].agregar_salida(self.nodes[989], random.randint(1,10))
        self.nodes[990].agregar_salida(self.nodes[991], random.randint(1,10))

        self.nodes[992].agregar_salida(self.nodes[991], random.randint(1,10))
        self.nodes[992].agregar_salida(self.nodes[993], random.randint(1,10))

        self.nodes[994].agregar_salida(self.nodes[993], random.randint(1,10))
        self.nodes[995].agregar_salida(self.nodes[994], random.randint(1,10))
        self.nodes[996].agregar_salida(self.nodes[995], random.randint(1,10))
        self.nodes[996].agregar_salida(self.nodes[997], random.randint(1,10))

        self.nodes[998].agregar_salida(self.nodes[997], random.randint(1,10))
        self.nodes[998].agregar_salida(self.nodes[999], random.randint(1,10))

        self.nodes[1000].agregar_salida(self.nodes[999], random.randint(1,10))
        self.nodes[1000].agregar_salida(self.nodes[1001], random.randint(1,10))

        self.nodes[1002].agregar_salida(self.nodes[1001], random.randint(1,10))
        self.nodes[1002].agregar_salida(self.nodes[1003], random.randint(1,10))

        self.nodes[1004].agregar_salida(self.nodes[1003], random.randint(1,10))
        self.nodes[1004].agregar_salida(self.nodes[1005], random.randint(1,10))

        self.nodes[1006].agregar_salida(self.nodes[1005], random.randint(1,10))

        self.nodes[977].agregar_salida(self.nodes[898], random.randint(1,10))
        self.nodes[977].agregar_salida(self.nodes[978], random.randint(1,10))

        self.nodes[979].agregar_salida(self.nodes[978], random.randint(1,10))
        self.nodes[979].agregar_salida(self.nodes[980], random.randint(1,10))

        self.nodes[981].agregar_salida(self.nodes[980], random.randint(1,10))
        self.nodes[981].agregar_salida(self.nodes[982], random.randint(1,10))

        self.nodes[983].agregar_salida(self.nodes[982], random.randint(1,10))
        self.nodes[983].agregar_salida(self.nodes[984], random.randint(1,10))

        self.nodes[984].agregar_salida(self.nodes[856], random.randint(1,10))
        self.nodes[984].agregar_salida(self.nodes[985], random.randint(1,10))

        self.nodes[983].agregar_salida(self.nodes[986], random.randint(1,10))
        self.nodes[982].agregar_salida(self.nodes[987], random.randint(1,10))

        self.nodes[981].agregar_salida(self.nodes[852], random.randint(1,10))
        self.nodes[981].agregar_salida(self.nodes[989], random.randint(1,10))

        self.nodes[980].agregar_salida(self.nodes[990], random.randint(1,10))
        self.nodes[980].agregar_salida(self.nodes[851], random.randint(1,10))

        self.nodes[979].agregar_salida(self.nodes[991], random.randint(1,10))
        self.nodes[979].agregar_salida(self.nodes[850], random.randint(1,10))

        self.nodes[978].agregar_salida(self.nodes[992], random.randint(1,10))
        self.nodes[978].agregar_salida(self.nodes[849], random.randint(1,10))

        self.nodes[977].agregar_salida(self.nodes[993], random.randint(1,10))
        self.nodes[977].agregar_salida(self.nodes[848], random.randint(1,10))
        
        self.nodes[862].agregar_salida(self.nodes[985], random.randint(1,10))
        self.nodes[862].agregar_salida(self.nodes[812], random.randint(1,10))

        self.nodes[863].agregar_salida(self.nodes[986], random.randint(1,10))
        self.nodes[863].agregar_salida(self.nodes[813], random.randint(1,10))

        self.nodes[864].agregar_salida(self.nodes[987], random.randint(1,10))
        
        self.nodes[865].agregar_salida(self.nodes[989], random.randint(1,10))
        self.nodes[865].agregar_salida(self.nodes[814], random.randint(1,10))

        self.nodes[866].agregar_salida(self.nodes[990], random.randint(1,10))
        
        self.nodes[867].agregar_salida(self.nodes[991], random.randint(1,10))
        self.nodes[867].agregar_salida(self.nodes[815], random.randint(1,10))

        self.nodes[868].agregar_salida(self.nodes[992], random.randint(1,10))
        self.nodes[868].agregar_salida(self.nodes[816], random.randint(1,10))

        self.nodes[869].agregar_salida(self.nodes[993], random.randint(1,10))
        self.nodes[869].agregar_salida(self.nodes[817], random.randint(1,10))

        self.nodes[260].agregar_salida(self.nodes[93], random.randint(1,10))
        self.nodes[260].agregar_salida(self.nodes[95], random.randint(1,10))

        self.nodes[261].agregar_salida(self.nodes[899], random.randint(1,10))
        self.nodes[261].agregar_salida(self.nodes[96], random.randint(1,10))

        self.nodes[263].agregar_salida(self.nodes[900], random.randint(1,10))
        self.nodes[263].agregar_salida(self.nodes[97], random.randint(1,10))

        self.nodes[264].agregar_salida(self.nodes[901], random.randint(1,10))
        
        self.nodes[265].agregar_salida(self.nodes[902], random.randint(1,10))
        self.nodes[265].agregar_salida(self.nodes[98], random.randint(1,10))

        self.nodes[266].agregar_salida(self.nodes[903], random.randint(1,10))
        self.nodes[266].agregar_salida(self.nodes[99], random.randint(1,10))

        self.nodes[267].agregar_salida(self.nodes[904], random.randint(1,10))
        self.nodes[267].agregar_salida(self.nodes[100], random.randint(1,10))

        self.nodes[268].agregar_salida(self.nodes[905], random.randint(1,10))
        self.nodes[268].agregar_salida(self.nodes[101], random.randint(1,10))

        self.nodes[270].agregar_salida(self.nodes[907], random.randint(1,10))
        self.nodes[270].agregar_salida(self.nodes[102], random.randint(1,10))

        self.nodes[271].agregar_salida(self.nodes[908], random.randint(1,10))
        
        self.nodes[272].agregar_salida(self.nodes[909], random.randint(1,10))
        self.nodes[272].agregar_salida(self.nodes[103], random.randint(1,10))

        self.nodes[273].agregar_salida(self.nodes[910], random.randint(1,10))
        self.nodes[273].agregar_salida(self.nodes[104], random.randint(1,10))

        self.nodes[274].agregar_salida(self.nodes[911], random.randint(1,10))
        self.nodes[274].agregar_salida(self.nodes[105], random.randint(1,10))

        self.nodes[275].agregar_salida(self.nodes[912], random.randint(1,10))
        self.nodes[275].agregar_salida(self.nodes[107], random.randint(1,10))

        self.nodes[276].agregar_salida(self.nodes[913], random.randint(1,10))

        self.nodes[277].agregar_salida(self.nodes[914], random.randint(1,10))
        self.nodes[277].agregar_salida(self.nodes[108], random.randint(1,10))

        self.nodes[278].agregar_salida(self.nodes[915], random.randint(1,10))
        self.nodes[278].agregar_salida(self.nodes[109], random.randint(1,10))

        self.nodes[279].agregar_salida(self.nodes[916], random.randint(1,10))
        self.nodes[279].agregar_salida(self.nodes[110], random.randint(1,10))

        self.nodes[280].agregar_salida(self.nodes[917], random.randint(1,10))
        self.nodes[280].agregar_salida(self.nodes[111], random.randint(1,10))

        self.nodes[281].agregar_salida(self.nodes[918], random.randint(1,10))
        self.nodes[281].agregar_salida(self.nodes[112], random.randint(1,10))

        self.nodes[282].agregar_salida(self.nodes[919], random.randint(1,10))
        self.nodes[282].agregar_salida(self.nodes[113], random.randint(1,10))

        self.nodes[283].agregar_salida(self.nodes[920], random.randint(1,10))
        self.nodes[283].agregar_salida(self.nodes[114], random.randint(1,10))

        self.nodes[284].agregar_salida(self.nodes[921], random.randint(1,10))
        self.nodes[284].agregar_salida(self.nodes[115], random.randint(1,10))

        self.nodes[285].agregar_salida(self.nodes[922], random.randint(1,10))
        self.nodes[285].agregar_salida(self.nodes[116], random.randint(1,10))

        self.nodes[286].agregar_salida(self.nodes[923], random.randint(1,10))
        
        self.nodes[287].agregar_salida(self.nodes[924], random.randint(1,10))
        self.nodes[287].agregar_salida(self.nodes[117], random.randint(1,10))

        self.nodes[288].agregar_salida(self.nodes[925], random.randint(1,10))
        self.nodes[288].agregar_salida(self.nodes[118], random.randint(1,10))

        self.nodes[289].agregar_salida(self.nodes[926], random.randint(1,10))
        self.nodes[289].agregar_salida(self.nodes[119], random.randint(1,10))

        self.nodes[290].agregar_salida(self.nodes[927], random.randint(1,10))
        self.nodes[290].agregar_salida(self.nodes[120], random.randint(1,10))

        self.nodes[291].agregar_salida(self.nodes[928], random.randint(1,10))
        self.nodes[291].agregar_salida(self.nodes[121], random.randint(1,10))

        self.nodes[292].agregar_salida(self.nodes[929], random.randint(1,10))
        self.nodes[292].agregar_salida(self.nodes[122], random.randint(1,10))

        self.nodes[293].agregar_salida(self.nodes[930], random.randint(1,10))
        self.nodes[293].agregar_salida(self.nodes[123], random.randint(1,10))

        self.nodes[294].agregar_salida(self.nodes[931], random.randint(1,10))
        self.nodes[294].agregar_salida(self.nodes[124], random.randint(1,10))

        self.nodes[295].agregar_salida(self.nodes[932], random.randint(1,10))
        self.nodes[295].agregar_salida(self.nodes[125], random.randint(1,10))

        self.nodes[286].agregar_salida(self.nodes[1007], random.randint(1,10))
        self.nodes[271].agregar_salida(self.nodes[1009], random.randint(1,10))
        self.nodes[276].agregar_salida(self.nodes[1008], random.randint(1,10))

        self.nodes[933].agregar_salida(self.nodes[296], random.randint(1,10))
        self.nodes[933].agregar_salida(self.nodes[934], random.randint(1,10))
        self.nodes[934].agregar_salida(self.nodes[219], random.randint(1,10))

        self.nodes[900].agregar_salida(self.nodes[901], random.randint(1,10))
        self.nodes[900].agregar_salida(self.nodes[899], random.randint(1,10))

        self.nodes[902].agregar_salida(self.nodes[903], random.randint(1,10))
        self.nodes[902].agregar_salida(self.nodes[901], random.randint(1,10))

        self.nodes[904].agregar_salida(self.nodes[903], random.randint(1,10))
        self.nodes[904].agregar_salida(self.nodes[905], random.randint(1,10))

        self.nodes[906].agregar_salida(self.nodes[905], random.randint(1,10))
        self.nodes[906].agregar_salida(self.nodes[907], random.randint(1,10))

        self.nodes[908].agregar_salida(self.nodes[907], random.randint(1,10))
        self.nodes[908].agregar_salida(self.nodes[909], random.randint(1,10))

        self.nodes[910].agregar_salida(self.nodes[909], random.randint(1,10))
        self.nodes[910].agregar_salida(self.nodes[911], random.randint(1,10))

        self.nodes[912].agregar_salida(self.nodes[911], random.randint(1,10))
        self.nodes[912].agregar_salida(self.nodes[913], random.randint(1,10))

        self.nodes[914].agregar_salida(self.nodes[913], random.randint(1,10))
        self.nodes[914].agregar_salida(self.nodes[915], random.randint(1,10))

        self.nodes[916].agregar_salida(self.nodes[915], random.randint(1,10))
        self.nodes[916].agregar_salida(self.nodes[917], random.randint(1,10))

        self.nodes[918].agregar_salida(self.nodes[917], random.randint(1,10))
        self.nodes[918].agregar_salida(self.nodes[919], random.randint(1,10))

        self.nodes[920].agregar_salida(self.nodes[919], random.randint(1,10))
        self.nodes[920].agregar_salida(self.nodes[921], random.randint(1,10))

        self.nodes[922].agregar_salida(self.nodes[921], random.randint(1,10))
        self.nodes[922].agregar_salida(self.nodes[923], random.randint(1,10))

        self.nodes[924].agregar_salida(self.nodes[923], random.randint(1,10))
        self.nodes[924].agregar_salida(self.nodes[925], random.randint(1,10))

        self.nodes[926].agregar_salida(self.nodes[925], random.randint(1,10))
        self.nodes[926].agregar_salida(self.nodes[927], random.randint(1,10))

        self.nodes[928].agregar_salida(self.nodes[927], random.randint(1,10))
        self.nodes[928].agregar_salida(self.nodes[929], random.randint(1,10))

        self.nodes[930].agregar_salida(self.nodes[929], random.randint(1,10))
        self.nodes[930].agregar_salida(self.nodes[931], random.randint(1,10))

        self.nodes[932].agregar_salida(self.nodes[931], random.randint(1,10))
        self.nodes[932].agregar_salida(self.nodes[933], random.randint(1,10))

        self.nodes[258].agregar_salida(self.nodes[91], random.randint(1,10))
        self.nodes[258].agregar_salida(self.nodes[968], random.randint(1,10))

        self.nodes[967].agregar_salida(self.nodes[968], random.randint(1,10))
        self.nodes[967].agregar_salida(self.nodes[966], random.randint(1,10))

        self.nodes[965].agregar_salida(self.nodes[966], random.randint(1,10))
        self.nodes[965].agregar_salida(self.nodes[964], random.randint(1,10))

        self.nodes[963].agregar_salida(self.nodes[964], random.randint(1,10))
        self.nodes[963].agregar_salida(self.nodes[962], random.randint(1,10))

        self.nodes[961].agregar_salida(self.nodes[962], random.randint(1,10))
        self.nodes[961].agregar_salida(self.nodes[960], random.randint(1,10))

        self.nodes[959].agregar_salida(self.nodes[960], random.randint(1,10))
        self.nodes[959].agregar_salida(self.nodes[958], random.randint(1,10))

        self.nodes[957].agregar_salida(self.nodes[958], random.randint(1,10))
        self.nodes[957].agregar_salida(self.nodes[956], random.randint(1,10))

        self.nodes[955].agregar_salida(self.nodes[956], random.randint(1,10))
        self.nodes[955].agregar_salida(self.nodes[954], random.randint(1,10))

        self.nodes[953].agregar_salida(self.nodes[954], random.randint(1,10))
        self.nodes[953].agregar_salida(self.nodes[952], random.randint(1,10))

        self.nodes[951].agregar_salida(self.nodes[952], random.randint(1,10))
        self.nodes[951].agregar_salida(self.nodes[950], random.randint(1,10))

        self.nodes[949].agregar_salida(self.nodes[950], random.randint(1,10))
        self.nodes[949].agregar_salida(self.nodes[948], random.randint(1,10))

        self.nodes[947].agregar_salida(self.nodes[948], random.randint(1,10))
        self.nodes[947].agregar_salida(self.nodes[946], random.randint(1,10))

        self.nodes[945].agregar_salida(self.nodes[946], random.randint(1,10))
        self.nodes[945].agregar_salida(self.nodes[944], random.randint(1,10))

        self.nodes[943].agregar_salida(self.nodes[944], random.randint(1,10))
        self.nodes[943].agregar_salida(self.nodes[942], random.randint(1,10))

        self.nodes[941].agregar_salida(self.nodes[942], random.randint(1,10))
        self.nodes[941].agregar_salida(self.nodes[940], random.randint(1,10))

        self.nodes[939].agregar_salida(self.nodes[940], random.randint(1,10))
        self.nodes[939].agregar_salida(self.nodes[938], random.randint(1,10))

        self.nodes[937].agregar_salida(self.nodes[938], random.randint(1,10))
        self.nodes[937].agregar_salida(self.nodes[936], random.randint(1,10))

        self.nodes[935].agregar_salida(self.nodes[936], random.randint(1,10))
        self.nodes[935].agregar_salida(self.nodes[934], random.randint(1,10))

        self.nodes[935].agregar_salida(self.nodes[932], random.randint(1,10))
        self.nodes[935].agregar_salida(self.nodes[220], random.randint(1,10))

        self.nodes[936].agregar_salida(self.nodes[931], random.randint(1,10))
        self.nodes[936].agregar_salida(self.nodes[221], random.randint(1,10))

        self.nodes[937].agregar_salida(self.nodes[930], random.randint(1,10))
        self.nodes[937].agregar_salida(self.nodes[222], random.randint(1,10))

        self.nodes[938].agregar_salida(self.nodes[929], random.randint(1,10))
        self.nodes[938].agregar_salida(self.nodes[223], random.randint(1,10))

        self.nodes[939].agregar_salida(self.nodes[928], random.randint(1,10))
        self.nodes[939].agregar_salida(self.nodes[224], random.randint(1,10))

        self.nodes[940].agregar_salida(self.nodes[927], random.randint(1,10))
        self.nodes[940].agregar_salida(self.nodes[225], random.randint(1,10))

        self.nodes[941].agregar_salida(self.nodes[926], random.randint(1,10))
        self.nodes[941].agregar_salida(self.nodes[226], random.randint(1,10))

        self.nodes[942].agregar_salida(self.nodes[925], random.randint(1,10))
        self.nodes[942].agregar_salida(self.nodes[227], random.randint(1,10))

        self.nodes[943].agregar_salida(self.nodes[924], random.randint(1,10))
        self.nodes[943].agregar_salida(self.nodes[228], random.randint(1,10))

        self.nodes[944].agregar_salida(self.nodes[923], random.randint(1,10))
        self.nodes[944].agregar_salida(self.nodes[229], random.randint(1,10))

        self.nodes[945].agregar_salida(self.nodes[922], random.randint(1,10))
        self.nodes[945].agregar_salida(self.nodes[230], random.randint(1,10))

        self.nodes[946].agregar_salida(self.nodes[921], random.randint(1,10))
        self.nodes[946].agregar_salida(self.nodes[231], random.randint(1,10))
        
        self.nodes[947].agregar_salida(self.nodes[920], random.randint(1,10))
        self.nodes[947].agregar_salida(self.nodes[232], random.randint(1,10))

        self.nodes[948].agregar_salida(self.nodes[919], random.randint(1,10))
        self.nodes[948].agregar_salida(self.nodes[233], random.randint(1,10))

        self.nodes[949].agregar_salida(self.nodes[918], random.randint(1,10))
        self.nodes[949].agregar_salida(self.nodes[234], random.randint(1,10))

        self.nodes[950].agregar_salida(self.nodes[917], random.randint(1,10))
        self.nodes[950].agregar_salida(self.nodes[235], random.randint(1,10))

        self.nodes[951].agregar_salida(self.nodes[976], random.randint(1,10))
        self.nodes[951].agregar_salida(self.nodes[236], random.randint(1,10))
        self.nodes[976].agregar_salida(self.nodes[916], random.randint(1,10))

        self.nodes[952].agregar_salida(self.nodes[975], random.randint(1,10))
        self.nodes[975].agregar_salida(self.nodes[915], random.randint(1,10))

        self.nodes[953].agregar_salida(self.nodes[974], random.randint(1,10))
        self.nodes[953].agregar_salida(self.nodes[239], random.randint(1,10))
        self.nodes[974].agregar_salida(self.nodes[914], random.randint(1,10))

        self.nodes[954].agregar_salida(self.nodes[973], random.randint(1,10))
        self.nodes[954].agregar_salida(self.nodes[240], random.randint(1,10))
        self.nodes[973].agregar_salida(self.nodes[913], random.randint(1,10))

        self.nodes[955].agregar_salida(self.nodes[972], random.randint(1,10))
        self.nodes[955].agregar_salida(self.nodes[241], random.randint(1,10))
        self.nodes[972].agregar_salida(self.nodes[912], random.randint(1,10))

        self.nodes[956].agregar_salida(self.nodes[971], random.randint(1,10))
        self.nodes[956].agregar_salida(self.nodes[242], random.randint(1,10))
        self.nodes[971].agregar_salida(self.nodes[911], random.randint(1,10))

        self.nodes[957].agregar_salida(self.nodes[970], random.randint(1,10))
        self.nodes[957].agregar_salida(self.nodes[243], random.randint(1,10))
        self.nodes[970].agregar_salida(self.nodes[910], random.randint(1,10))

        self.nodes[958].agregar_salida(self.nodes[969], random.randint(1,10))
        self.nodes[958].agregar_salida(self.nodes[244], random.randint(1,10))
        self.nodes[969].agregar_salida(self.nodes[909], random.randint(1,10))

        self.nodes[959].agregar_salida(self.nodes[246], random.randint(1,10))
        self.nodes[959].agregar_salida(self.nodes[908], random.randint(1,10))

        self.nodes[960].agregar_salida(self.nodes[247], random.randint(1,10))
        self.nodes[960].agregar_salida(self.nodes[907], random.randint(1,10))

        self.nodes[961].agregar_salida(self.nodes[248], random.randint(1,10))
        self.nodes[961].agregar_salida(self.nodes[906], random.randint(1,10))

        self.nodes[962].agregar_salida(self.nodes[250], random.randint(1,10))
        self.nodes[962].agregar_salida(self.nodes[905], random.randint(1,10))

        self.nodes[963].agregar_salida(self.nodes[251], random.randint(1,10))
        self.nodes[963].agregar_salida(self.nodes[904], random.randint(1,10))

        self.nodes[964].agregar_salida(self.nodes[903], random.randint(1,10))
        self.nodes[964].agregar_salida(self.nodes[83], random.randint(1,10))

        self.nodes[965].agregar_salida(self.nodes[253], random.randint(1,10))
        self.nodes[965].agregar_salida(self.nodes[902], random.randint(1,10))

        self.nodes[966].agregar_salida(self.nodes[254], random.randint(1,10))
        self.nodes[966].agregar_salida(self.nodes[901], random.randint(1,10))

        self.nodes[967].agregar_salida(self.nodes[255], random.randint(1,10))
        self.nodes[967].agregar_salida(self.nodes[900], random.randint(1,10))

        self.nodes[968].agregar_salida(self.nodes[899], random.randint(1,10))
        self.nodes[968].agregar_salida(self.nodes[256], random.randint(1,10))

        self.nodes[296].agregar_salida(self.nodes[127], random.randint(1,10))
        self.nodes[297].agregar_salida(self.nodes[1010], random.randint(1,10))
        self.nodes[298].agregar_salida(self.nodes[128], random.randint(1,10))
        self.nodes[299].agregar_salida(self.nodes[129], random.randint(1,10))
        self.nodes[301].agregar_salida(self.nodes[130], random.randint(1,10))
        self.nodes[302].agregar_salida(self.nodes[131], random.randint(1,10))
        self.nodes[303].agregar_salida(self.nodes[132], random.randint(1,10))
        self.nodes[304].agregar_salida(self.nodes[133], random.randint(1,10))
        self.nodes[305].agregar_salida(self.nodes[1012], random.randint(1,10))
        self.nodes[306].agregar_salida(self.nodes[134], random.randint(1,10))
        self.nodes[307].agregar_salida(self.nodes[1011], random.randint(1,10))
        self.nodes[308].agregar_salida(self.nodes[135], random.randint(1,10))
        self.nodes[309].agregar_salida(self.nodes[1013], random.randint(1,10))
        self.nodes[310].agregar_salida(self.nodes[136], random.randint(1,10))
        self.nodes[311].agregar_salida(self.nodes[137], random.randint(1,10))
        self.nodes[312].agregar_salida(self.nodes[138], random.randint(1,10))
        self.nodes[313].agregar_salida(self.nodes[139], random.randint(1,10))
        self.nodes[315].agregar_salida(self.nodes[142], random.randint(1,10))
        self.nodes[316].agregar_salida(self.nodes[143], random.randint(1,10))
        self.nodes[317].agregar_salida(self.nodes[144], random.randint(1,10))
        self.nodes[318].agregar_salida(self.nodes[145], random.randint(1,10))
        self.nodes[319].agregar_salida(self.nodes[146], random.randint(1,10))
        self.nodes[320].agregar_salida(self.nodes[147], random.randint(1,10))
        self.nodes[321].agregar_salida(self.nodes[148], random.randint(1,10))
        self.nodes[322].agregar_salida(self.nodes[149], random.randint(1,10))
        self.nodes[323].agregar_salida(self.nodes[150], random.randint(1,10))
        self.nodes[324].agregar_salida(self.nodes[151], random.randint(1,10))
        self.nodes[325].agregar_salida(self.nodes[152], random.randint(1,10))
        self.nodes[326].agregar_salida(self.nodes[153], random.randint(1,10))
        self.nodes[327].agregar_salida(self.nodes[154], random.randint(1,10))
        self.nodes[328].agregar_salida(self.nodes[155], random.randint(1,10))
        self.nodes[329].agregar_salida(self.nodes[156], random.randint(1,10))
        self.nodes[330].agregar_salida(self.nodes[158], random.randint(1,10))
        self.nodes[331].agregar_salida(self.nodes[159], random.randint(1,10))
        self.nodes[332].agregar_salida(self.nodes[160], random.randint(1,10))
        self.nodes[336].agregar_salida(self.nodes[161], random.randint(1,10))
        self.nodes[337].agregar_salida(self.nodes[163], random.randint(1,10))
        self.nodes[338].agregar_salida(self.nodes[164], random.randint(1,10))
        self.nodes[339].agregar_salida(self.nodes[165], random.randint(1,10))
        self.nodes[340].agregar_salida(self.nodes[166], random.randint(1,10))
        self.nodes[341].agregar_salida(self.nodes[167], random.randint(1,10))
        self.nodes[168].agregar_salida(self.nodes[342], random.randint(1,10))
        self.nodes[169].agregar_salida(self.nodes[486], random.randint(1,10))
        self.nodes[486].agregar_salida(self.nodes[416], random.randint(1,10))
        self.nodes[415].agregar_salida(self.nodes[342], random.randint(1,10))


        self.nodes[169].agregar_salida(self.nodes[1], random.randint(1,10))
        self.nodes[488].agregar_salida(self.nodes[1], random.randint(1,10))

        self.nodes[170].agregar_salida(self.nodes[2], random.randint(1,10))
        self.nodes[489].agregar_salida(self.nodes[2], random.randint(1,10))

        self.nodes[171].agregar_salida(self.nodes[3], random.randint(1,10))
        self.nodes[585].agregar_salida(self.nodes[31], random.randint(1,10))

        self.nodes[172].agregar_salida(self.nodes[4], random.randint(1,10))
        self.nodes[491].agregar_salida(self.nodes[4], random.randint(1,10))

        self.nodes[173].agregar_salida(self.nodes[5], random.randint(1,10))

        self.nodes[174].agregar_salida(self.nodes[6], random.randint(1,10))
        self.nodes[493].agregar_salida(self.nodes[6], random.randint(1,10))

        self.nodes[175].agregar_salida(self.nodes[7], random.randint(1,10))

        self.nodes[177].agregar_salida(self.nodes[8], random.randint(1,10))
        self.nodes[495].agregar_salida(self.nodes[8], random.randint(1,10))

        self.nodes[178].agregar_salida(self.nodes[9], random.randint(1,10))

        self.nodes[498].agregar_salida(self.nodes[10], random.randint(1,10))

        self.nodes[179].agregar_salida(self.nodes[11], random.randint(1,10))
        self.nodes[499].agregar_salida(self.nodes[11], random.randint(1,10))

        self.nodes[180].agregar_salida(self.nodes[12], random.randint(1,10))
        self.nodes[500].agregar_salida(self.nodes[12], random.randint(1,10))

        self.nodes[181].agregar_salida(self.nodes[13], random.randint(1,10))
        self.nodes[501].agregar_salida(self.nodes[13], random.randint(1,10))

        self.nodes[182].agregar_salida(self.nodes[14], random.randint(1,10))
        self.nodes[502].agregar_salida(self.nodes[14], random.randint(1,10))

        self.nodes[183].agregar_salida(self.nodes[15], random.randint(1,10))
        self.nodes[503].agregar_salida(self.nodes[15], random.randint(1,10))

        self.nodes[504].agregar_salida(self.nodes[16], random.randint(1,10))

        self.nodes[184].agregar_salida(self.nodes[17], random.randint(1,10))
        self.nodes[506].agregar_salida(self.nodes[17], random.randint(1,10))

        self.nodes[185].agregar_salida(self.nodes[18], random.randint(1,10))
        self.nodes[507].agregar_salida(self.nodes[18], random.randint(1,10))

        self.nodes[186].agregar_salida(self.nodes[19], random.randint(1,10))
        self.nodes[508].agregar_salida(self.nodes[19], random.randint(1,10))

        self.nodes[187].agregar_salida(self.nodes[20], random.randint(1,10))
        self.nodes[509].agregar_salida(self.nodes[20], random.randint(1,10))

        self.nodes[188].agregar_salida(self.nodes[21], random.randint(1,10))
        self.nodes[510].agregar_salida(self.nodes[21], random.randint(1,10))

        self.nodes[189].agregar_salida(self.nodes[22], random.randint(1,10))
        self.nodes[511].agregar_salida(self.nodes[22], random.randint(1,10))

        self.nodes[191].agregar_salida(self.nodes[23], random.randint(1,10))
        self.nodes[512].agregar_salida(self.nodes[23], random.randint(1,10))

        self.nodes[192].agregar_salida(self.nodes[24], random.randint(1,10))
        self.nodes[513].agregar_salida(self.nodes[24], random.randint(1,10))

        self.nodes[193].agregar_salida(self.nodes[25], random.randint(1,10))
        self.nodes[514].agregar_salida(self.nodes[25], random.randint(1,10))

        self.nodes[194].agregar_salida(self.nodes[26], random.randint(1,10))
        self.nodes[515].agregar_salida(self.nodes[26], random.randint(1,10))

        self.nodes[195].agregar_salida(self.nodes[27], random.randint(1,10))
        self.nodes[516].agregar_salida(self.nodes[27], random.randint(1,10))

        self.nodes[197].agregar_salida(self.nodes[28], random.randint(1,10))
        self.nodes[517].agregar_salida(self.nodes[28], random.randint(1,10))

        self.nodes[198].agregar_salida(self.nodes[29], random.randint(1,10))
        self.nodes[518].agregar_salida(self.nodes[29], random.randint(1,10))

        self.nodes[199].agregar_salida(self.nodes[30], random.randint(1,10))
        self.nodes[519].agregar_salida(self.nodes[30], random.randint(1,10))

        self.nodes[200].agregar_salida(self.nodes[31], random.randint(1,10))

        self.nodes[201].agregar_salida(self.nodes[32], random.randint(1,10))
        self.nodes[520].agregar_salida(self.nodes[32], random.randint(1,10))

        self.nodes[202].agregar_salida(self.nodes[33], random.randint(1,10))
        self.nodes[521].agregar_salida(self.nodes[33], random.randint(1,10))

        self.nodes[203].agregar_salida(self.nodes[34], random.randint(1,10))
        self.nodes[522].agregar_salida(self.nodes[34], random.randint(1,10))

        self.nodes[204].agregar_salida(self.nodes[35], random.randint(1,10))
        self.nodes[523].agregar_salida(self.nodes[35], random.randint(1,10))

        self.nodes[205].agregar_salida(self.nodes[36], random.randint(1,10))
        self.nodes[524].agregar_salida(self.nodes[36], random.randint(1,10))

        self.nodes[206].agregar_salida(self.nodes[37], random.randint(1,10))
        self.nodes[525].agregar_salida(self.nodes[37], random.randint(1,10))

        self.nodes[207].agregar_salida(self.nodes[38], random.randint(1,10))
        self.nodes[526].agregar_salida(self.nodes[38], random.randint(1,10))

        self.nodes[208].agregar_salida(self.nodes[39], random.randint(1,10))
        self.nodes[527].agregar_salida(self.nodes[39], random.randint(1,10))

        self.nodes[209].agregar_salida(self.nodes[40], random.randint(1,10))
        self.nodes[528].agregar_salida(self.nodes[40], random.randint(1,10))

        self.nodes[210].agregar_salida(self.nodes[41], random.randint(1,10))
        self.nodes[529].agregar_salida(self.nodes[41], random.randint(1,10))

        self.nodes[211].agregar_salida(self.nodes[42], random.randint(1,10))
        self.nodes[530].agregar_salida(self.nodes[42], random.randint(1,10))

        self.nodes[212].agregar_salida(self.nodes[43], random.randint(1,10))
        self.nodes[531].agregar_salida(self.nodes[43], random.randint(1,10))

        self.nodes[213].agregar_salida(self.nodes[44], random.randint(1,10))
        self.nodes[532].agregar_salida(self.nodes[44], random.randint(1,10))

        self.nodes[214].agregar_salida(self.nodes[45], random.randint(1,10))
        self.nodes[533].agregar_salida(self.nodes[45], random.randint(1,10))

        self.nodes[215].agregar_salida(self.nodes[46], random.randint(1,10))
        self.nodes[534].agregar_salida(self.nodes[46], random.randint(1,10))

        self.nodes[216].agregar_salida(self.nodes[47], random.randint(1,10))
        self.nodes[535].agregar_salida(self.nodes[47], random.randint(1,10))

        self.nodes[218].agregar_salida(self.nodes[48], random.randint(1,10))
        self.nodes[538].agregar_salida(self.nodes[48], random.randint(1,10))

        self.nodes[536].agregar_salida(self.nodes[217], random.randint(1,10))

        self.nodes[219].agregar_salida(self.nodes[49], random.randint(1,10))
        self.nodes[539].agregar_salida(self.nodes[49], random.randint(1,10))

        self.nodes[220].agregar_salida(self.nodes[50], random.randint(1,10))
        self.nodes[540].agregar_salida(self.nodes[50], random.randint(1,10))

        self.nodes[221].agregar_salida(self.nodes[51], random.randint(1,10))
        self.nodes[541].agregar_salida(self.nodes[51], random.randint(1,10))

        self.nodes[222].agregar_salida(self.nodes[52], random.randint(1,10))
        self.nodes[542].agregar_salida(self.nodes[52], random.randint(1,10))

        self.nodes[223].agregar_salida(self.nodes[53], random.randint(1,10))
        self.nodes[543].agregar_salida(self.nodes[53], random.randint(1,10))

        self.nodes[224].agregar_salida(self.nodes[54], random.randint(1,10))
        self.nodes[544].agregar_salida(self.nodes[54], random.randint(1,10))

        self.nodes[225].agregar_salida(self.nodes[55], random.randint(1,10))
        self.nodes[545].agregar_salida(self.nodes[55], random.randint(1,10))

        self.nodes[226].agregar_salida(self.nodes[56], random.randint(1,10))
        self.nodes[546].agregar_salida(self.nodes[56], random.randint(1,10))

        self.nodes[227].agregar_salida(self.nodes[57], random.randint(1,10))
        self.nodes[547].agregar_salida(self.nodes[57], random.randint(1,10))

        self.nodes[228].agregar_salida(self.nodes[58], random.randint(1,10))
        self.nodes[548].agregar_salida(self.nodes[58], random.randint(1,10))

        self.nodes[229].agregar_salida(self.nodes[59], random.randint(1,10))
        self.nodes[549].agregar_salida(self.nodes[59], random.randint(1,10))

        self.nodes[230].agregar_salida(self.nodes[61], random.randint(1,10))
        self.nodes[550].agregar_salida(self.nodes[61], random.randint(1,10))

        self.nodes[231].agregar_salida(self.nodes[62], random.randint(1,10))
        self.nodes[551].agregar_salida(self.nodes[62], random.randint(1,10))

        self.nodes[232].agregar_salida(self.nodes[63], random.randint(1,10))
        self.nodes[857].agregar_salida(self.nodes[63], random.randint(1,10))

        self.nodes[858].agregar_salida(self.nodes[857], random.randint(1,10))

        self.nodes[233].agregar_salida(self.nodes[64], random.randint(1,10))
        self.nodes[856].agregar_salida(self.nodes[64], random.randint(1,10))

        self.nodes[234].agregar_salida(self.nodes[65], random.randint(1,10))
        self.nodes[855].agregar_salida(self.nodes[65], random.randint(1,10))

        self.nodes[854].agregar_salida(self.nodes[235], random.randint(1,10))

        self.nodes[236].agregar_salida(self.nodes[66], random.randint(1,10))
        self.nodes[853].agregar_salida(self.nodes[66], random.randint(1,10))
        self.nodes[852].agregar_salida(self.nodes[853], random.randint(1,10))

        self.nodes[238].agregar_salida(self.nodes[68], random.randint(1,10))
        self.nodes[851].agregar_salida(self.nodes[68], random.randint(1,10))

        self.nodes[239].agregar_salida(self.nodes[69], random.randint(1,10))
        self.nodes[850].agregar_salida(self.nodes[69], random.randint(1,10))

        self.nodes[240].agregar_salida(self.nodes[70], random.randint(1,10))
        self.nodes[849].agregar_salida(self.nodes[70], random.randint(1,10))

        self.nodes[241].agregar_salida(self.nodes[71], random.randint(1,10))
        self.nodes[848].agregar_salida(self.nodes[71], random.randint(1,10))

        self.nodes[242].agregar_salida(self.nodes[72], random.randint(1,10))
        self.nodes[847].agregar_salida(self.nodes[72], random.randint(1,10))

        self.nodes[243].agregar_salida(self.nodes[73], random.randint(1,10))
        self.nodes[846].agregar_salida(self.nodes[73], random.randint(1,10))

        self.nodes[244].agregar_salida(self.nodes[74], random.randint(1,10))
        self.nodes[845].agregar_salida(self.nodes[74], random.randint(1,10))

        self.nodes[245].agregar_salida(self.nodes[78], random.randint(1,10))
        self.nodes[844].agregar_salida(self.nodes[78], random.randint(1,10))

        self.nodes[247].agregar_salida(self.nodes[79], random.randint(1,10))
        self.nodes[843].agregar_salida(self.nodes[79], random.randint(1,10))

        self.nodes[248].agregar_salida(self.nodes[80], random.randint(1,10))
        self.nodes[842].agregar_salida(self.nodes[80], random.randint(1,10))

        self.nodes[250].agregar_salida(self.nodes[81], random.randint(1,10))
        self.nodes[841].agregar_salida(self.nodes[81], random.randint(1,10))

        self.nodes[251].agregar_salida(self.nodes[82], random.randint(1,10))
        self.nodes[840].agregar_salida(self.nodes[82], random.randint(1,10))

        self.nodes[839].agregar_salida(self.nodes[83], random.randint(1,10))

        self.nodes[253].agregar_salida(self.nodes[84], random.randint(1,10))
        self.nodes[838].agregar_salida(self.nodes[84], random.randint(1,10))

        self.nodes[254].agregar_salida(self.nodes[85], random.randint(1,10))
        self.nodes[837].agregar_salida(self.nodes[85], random.randint(1,10))

        self.nodes[255].agregar_salida(self.nodes[86], random.randint(1,10))
        self.nodes[836].agregar_salida(self.nodes[86], random.randint(1,10))

        self.nodes[835].agregar_salida(self.nodes[87], random.randint(1,10))

        self.nodes[834].agregar_salida(self.nodes[88], random.randint(1,10))

        self.nodes[833].agregar_salida(self.nodes[89], random.randint(1,10))

        self.nodes[257].agregar_salida(self.nodes[90], random.randint(1,10))

        self.nodes[487].agregar_salida(self.nodes[617], random.randint(1,10))

        self.nodes[488].agregar_salida(self.nodes[616], random.randint(1,10))
        self.nodes[619].agregar_salida(self.nodes[616], random.randint(1,10))

        self.nodes[489].agregar_salida(self.nodes[615], random.randint(1,10))
        self.nodes[620].agregar_salida(self.nodes[615], random.randint(1,10))

        self.nodes[621].agregar_salida(self.nodes[614], random.randint(1,10))
        self.nodes[490].agregar_salida(self.nodes[614], random.randint(1,10))

        self.nodes[622].agregar_salida(self.nodes[613], random.randint(1,10))
        self.nodes[491].agregar_salida(self.nodes[613], random.randint(1,10))

        self.nodes[624].agregar_salida(self.nodes[612], random.randint(1,10))
        self.nodes[492].agregar_salida(self.nodes[612], random.randint(1,10))

        self.nodes[625].agregar_salida(self.nodes[611], random.randint(1,10))
        self.nodes[493].agregar_salida(self.nodes[611], random.randint(1,10))

        self.nodes[626].agregar_salida(self.nodes[610], random.randint(1,10))
        self.nodes[494].agregar_salida(self.nodes[610], random.randint(1,10))

        self.nodes[627].agregar_salida(self.nodes[609], random.randint(1,10))
        self.nodes[495].agregar_salida(self.nodes[609], random.randint(1,10))

        self.nodes[628].agregar_salida(self.nodes[608], random.randint(1,10))
        self.nodes[496].agregar_salida(self.nodes[608], random.randint(1,10))

        self.nodes[629].agregar_salida(self.nodes[607], random.randint(1,10))
        self.nodes[497].agregar_salida(self.nodes[607], random.randint(1,10))

        self.nodes[630].agregar_salida(self.nodes[606], random.randint(1,10))
        self.nodes[498].agregar_salida(self.nodes[606], random.randint(1,10))

        self.nodes[632].agregar_salida(self.nodes[605], random.randint(1,10))
        self.nodes[499].agregar_salida(self.nodes[605], random.randint(1,10))

        self.nodes[633].agregar_salida(self.nodes[604], random.randint(1,10))
        self.nodes[500].agregar_salida(self.nodes[604], random.randint(1,10))

        self.nodes[634].agregar_salida(self.nodes[603], random.randint(1,10))
        self.nodes[501].agregar_salida(self.nodes[603], random.randint(1,10))

        self.nodes[635].agregar_salida(self.nodes[602], random.randint(1,10))
        self.nodes[502].agregar_salida(self.nodes[602], random.randint(1,10))

        self.nodes[636].agregar_salida(self.nodes[601], random.randint(1,10))
        self.nodes[503].agregar_salida(self.nodes[601], random.randint(1,10))

        self.nodes[637].agregar_salida(self.nodes[600], random.randint(1,10))
        self.nodes[504].agregar_salida(self.nodes[600], random.randint(1,10))

        self.nodes[638].agregar_salida(self.nodes[599], random.randint(1,10))
        self.nodes[506].agregar_salida(self.nodes[599], random.randint(1,10))

        self.nodes[639].agregar_salida(self.nodes[598], random.randint(1,10))
        self.nodes[507].agregar_salida(self.nodes[598], random.randint(1,10))

        self.nodes[641].agregar_salida(self.nodes[597], random.randint(1,10))
        self.nodes[508].agregar_salida(self.nodes[597], random.randint(1,10))

        self.nodes[642].agregar_salida(self.nodes[596], random.randint(1,10))
        self.nodes[509].agregar_salida(self.nodes[596], random.randint(1,10))

        self.nodes[643].agregar_salida(self.nodes[595], random.randint(1,10))
        self.nodes[510].agregar_salida(self.nodes[595], random.randint(1,10))

        self.nodes[644].agregar_salida(self.nodes[594], random.randint(1,10))
        self.nodes[511].agregar_salida(self.nodes[594], random.randint(1,10))

        self.nodes[645].agregar_salida(self.nodes[593], random.randint(1,10))
        self.nodes[512].agregar_salida(self.nodes[593], random.randint(1,10))

        self.nodes[646].agregar_salida(self.nodes[592], random.randint(1,10))
        self.nodes[513].agregar_salida(self.nodes[592], random.randint(1,10))

        self.nodes[647].agregar_salida(self.nodes[591], random.randint(1,10))
        self.nodes[514].agregar_salida(self.nodes[591], random.randint(1,10))

        self.nodes[648].agregar_salida(self.nodes[590], random.randint(1,10))
        self.nodes[515].agregar_salida(self.nodes[590], random.randint(1,10))

        self.nodes[649].agregar_salida(self.nodes[589], random.randint(1,10))
        self.nodes[516].agregar_salida(self.nodes[589], random.randint(1,10))

        self.nodes[650].agregar_salida(self.nodes[588], random.randint(1,10))
        self.nodes[517].agregar_salida(self.nodes[588], random.randint(1,10))

        self.nodes[651].agregar_salida(self.nodes[587], random.randint(1,10))
        self.nodes[518].agregar_salida(self.nodes[587], random.randint(1,10))

        self.nodes[653].agregar_salida(self.nodes[586], random.randint(1,10))
        self.nodes[519].agregar_salida(self.nodes[586], random.randint(1,10))

        self.nodes[654].agregar_salida(self.nodes[585], random.randint(1,10))

        self.nodes[655].agregar_salida(self.nodes[584], random.randint(1,10))
        self.nodes[520].agregar_salida(self.nodes[584], random.randint(1,10))

        self.nodes[656].agregar_salida(self.nodes[583], random.randint(1,10))
        self.nodes[521].agregar_salida(self.nodes[583], random.randint(1,10))

        self.nodes[657].agregar_salida(self.nodes[582], random.randint(1,10))
        self.nodes[522].agregar_salida(self.nodes[582], random.randint(1,10))

        self.nodes[658].agregar_salida(self.nodes[581], random.randint(1,10))
        self.nodes[523].agregar_salida(self.nodes[581], random.randint(1,10))

        self.nodes[659].agregar_salida(self.nodes[580], random.randint(1,10))
        self.nodes[524].agregar_salida(self.nodes[580], random.randint(1,10))

        self.nodes[660].agregar_salida(self.nodes[579], random.randint(1,10))
        self.nodes[525].agregar_salida(self.nodes[579], random.randint(1,10))

        self.nodes[661].agregar_salida(self.nodes[578], random.randint(1,10))
        self.nodes[526].agregar_salida(self.nodes[578], random.randint(1,10))

        self.nodes[662].agregar_salida(self.nodes[577], random.randint(1,10))
        self.nodes[527].agregar_salida(self.nodes[577], random.randint(1,10))

        self.nodes[663].agregar_salida(self.nodes[576], random.randint(1,10))
        self.nodes[528].agregar_salida(self.nodes[576], random.randint(1,10))

        self.nodes[664].agregar_salida(self.nodes[575], random.randint(1,10))
        self.nodes[529].agregar_salida(self.nodes[575], random.randint(1,10))

        self.nodes[665].agregar_salida(self.nodes[574], random.randint(1,10))
        self.nodes[530].agregar_salida(self.nodes[574], random.randint(1,10))

        self.nodes[666].agregar_salida(self.nodes[573], random.randint(1,10))
        self.nodes[531].agregar_salida(self.nodes[573], random.randint(1,10))

        self.nodes[667].agregar_salida(self.nodes[572], random.randint(1,10))
        self.nodes[532].agregar_salida(self.nodes[572], random.randint(1,10))

        self.nodes[668].agregar_salida(self.nodes[571], random.randint(1,10))
        self.nodes[533].agregar_salida(self.nodes[571], random.randint(1,10))

        self.nodes[669].agregar_salida(self.nodes[570], random.randint(1,10))
        self.nodes[534].agregar_salida(self.nodes[570], random.randint(1,10))

        self.nodes[670].agregar_salida(self.nodes[569], random.randint(1,10))
        self.nodes[535].agregar_salida(self.nodes[569], random.randint(1,10))

        self.nodes[671].agregar_salida(self.nodes[568], random.randint(1,10))
        self.nodes[536].agregar_salida(self.nodes[568], random.randint(1,10))

        self.nodes[672].agregar_salida(self.nodes[567], random.randint(1,10))
        self.nodes[538].agregar_salida(self.nodes[567], random.randint(1,10))

        self.nodes[673].agregar_salida(self.nodes[566], random.randint(1,10))
        self.nodes[539].agregar_salida(self.nodes[566], random.randint(1,10))

        self.nodes[674].agregar_salida(self.nodes[565], random.randint(1,10))
        self.nodes[540].agregar_salida(self.nodes[565], random.randint(1,10))

        self.nodes[675].agregar_salida(self.nodes[564], random.randint(1,10))
        self.nodes[541].agregar_salida(self.nodes[564], random.randint(1,10))

        self.nodes[676].agregar_salida(self.nodes[563], random.randint(1,10))
        self.nodes[542].agregar_salida(self.nodes[563], random.randint(1,10))

        self.nodes[677].agregar_salida(self.nodes[562], random.randint(1,10))
        self.nodes[543].agregar_salida(self.nodes[562], random.randint(1,10))

        self.nodes[678].agregar_salida(self.nodes[561], random.randint(1,10))
        self.nodes[544].agregar_salida(self.nodes[561], random.randint(1,10))

        self.nodes[679].agregar_salida(self.nodes[560], random.randint(1,10))
        self.nodes[545].agregar_salida(self.nodes[560], random.randint(1,10))

        self.nodes[680].agregar_salida(self.nodes[559], random.randint(1,10))
        self.nodes[546].agregar_salida(self.nodes[559], random.randint(1,10))

        self.nodes[681].agregar_salida(self.nodes[558], random.randint(1,10))
        self.nodes[547].agregar_salida(self.nodes[558], random.randint(1,10))

        self.nodes[682].agregar_salida(self.nodes[557], random.randint(1,10))
        self.nodes[548].agregar_salida(self.nodes[557], random.randint(1,10))

        self.nodes[683].agregar_salida(self.nodes[556], random.randint(1,10))
        self.nodes[549].agregar_salida(self.nodes[556], random.randint(1,10))

        self.nodes[684].agregar_salida(self.nodes[555], random.randint(1,10))
        self.nodes[550].agregar_salida(self.nodes[555], random.randint(1,10))

        self.nodes[685].agregar_salida(self.nodes[554], random.randint(1,10))
        self.nodes[551].agregar_salida(self.nodes[554], random.randint(1,10))

        self.nodes[686].agregar_salida(self.nodes[553], random.randint(1,10))

        self.nodes[618].agregar_salida(self.nodes[748], random.randint(1,10))

        self.nodes[619].agregar_salida(self.nodes[747], random.randint(1,10))
        self.nodes[750].agregar_salida(self.nodes[747], random.randint(1,10))

        self.nodes[751].agregar_salida(self.nodes[746], random.randint(1,10))

        self.nodes[623].agregar_salida(self.nodes[745], random.randint(1,10))
        self.nodes[753].agregar_salida(self.nodes[745], random.randint(1,10))

        self.nodes[754].agregar_salida(self.nodes[744], random.randint(1,10))
        self.nodes[624].agregar_salida(self.nodes[744], random.randint(1,10))

        self.nodes[755].agregar_salida(self.nodes[743], random.randint(1,10))
        self.nodes[625].agregar_salida(self.nodes[743], random.randint(1,10))

        self.nodes[756].agregar_salida(self.nodes[742], random.randint(1,10))

        self.nodes[757].agregar_salida(self.nodes[741], random.randint(1,10))
        self.nodes[627].agregar_salida(self.nodes[741], random.randint(1,10))

        self.nodes[758].agregar_salida(self.nodes[740], random.randint(1,10))

        self.nodes[759].agregar_salida(self.nodes[739], random.randint(1,10))

        self.nodes[760].agregar_salida(self.nodes[738], random.randint(1,10))
        self.nodes[630].agregar_salida(self.nodes[738], random.randint(1,10))

        self.nodes[633].agregar_salida(self.nodes[737], random.randint(1,10))
        self.nodes[761].agregar_salida(self.nodes[737], random.randint(1,10))

        self.nodes[762].agregar_salida(self.nodes[736], random.randint(1,10))
        self.nodes[634].agregar_salida(self.nodes[736], random.randint(1,10))

        self.nodes[764].agregar_salida(self.nodes[735], random.randint(1,10))
        self.nodes[636].agregar_salida(self.nodes[735], random.randint(1,10))

        self.nodes[765].agregar_salida(self.nodes[734], random.randint(1,10))
        self.nodes[637].agregar_salida(self.nodes[734], random.randint(1,10))

        self.nodes[635].agregar_salida(self.nodes[763], random.randint(1,10))

        self.nodes[766].agregar_salida(self.nodes[733], random.randint(1,10))
        self.nodes[638].agregar_salida(self.nodes[733], random.randint(1,10))

        self.nodes[767].agregar_salida(self.nodes[732], random.randint(1,10))
        self.nodes[639].agregar_salida(self.nodes[732], random.randint(1,10))

        self.nodes[768].agregar_salida(self.nodes[731], random.randint(1,10))
        self.nodes[641].agregar_salida(self.nodes[731], random.randint(1,10))

        self.nodes[769].agregar_salida(self.nodes[730], random.randint(1,10))
        self.nodes[642].agregar_salida(self.nodes[730], random.randint(1,10))

        self.nodes[770].agregar_salida(self.nodes[729], random.randint(1,10))
        self.nodes[643].agregar_salida(self.nodes[729], random.randint(1,10))

        self.nodes[771].agregar_salida(self.nodes[728], random.randint(1,10))
        self.nodes[644].agregar_salida(self.nodes[728], random.randint(1,10))

        self.nodes[772].agregar_salida(self.nodes[727], random.randint(1,10))
        self.nodes[645].agregar_salida(self.nodes[727], random.randint(1,10))

        self.nodes[773].agregar_salida(self.nodes[726], random.randint(1,10))
        self.nodes[646].agregar_salida(self.nodes[726], random.randint(1,10))

        self.nodes[774].agregar_salida(self.nodes[725], random.randint(1,10))
        self.nodes[647].agregar_salida(self.nodes[725], random.randint(1,10))

        self.nodes[775].agregar_salida(self.nodes[724], random.randint(1,10))
        self.nodes[648].agregar_salida(self.nodes[724], random.randint(1,10))

        self.nodes[776].agregar_salida(self.nodes[723], random.randint(1,10))
        self.nodes[649].agregar_salida(self.nodes[723], random.randint(1,10))

        self.nodes[778].agregar_salida(self.nodes[722], random.randint(1,10))
        self.nodes[650].agregar_salida(self.nodes[722], random.randint(1,10))

        self.nodes[779].agregar_salida(self.nodes[721], random.randint(1,10))
        self.nodes[651].agregar_salida(self.nodes[721], random.randint(1,10))

        self.nodes[780].agregar_salida(self.nodes[720], random.randint(1,10))
        self.nodes[653].agregar_salida(self.nodes[720], random.randint(1,10))

        self.nodes[781].agregar_salida(self.nodes[719], random.randint(1,10))
        self.nodes[654].agregar_salida(self.nodes[719], random.randint(1,10))

        self.nodes[782].agregar_salida(self.nodes[718], random.randint(1,10))
        self.nodes[655].agregar_salida(self.nodes[718], random.randint(1,10))

        self.nodes[783].agregar_salida(self.nodes[717], random.randint(1,10))
        self.nodes[656].agregar_salida(self.nodes[717], random.randint(1,10))

        self.nodes[784].agregar_salida(self.nodes[716], random.randint(1,10))
        self.nodes[657].agregar_salida(self.nodes[716], random.randint(1,10))

        self.nodes[785].agregar_salida(self.nodes[715], random.randint(1,10))
        self.nodes[658].agregar_salida(self.nodes[715], random.randint(1,10))

        self.nodes[786].agregar_salida(self.nodes[714], random.randint(1,10))
        self.nodes[659].agregar_salida(self.nodes[714], random.randint(1,10))

        self.nodes[787].agregar_salida(self.nodes[713], random.randint(1,10))
        self.nodes[660].agregar_salida(self.nodes[713], random.randint(1,10))

        self.nodes[788].agregar_salida(self.nodes[712], random.randint(1,10))
        self.nodes[661].agregar_salida(self.nodes[712], random.randint(1,10))

        self.nodes[789].agregar_salida(self.nodes[711], random.randint(1,10))
        self.nodes[662].agregar_salida(self.nodes[711], random.randint(1,10))

        self.nodes[790].agregar_salida(self.nodes[710], random.randint(1,10))
        self.nodes[663].agregar_salida(self.nodes[710], random.randint(1,10))

        self.nodes[791].agregar_salida(self.nodes[709], random.randint(1,10))
        self.nodes[664].agregar_salida(self.nodes[709], random.randint(1,10))

        self.nodes[792].agregar_salida(self.nodes[708], random.randint(1,10))
        self.nodes[665].agregar_salida(self.nodes[708], random.randint(1,10))

        self.nodes[793].agregar_salida(self.nodes[707], random.randint(1,10))
        self.nodes[666].agregar_salida(self.nodes[707], random.randint(1,10))

        self.nodes[794].agregar_salida(self.nodes[706], random.randint(1,10))
        self.nodes[667].agregar_salida(self.nodes[706], random.randint(1,10))

        self.nodes[795].agregar_salida(self.nodes[705], random.randint(1,10))
        self.nodes[668].agregar_salida(self.nodes[705], random.randint(1,10))

        self.nodes[796].agregar_salida(self.nodes[704], random.randint(1,10))
        self.nodes[669].agregar_salida(self.nodes[704], random.randint(1,10))

        self.nodes[797].agregar_salida(self.nodes[703], random.randint(1,10))
        self.nodes[670].agregar_salida(self.nodes[703], random.randint(1,10))

        self.nodes[798].agregar_salida(self.nodes[702], random.randint(1,10))
        self.nodes[671].agregar_salida(self.nodes[702], random.randint(1,10))

        self.nodes[799].agregar_salida(self.nodes[701], random.randint(1,10))
        self.nodes[672].agregar_salida(self.nodes[701], random.randint(1,10))

        self.nodes[800].agregar_salida(self.nodes[700], random.randint(1,10))
        self.nodes[673].agregar_salida(self.nodes[700], random.randint(1,10))

        self.nodes[801].agregar_salida(self.nodes[699], random.randint(1,10))
        self.nodes[674].agregar_salida(self.nodes[699], random.randint(1,10))

        self.nodes[802].agregar_salida(self.nodes[698], random.randint(1,10))
        self.nodes[675].agregar_salida(self.nodes[698], random.randint(1,10))

        self.nodes[803].agregar_salida(self.nodes[697], random.randint(1,10))
        self.nodes[676].agregar_salida(self.nodes[697], random.randint(1,10))

        self.nodes[804].agregar_salida(self.nodes[696], random.randint(1,10))
        self.nodes[677].agregar_salida(self.nodes[696], random.randint(1,10))

        self.nodes[805].agregar_salida(self.nodes[695], random.randint(1,10))
        self.nodes[678].agregar_salida(self.nodes[695], random.randint(1,10))

        self.nodes[806].agregar_salida(self.nodes[694], random.randint(1,10))
        self.nodes[679].agregar_salida(self.nodes[694], random.randint(1,10))

        self.nodes[807].agregar_salida(self.nodes[693], random.randint(1,10))
        self.nodes[680].agregar_salida(self.nodes[693], random.randint(1,10))

        self.nodes[808].agregar_salida(self.nodes[692], random.randint(1,10))
        self.nodes[681].agregar_salida(self.nodes[692], random.randint(1,10))

        self.nodes[809].agregar_salida(self.nodes[691], random.randint(1,10))
        self.nodes[682].agregar_salida(self.nodes[691], random.randint(1,10))

        self.nodes[810].agregar_salida(self.nodes[690], random.randint(1,10))
        self.nodes[683].agregar_salida(self.nodes[690], random.randint(1,10))

        self.nodes[684].agregar_salida(self.nodes[689], random.randint(1,10))

        self.nodes[685].agregar_salida(self.nodes[688], random.randint(1,10))

        self.nodes[686].agregar_salida(self.nodes[687], random.randint(1,10))
        self.nodes[811].agregar_salida(self.nodes[687], random.randint(1,10))

        self.nodes[834].agregar_salida(self.nodes[885], random.randint(1,10))
        self.nodes[884].agregar_salida(self.nodes[885], random.randint(1,10))

        self.nodes[835].agregar_salida(self.nodes[886], random.randint(1,10))
        self.nodes[1006].agregar_salida(self.nodes[886], random.randint(1,10))

        self.nodes[836].agregar_salida(self.nodes[887], random.randint(1,10))
        self.nodes[1005].agregar_salida(self.nodes[887], random.randint(1,10))

        self.nodes[837].agregar_salida(self.nodes[888], random.randint(1,10))
        self.nodes[1004].agregar_salida(self.nodes[888], random.randint(1,10))

        self.nodes[838].agregar_salida(self.nodes[889], random.randint(1,10))
        self.nodes[1003].agregar_salida(self.nodes[889], random.randint(1,10))

        self.nodes[839].agregar_salida(self.nodes[890], random.randint(1,10))
        self.nodes[1002].agregar_salida(self.nodes[890], random.randint(1,10))

        self.nodes[840].agregar_salida(self.nodes[891], random.randint(1,10))
        self.nodes[1001].agregar_salida(self.nodes[891], random.randint(1,10))

        self.nodes[841].agregar_salida(self.nodes[892], random.randint(1,10))
        self.nodes[1000].agregar_salida(self.nodes[892], random.randint(1,10))

        self.nodes[842].agregar_salida(self.nodes[893], random.randint(1,10))
        self.nodes[999].agregar_salida(self.nodes[893], random.randint(1,10))

        self.nodes[843].agregar_salida(self.nodes[894], random.randint(1,10))
        self.nodes[998].agregar_salida(self.nodes[894], random.randint(1,10))

        self.nodes[844].agregar_salida(self.nodes[895], random.randint(1,10))
        self.nodes[997].agregar_salida(self.nodes[895], random.randint(1,10))

        self.nodes[845].agregar_salida(self.nodes[896], random.randint(1,10))
        self.nodes[996].agregar_salida(self.nodes[896], random.randint(1,10))

        self.nodes[846].agregar_salida(self.nodes[897], random.randint(1,10))
        self.nodes[995].agregar_salida(self.nodes[897], random.randint(1,10))

        self.nodes[847].agregar_salida(self.nodes[898], random.randint(1,10))
        self.nodes[994].agregar_salida(self.nodes[898], random.randint(1,10))

        self.nodes[994].agregar_salida(self.nodes[870], random.randint(1,10))
        self.nodes[819].agregar_salida(self.nodes[870], random.randint(1,10))

        self.nodes[995].agregar_salida(self.nodes[871], random.randint(1,10))
        self.nodes[820].agregar_salida(self.nodes[871], random.randint(1,10))

        self.nodes[996].agregar_salida(self.nodes[872], random.randint(1,10))
        self.nodes[821].agregar_salida(self.nodes[872], random.randint(1,10))

        self.nodes[997].agregar_salida(self.nodes[873], random.randint(1,10))
        self.nodes[822].agregar_salida(self.nodes[873], random.randint(1,10))

        self.nodes[998].agregar_salida(self.nodes[874], random.randint(1,10))
        self.nodes[823].agregar_salida(self.nodes[874], random.randint(1,10))

        self.nodes[999].agregar_salida(self.nodes[875], random.randint(1,10))

        self.nodes[1000].agregar_salida(self.nodes[876], random.randint(1,10))

        self.nodes[1001].agregar_salida(self.nodes[877], random.randint(1,10))
        self.nodes[824].agregar_salida(self.nodes[877], random.randint(1,10))

        self.nodes[1002].agregar_salida(self.nodes[878], random.randint(1,10))
        self.nodes[825].agregar_salida(self.nodes[878], random.randint(1,10))

        self.nodes[1003].agregar_salida(self.nodes[879], random.randint(1,10))
        self.nodes[826].agregar_salida(self.nodes[879], random.randint(1,10))

        self.nodes[1004].agregar_salida(self.nodes[880], random.randint(1,10))

        self.nodes[1005].agregar_salida(self.nodes[881], random.randint(1,10))
        self.nodes[827].agregar_salida(self.nodes[881], random.randint(1,10))

        self.nodes[1006].agregar_salida(self.nodes[882], random.randint(1,10))
        self.nodes[828].agregar_salida(self.nodes[882], random.randint(1,10))

        self.nodes[884].agregar_salida(self.nodes[883], random.randint(1,10))

        self.nodes[886].agregar_salida(self.nodes[885], random.randint(1,10))
        self.nodes[832].agregar_salida(self.nodes[885], random.randint(1,10))

        self.nodes[888].agregar_salida(self.nodes[887], random.randint(1,10))
        self.nodes[886].agregar_salida(self.nodes[887], random.randint(1,10))

        self.nodes[890].agregar_salida(self.nodes[889], random.randint(1,10))
        self.nodes[888].agregar_salida(self.nodes[889], random.randint(1,10))

        self.nodes[892].agregar_salida(self.nodes[891], random.randint(1,10))
        self.nodes[890].agregar_salida(self.nodes[891], random.randint(1,10))

        self.nodes[894].agregar_salida(self.nodes[893], random.randint(1,10))
        self.nodes[892].agregar_salida(self.nodes[893], random.randint(1,10))

        self.nodes[896].agregar_salida(self.nodes[895], random.randint(1,10))
        self.nodes[894].agregar_salida(self.nodes[895], random.randint(1,10))

        self.nodes[898].agregar_salida(self.nodes[897], random.randint(1,10))
        self.nodes[896].agregar_salida(self.nodes[897], random.randint(1,10))

        self.nodes[831].agregar_salida(self.nodes[884], random.randint(1,10))
        self.nodes[1006].agregar_salida(self.nodes[884], random.randint(1,10))

        self.nodes[830].agregar_salida(self.nodes[883], random.randint(1,10))
        self.nodes[882].agregar_salida(self.nodes[883], random.randint(1,10))

        self.nodes[881].agregar_salida(self.nodes[880], random.randint(1,10))
        self.nodes[879].agregar_salida(self.nodes[880], random.randint(1,10))

        self.nodes[879].agregar_salida(self.nodes[878], random.randint(1,10))
        self.nodes[877].agregar_salida(self.nodes[878], random.randint(1,10))

        self.nodes[877].agregar_salida(self.nodes[876], random.randint(1,10))
        self.nodes[875].agregar_salida(self.nodes[876], random.randint(1,10))

        self.nodes[875].agregar_salida(self.nodes[874], random.randint(1,10))
        self.nodes[873].agregar_salida(self.nodes[874], random.randint(1,10))

        self.nodes[873].agregar_salida(self.nodes[872], random.randint(1,10))
        self.nodes[871].agregar_salida(self.nodes[872], random.randint(1,10))

        self.nodes[871].agregar_salida(self.nodes[870], random.randint(1,10))
        self.nodes[869].agregar_salida(self.nodes[870], random.randint(1,10))

        self.nodes[869].agregar_salida(self.nodes[868], random.randint(1,10))
        self.nodes[867].agregar_salida(self.nodes[868], random.randint(1,10))

        self.nodes[867].agregar_salida(self.nodes[866], random.randint(1,10))
        self.nodes[865].agregar_salida(self.nodes[866], random.randint(1,10))

        self.nodes[865].agregar_salida(self.nodes[864], random.randint(1,10))
        self.nodes[863].agregar_salida(self.nodes[864], random.randint(1,10))

        self.nodes[863].agregar_salida(self.nodes[862], random.randint(1,10))
        self.nodes[687].agregar_salida(self.nodes[862], random.randint(1,10))

        self.nodes[686].agregar_salida(self.nodes[985], random.randint(1,10))
        self.nodes[986].agregar_salida(self.nodes[985], random.randint(1,10))

        self.nodes[986].agregar_salida(self.nodes[987], random.randint(1,10))
        self.nodes[989].agregar_salida(self.nodes[987], random.randint(1,10))

        self.nodes[989].agregar_salida(self.nodes[990], random.randint(1,10))
        self.nodes[991].agregar_salida(self.nodes[990], random.randint(1,10))

        self.nodes[991].agregar_salida(self.nodes[992], random.randint(1,10))
        self.nodes[993].agregar_salida(self.nodes[992], random.randint(1,10))

        self.nodes[993].agregar_salida(self.nodes[994], random.randint(1,10))
        self.nodes[994].agregar_salida(self.nodes[995], random.randint(1,10))
        self.nodes[995].agregar_salida(self.nodes[996], random.randint(1,10))
        self.nodes[997].agregar_salida(self.nodes[996], random.randint(1,10))

        self.nodes[997].agregar_salida(self.nodes[998], random.randint(1,10))
        self.nodes[999].agregar_salida(self.nodes[998], random.randint(1,10))

        self.nodes[999].agregar_salida(self.nodes[1000], random.randint(1,10))
        self.nodes[1001].agregar_salida(self.nodes[1000], random.randint(1,10))

        self.nodes[1001].agregar_salida(self.nodes[1002], random.randint(1,10))
        self.nodes[1003].agregar_salida(self.nodes[1002], random.randint(1,10))

        self.nodes[1003].agregar_salida(self.nodes[1004], random.randint(1,10))
        self.nodes[1005].agregar_salida(self.nodes[1004], random.randint(1,10))

        self.nodes[1005].agregar_salida(self.nodes[1006], random.randint(1,10))

        self.nodes[898].agregar_salida(self.nodes[977], random.randint(1,10))
        self.nodes[978].agregar_salida(self.nodes[977], random.randint(1,10))

        self.nodes[978].agregar_salida(self.nodes[979], random.randint(1,10))
        self.nodes[980].agregar_salida(self.nodes[979], random.randint(1,10))

        self.nodes[980].agregar_salida(self.nodes[981], random.randint(1,10))
        self.nodes[982].agregar_salida(self.nodes[981], random.randint(1,10))

        self.nodes[982].agregar_salida(self.nodes[983], random.randint(1,10))
        self.nodes[984].agregar_salida(self.nodes[983], random.randint(1,10))

        self.nodes[985].agregar_salida(self.nodes[984], random.randint(1,10))
        self.nodes[986].agregar_salida(self.nodes[983], random.randint(1,10))

        self.nodes[987].agregar_salida(self.nodes[982], random.randint(1,10))
        self.nodes[989].agregar_salida(self.nodes[981], random.randint(1,10))

        self.nodes[852].agregar_salida(self.nodes[981], random.randint(1,10))
        self.nodes[989].agregar_salida(self.nodes[980], random.randint(1,10))

        self.nodes[990].agregar_salida(self.nodes[980], random.randint(1,10))
        self.nodes[851].agregar_salida(self.nodes[980], random.randint(1,10))

        self.nodes[991].agregar_salida(self.nodes[979], random.randint(1,10))
        self.nodes[850].agregar_salida(self.nodes[979], random.randint(1,10))

        self.nodes[992].agregar_salida(self.nodes[978], random.randint(1,10))
        self.nodes[849].agregar_salida(self.nodes[978], random.randint(1,10))

        self.nodes[993].agregar_salida(self.nodes[977], random.randint(1,10))
        self.nodes[848].agregar_salida(self.nodes[977], random.randint(1,10))

        self.nodes[985].agregar_salida(self.nodes[862], random.randint(1,10))
        self.nodes[812].agregar_salida(self.nodes[862], random.randint(1,10))

        self.nodes[986].agregar_salida(self.nodes[863], random.randint(1,10))
        self.nodes[813].agregar_salida(self.nodes[863], random.randint(1,10))

        self.nodes[987].agregar_salida(self.nodes[864], random.randint(1,10))

        self.nodes[989].agregar_salida(self.nodes[865], random.randint(1,10))
        self.nodes[814].agregar_salida(self.nodes[865], random.randint(1,10))

        self.nodes[990].agregar_salida(self.nodes[866], random.randint(1,10))

        self.nodes[991].agregar_salida(self.nodes[867], random.randint(1,10))
        self.nodes[815].agregar_salida(self.nodes[867], random.randint(1,10))

        self.nodes[992].agregar_salida(self.nodes[868], random.randint(1,10))
        self.nodes[816].agregar_salida(self.nodes[868], random.randint(1,10))

        self.nodes[993].agregar_salida(self.nodes[869], random.randint(1,10))
        self.nodes[817].agregar_salida(self.nodes[869], random.randint(1,10))

        self.nodes[93].agregar_salida(self.nodes[260], random.randint(1,10))
        self.nodes[95].agregar_salida(self.nodes[260], random.randint(1,10))

        self.nodes[899].agregar_salida(self.nodes[261], random.randint(1,10))
        self.nodes[96].agregar_salida(self.nodes[261], random.randint(1,10))

        self.nodes[900].agregar_salida(self.nodes[263], random.randint(1,10))
        self.nodes[97].agregar_salida(self.nodes[263], random.randint(1,10))

        self.nodes[901].agregar_salida(self.nodes[264], random.randint(1,10))

        self.nodes[902].agregar_salida(self.nodes[265], random.randint(1,10))
        self.nodes[98].agregar_salida(self.nodes[265], random.randint(1,10))

        self.nodes[903].agregar_salida(self.nodes[266], random.randint(1,10))
        self.nodes[99].agregar_salida(self.nodes[266], random.randint(1,10))

        self.nodes[904].agregar_salida(self.nodes[267], random.randint(1,10))
        self.nodes[100].agregar_salida(self.nodes[267], random.randint(1,10))

        self.nodes[905].agregar_salida(self.nodes[268], random.randint(1,10))
        self.nodes[101].agregar_salida(self.nodes[268], random.randint(1,10))

        self.nodes[907].agregar_salida(self.nodes[270], random.randint(1,10))
        self.nodes[102].agregar_salida(self.nodes[270], random.randint(1,10))

        self.nodes[908].agregar_salida(self.nodes[271], random.randint(1,10))

        self.nodes[909].agregar_salida(self.nodes[272], random.randint(1,10))
        self.nodes[103].agregar_salida(self.nodes[272], random.randint(1,10))

        self.nodes[910].agregar_salida(self.nodes[273], random.randint(1,10))
        self.nodes[104].agregar_salida(self.nodes[273], random.randint(1,10))

        self.nodes[911].agregar_salida(self.nodes[274], random.randint(1,10))
        self.nodes[105].agregar_salida(self.nodes[274], random.randint(1,10))

        self.nodes[912].agregar_salida(self.nodes[275], random.randint(1,10))
        self.nodes[107].agregar_salida(self.nodes[275], random.randint(1,10))

        self.nodes[913].agregar_salida(self.nodes[276], random.randint(1,10))

        self.nodes[914].agregar_salida(self.nodes[277], random.randint(1,10))
        self.nodes[108].agregar_salida(self.nodes[277], random.randint(1,10))

        self.nodes[915].agregar_salida(self.nodes[278], random.randint(1,10))
        self.nodes[109].agregar_salida(self.nodes[278], random.randint(1,10))

        self.nodes[916].agregar_salida(self.nodes[279], random.randint(1,10))
        self.nodes[110].agregar_salida(self.nodes[279], random.randint(1,10))

        self.nodes[917].agregar_salida(self.nodes[280], random.randint(1,10))
        self.nodes[111].agregar_salida(self.nodes[280], random.randint(1,10))

        self.nodes[918].agregar_salida(self.nodes[281], random.randint(1,10))
        self.nodes[112].agregar_salida(self.nodes[281], random.randint(1,10))

        self.nodes[919].agregar_salida(self.nodes[282], random.randint(1,10))
        self.nodes[113].agregar_salida(self.nodes[282], random.randint(1,10))

        self.nodes[920].agregar_salida(self.nodes[283], random.randint(1,10))
        self.nodes[114].agregar_salida(self.nodes[283], random.randint(1,10))

        self.nodes[921].agregar_salida(self.nodes[284], random.randint(1,10))
        self.nodes[115].agregar_salida(self.nodes[284], random.randint(1,10))

        self.nodes[922].agregar_salida(self.nodes[285], random.randint(1,10))
        self.nodes[116].agregar_salida(self.nodes[285], random.randint(1,10))

        self.nodes[923].agregar_salida(self.nodes[286], random.randint(1,10))

        self.nodes[924].agregar_salida(self.nodes[287], random.randint(1,10))
        self.nodes[117].agregar_salida(self.nodes[287], random.randint(1,10))

        self.nodes[925].agregar_salida(self.nodes[288], random.randint(1,10))
        self.nodes[118].agregar_salida(self.nodes[288], random.randint(1,10))

        self.nodes[926].agregar_salida(self.nodes[289], random.randint(1,10))
        self.nodes[119].agregar_salida(self.nodes[289], random.randint(1,10))

        self.nodes[927].agregar_salida(self.nodes[290], random.randint(1,10))
        self.nodes[120].agregar_salida(self.nodes[290], random.randint(1,10))

        self.nodes[928].agregar_salida(self.nodes[291], random.randint(1,10))
        self.nodes[121].agregar_salida(self.nodes[291], random.randint(1,10))

        self.nodes[929].agregar_salida(self.nodes[292], random.randint(1,10))
        self.nodes[122].agregar_salida(self.nodes[292], random.randint(1,10))

        self.nodes[930].agregar_salida(self.nodes[293], random.randint(1,10))
        self.nodes[123].agregar_salida(self.nodes[293], random.randint(1,10))

        self.nodes[931].agregar_salida(self.nodes[294], random.randint(1,10))
        self.nodes[124].agregar_salida(self.nodes[294], random.randint(1,10))

        self.nodes[932].agregar_salida(self.nodes[295], random.randint(1,10))
        self.nodes[125].agregar_salida(self.nodes[295], random.randint(1,10))

        self.nodes[1007].agregar_salida(self.nodes[286], random.randint(1,10))
        self.nodes[1009].agregar_salida(self.nodes[271], random.randint(1,10))
        self.nodes[1008].agregar_salida(self.nodes[276], random.randint(1,10))

        self.nodes[296].agregar_salida(self.nodes[933], random.randint(1,10))
        self.nodes[934].agregar_salida(self.nodes[933], random.randint(1,10))
        self.nodes[219].agregar_salida(self.nodes[934], random.randint(1,10))

        self.nodes[901].agregar_salida(self.nodes[900], random.randint(1,10))
        self.nodes[899].agregar_salida(self.nodes[900], random.randint(1,10))

        self.nodes[903].agregar_salida(self.nodes[902], random.randint(1,10))
        self.nodes[901].agregar_salida(self.nodes[902], random.randint(1,10))

        self.nodes[905].agregar_salida(self.nodes[904], random.randint(1,10))
        self.nodes[903].agregar_salida(self.nodes[904], random.randint(1,10))

        self.nodes[907].agregar_salida(self.nodes[906], random.randint(1,10))
        self.nodes[905].agregar_salida(self.nodes[906], random.randint(1,10))

        self.nodes[909].agregar_salida(self.nodes[908], random.randint(1,10))
        self.nodes[907].agregar_salida(self.nodes[908], random.randint(1,10))

        self.nodes[911].agregar_salida(self.nodes[910], random.randint(1,10))
        self.nodes[909].agregar_salida(self.nodes[910], random.randint(1,10))

        self.nodes[913].agregar_salida(self.nodes[912], random.randint(1,10))
        self.nodes[911].agregar_salida(self.nodes[912], random.randint(1,10))

        self.nodes[915].agregar_salida(self.nodes[914], random.randint(1,10))
        self.nodes[913].agregar_salida(self.nodes[914], random.randint(1,10))

        self.nodes[917].agregar_salida(self.nodes[916], random.randint(1,10))
        self.nodes[915].agregar_salida(self.nodes[916], random.randint(1,10))

        self.nodes[919].agregar_salida(self.nodes[918], random.randint(1,10))
        self.nodes[917].agregar_salida(self.nodes[918], random.randint(1,10))

        self.nodes[921].agregar_salida(self.nodes[920], random.randint(1,10))
        self.nodes[919].agregar_salida(self.nodes[920], random.randint(1,10))

        self.nodes[923].agregar_salida(self.nodes[922], random.randint(1,10))
        self.nodes[921].agregar_salida(self.nodes[922], random.randint(1,10))

        self.nodes[925].agregar_salida(self.nodes[924], random.randint(1,10))
        self.nodes[923].agregar_salida(self.nodes[924], random.randint(1,10))

        self.nodes[927].agregar_salida(self.nodes[926], random.randint(1,10))
        self.nodes[925].agregar_salida(self.nodes[926], random.randint(1,10))

        self.nodes[929].agregar_salida(self.nodes[928], random.randint(1,10))
        self.nodes[927].agregar_salida(self.nodes[928], random.randint(1,10))

        self.nodes[931].agregar_salida(self.nodes[930], random.randint(1,10))
        self.nodes[929].agregar_salida(self.nodes[930], random.randint(1,10))

        self.nodes[933].agregar_salida(self.nodes[932], random.randint(1,10))
        self.nodes[931].agregar_salida(self.nodes[932], random.randint(1,10))

        self.nodes[91].agregar_salida(self.nodes[258], random.randint(1,10))
        self.nodes[968].agregar_salida(self.nodes[258], random.randint(1,10))

        self.nodes[968].agregar_salida(self.nodes[967], random.randint(1,10))
        self.nodes[966].agregar_salida(self.nodes[967], random.randint(1,10))

        self.nodes[966].agregar_salida(self.nodes[965], random.randint(1,10))
        self.nodes[964].agregar_salida(self.nodes[965], random.randint(1,10))

        self.nodes[964].agregar_salida(self.nodes[963], random.randint(1,10))
        self.nodes[962].agregar_salida(self.nodes[963], random.randint(1,10))

        self.nodes[962].agregar_salida(self.nodes[961], random.randint(1,10))
        self.nodes[960].agregar_salida(self.nodes[961], random.randint(1,10))

        self.nodes[960].agregar_salida(self.nodes[959], random.randint(1,10))
        self.nodes[958].agregar_salida(self.nodes[959], random.randint(1,10))

        self.nodes[958].agregar_salida(self.nodes[957], random.randint(1,10))
        self.nodes[956].agregar_salida(self.nodes[957], random.randint(1,10))

        self.nodes[956].agregar_salida(self.nodes[955], random.randint(1,10))
        self.nodes[954].agregar_salida(self.nodes[955], random.randint(1,10))

        self.nodes[954].agregar_salida(self.nodes[953], random.randint(1,10))
        self.nodes[952].agregar_salida(self.nodes[953], random.randint(1,10))

        self.nodes[952].agregar_salida(self.nodes[951], random.randint(1,10))
        self.nodes[950].agregar_salida(self.nodes[951], random.randint(1,10))

        self.nodes[950].agregar_salida(self.nodes[949], random.randint(1,10))
        self.nodes[948].agregar_salida(self.nodes[949], random.randint(1,10))

        self.nodes[948].agregar_salida(self.nodes[947], random.randint(1,10))
        self.nodes[946].agregar_salida(self.nodes[947], random.randint(1,10))

        self.nodes[946].agregar_salida(self.nodes[945], random.randint(1,10))
        self.nodes[944].agregar_salida(self.nodes[945], random.randint(1,10))

        self.nodes[944].agregar_salida(self.nodes[943], random.randint(1,10))
        self.nodes[942].agregar_salida(self.nodes[943], random.randint(1,10))

        self.nodes[942].agregar_salida(self.nodes[941], random.randint(1,10))
        self.nodes[940].agregar_salida(self.nodes[941], random.randint(1,10))

        self.nodes[940].agregar_salida(self.nodes[939], random.randint(1,10))
        self.nodes[938].agregar_salida(self.nodes[939], random.randint(1,10))

        self.nodes[938].agregar_salida(self.nodes[937], random.randint(1,10))
        self.nodes[936].agregar_salida(self.nodes[937], random.randint(1,10))

        self.nodes[936].agregar_salida(self.nodes[935], random.randint(1,10))
        self.nodes[934].agregar_salida(self.nodes[935], random.randint(1,10))

        self.nodes[932].agregar_salida(self.nodes[935], random.randint(1,10))
        self.nodes[220].agregar_salida(self.nodes[935], random.randint(1,10))

        self.nodes[931].agregar_salida(self.nodes[936], random.randint(1,10))
        self.nodes[221].agregar_salida(self.nodes[936], random.randint(1,10))

        self.nodes[930].agregar_salida(self.nodes[937], random.randint(1,10))
        self.nodes[222].agregar_salida(self.nodes[937], random.randint(1,10))

        self.nodes[929].agregar_salida(self.nodes[938], random.randint(1,10))
        self.nodes[223].agregar_salida(self.nodes[938], random.randint(1,10))

        self.nodes[928].agregar_salida(self.nodes[939], random.randint(1,10))
        self.nodes[224].agregar_salida(self.nodes[939], random.randint(1,10))

        self.nodes[927].agregar_salida(self.nodes[940], random.randint(1,10))
        self.nodes[225].agregar_salida(self.nodes[940], random.randint(1,10))

        self.nodes[926].agregar_salida(self.nodes[941], random.randint(1,10))
        self.nodes[226].agregar_salida(self.nodes[941], random.randint(1,10))

        self.nodes[925].agregar_salida(self.nodes[942], random.randint(1,10))
        self.nodes[227].agregar_salida(self.nodes[942], random.randint(1,10))

        self.nodes[924].agregar_salida(self.nodes[943], random.randint(1,10))
        self.nodes[228].agregar_salida(self.nodes[943], random.randint(1,10))

        self.nodes[923].agregar_salida(self.nodes[944], random.randint(1,10))
        self.nodes[229].agregar_salida(self.nodes[944], random.randint(1,10))

        self.nodes[922].agregar_salida(self.nodes[945], random.randint(1,10))
        self.nodes[230].agregar_salida(self.nodes[945], random.randint(1,10))

        self.nodes[921].agregar_salida(self.nodes[946], random.randint(1,10))
        self.nodes[231].agregar_salida(self.nodes[946], random.randint(1,10))

        self.nodes[920].agregar_salida(self.nodes[947], random.randint(1,10))
        self.nodes[232].agregar_salida(self.nodes[947], random.randint(1,10))

        self.nodes[919].agregar_salida(self.nodes[948], random.randint(1,10))
        self.nodes[233].agregar_salida(self.nodes[948], random.randint(1,10))

        self.nodes[918].agregar_salida(self.nodes[949], random.randint(1,10))
        self.nodes[234].agregar_salida(self.nodes[949], random.randint(1,10))

        self.nodes[917].agregar_salida(self.nodes[950], random.randint(1,10))
        self.nodes[235].agregar_salida(self.nodes[950], random.randint(1,10))

        self.nodes[976].agregar_salida(self.nodes[951], random.randint(1,10))
        self.nodes[236].agregar_salida(self.nodes[951], random.randint(1,10))
        self.nodes[916].agregar_salida(self.nodes[951], random.randint(1,10))

        self.nodes[975].agregar_salida(self.nodes[952], random.randint(1,10))
        self.nodes[915].agregar_salida(self.nodes[975], random.randint(1,10))

        self.nodes[974].agregar_salida(self.nodes[953], random.randint(1,10))
        self.nodes[239].agregar_salida(self.nodes[953], random.randint(1,10))
        self.nodes[914].agregar_salida(self.nodes[974], random.randint(1,10))

        self.nodes[973].agregar_salida(self.nodes[954], random.randint(1,10))
        self.nodes[240].agregar_salida(self.nodes[954], random.randint(1,10))
        self.nodes[913].agregar_salida(self.nodes[973], random.randint(1,10))

        self.nodes[972].agregar_salida(self.nodes[955], random.randint(1,10))
        self.nodes[241].agregar_salida(self.nodes[955], random.randint(1,10))
        self.nodes[912].agregar_salida(self.nodes[972], random.randint(1,10))

        self.nodes[971].agregar_salida(self.nodes[956], random.randint(1,10))
        self.nodes[242].agregar_salida(self.nodes[956], random.randint(1,10))
        self.nodes[911].agregar_salida(self.nodes[971], random.randint(1,10))

        self.nodes[970].agregar_salida(self.nodes[957], random.randint(1,10))
        self.nodes[243].agregar_salida(self.nodes[957], random.randint(1,10))
        self.nodes[910].agregar_salida(self.nodes[970], random.randint(1,10))

        self.nodes[969].agregar_salida(self.nodes[958], random.randint(1,10))
        self.nodes[244].agregar_salida(self.nodes[958], random.randint(1,10))
        self.nodes[909].agregar_salida(self.nodes[969], random.randint(1,10))

        self.nodes[246].agregar_salida(self.nodes[959], random.randint(1,10))
        self.nodes[908].agregar_salida(self.nodes[959], random.randint(1,10))

        self.nodes[247].agregar_salida(self.nodes[960], random.randint(1,10))
        self.nodes[907].agregar_salida(self.nodes[960], random.randint(1,10))

        self.nodes[248].agregar_salida(self.nodes[961], random.randint(1,10))
        self.nodes[906].agregar_salida(self.nodes[961], random.randint(1,10))

        self.nodes[250].agregar_salida(self.nodes[962], random.randint(1,10))
        self.nodes[905].agregar_salida(self.nodes[962], random.randint(1,10))

        self.nodes[251].agregar_salida(self.nodes[963], random.randint(1,10))
        self.nodes[904].agregar_salida(self.nodes[963], random.randint(1,10))

        self.nodes[903].agregar_salida(self.nodes[964], random.randint(1,10))
        self.nodes[83].agregar_salida(self.nodes[964], random.randint(1,10))

        self.nodes[253].agregar_salida(self.nodes[965], random.randint(1,10))
        self.nodes[902].agregar_salida(self.nodes[965], random.randint(1,10))

        self.nodes[254].agregar_salida(self.nodes[966], random.randint(1,10))
        self.nodes[901].agregar_salida(self.nodes[966], random.randint(1,10))

        self.nodes[255].agregar_salida(self.nodes[967], random.randint(1,10))
        self.nodes[900].agregar_salida(self.nodes[967], random.randint(1,10))

        self.nodes[899].agregar_salida(self.nodes[968], random.randint(1,10))
        self.nodes[256].agregar_salida(self.nodes[968], random.randint(1,10))

        self.nodes[127].agregar_salida(self.nodes[296], random.randint(1,10))
        self.nodes[1010].agregar_salida(self.nodes[297], random.randint(1,10))
        self.nodes[128].agregar_salida(self.nodes[298], random.randint(1,10))
        self.nodes[129].agregar_salida(self.nodes[299], random.randint(1,10))
        self.nodes[130].agregar_salida(self.nodes[301], random.randint(1,10))
        self.nodes[131].agregar_salida(self.nodes[302], random.randint(1,10))
        self.nodes[132].agregar_salida(self.nodes[303], random.randint(1,10))
        self.nodes[133].agregar_salida(self.nodes[304], random.randint(1,10))
        self.nodes[1012].agregar_salida(self.nodes[305], random.randint(1,10))
        self.nodes[134].agregar_salida(self.nodes[306], random.randint(1,10))
        self.nodes[1011].agregar_salida(self.nodes[307], random.randint(1,10))
        self.nodes[135].agregar_salida(self.nodes[308], random.randint(1,10))
        self.nodes[1013].agregar_salida(self.nodes[309], random.randint(1,10))
        self.nodes[136].agregar_salida(self.nodes[310], random.randint(1,10))
        self.nodes[137].agregar_salida(self.nodes[311], random.randint(1,10))
        self.nodes[138].agregar_salida(self.nodes[312], random.randint(1,10))
        self.nodes[139].agregar_salida(self.nodes[313], random.randint(1,10))
        self.nodes[142].agregar_salida(self.nodes[315], random.randint(1,10))
        self.nodes[143].agregar_salida(self.nodes[316], random.randint(1,10))
        self.nodes[144].agregar_salida(self.nodes[317], random.randint(1,10))
        self.nodes[145].agregar_salida(self.nodes[318], random.randint(1,10))
        self.nodes[146].agregar_salida(self.nodes[319], random.randint(1,10))
        self.nodes[147].agregar_salida(self.nodes[320], random.randint(1,10))
        self.nodes[148].agregar_salida(self.nodes[321], random.randint(1,10))
        self.nodes[149].agregar_salida(self.nodes[322], random.randint(1,10))
        self.nodes[150].agregar_salida(self.nodes[323], random.randint(1,10))
        self.nodes[151].agregar_salida(self.nodes[324], random.randint(1,10))
        self.nodes[152].agregar_salida(self.nodes[325], random.randint(1,10))
        self.nodes[153].agregar_salida(self.nodes[326], random.randint(1,10))
        self.nodes[154].agregar_salida(self.nodes[327], random.randint(1,10))
        self.nodes[155].agregar_salida(self.nodes[328], random.randint(1,10))
        self.nodes[156].agregar_salida(self.nodes[329], random.randint(1,10))
        self.nodes[158].agregar_salida(self.nodes[330], random.randint(1,10))
        self.nodes[159].agregar_salida(self.nodes[331], random.randint(1,10))
        self.nodes[160].agregar_salida(self.nodes[332], random.randint(1,10))
        self.nodes[161].agregar_salida(self.nodes[336], random.randint(1,10))
        self.nodes[163].agregar_salida(self.nodes[337], random.randint(1,10))
        self.nodes[164].agregar_salida(self.nodes[338], random.randint(1,10))
        self.nodes[165].agregar_salida(self.nodes[339], random.randint(1,10))
        self.nodes[166].agregar_salida(self.nodes[340], random.randint(1,10))
        self.nodes[167].agregar_salida(self.nodes[341], random.randint(1,10))
        self.nodes[342].agregar_salida(self.nodes[168], random.randint(1,10))
        self.nodes[486].agregar_salida(self.nodes[169], random.randint(1,10))
        self.nodes[416].agregar_salida(self.nodes[486], random.randint(1,10))
        self.nodes[342].agregar_salida(self.nodes[415], random.randint(1,10))

        self.nodes[380].agregar_salida(self.nodes[377], random.randint(1,10))
        self.nodes[377].agregar_salida(self.nodes[380], random.randint(1,10))

        self.nodes[381].agregar_salida(self.nodes[376], random.randint(1,10))
        self.nodes[376].agregar_salida(self.nodes[381], random.randint(1,10))

        self.nodes[381].agregar_salida(self.nodes[450], random.randint(1,10))
        self.nodes[450].agregar_salida(self.nodes[381], random.randint(1,10))

        self.nodes[382].agregar_salida(self.nodes[375], random.randint(1,10))
        self.nodes[375].agregar_salida(self.nodes[382], random.randint(1,10))

        self.nodes[383].agregar_salida(self.nodes[449], random.randint(1,10))
        self.nodes[449].agregar_salida(self.nodes[383], random.randint(1,10))
        self.nodes[383].agregar_salida(self.nodes[374], random.randint(1,10))
        self.nodes[374].agregar_salida(self.nodes[383], random.randint(1,10))

        self.nodes[384].agregar_salida(self.nodes[448], random.randint(1,10))
        self.nodes[448].agregar_salida(self.nodes[384], random.randint(1,10))
        self.nodes[384].agregar_salida(self.nodes[373], random.randint(1,10))
        self.nodes[373].agregar_salida(self.nodes[384], random.randint(1,10))

        self.nodes[385].agregar_salida(self.nodes[372], random.randint(1,10))
        self.nodes[372].agregar_salida(self.nodes[385], random.randint(1,10))

        self.nodes[386].agregar_salida(self.nodes[447], random.randint(1,10))
        self.nodes[447].agregar_salida(self.nodes[386], random.randint(1,10))

        self.nodes[387].agregar_salida(self.nodes[371], random.randint(1,10))
        self.nodes[371].agregar_salida(self.nodes[387], random.randint(1,10))
        self.nodes[387].agregar_salida(self.nodes[446], random.randint(1,10))
        self.nodes[446].agregar_salida(self.nodes[387], random.randint(1,10))

        self.nodes[388].agregar_salida(self.nodes[444], random.randint(1,10))
        self.nodes[444].agregar_salida(self.nodes[388], random.randint(1,10))
        self.nodes[388].agregar_salida(self.nodes[370], random.randint(1,10))
        self.nodes[370].agregar_salida(self.nodes[388], random.randint(1,10))

        self.nodes[389].agregar_salida(self.nodes[369], random.randint(1,10))
        self.nodes[369].agregar_salida(self.nodes[389], random.randint(1,10))
        self.nodes[389].agregar_salida(self.nodes[443], random.randint(1,10))
        self.nodes[443].agregar_salida(self.nodes[389], random.randint(1,10))

        self.nodes[390].agregar_salida(self.nodes[442], random.randint(1,10))
        self.nodes[442].agregar_salida(self.nodes[390], random.randint(1,10))

        self.nodes[391].agregar_salida(self.nodes[368], random.randint(1,10))
        self.nodes[368].agregar_salida(self.nodes[391], random.randint(1,10))
        self.nodes[391].agregar_salida(self.nodes[441], random.randint(1,10))
        self.nodes[441].agregar_salida(self.nodes[391], random.randint(1,10))

        self.nodes[392].agregar_salida(self.nodes[367], random.randint(1,10))
        self.nodes[367].agregar_salida(self.nodes[392], random.randint(1,10))
        self.nodes[392].agregar_salida(self.nodes[440], random.randint(1,10))
        self.nodes[440].agregar_salida(self.nodes[392], random.randint(1,10))
        
        self.nodes[393].agregar_salida(self.nodes[439], random.randint(1,10))
        self.nodes[439].agregar_salida(self.nodes[393], random.randint(1,10))
        self.nodes[393].agregar_salida(self.nodes[366], random.randint(1,10))
        self.nodes[366].agregar_salida(self.nodes[393], random.randint(1,10))

        self.nodes[394].agregar_salida(self.nodes[438], random.randint(1,10))
        self.nodes[438].agregar_salida(self.nodes[394], random.randint(1,10))
        self.nodes[394].agregar_salida(self.nodes[365], random.randint(1,10))
        self.nodes[365].agregar_salida(self.nodes[394], random.randint(1,10))

        self.nodes[395].agregar_salida(self.nodes[437], random.randint(1,10))
        self.nodes[437].agregar_salida(self.nodes[395], random.randint(1,10))
        self.nodes[395].agregar_salida(self.nodes[364], random.randint(1,10))
        self.nodes[364].agregar_salida(self.nodes[395], random.randint(1,10))

        self.nodes[396].agregar_salida(self.nodes[363], random.randint(1,10))
        self.nodes[363].agregar_salida(self.nodes[396], random.randint(1,10))
        self.nodes[396].agregar_salida(self.nodes[436], random.randint(1,10))
        self.nodes[436].agregar_salida(self.nodes[396], random.randint(1,10))

        self.nodes[398].agregar_salida(self.nodes[362], random.randint(1,10))
        self.nodes[362].agregar_salida(self.nodes[398], random.randint(1,10))
        self.nodes[398].agregar_salida(self.nodes[435], random.randint(1,10))
        self.nodes[435].agregar_salida(self.nodes[398], random.randint(1,10))

        self.nodes[399].agregar_salida(self.nodes[434], random.randint(1,10))
        self.nodes[434].agregar_salida(self.nodes[399], random.randint(1,10))

        self.nodes[400].agregar_salida(self.nodes[360], random.randint(1,10))
        self.nodes[360].agregar_salida(self.nodes[400], random.randint(1,10))
        self.nodes[400].agregar_salida(self.nodes[433], random.randint(1,10))
        self.nodes[433].agregar_salida(self.nodes[400], random.randint(1,10))

        self.nodes[401].agregar_salida(self.nodes[432], random.randint(1,10))
        self.nodes[432].agregar_salida(self.nodes[401], random.randint(1,10))
        self.nodes[401].agregar_salida(self.nodes[359], random.randint(1,10))
        self.nodes[359].agregar_salida(self.nodes[401], random.randint(1,10))

        self.nodes[402].agregar_salida(self.nodes[358], random.randint(1,10))
        self.nodes[358].agregar_salida(self.nodes[402], random.randint(1,10))
        self.nodes[402].agregar_salida(self.nodes[431], random.randint(1,10))
        self.nodes[431].agregar_salida(self.nodes[402], random.randint(1,10))

        self.nodes[357].agregar_salida(self.nodes[430], random.randint(1,10))
        self.nodes[430].agregar_salida(self.nodes[357], random.randint(1,10))

        self.nodes[403].agregar_salida(self.nodes[356], random.randint(1,10))
        self.nodes[356].agregar_salida(self.nodes[403], random.randint(1,10))
        self.nodes[403].agregar_salida(self.nodes[429], random.randint(1,10))
        self.nodes[429].agregar_salida(self.nodes[403], random.randint(1,10))

        self.nodes[404].agregar_salida(self.nodes[428], random.randint(1,10))
        self.nodes[428].agregar_salida(self.nodes[404], random.randint(1,10))
        self.nodes[404].agregar_salida(self.nodes[355], random.randint(1,10))
        self.nodes[355].agregar_salida(self.nodes[404], random.randint(1,10))

        self.nodes[405].agregar_salida(self.nodes[427], random.randint(1,10))
        self.nodes[427].agregar_salida(self.nodes[405], random.randint(1,10))
        self.nodes[405].agregar_salida(self.nodes[354], random.randint(1,10))
        self.nodes[354].agregar_salida(self.nodes[405], random.randint(1,10))

        self.nodes[406].agregar_salida(self.nodes[353], random.randint(1,10))
        self.nodes[353].agregar_salida(self.nodes[406], random.randint(1,10))
        self.nodes[406].agregar_salida(self.nodes[426], random.randint(1,10))
        self.nodes[426].agregar_salida(self.nodes[406], random.randint(1,10))

        self.nodes[407].agregar_salida(self.nodes[425], random.randint(1,10))
        self.nodes[425].agregar_salida(self.nodes[407], random.randint(1,10))
        self.nodes[407].agregar_salida(self.nodes[352], random.randint(1,10))
        self.nodes[352].agregar_salida(self.nodes[407], random.randint(1,10))

        self.nodes[408].agregar_salida(self.nodes[424], random.randint(1,10))
        self.nodes[424].agregar_salida(self.nodes[408], random.randint(1,10))
        self.nodes[408].agregar_salida(self.nodes[351], random.randint(1,10))
        self.nodes[351].agregar_salida(self.nodes[408], random.randint(1,10))

        self.nodes[350].agregar_salida(self.nodes[423], random.randint(1,10))
        self.nodes[423].agregar_salida(self.nodes[350], random.randint(1,10))

        self.nodes[409].agregar_salida(self.nodes[349], random.randint(1,10))
        self.nodes[349].agregar_salida(self.nodes[409], random.randint(1,10))
        self.nodes[409].agregar_salida(self.nodes[422], random.randint(1,10))
        self.nodes[422].agregar_salida(self.nodes[409], random.randint(1,10))

        self.nodes[410].agregar_salida(self.nodes[421], random.randint(1,10))
        self.nodes[421].agregar_salida(self.nodes[410], random.randint(1,10))
        self.nodes[410].agregar_salida(self.nodes[348], random.randint(1,10))
        self.nodes[348].agregar_salida(self.nodes[410], random.randint(1,10))

        self.nodes[411].agregar_salida(self.nodes[420], random.randint(1,10))
        self.nodes[420].agregar_salida(self.nodes[411], random.randint(1,10))
        self.nodes[411].agregar_salida(self.nodes[347], random.randint(1,10))
        self.nodes[347].agregar_salida(self.nodes[411], random.randint(1,10))

        self.nodes[412].agregar_salida(self.nodes[419], random.randint(1,10))
        self.nodes[419].agregar_salida(self.nodes[412], random.randint(1,10))
        self.nodes[412].agregar_salida(self.nodes[346], random.randint(1,10))
        self.nodes[346].agregar_salida(self.nodes[412], random.randint(1,10))

        self.nodes[413].agregar_salida(self.nodes[418], random.randint(1,10))
        self.nodes[418].agregar_salida(self.nodes[413], random.randint(1,10))
        self.nodes[413].agregar_salida(self.nodes[345], random.randint(1,10))
        self.nodes[345].agregar_salida(self.nodes[413], random.randint(1,10))

        self.nodes[414].agregar_salida(self.nodes[344], random.randint(1,10))
        self.nodes[344].agregar_salida(self.nodes[414], random.randint(1,10))
        self.nodes[414].agregar_salida(self.nodes[417], random.randint(1,10))
        self.nodes[417].agregar_salida(self.nodes[414], random.randint(1,10))

        self.nodes[417].agregar_salida(self.nodes[485], random.randint(1,10))
        self.nodes[485].agregar_salida(self.nodes[417], random.randint(1,10))

        self.nodes[418].agregar_salida(self.nodes[484], random.randint(1,10))
        self.nodes[484].agregar_salida(self.nodes[418], random.randint(1,10))

        self.nodes[421].agregar_salida(self.nodes[482], random.randint(1,10))
        self.nodes[482].agregar_salida(self.nodes[421], random.randint(1,10))

        self.nodes[422].agregar_salida(self.nodes[481], random.randint(1,10))
        self.nodes[481].agregar_salida(self.nodes[422], random.randint(1,10))

        self.nodes[423].agregar_salida(self.nodes[480], random.randint(1,10))
        self.nodes[480].agregar_salida(self.nodes[423], random.randint(1,10))

        self.nodes[424].agregar_salida(self.nodes[479], random.randint(1,10))
        self.nodes[479].agregar_salida(self.nodes[424], random.randint(1,10))

        self.nodes[425].agregar_salida(self.nodes[478], random.randint(1,10))
        self.nodes[478].agregar_salida(self.nodes[425], random.randint(1,10))

        self.nodes[426].agregar_salida(self.nodes[475], random.randint(1,10))
        self.nodes[475].agregar_salida(self.nodes[426], random.randint(1,10))
        self.nodes[475].agregar_salida(self.nodes[473], random.randint(1,10))
        self.nodes[473].agregar_salida(self.nodes[475], random.randint(1,10))

        self.nodes[427].agregar_salida(self.nodes[473], random.randint(1,10))
        self.nodes[473].agregar_salida(self.nodes[427], random.randint(1,10))
        self.nodes[473].agregar_salida(self.nodes[471], random.randint(1,10))
        self.nodes[471].agregar_salida(self.nodes[473], random.randint(1,10))

        self.nodes[428].agregar_salida(self.nodes[471], random.randint(1,10))
        self.nodes[471].agregar_salida(self.nodes[428], random.randint(1,10))
        self.nodes[471].agregar_salida(self.nodes[469], random.randint(1,10))
        self.nodes[469].agregar_salida(self.nodes[471], random.randint(1,10))

        self.nodes[429].agregar_salida(self.nodes[469], random.randint(1,10))
        self.nodes[469].agregar_salida(self.nodes[429], random.randint(1,10))
        self.nodes[469].agregar_salida(self.nodes[467], random.randint(1,10))
        self.nodes[467].agregar_salida(self.nodes[469], random.randint(1,10))

        self.nodes[430].agregar_salida(self.nodes[467], random.randint(1,10))
        self.nodes[467].agregar_salida(self.nodes[430], random.randint(1,10))

        self.nodes[476].agregar_salida(self.nodes[474], random.randint(1,10))
        self.nodes[474].agregar_salida(self.nodes[476], random.randint(1,10))
        self.nodes[474].agregar_salida(self.nodes[472], random.randint(1,10))
        self.nodes[472].agregar_salida(self.nodes[474], random.randint(1,10))
        self.nodes[472].agregar_salida(self.nodes[470], random.randint(1,10))
        self.nodes[470].agregar_salida(self.nodes[472], random.randint(1,10))
        self.nodes[470].agregar_salida(self.nodes[468], random.randint(1,10))
        self.nodes[468].agregar_salida(self.nodes[470], random.randint(1,10))

        self.nodes[432].agregar_salida(self.nodes[465], random.randint(1,10))
        self.nodes[465].agregar_salida(self.nodes[432], random.randint(1,10))

        self.nodes[433].agregar_salida(self.nodes[464], random.randint(1,10))
        self.nodes[464].agregar_salida(self.nodes[433], random.randint(1,10))

        self.nodes[434].agregar_salida(self.nodes[463], random.randint(1,10))
        self.nodes[463].agregar_salida(self.nodes[434], random.randint(1,10))

        self.nodes[435].agregar_salida(self.nodes[462], random.randint(1,10))
        self.nodes[462].agregar_salida(self.nodes[435], random.randint(1,10))

        self.nodes[436].agregar_salida(self.nodes[461], random.randint(1,10))
        self.nodes[461].agregar_salida(self.nodes[436], random.randint(1,10))

        self.nodes[437].agregar_salida(self.nodes[460], random.randint(1,10))
        self.nodes[460].agregar_salida(self.nodes[437], random.randint(1,10))

        self.nodes[438].agregar_salida(self.nodes[459], random.randint(1,10))
        self.nodes[459].agregar_salida(self.nodes[438], random.randint(1,10))

        self.nodes[441].agregar_salida(self.nodes[457], random.randint(1,10))
        self.nodes[457].agregar_salida(self.nodes[441], random.randint(1,10))

        self.nodes[443].agregar_salida(self.nodes[455], random.randint(1,10))
        self.nodes[455].agregar_salida(self.nodes[443], random.randint(1,10))

        self.nodes[444].agregar_salida(self.nodes[454], random.randint(1,10))
        self.nodes[454].agregar_salida(self.nodes[444], random.randint(1,10))

        self.nodes[445].agregar_salida(self.nodes[453], random.randint(1,10))
        self.nodes[453].agregar_salida(self.nodes[445], random.randint(1,10))

        self.nodes[448].agregar_salida(self.nodes[451], random.randint(1,10))