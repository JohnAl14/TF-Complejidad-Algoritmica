import heapq  

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

    def cargar_conecciones(self, rand):
       
        for i in range(1013):
            if i!=168:
                self.nodes[i].agregar_salida(self.nodes[i+1],rand)

        for i in range(1000, 0, -1):
            if i!=169:
                self.nodes[i].agregar_salida(self.nodes[i-1],rand)


        self.nodes[0].agregar_salida(self.nodes[486], rand)
        self.nodes[0].agregar_salida(self.nodes[487], rand)

        self.nodes[486].agregar_salida(self.nodes[0], rand)
        self.nodes[487].agregar_salida(self.nodes[0], rand)

        self.nodes[1].agregar_salida(self.nodes[169], rand)
        self.nodes[1].agregar_salida(self.nodes[488], rand)

        self.nodes[2].agregar_salida(self.nodes[170], rand)
        self.nodes[2].agregar_salida(self.nodes[489], rand)

        self.nodes[3].agregar_salida(self.nodes[171], rand)
        self.nodes[31].agregar_salida(self.nodes[585], rand)

        self.nodes[4].agregar_salida(self.nodes[172], rand)
        self.nodes[4].agregar_salida(self.nodes[491], rand)

        self.nodes[5].agregar_salida(self.nodes[173], rand)

        self.nodes[6].agregar_salida(self.nodes[174], rand)
        self.nodes[6].agregar_salida(self.nodes[493], rand)

        self.nodes[7].agregar_salida(self.nodes[175], rand)
        
        self.nodes[8].agregar_salida(self.nodes[177], rand)
        self.nodes[8].agregar_salida(self.nodes[495], rand)

        self.nodes[9].agregar_salida(self.nodes[178], rand)
        
        self.nodes[10].agregar_salida(self.nodes[498], rand)

        self.nodes[11].agregar_salida(self.nodes[179], rand)
        self.nodes[11].agregar_salida(self.nodes[499], rand)

        self.nodes[12].agregar_salida(self.nodes[180], rand)
        self.nodes[12].agregar_salida(self.nodes[500], rand)

        self.nodes[13].agregar_salida(self.nodes[181], rand)
        self.nodes[13].agregar_salida(self.nodes[501], rand)

        self.nodes[14].agregar_salida(self.nodes[182], rand)
        self.nodes[14].agregar_salida(self.nodes[502], rand)

        self.nodes[15].agregar_salida(self.nodes[183], rand)
        self.nodes[15].agregar_salida(self.nodes[503], rand)

        self.nodes[16].agregar_salida(self.nodes[504], rand)

        self.nodes[17].agregar_salida(self.nodes[184], rand)
        self.nodes[17].agregar_salida(self.nodes[506], rand)

        self.nodes[18].agregar_salida(self.nodes[185], rand)
        self.nodes[18].agregar_salida(self.nodes[507], rand)

        self.nodes[19].agregar_salida(self.nodes[186], rand)
        self.nodes[19].agregar_salida(self.nodes[508], rand)

        self.nodes[20].agregar_salida(self.nodes[187], rand)
        self.nodes[20].agregar_salida(self.nodes[509], rand)

        self.nodes[21].agregar_salida(self.nodes[188], rand)
        self.nodes[21].agregar_salida(self.nodes[510], rand)

        self.nodes[22].agregar_salida(self.nodes[189], rand)
        self.nodes[22].agregar_salida(self.nodes[511], rand)

        self.nodes[23].agregar_salida(self.nodes[191], rand)
        self.nodes[23].agregar_salida(self.nodes[512], rand)

        self.nodes[24].agregar_salida(self.nodes[192], rand)
        self.nodes[24].agregar_salida(self.nodes[513], rand)

        self.nodes[25].agregar_salida(self.nodes[193], rand)
        self.nodes[25].agregar_salida(self.nodes[514], rand)

        self.nodes[26].agregar_salida(self.nodes[194], rand)
        self.nodes[26].agregar_salida(self.nodes[515], rand)

        self.nodes[27].agregar_salida(self.nodes[195], rand)
        self.nodes[27].agregar_salida(self.nodes[516], rand)

        self.nodes[28].agregar_salida(self.nodes[197], rand)
        self.nodes[28].agregar_salida(self.nodes[517], rand)

        self.nodes[29].agregar_salida(self.nodes[198], rand)
        self.nodes[29].agregar_salida(self.nodes[518], rand)

        self.nodes[30].agregar_salida(self.nodes[199], rand)
        self.nodes[30].agregar_salida(self.nodes[519], rand)

        self.nodes[31].agregar_salida(self.nodes[200], rand)
        

        self.nodes[32].agregar_salida(self.nodes[201], rand)
        self.nodes[32].agregar_salida(self.nodes[520], rand)
        
        self.nodes[33].agregar_salida(self.nodes[202], rand)
        self.nodes[33].agregar_salida(self.nodes[521], rand)

        self.nodes[34].agregar_salida(self.nodes[203], rand)
        self.nodes[34].agregar_salida(self.nodes[522], rand)

        self.nodes[35].agregar_salida(self.nodes[204], rand)
        self.nodes[35].agregar_salida(self.nodes[523], rand)

        self.nodes[36].agregar_salida(self.nodes[205], rand)
        self.nodes[36].agregar_salida(self.nodes[524], rand)

        self.nodes[37].agregar_salida(self.nodes[206], rand)
        self.nodes[37].agregar_salida(self.nodes[525], rand)

        self.nodes[38].agregar_salida(self.nodes[207], rand)
        self.nodes[38].agregar_salida(self.nodes[526], rand)

        self.nodes[39].agregar_salida(self.nodes[208], rand)
        self.nodes[39].agregar_salida(self.nodes[527], rand)

        self.nodes[40].agregar_salida(self.nodes[209], rand)
        self.nodes[40].agregar_salida(self.nodes[528], rand)

        self.nodes[41].agregar_salida(self.nodes[210], rand)
        self.nodes[41].agregar_salida(self.nodes[529], rand)

        self.nodes[42].agregar_salida(self.nodes[211], rand)
        self.nodes[42].agregar_salida(self.nodes[530], rand)

        self.nodes[43].agregar_salida(self.nodes[212], rand)
        self.nodes[43].agregar_salida(self.nodes[531], rand)

        self.nodes[44].agregar_salida(self.nodes[213], rand)
        self.nodes[44].agregar_salida(self.nodes[532], rand)

        self.nodes[45].agregar_salida(self.nodes[214], rand)
        self.nodes[45].agregar_salida(self.nodes[533], rand)

        self.nodes[46].agregar_salida(self.nodes[215], rand)
        self.nodes[46].agregar_salida(self.nodes[534], rand)

        self.nodes[47].agregar_salida(self.nodes[216], rand)
        self.nodes[47].agregar_salida(self.nodes[535], rand)

        self.nodes[48].agregar_salida(self.nodes[218], rand)
        self.nodes[48].agregar_salida(self.nodes[538], rand)

        self.nodes[217].agregar_salida(self.nodes[536], rand)

        self.nodes[49].agregar_salida(self.nodes[219], rand)
        self.nodes[49].agregar_salida(self.nodes[539], rand)

        self.nodes[50].agregar_salida(self.nodes[220], rand)
        self.nodes[50].agregar_salida(self.nodes[540], rand)

        self.nodes[51].agregar_salida(self.nodes[221], rand)
        self.nodes[51].agregar_salida(self.nodes[541], rand)

        self.nodes[52].agregar_salida(self.nodes[222], rand)
        self.nodes[52].agregar_salida(self.nodes[542], rand)

        self.nodes[53].agregar_salida(self.nodes[223], rand)
        self.nodes[53].agregar_salida(self.nodes[543], rand)

        self.nodes[54].agregar_salida(self.nodes[224], rand)
        self.nodes[54].agregar_salida(self.nodes[544], rand)

        self.nodes[55].agregar_salida(self.nodes[225], rand)
        self.nodes[55].agregar_salida(self.nodes[545], rand)

        self.nodes[56].agregar_salida(self.nodes[226], rand)
        self.nodes[56].agregar_salida(self.nodes[546], rand)

        self.nodes[57].agregar_salida(self.nodes[227], rand)
        self.nodes[57].agregar_salida(self.nodes[547], rand)

        self.nodes[58].agregar_salida(self.nodes[228], rand)
        self.nodes[58].agregar_salida(self.nodes[548], rand)

        self.nodes[59].agregar_salida(self.nodes[229], rand)
        self.nodes[59].agregar_salida(self.nodes[549], rand)

        self.nodes[61].agregar_salida(self.nodes[230], rand)
        self.nodes[61].agregar_salida(self.nodes[550], rand)

        self.nodes[62].agregar_salida(self.nodes[231], rand)
        self.nodes[62].agregar_salida(self.nodes[551], rand)

        self.nodes[63].agregar_salida(self.nodes[232], rand)
        self.nodes[63].agregar_salida(self.nodes[857], rand)

        self.nodes[857].agregar_salida(self.nodes[858], rand)

        self.nodes[64].agregar_salida(self.nodes[233], rand)
        self.nodes[64].agregar_salida(self.nodes[856], rand)

        self.nodes[65].agregar_salida(self.nodes[234], rand)
        self.nodes[65].agregar_salida(self.nodes[855], rand)

        self.nodes[235].agregar_salida(self.nodes[854], rand)

        self.nodes[66].agregar_salida(self.nodes[236], rand)
        self.nodes[66].agregar_salida(self.nodes[853], rand)
        self.nodes[853].agregar_salida(self.nodes[852], rand)

        self.nodes[68].agregar_salida(self.nodes[238], rand)
        self.nodes[68].agregar_salida(self.nodes[851], rand)

        self.nodes[69].agregar_salida(self.nodes[239], rand)
        self.nodes[69].agregar_salida(self.nodes[850], rand)

        self.nodes[70].agregar_salida(self.nodes[240], rand)
        self.nodes[70].agregar_salida(self.nodes[849], rand)

        self.nodes[71].agregar_salida(self.nodes[241], rand)
        self.nodes[71].agregar_salida(self.nodes[848], rand)

        self.nodes[72].agregar_salida(self.nodes[242], rand)
        self.nodes[72].agregar_salida(self.nodes[847], rand)

        self.nodes[73].agregar_salida(self.nodes[243], rand)
        self.nodes[73].agregar_salida(self.nodes[846], rand)

        self.nodes[74].agregar_salida(self.nodes[244], rand)
        self.nodes[74].agregar_salida(self.nodes[845], rand)

        self.nodes[78].agregar_salida(self.nodes[245], rand)
        self.nodes[78].agregar_salida(self.nodes[844], rand)

        self.nodes[79].agregar_salida(self.nodes[247], rand)
        self.nodes[79].agregar_salida(self.nodes[843], rand)

        self.nodes[80].agregar_salida(self.nodes[248], rand)
        self.nodes[80].agregar_salida(self.nodes[842], rand)

        self.nodes[81].agregar_salida(self.nodes[250], rand)
        self.nodes[81].agregar_salida(self.nodes[841], rand)

        self.nodes[82].agregar_salida(self.nodes[251], rand)
        self.nodes[82].agregar_salida(self.nodes[840], rand)

        self.nodes[83].agregar_salida(self.nodes[839], rand)

        self.nodes[84].agregar_salida(self.nodes[253], rand)
        self.nodes[84].agregar_salida(self.nodes[838], rand)

        self.nodes[85].agregar_salida(self.nodes[254], rand)
        self.nodes[85].agregar_salida(self.nodes[837], rand)

        self.nodes[86].agregar_salida(self.nodes[255], rand)
        self.nodes[86].agregar_salida(self.nodes[836], rand)

        self.nodes[87].agregar_salida(self.nodes[835], rand)
        
        self.nodes[88].agregar_salida(self.nodes[834], rand)

        self.nodes[89].agregar_salida(self.nodes[833], rand)

        self.nodes[90].agregar_salida(self.nodes[257], rand)

        self.nodes[617].agregar_salida(self.nodes[487], rand)

        self.nodes[616].agregar_salida(self.nodes[488], rand)
        self.nodes[616].agregar_salida(self.nodes[619], rand)

        self.nodes[615].agregar_salida(self.nodes[489], rand)
        self.nodes[615].agregar_salida(self.nodes[620], rand)

        self.nodes[614].agregar_salida(self.nodes[621], rand)
        self.nodes[614].agregar_salida(self.nodes[490], rand)

        self.nodes[613].agregar_salida(self.nodes[622], rand)
        self.nodes[613].agregar_salida(self.nodes[491], rand)

        self.nodes[612].agregar_salida(self.nodes[624], rand)
        self.nodes[612].agregar_salida(self.nodes[492], rand)

        self.nodes[611].agregar_salida(self.nodes[625], rand)
        self.nodes[611].agregar_salida(self.nodes[493], rand)

        self.nodes[610].agregar_salida(self.nodes[626], rand)
        self.nodes[610].agregar_salida(self.nodes[494], rand)

        self.nodes[609].agregar_salida(self.nodes[627], rand)
        self.nodes[609].agregar_salida(self.nodes[495], rand)

        self.nodes[608].agregar_salida(self.nodes[628], rand)
        self.nodes[608].agregar_salida(self.nodes[496], rand)

        self.nodes[607].agregar_salida(self.nodes[629], rand)
        self.nodes[607].agregar_salida(self.nodes[497], rand)

        self.nodes[606].agregar_salida(self.nodes[630], rand)
        self.nodes[606].agregar_salida(self.nodes[498], rand)

        self.nodes[605].agregar_salida(self.nodes[632], rand)
        self.nodes[605].agregar_salida(self.nodes[499], rand)

        self.nodes[604].agregar_salida(self.nodes[633], rand)
        self.nodes[604].agregar_salida(self.nodes[500], rand)

        self.nodes[603].agregar_salida(self.nodes[634], rand)
        self.nodes[603].agregar_salida(self.nodes[501], rand)

        self.nodes[602].agregar_salida(self.nodes[635], rand)
        self.nodes[602].agregar_salida(self.nodes[502], rand)

        self.nodes[601].agregar_salida(self.nodes[636], rand)
        self.nodes[601].agregar_salida(self.nodes[503], rand)

        self.nodes[600].agregar_salida(self.nodes[637], rand)
        self.nodes[600].agregar_salida(self.nodes[504], rand)

        self.nodes[599].agregar_salida(self.nodes[638], rand)
        self.nodes[599].agregar_salida(self.nodes[506], rand)

        self.nodes[598].agregar_salida(self.nodes[639], rand)
        self.nodes[598].agregar_salida(self.nodes[507], rand)

        self.nodes[597].agregar_salida(self.nodes[641], rand)
        self.nodes[597].agregar_salida(self.nodes[508], rand)

        self.nodes[596].agregar_salida(self.nodes[642], rand)
        self.nodes[596].agregar_salida(self.nodes[509], rand)

        self.nodes[595].agregar_salida(self.nodes[643], rand)
        self.nodes[595].agregar_salida(self.nodes[510], rand)

        self.nodes[594].agregar_salida(self.nodes[644], rand)
        self.nodes[594].agregar_salida(self.nodes[511], rand)

        self.nodes[593].agregar_salida(self.nodes[645], rand)
        self.nodes[593].agregar_salida(self.nodes[512], rand)

        self.nodes[592].agregar_salida(self.nodes[646], rand)
        self.nodes[592].agregar_salida(self.nodes[513], rand)

        self.nodes[591].agregar_salida(self.nodes[647], rand)
        self.nodes[591].agregar_salida(self.nodes[514], rand)

        self.nodes[590].agregar_salida(self.nodes[648], rand)
        self.nodes[590].agregar_salida(self.nodes[515], rand)

        self.nodes[589].agregar_salida(self.nodes[649], rand)
        self.nodes[589].agregar_salida(self.nodes[516], rand)

        self.nodes[588].agregar_salida(self.nodes[650], rand)
        self.nodes[588].agregar_salida(self.nodes[517], rand)

        self.nodes[587].agregar_salida(self.nodes[651], rand)
        self.nodes[587].agregar_salida(self.nodes[518], rand)

        self.nodes[586].agregar_salida(self.nodes[653], rand)
        self.nodes[586].agregar_salida(self.nodes[519], rand)

        self.nodes[585].agregar_salida(self.nodes[654], rand)

        self.nodes[584].agregar_salida(self.nodes[655], rand)
        self.nodes[584].agregar_salida(self.nodes[520], rand)

        self.nodes[583].agregar_salida(self.nodes[656], rand)
        self.nodes[583].agregar_salida(self.nodes[521], rand)

        self.nodes[582].agregar_salida(self.nodes[657], rand)
        self.nodes[582].agregar_salida(self.nodes[522], rand)

        self.nodes[581].agregar_salida(self.nodes[658], rand)
        self.nodes[581].agregar_salida(self.nodes[523], rand)

        self.nodes[580].agregar_salida(self.nodes[659], rand)
        self.nodes[580].agregar_salida(self.nodes[524], rand)

        self.nodes[579].agregar_salida(self.nodes[660], rand)
        self.nodes[579].agregar_salida(self.nodes[525], rand)

        self.nodes[578].agregar_salida(self.nodes[661], rand)
        self.nodes[578].agregar_salida(self.nodes[526], rand)

        self.nodes[577].agregar_salida(self.nodes[662], rand)
        self.nodes[577].agregar_salida(self.nodes[527], rand)

        self.nodes[576].agregar_salida(self.nodes[663], rand)
        self.nodes[576].agregar_salida(self.nodes[528], rand)

        self.nodes[575].agregar_salida(self.nodes[664], rand)
        self.nodes[575].agregar_salida(self.nodes[529], rand)

        self.nodes[574].agregar_salida(self.nodes[665], rand)
        self.nodes[574].agregar_salida(self.nodes[530], rand)

        self.nodes[573].agregar_salida(self.nodes[666], rand)
        self.nodes[573].agregar_salida(self.nodes[531], rand)

        self.nodes[572].agregar_salida(self.nodes[667], rand)
        self.nodes[572].agregar_salida(self.nodes[532], rand)

        self.nodes[571].agregar_salida(self.nodes[668], rand)
        self.nodes[571].agregar_salida(self.nodes[533], rand)

        self.nodes[570].agregar_salida(self.nodes[669], rand)
        self.nodes[570].agregar_salida(self.nodes[534], rand)

        self.nodes[569].agregar_salida(self.nodes[670], rand)
        self.nodes[569].agregar_salida(self.nodes[535], rand)

        self.nodes[568].agregar_salida(self.nodes[671], rand)
        self.nodes[568].agregar_salida(self.nodes[536], rand)

        self.nodes[567].agregar_salida(self.nodes[672], rand)
        self.nodes[567].agregar_salida(self.nodes[538], rand)

        self.nodes[566].agregar_salida(self.nodes[673], rand)
        self.nodes[566].agregar_salida(self.nodes[539], rand)

        self.nodes[565].agregar_salida(self.nodes[674], rand)
        self.nodes[565].agregar_salida(self.nodes[540], rand)

        self.nodes[564].agregar_salida(self.nodes[675], rand)
        self.nodes[564].agregar_salida(self.nodes[541], rand)

        self.nodes[563].agregar_salida(self.nodes[676], rand)
        self.nodes[563].agregar_salida(self.nodes[542], rand)

        self.nodes[562].agregar_salida(self.nodes[677], rand)
        self.nodes[562].agregar_salida(self.nodes[543], rand)

        self.nodes[561].agregar_salida(self.nodes[678], rand)
        self.nodes[561].agregar_salida(self.nodes[544], rand)

        self.nodes[560].agregar_salida(self.nodes[679], rand)
        self.nodes[560].agregar_salida(self.nodes[545], rand)

        self.nodes[559].agregar_salida(self.nodes[680], rand)
        self.nodes[559].agregar_salida(self.nodes[546], rand)

        self.nodes[558].agregar_salida(self.nodes[681], rand)
        self.nodes[558].agregar_salida(self.nodes[547], rand)

        self.nodes[557].agregar_salida(self.nodes[682], rand)
        self.nodes[557].agregar_salida(self.nodes[548], rand)

        self.nodes[556].agregar_salida(self.nodes[683], rand)
        self.nodes[556].agregar_salida(self.nodes[549], rand)

        self.nodes[555].agregar_salida(self.nodes[684], rand)
        self.nodes[555].agregar_salida(self.nodes[550], rand)

        self.nodes[554].agregar_salida(self.nodes[685], rand)
        self.nodes[554].agregar_salida(self.nodes[551], rand)

        self.nodes[553].agregar_salida(self.nodes[686], rand)

        self.nodes[748].agregar_salida(self.nodes[618], rand)

        self.nodes[747].agregar_salida(self.nodes[619], rand)
        self.nodes[747].agregar_salida(self.nodes[750], rand)

        self.nodes[746].agregar_salida(self.nodes[751], rand)

        self.nodes[745].agregar_salida(self.nodes[623], rand)
        self.nodes[745].agregar_salida(self.nodes[753], rand)

        self.nodes[744].agregar_salida(self.nodes[754], rand)
        self.nodes[744].agregar_salida(self.nodes[624], rand)

        self.nodes[743].agregar_salida(self.nodes[755], rand)
        self.nodes[743].agregar_salida(self.nodes[625], rand)

        self.nodes[742].agregar_salida(self.nodes[756], rand)

        self.nodes[741].agregar_salida(self.nodes[757], rand)
        self.nodes[741].agregar_salida(self.nodes[627], rand)

        self.nodes[740].agregar_salida(self.nodes[758], rand)

        self.nodes[739].agregar_salida(self.nodes[759], rand)

        self.nodes[738].agregar_salida(self.nodes[760], rand)
        self.nodes[738].agregar_salida(self.nodes[630], rand)

        self.nodes[737].agregar_salida(self.nodes[761], rand)
        self.nodes[737].agregar_salida(self.nodes[633], rand)

        self.nodes[736].agregar_salida(self.nodes[762], rand)
        self.nodes[736].agregar_salida(self.nodes[634], rand)

        self.nodes[735].agregar_salida(self.nodes[764], rand)
        self.nodes[735].agregar_salida(self.nodes[636], rand)

        self.nodes[734].agregar_salida(self.nodes[765], rand)
        self.nodes[734].agregar_salida(self.nodes[637], rand)

        self.nodes[763].agregar_salida(self.nodes[635], rand)

        self.nodes[733].agregar_salida(self.nodes[766], rand)
        self.nodes[733].agregar_salida(self.nodes[638], rand)

        self.nodes[732].agregar_salida(self.nodes[767], rand)
        self.nodes[732].agregar_salida(self.nodes[639], rand)

        self.nodes[731].agregar_salida(self.nodes[768], rand)
        self.nodes[731].agregar_salida(self.nodes[641], rand)

        self.nodes[730].agregar_salida(self.nodes[769], rand)
        self.nodes[730].agregar_salida(self.nodes[642], rand)

        self.nodes[729].agregar_salida(self.nodes[770], rand)
        self.nodes[729].agregar_salida(self.nodes[643], rand)

        self.nodes[728].agregar_salida(self.nodes[771], rand)
        self.nodes[728].agregar_salida(self.nodes[644], rand)

        self.nodes[727].agregar_salida(self.nodes[772], rand)
        self.nodes[727].agregar_salida(self.nodes[645], rand)

        self.nodes[726].agregar_salida(self.nodes[773], rand)
        self.nodes[726].agregar_salida(self.nodes[646], rand)

        self.nodes[725].agregar_salida(self.nodes[774], rand)
        self.nodes[725].agregar_salida(self.nodes[647], rand)

        self.nodes[724].agregar_salida(self.nodes[775], rand)
        self.nodes[724].agregar_salida(self.nodes[648], rand)

        self.nodes[723].agregar_salida(self.nodes[776], rand)
        self.nodes[723].agregar_salida(self.nodes[649], rand)

        self.nodes[722].agregar_salida(self.nodes[778], rand)
        self.nodes[722].agregar_salida(self.nodes[650], rand)

        self.nodes[721].agregar_salida(self.nodes[779], rand)
        self.nodes[721].agregar_salida(self.nodes[651], rand)

        self.nodes[720].agregar_salida(self.nodes[780], rand)
        self.nodes[720].agregar_salida(self.nodes[653], rand)

        self.nodes[719].agregar_salida(self.nodes[781], rand)
        self.nodes[719].agregar_salida(self.nodes[654], rand)

        self.nodes[718].agregar_salida(self.nodes[782], rand)
        self.nodes[718].agregar_salida(self.nodes[655], rand)

        self.nodes[717].agregar_salida(self.nodes[783], rand)
        self.nodes[717].agregar_salida(self.nodes[656], rand)

        self.nodes[716].agregar_salida(self.nodes[784], rand)
        self.nodes[716].agregar_salida(self.nodes[657], rand)

        self.nodes[715].agregar_salida(self.nodes[785], rand)
        self.nodes[715].agregar_salida(self.nodes[658], rand)

        self.nodes[714].agregar_salida(self.nodes[786], rand)
        self.nodes[714].agregar_salida(self.nodes[659], rand)

        self.nodes[713].agregar_salida(self.nodes[787], rand)
        self.nodes[713].agregar_salida(self.nodes[660], rand)

        self.nodes[712].agregar_salida(self.nodes[788], rand)
        self.nodes[712].agregar_salida(self.nodes[661], rand)

        self.nodes[711].agregar_salida(self.nodes[789], rand)
        self.nodes[711].agregar_salida(self.nodes[662], rand)

        self.nodes[710].agregar_salida(self.nodes[790], rand)
        self.nodes[710].agregar_salida(self.nodes[663], rand)

        self.nodes[709].agregar_salida(self.nodes[791], rand)
        self.nodes[709].agregar_salida(self.nodes[664], rand)

        self.nodes[708].agregar_salida(self.nodes[792], rand)
        self.nodes[708].agregar_salida(self.nodes[665], rand)

        self.nodes[707].agregar_salida(self.nodes[793], rand)
        self.nodes[707].agregar_salida(self.nodes[666], rand)

        self.nodes[706].agregar_salida(self.nodes[794], rand)
        self.nodes[706].agregar_salida(self.nodes[667], rand)

        self.nodes[705].agregar_salida(self.nodes[795], rand)
        self.nodes[705].agregar_salida(self.nodes[668], rand)

        self.nodes[704].agregar_salida(self.nodes[796], rand)
        self.nodes[704].agregar_salida(self.nodes[669], rand)

        self.nodes[703].agregar_salida(self.nodes[797], rand)
        self.nodes[703].agregar_salida(self.nodes[670], rand)

        self.nodes[702].agregar_salida(self.nodes[798], rand)
        self.nodes[702].agregar_salida(self.nodes[671], rand)

        self.nodes[701].agregar_salida(self.nodes[799], rand)
        self.nodes[701].agregar_salida(self.nodes[672], rand)

        self.nodes[700].agregar_salida(self.nodes[800], rand)
        self.nodes[700].agregar_salida(self.nodes[673], rand)

        self.nodes[699].agregar_salida(self.nodes[801], rand)
        self.nodes[699].agregar_salida(self.nodes[674], rand)

        self.nodes[698].agregar_salida(self.nodes[802], rand)
        self.nodes[698].agregar_salida(self.nodes[675], rand)

        self.nodes[697].agregar_salida(self.nodes[803], rand)
        self.nodes[697].agregar_salida(self.nodes[676], rand)

        self.nodes[696].agregar_salida(self.nodes[804], rand)
        self.nodes[696].agregar_salida(self.nodes[677], rand)

        self.nodes[695].agregar_salida(self.nodes[805], rand)
        self.nodes[695].agregar_salida(self.nodes[678], rand)

        self.nodes[694].agregar_salida(self.nodes[806], rand)
        self.nodes[694].agregar_salida(self.nodes[679], rand)

        self.nodes[693].agregar_salida(self.nodes[807], rand)
        self.nodes[693].agregar_salida(self.nodes[680], rand)

        self.nodes[692].agregar_salida(self.nodes[808], rand)
        self.nodes[692].agregar_salida(self.nodes[681], rand)

        self.nodes[691].agregar_salida(self.nodes[809], rand)
        self.nodes[691].agregar_salida(self.nodes[682], rand)

        self.nodes[690].agregar_salida(self.nodes[810], rand)
        self.nodes[690].agregar_salida(self.nodes[683], rand)

        self.nodes[689].agregar_salida(self.nodes[684], rand)

        self.nodes[688].agregar_salida(self.nodes[685], rand)

        self.nodes[687].agregar_salida(self.nodes[686], rand)
        self.nodes[687].agregar_salida(self.nodes[811], rand)

        self.nodes[885].agregar_salida(self.nodes[834], rand)
        self.nodes[885].agregar_salida(self.nodes[884], rand)

        self.nodes[886].agregar_salida(self.nodes[835], rand)
        self.nodes[886].agregar_salida(self.nodes[1006], rand)

        self.nodes[887].agregar_salida(self.nodes[836], rand)
        self.nodes[887].agregar_salida(self.nodes[1005], rand)

        self.nodes[888].agregar_salida(self.nodes[837], rand)
        self.nodes[888].agregar_salida(self.nodes[1004], rand)

        self.nodes[889].agregar_salida(self.nodes[838], rand)
        self.nodes[889].agregar_salida(self.nodes[1003], rand)

        self.nodes[890].agregar_salida(self.nodes[839], rand)
        self.nodes[890].agregar_salida(self.nodes[1002], rand)

        self.nodes[891].agregar_salida(self.nodes[840], rand)
        self.nodes[891].agregar_salida(self.nodes[1001], rand)

        self.nodes[892].agregar_salida(self.nodes[841], rand)
        self.nodes[892].agregar_salida(self.nodes[1000], rand)

        self.nodes[893].agregar_salida(self.nodes[842], rand)
        self.nodes[893].agregar_salida(self.nodes[999], rand)

        self.nodes[894].agregar_salida(self.nodes[843], rand)
        self.nodes[894].agregar_salida(self.nodes[998], rand)

        self.nodes[895].agregar_salida(self.nodes[844], rand)
        self.nodes[895].agregar_salida(self.nodes[997], rand)

        self.nodes[896].agregar_salida(self.nodes[845], rand)
        self.nodes[896].agregar_salida(self.nodes[996], rand)

        self.nodes[897].agregar_salida(self.nodes[846], rand)
        self.nodes[897].agregar_salida(self.nodes[995], rand)

        self.nodes[898].agregar_salida(self.nodes[847], rand)
        self.nodes[898].agregar_salida(self.nodes[994], rand)

        self.nodes[870].agregar_salida(self.nodes[994], rand)
        self.nodes[870].agregar_salida(self.nodes[819], rand)

        self.nodes[871].agregar_salida(self.nodes[995], rand)
        self.nodes[871].agregar_salida(self.nodes[820], rand)

        self.nodes[872].agregar_salida(self.nodes[996], rand)
        self.nodes[872].agregar_salida(self.nodes[821], rand)

        self.nodes[873].agregar_salida(self.nodes[997], rand)
        self.nodes[873].agregar_salida(self.nodes[822], rand)

        self.nodes[874].agregar_salida(self.nodes[998], rand)
        self.nodes[874].agregar_salida(self.nodes[823], rand)

        self.nodes[875].agregar_salida(self.nodes[999], rand)

        self.nodes[876].agregar_salida(self.nodes[1000], rand)

        self.nodes[877].agregar_salida(self.nodes[1001], rand)
        self.nodes[877].agregar_salida(self.nodes[824], rand)

        self.nodes[878].agregar_salida(self.nodes[1002], rand)
        self.nodes[878].agregar_salida(self.nodes[825], rand)

        self.nodes[879].agregar_salida(self.nodes[1003], rand)
        self.nodes[879].agregar_salida(self.nodes[826], rand)

        self.nodes[880].agregar_salida(self.nodes[1004], rand)

        self.nodes[881].agregar_salida(self.nodes[1005], rand)
        self.nodes[881].agregar_salida(self.nodes[827], rand)

        self.nodes[882].agregar_salida(self.nodes[1006], rand)
        self.nodes[882].agregar_salida(self.nodes[828], rand)

        self.nodes[883].agregar_salida(self.nodes[884], rand)

        self.nodes[885].agregar_salida(self.nodes[886], rand)
        self.nodes[885].agregar_salida(self.nodes[832], rand)

        self.nodes[887].agregar_salida(self.nodes[888], rand)
        self.nodes[887].agregar_salida(self.nodes[886], rand)

        self.nodes[889].agregar_salida(self.nodes[890], rand)
        self.nodes[889].agregar_salida(self.nodes[888], rand)

        self.nodes[891].agregar_salida(self.nodes[892], rand)
        self.nodes[891].agregar_salida(self.nodes[890], rand)

        self.nodes[893].agregar_salida(self.nodes[894], rand)
        self.nodes[893].agregar_salida(self.nodes[892], rand)

        self.nodes[895].agregar_salida(self.nodes[896], rand)
        self.nodes[895].agregar_salida(self.nodes[894], rand)

        self.nodes[897].agregar_salida(self.nodes[898], rand)
        self.nodes[897].agregar_salida(self.nodes[896], rand)

        self.nodes[884].agregar_salida(self.nodes[831], rand)
        self.nodes[884].agregar_salida(self.nodes[1006], rand)

        self.nodes[883].agregar_salida(self.nodes[830], rand)
        self.nodes[883].agregar_salida(self.nodes[882], rand)

        self.nodes[880].agregar_salida(self.nodes[881], rand)
        self.nodes[880].agregar_salida(self.nodes[879], rand)

        self.nodes[878].agregar_salida(self.nodes[879], rand)
        self.nodes[878].agregar_salida(self.nodes[877], rand)

        self.nodes[876].agregar_salida(self.nodes[877], rand)
        self.nodes[876].agregar_salida(self.nodes[875], rand)

        self.nodes[874].agregar_salida(self.nodes[875], rand)
        self.nodes[874].agregar_salida(self.nodes[873], rand)

        self.nodes[872].agregar_salida(self.nodes[873], rand)
        self.nodes[872].agregar_salida(self.nodes[871], rand)

        self.nodes[870].agregar_salida(self.nodes[871], rand)
        self.nodes[870].agregar_salida(self.nodes[869], rand)

        self.nodes[868].agregar_salida(self.nodes[869], rand)
        self.nodes[868].agregar_salida(self.nodes[867], rand)

        self.nodes[866].agregar_salida(self.nodes[867], rand)
        self.nodes[866].agregar_salida(self.nodes[865], rand)

        self.nodes[864].agregar_salida(self.nodes[865], rand)
        self.nodes[864].agregar_salida(self.nodes[863], rand)

        self.nodes[862].agregar_salida(self.nodes[863], rand)
        self.nodes[862].agregar_salida(self.nodes[687], rand)
        
        self.nodes[985].agregar_salida(self.nodes[686], rand)
        self.nodes[985].agregar_salida(self.nodes[986], rand)

        self.nodes[987].agregar_salida(self.nodes[986], rand)
        self.nodes[987].agregar_salida(self.nodes[989], rand)

        self.nodes[990].agregar_salida(self.nodes[989], rand)
        self.nodes[990].agregar_salida(self.nodes[991], rand)

        self.nodes[992].agregar_salida(self.nodes[991], rand)
        self.nodes[992].agregar_salida(self.nodes[993], rand)

        self.nodes[994].agregar_salida(self.nodes[993], rand)
        self.nodes[995].agregar_salida(self.nodes[994], rand)
        self.nodes[996].agregar_salida(self.nodes[995], rand)
        self.nodes[996].agregar_salida(self.nodes[997], rand)

        self.nodes[998].agregar_salida(self.nodes[997], rand)
        self.nodes[998].agregar_salida(self.nodes[999], rand)

        self.nodes[1000].agregar_salida(self.nodes[999], rand)
        self.nodes[1000].agregar_salida(self.nodes[1001], rand)

        self.nodes[1002].agregar_salida(self.nodes[1001], rand)
        self.nodes[1002].agregar_salida(self.nodes[1003], rand)

        self.nodes[1004].agregar_salida(self.nodes[1003], rand)
        self.nodes[1004].agregar_salida(self.nodes[1005], rand)

        self.nodes[1006].agregar_salida(self.nodes[1005], rand)

        self.nodes[977].agregar_salida(self.nodes[898], rand)
        self.nodes[977].agregar_salida(self.nodes[978], rand)

        self.nodes[979].agregar_salida(self.nodes[978], rand)
        self.nodes[979].agregar_salida(self.nodes[980], rand)

        self.nodes[981].agregar_salida(self.nodes[980], rand)
        self.nodes[981].agregar_salida(self.nodes[982], rand)

        self.nodes[983].agregar_salida(self.nodes[982], rand)
        self.nodes[983].agregar_salida(self.nodes[984], rand)

        self.nodes[984].agregar_salida(self.nodes[856], rand)
        self.nodes[984].agregar_salida(self.nodes[985], rand)

        self.nodes[983].agregar_salida(self.nodes[986], rand)
        self.nodes[982].agregar_salida(self.nodes[987], rand)

        self.nodes[981].agregar_salida(self.nodes[852], rand)
        self.nodes[981].agregar_salida(self.nodes[989], rand)

        self.nodes[980].agregar_salida(self.nodes[990], rand)
        self.nodes[980].agregar_salida(self.nodes[851], rand)

        self.nodes[979].agregar_salida(self.nodes[991], rand)
        self.nodes[979].agregar_salida(self.nodes[850], rand)

        self.nodes[978].agregar_salida(self.nodes[992], rand)
        self.nodes[978].agregar_salida(self.nodes[849], rand)

        self.nodes[977].agregar_salida(self.nodes[993], rand)
        self.nodes[977].agregar_salida(self.nodes[848], rand)
        
        self.nodes[862].agregar_salida(self.nodes[985], rand)
        self.nodes[862].agregar_salida(self.nodes[812], rand)

        self.nodes[863].agregar_salida(self.nodes[986], rand)
        self.nodes[863].agregar_salida(self.nodes[813], rand)

        self.nodes[864].agregar_salida(self.nodes[987], rand)
        
        self.nodes[865].agregar_salida(self.nodes[989], rand)
        self.nodes[865].agregar_salida(self.nodes[814], rand)

        self.nodes[866].agregar_salida(self.nodes[990], rand)
        
        self.nodes[867].agregar_salida(self.nodes[991], rand)
        self.nodes[867].agregar_salida(self.nodes[815], rand)

        self.nodes[868].agregar_salida(self.nodes[992], rand)
        self.nodes[868].agregar_salida(self.nodes[816], rand)

        self.nodes[869].agregar_salida(self.nodes[993], rand)
        self.nodes[869].agregar_salida(self.nodes[817], rand)

        self.nodes[260].agregar_salida(self.nodes[93], rand)
        self.nodes[260].agregar_salida(self.nodes[95], rand)

        self.nodes[261].agregar_salida(self.nodes[899], rand)
        self.nodes[261].agregar_salida(self.nodes[96], rand)

        self.nodes[263].agregar_salida(self.nodes[900], rand)
        self.nodes[263].agregar_salida(self.nodes[97], rand)

        self.nodes[264].agregar_salida(self.nodes[901], rand)
        
        self.nodes[265].agregar_salida(self.nodes[902], rand)
        self.nodes[265].agregar_salida(self.nodes[98], rand)

        self.nodes[266].agregar_salida(self.nodes[903], rand)
        self.nodes[266].agregar_salida(self.nodes[99], rand)

        self.nodes[267].agregar_salida(self.nodes[904], rand)
        self.nodes[267].agregar_salida(self.nodes[100], rand)

        self.nodes[268].agregar_salida(self.nodes[905], rand)
        self.nodes[268].agregar_salida(self.nodes[101], rand)

        self.nodes[270].agregar_salida(self.nodes[907], rand)
        self.nodes[270].agregar_salida(self.nodes[102], rand)

        self.nodes[271].agregar_salida(self.nodes[908], rand)
        
        self.nodes[272].agregar_salida(self.nodes[909], rand)
        self.nodes[272].agregar_salida(self.nodes[103], rand)

        self.nodes[273].agregar_salida(self.nodes[910], rand)
        self.nodes[273].agregar_salida(self.nodes[104], rand)

        self.nodes[274].agregar_salida(self.nodes[911], rand)
        self.nodes[274].agregar_salida(self.nodes[105], rand)

        self.nodes[275].agregar_salida(self.nodes[912], rand)
        self.nodes[275].agregar_salida(self.nodes[107], rand)

        self.nodes[276].agregar_salida(self.nodes[913], rand)

        self.nodes[277].agregar_salida(self.nodes[914], rand)
        self.nodes[277].agregar_salida(self.nodes[108], rand)

        self.nodes[278].agregar_salida(self.nodes[915], rand)
        self.nodes[278].agregar_salida(self.nodes[109], rand)

        self.nodes[279].agregar_salida(self.nodes[916], rand)
        self.nodes[279].agregar_salida(self.nodes[110], rand)

        self.nodes[280].agregar_salida(self.nodes[917], rand)
        self.nodes[280].agregar_salida(self.nodes[111], rand)

        self.nodes[281].agregar_salida(self.nodes[918], rand)
        self.nodes[281].agregar_salida(self.nodes[112], rand)

        self.nodes[282].agregar_salida(self.nodes[919], rand)
        self.nodes[282].agregar_salida(self.nodes[113], rand)

        self.nodes[283].agregar_salida(self.nodes[920], rand)
        self.nodes[283].agregar_salida(self.nodes[114], rand)

        self.nodes[284].agregar_salida(self.nodes[921], rand)
        self.nodes[284].agregar_salida(self.nodes[115], rand)

        self.nodes[285].agregar_salida(self.nodes[922], rand)
        self.nodes[285].agregar_salida(self.nodes[116], rand)

        self.nodes[286].agregar_salida(self.nodes[923], rand)
        
        self.nodes[287].agregar_salida(self.nodes[924], rand)
        self.nodes[287].agregar_salida(self.nodes[117], rand)

        self.nodes[288].agregar_salida(self.nodes[925], rand)
        self.nodes[288].agregar_salida(self.nodes[118], rand)

        self.nodes[289].agregar_salida(self.nodes[926], rand)
        self.nodes[289].agregar_salida(self.nodes[119], rand)

        self.nodes[290].agregar_salida(self.nodes[927], rand)
        self.nodes[290].agregar_salida(self.nodes[120], rand)

        self.nodes[291].agregar_salida(self.nodes[928], rand)
        self.nodes[291].agregar_salida(self.nodes[121], rand)

        self.nodes[292].agregar_salida(self.nodes[929], rand)
        self.nodes[292].agregar_salida(self.nodes[122], rand)

        self.nodes[293].agregar_salida(self.nodes[930], rand)
        self.nodes[293].agregar_salida(self.nodes[123], rand)

        self.nodes[294].agregar_salida(self.nodes[931], rand)
        self.nodes[294].agregar_salida(self.nodes[124], rand)

        self.nodes[295].agregar_salida(self.nodes[932], rand)
        self.nodes[295].agregar_salida(self.nodes[125], rand)

        self.nodes[286].agregar_salida(self.nodes[1007], rand)
        self.nodes[271].agregar_salida(self.nodes[1009], rand)
        self.nodes[276].agregar_salida(self.nodes[1008], rand)

        self.nodes[933].agregar_salida(self.nodes[296], rand)
        self.nodes[933].agregar_salida(self.nodes[934], rand)
        self.nodes[934].agregar_salida(self.nodes[219], rand)

        self.nodes[900].agregar_salida(self.nodes[901], rand)
        self.nodes[900].agregar_salida(self.nodes[899], rand)

        self.nodes[902].agregar_salida(self.nodes[903], rand)
        self.nodes[902].agregar_salida(self.nodes[901], rand)

        self.nodes[904].agregar_salida(self.nodes[903], rand)
        self.nodes[904].agregar_salida(self.nodes[905], rand)

        self.nodes[906].agregar_salida(self.nodes[905], rand)
        self.nodes[906].agregar_salida(self.nodes[907], rand)

        self.nodes[908].agregar_salida(self.nodes[907], rand)
        self.nodes[908].agregar_salida(self.nodes[909], rand)

        self.nodes[910].agregar_salida(self.nodes[909], rand)
        self.nodes[910].agregar_salida(self.nodes[911], rand)

        self.nodes[912].agregar_salida(self.nodes[911], rand)
        self.nodes[912].agregar_salida(self.nodes[913], rand)

        self.nodes[914].agregar_salida(self.nodes[913], rand)
        self.nodes[914].agregar_salida(self.nodes[915], rand)

        self.nodes[916].agregar_salida(self.nodes[915], rand)
        self.nodes[916].agregar_salida(self.nodes[917], rand)

        self.nodes[918].agregar_salida(self.nodes[917], rand)
        self.nodes[918].agregar_salida(self.nodes[919], rand)

        self.nodes[920].agregar_salida(self.nodes[919], rand)
        self.nodes[920].agregar_salida(self.nodes[921], rand)

        self.nodes[922].agregar_salida(self.nodes[921], rand)
        self.nodes[922].agregar_salida(self.nodes[923], rand)

        self.nodes[924].agregar_salida(self.nodes[923], rand)
        self.nodes[924].agregar_salida(self.nodes[925], rand)

        self.nodes[926].agregar_salida(self.nodes[925], rand)
        self.nodes[926].agregar_salida(self.nodes[927], rand)

        self.nodes[928].agregar_salida(self.nodes[927], rand)
        self.nodes[928].agregar_salida(self.nodes[929], rand)

        self.nodes[930].agregar_salida(self.nodes[929], rand)
        self.nodes[930].agregar_salida(self.nodes[931], rand)

        self.nodes[932].agregar_salida(self.nodes[931], rand)
        self.nodes[932].agregar_salida(self.nodes[933], rand)

        self.nodes[258].agregar_salida(self.nodes[91], rand)
        self.nodes[258].agregar_salida(self.nodes[968], rand)

        self.nodes[967].agregar_salida(self.nodes[968], rand)
        self.nodes[967].agregar_salida(self.nodes[966], rand)

        self.nodes[965].agregar_salida(self.nodes[966], rand)
        self.nodes[965].agregar_salida(self.nodes[964], rand)

        self.nodes[963].agregar_salida(self.nodes[964], rand)
        self.nodes[963].agregar_salida(self.nodes[962], rand)

        self.nodes[961].agregar_salida(self.nodes[962], rand)
        self.nodes[961].agregar_salida(self.nodes[960], rand)

        self.nodes[959].agregar_salida(self.nodes[960], rand)
        self.nodes[959].agregar_salida(self.nodes[958], rand)

        self.nodes[957].agregar_salida(self.nodes[958], rand)
        self.nodes[957].agregar_salida(self.nodes[956], rand)

        self.nodes[955].agregar_salida(self.nodes[956], rand)
        self.nodes[955].agregar_salida(self.nodes[954], rand)

        self.nodes[953].agregar_salida(self.nodes[954], rand)
        self.nodes[953].agregar_salida(self.nodes[952], rand)

        self.nodes[951].agregar_salida(self.nodes[952], rand)
        self.nodes[951].agregar_salida(self.nodes[950], rand)

        self.nodes[949].agregar_salida(self.nodes[950], rand)
        self.nodes[949].agregar_salida(self.nodes[948], rand)

        self.nodes[947].agregar_salida(self.nodes[948], rand)
        self.nodes[947].agregar_salida(self.nodes[946], rand)

        self.nodes[945].agregar_salida(self.nodes[946], rand)
        self.nodes[945].agregar_salida(self.nodes[944], rand)

        self.nodes[943].agregar_salida(self.nodes[944], rand)
        self.nodes[943].agregar_salida(self.nodes[942], rand)

        self.nodes[941].agregar_salida(self.nodes[942], rand)
        self.nodes[941].agregar_salida(self.nodes[940], rand)

        self.nodes[939].agregar_salida(self.nodes[940], rand)
        self.nodes[939].agregar_salida(self.nodes[938], rand)

        self.nodes[937].agregar_salida(self.nodes[938], rand)
        self.nodes[937].agregar_salida(self.nodes[936], rand)

        self.nodes[935].agregar_salida(self.nodes[936], rand)
        self.nodes[935].agregar_salida(self.nodes[934], rand)

        self.nodes[935].agregar_salida(self.nodes[932], rand)
        self.nodes[935].agregar_salida(self.nodes[220], rand)

        self.nodes[936].agregar_salida(self.nodes[931], rand)
        self.nodes[936].agregar_salida(self.nodes[221], rand)

        self.nodes[937].agregar_salida(self.nodes[930], rand)
        self.nodes[937].agregar_salida(self.nodes[222], rand)

        self.nodes[938].agregar_salida(self.nodes[929], rand)
        self.nodes[938].agregar_salida(self.nodes[223], rand)

        self.nodes[939].agregar_salida(self.nodes[928], rand)
        self.nodes[939].agregar_salida(self.nodes[224], rand)

        self.nodes[940].agregar_salida(self.nodes[927], rand)
        self.nodes[940].agregar_salida(self.nodes[225], rand)

        self.nodes[941].agregar_salida(self.nodes[926], rand)
        self.nodes[941].agregar_salida(self.nodes[226], rand)

        self.nodes[942].agregar_salida(self.nodes[925], rand)
        self.nodes[942].agregar_salida(self.nodes[227], rand)

        self.nodes[943].agregar_salida(self.nodes[924], rand)
        self.nodes[943].agregar_salida(self.nodes[228], rand)

        self.nodes[944].agregar_salida(self.nodes[923], rand)
        self.nodes[944].agregar_salida(self.nodes[229], rand)

        self.nodes[945].agregar_salida(self.nodes[922], rand)
        self.nodes[945].agregar_salida(self.nodes[230], rand)

        self.nodes[946].agregar_salida(self.nodes[921], rand)
        self.nodes[946].agregar_salida(self.nodes[231], rand)
        
        self.nodes[947].agregar_salida(self.nodes[920], rand)
        self.nodes[947].agregar_salida(self.nodes[232], rand)

        self.nodes[948].agregar_salida(self.nodes[919], rand)
        self.nodes[948].agregar_salida(self.nodes[233], rand)

        self.nodes[949].agregar_salida(self.nodes[918], rand)
        self.nodes[949].agregar_salida(self.nodes[234], rand)

        self.nodes[950].agregar_salida(self.nodes[917], rand)
        self.nodes[950].agregar_salida(self.nodes[235], rand)

        self.nodes[951].agregar_salida(self.nodes[976], rand)
        self.nodes[951].agregar_salida(self.nodes[236], rand)
        self.nodes[976].agregar_salida(self.nodes[916], rand)

        self.nodes[952].agregar_salida(self.nodes[975], rand)
        self.nodes[975].agregar_salida(self.nodes[915], rand)

        self.nodes[953].agregar_salida(self.nodes[974], rand)
        self.nodes[953].agregar_salida(self.nodes[239], rand)
        self.nodes[974].agregar_salida(self.nodes[914], rand)

        self.nodes[954].agregar_salida(self.nodes[973], rand)
        self.nodes[954].agregar_salida(self.nodes[240], rand)
        self.nodes[973].agregar_salida(self.nodes[913], rand)

        self.nodes[955].agregar_salida(self.nodes[972], rand)
        self.nodes[955].agregar_salida(self.nodes[241], rand)
        self.nodes[972].agregar_salida(self.nodes[912], rand)

        self.nodes[956].agregar_salida(self.nodes[971], rand)
        self.nodes[956].agregar_salida(self.nodes[242], rand)
        self.nodes[971].agregar_salida(self.nodes[911], rand)

        self.nodes[957].agregar_salida(self.nodes[970], rand)
        self.nodes[957].agregar_salida(self.nodes[243], rand)
        self.nodes[970].agregar_salida(self.nodes[910], rand)

        self.nodes[958].agregar_salida(self.nodes[969], rand)
        self.nodes[958].agregar_salida(self.nodes[244], rand)
        self.nodes[969].agregar_salida(self.nodes[909], rand)

        self.nodes[959].agregar_salida(self.nodes[246], rand)
        self.nodes[959].agregar_salida(self.nodes[908], rand)

        self.nodes[960].agregar_salida(self.nodes[247], rand)
        self.nodes[960].agregar_salida(self.nodes[907], rand)

        self.nodes[961].agregar_salida(self.nodes[248], rand)
        self.nodes[961].agregar_salida(self.nodes[906], rand)

        self.nodes[962].agregar_salida(self.nodes[250], rand)
        self.nodes[962].agregar_salida(self.nodes[905], rand)

        self.nodes[963].agregar_salida(self.nodes[251], rand)
        self.nodes[963].agregar_salida(self.nodes[904], rand)

        self.nodes[964].agregar_salida(self.nodes[903], rand)
        self.nodes[964].agregar_salida(self.nodes[83], rand)

        self.nodes[965].agregar_salida(self.nodes[253], rand)
        self.nodes[965].agregar_salida(self.nodes[902], rand)

        self.nodes[966].agregar_salida(self.nodes[254], rand)
        self.nodes[966].agregar_salida(self.nodes[901], rand)

        self.nodes[967].agregar_salida(self.nodes[255], rand)
        self.nodes[967].agregar_salida(self.nodes[900], rand)

        self.nodes[968].agregar_salida(self.nodes[899], rand)
        self.nodes[968].agregar_salida(self.nodes[256], rand)

        self.nodes[296].agregar_salida(self.nodes[127], rand)
        self.nodes[297].agregar_salida(self.nodes[1010], rand)
        self.nodes[298].agregar_salida(self.nodes[128], rand)
        self.nodes[299].agregar_salida(self.nodes[129], rand)
        self.nodes[301].agregar_salida(self.nodes[130], rand)
        self.nodes[302].agregar_salida(self.nodes[131], rand)
        self.nodes[303].agregar_salida(self.nodes[132], rand)
        self.nodes[304].agregar_salida(self.nodes[133], rand)
        self.nodes[305].agregar_salida(self.nodes[1012], rand)
        self.nodes[306].agregar_salida(self.nodes[134], rand)
        self.nodes[307].agregar_salida(self.nodes[1011], rand)
        self.nodes[308].agregar_salida(self.nodes[135], rand)
        self.nodes[309].agregar_salida(self.nodes[1013], rand)
        self.nodes[310].agregar_salida(self.nodes[136], rand)
        self.nodes[311].agregar_salida(self.nodes[137], rand)
        self.nodes[312].agregar_salida(self.nodes[138], rand)
        self.nodes[313].agregar_salida(self.nodes[139], rand)
        self.nodes[315].agregar_salida(self.nodes[142], rand)
        self.nodes[316].agregar_salida(self.nodes[143], rand)
        self.nodes[317].agregar_salida(self.nodes[144], rand)
        self.nodes[318].agregar_salida(self.nodes[145], rand)
        self.nodes[319].agregar_salida(self.nodes[146], rand)
        self.nodes[320].agregar_salida(self.nodes[147], rand)
        self.nodes[321].agregar_salida(self.nodes[148], rand)
        self.nodes[322].agregar_salida(self.nodes[149], rand)
        self.nodes[323].agregar_salida(self.nodes[150], rand)
        self.nodes[324].agregar_salida(self.nodes[151], rand)
        self.nodes[325].agregar_salida(self.nodes[152], rand)
        self.nodes[326].agregar_salida(self.nodes[153], rand)
        self.nodes[327].agregar_salida(self.nodes[154], rand)
        self.nodes[328].agregar_salida(self.nodes[155], rand)
        self.nodes[329].agregar_salida(self.nodes[156], rand)
        self.nodes[330].agregar_salida(self.nodes[158], rand)
        self.nodes[331].agregar_salida(self.nodes[159], rand)
        self.nodes[332].agregar_salida(self.nodes[160], rand)
        self.nodes[336].agregar_salida(self.nodes[161], rand)
        self.nodes[337].agregar_salida(self.nodes[163], rand)
        self.nodes[338].agregar_salida(self.nodes[164], rand)
        self.nodes[339].agregar_salida(self.nodes[165], rand)
        self.nodes[340].agregar_salida(self.nodes[166], rand)
        self.nodes[341].agregar_salida(self.nodes[167], rand)
        self.nodes[168].agregar_salida(self.nodes[342], rand)
        self.nodes[169].agregar_salida(self.nodes[486], rand)
        self.nodes[486].agregar_salida(self.nodes[416], rand)
        self.nodes[415].agregar_salida(self.nodes[342], rand)


        self.nodes[169].agregar_salida(self.nodes[1], rand)
        self.nodes[488].agregar_salida(self.nodes[1], rand)

        self.nodes[170].agregar_salida(self.nodes[2], rand)
        self.nodes[489].agregar_salida(self.nodes[2], rand)

        self.nodes[171].agregar_salida(self.nodes[3], rand)
        self.nodes[585].agregar_salida(self.nodes[31], rand)

        self.nodes[172].agregar_salida(self.nodes[4], rand)
        self.nodes[491].agregar_salida(self.nodes[4], rand)

        self.nodes[173].agregar_salida(self.nodes[5], rand)

        self.nodes[174].agregar_salida(self.nodes[6], rand)
        self.nodes[493].agregar_salida(self.nodes[6], rand)

        self.nodes[175].agregar_salida(self.nodes[7], rand)

        self.nodes[177].agregar_salida(self.nodes[8], rand)
        self.nodes[495].agregar_salida(self.nodes[8], rand)

        self.nodes[178].agregar_salida(self.nodes[9], rand)

        self.nodes[498].agregar_salida(self.nodes[10], rand)

        self.nodes[179].agregar_salida(self.nodes[11], rand)
        self.nodes[499].agregar_salida(self.nodes[11], rand)

        self.nodes[180].agregar_salida(self.nodes[12], rand)
        self.nodes[500].agregar_salida(self.nodes[12], rand)

        self.nodes[181].agregar_salida(self.nodes[13], rand)
        self.nodes[501].agregar_salida(self.nodes[13], rand)

        self.nodes[182].agregar_salida(self.nodes[14], rand)
        self.nodes[502].agregar_salida(self.nodes[14], rand)

        self.nodes[183].agregar_salida(self.nodes[15], rand)
        self.nodes[503].agregar_salida(self.nodes[15], rand)

        self.nodes[504].agregar_salida(self.nodes[16], rand)

        self.nodes[184].agregar_salida(self.nodes[17], rand)
        self.nodes[506].agregar_salida(self.nodes[17], rand)

        self.nodes[185].agregar_salida(self.nodes[18], rand)
        self.nodes[507].agregar_salida(self.nodes[18], rand)

        self.nodes[186].agregar_salida(self.nodes[19], rand)
        self.nodes[508].agregar_salida(self.nodes[19], rand)

        self.nodes[187].agregar_salida(self.nodes[20], rand)
        self.nodes[509].agregar_salida(self.nodes[20], rand)

        self.nodes[188].agregar_salida(self.nodes[21], rand)
        self.nodes[510].agregar_salida(self.nodes[21], rand)

        self.nodes[189].agregar_salida(self.nodes[22], rand)
        self.nodes[511].agregar_salida(self.nodes[22], rand)

        self.nodes[191].agregar_salida(self.nodes[23], rand)
        self.nodes[512].agregar_salida(self.nodes[23], rand)

        self.nodes[192].agregar_salida(self.nodes[24], rand)
        self.nodes[513].agregar_salida(self.nodes[24], rand)

        self.nodes[193].agregar_salida(self.nodes[25], rand)
        self.nodes[514].agregar_salida(self.nodes[25], rand)

        self.nodes[194].agregar_salida(self.nodes[26], rand)
        self.nodes[515].agregar_salida(self.nodes[26], rand)

        self.nodes[195].agregar_salida(self.nodes[27], rand)
        self.nodes[516].agregar_salida(self.nodes[27], rand)

        self.nodes[197].agregar_salida(self.nodes[28], rand)
        self.nodes[517].agregar_salida(self.nodes[28], rand)

        self.nodes[198].agregar_salida(self.nodes[29], rand)
        self.nodes[518].agregar_salida(self.nodes[29], rand)

        self.nodes[199].agregar_salida(self.nodes[30], rand)
        self.nodes[519].agregar_salida(self.nodes[30], rand)

        self.nodes[200].agregar_salida(self.nodes[31], rand)

        self.nodes[201].agregar_salida(self.nodes[32], rand)
        self.nodes[520].agregar_salida(self.nodes[32], rand)

        self.nodes[202].agregar_salida(self.nodes[33], rand)
        self.nodes[521].agregar_salida(self.nodes[33], rand)

        self.nodes[203].agregar_salida(self.nodes[34], rand)
        self.nodes[522].agregar_salida(self.nodes[34], rand)

        self.nodes[204].agregar_salida(self.nodes[35], rand)
        self.nodes[523].agregar_salida(self.nodes[35], rand)

        self.nodes[205].agregar_salida(self.nodes[36], rand)
        self.nodes[524].agregar_salida(self.nodes[36], rand)

        self.nodes[206].agregar_salida(self.nodes[37], rand)
        self.nodes[525].agregar_salida(self.nodes[37], rand)

        self.nodes[207].agregar_salida(self.nodes[38], rand)
        self.nodes[526].agregar_salida(self.nodes[38], rand)

        self.nodes[208].agregar_salida(self.nodes[39], rand)
        self.nodes[527].agregar_salida(self.nodes[39], rand)

        self.nodes[209].agregar_salida(self.nodes[40], rand)
        self.nodes[528].agregar_salida(self.nodes[40], rand)

        self.nodes[210].agregar_salida(self.nodes[41], rand)
        self.nodes[529].agregar_salida(self.nodes[41], rand)

        self.nodes[211].agregar_salida(self.nodes[42], rand)
        self.nodes[530].agregar_salida(self.nodes[42], rand)

        self.nodes[212].agregar_salida(self.nodes[43], rand)
        self.nodes[531].agregar_salida(self.nodes[43], rand)

        self.nodes[213].agregar_salida(self.nodes[44], rand)
        self.nodes[532].agregar_salida(self.nodes[44], rand)

        self.nodes[214].agregar_salida(self.nodes[45], rand)
        self.nodes[533].agregar_salida(self.nodes[45], rand)

        self.nodes[215].agregar_salida(self.nodes[46], rand)
        self.nodes[534].agregar_salida(self.nodes[46], rand)

        self.nodes[216].agregar_salida(self.nodes[47], rand)
        self.nodes[535].agregar_salida(self.nodes[47], rand)

        self.nodes[218].agregar_salida(self.nodes[48], rand)
        self.nodes[538].agregar_salida(self.nodes[48], rand)

        self.nodes[536].agregar_salida(self.nodes[217], rand)

        self.nodes[219].agregar_salida(self.nodes[49], rand)
        self.nodes[539].agregar_salida(self.nodes[49], rand)

        self.nodes[220].agregar_salida(self.nodes[50], rand)
        self.nodes[540].agregar_salida(self.nodes[50], rand)

        self.nodes[221].agregar_salida(self.nodes[51], rand)
        self.nodes[541].agregar_salida(self.nodes[51], rand)

        self.nodes[222].agregar_salida(self.nodes[52], rand)
        self.nodes[542].agregar_salida(self.nodes[52], rand)

        self.nodes[223].agregar_salida(self.nodes[53], rand)
        self.nodes[543].agregar_salida(self.nodes[53], rand)

        self.nodes[224].agregar_salida(self.nodes[54], rand)
        self.nodes[544].agregar_salida(self.nodes[54], rand)

        self.nodes[225].agregar_salida(self.nodes[55], rand)
        self.nodes[545].agregar_salida(self.nodes[55], rand)

        self.nodes[226].agregar_salida(self.nodes[56], rand)
        self.nodes[546].agregar_salida(self.nodes[56], rand)

        self.nodes[227].agregar_salida(self.nodes[57], rand)
        self.nodes[547].agregar_salida(self.nodes[57], rand)

        self.nodes[228].agregar_salida(self.nodes[58], rand)
        self.nodes[548].agregar_salida(self.nodes[58], rand)

        self.nodes[229].agregar_salida(self.nodes[59], rand)
        self.nodes[549].agregar_salida(self.nodes[59], rand)

        self.nodes[230].agregar_salida(self.nodes[61], rand)
        self.nodes[550].agregar_salida(self.nodes[61], rand)

        self.nodes[231].agregar_salida(self.nodes[62], rand)
        self.nodes[551].agregar_salida(self.nodes[62], rand)

        self.nodes[232].agregar_salida(self.nodes[63], rand)
        self.nodes[857].agregar_salida(self.nodes[63], rand)

        self.nodes[858].agregar_salida(self.nodes[857], rand)

        self.nodes[233].agregar_salida(self.nodes[64], rand)
        self.nodes[856].agregar_salida(self.nodes[64], rand)

        self.nodes[234].agregar_salida(self.nodes[65], rand)
        self.nodes[855].agregar_salida(self.nodes[65], rand)

        self.nodes[854].agregar_salida(self.nodes[235], rand)

        self.nodes[236].agregar_salida(self.nodes[66], rand)
        self.nodes[853].agregar_salida(self.nodes[66], rand)
        self.nodes[852].agregar_salida(self.nodes[853], rand)

        self.nodes[238].agregar_salida(self.nodes[68], rand)
        self.nodes[851].agregar_salida(self.nodes[68], rand)

        self.nodes[239].agregar_salida(self.nodes[69], rand)
        self.nodes[850].agregar_salida(self.nodes[69], rand)

        self.nodes[240].agregar_salida(self.nodes[70], rand)
        self.nodes[849].agregar_salida(self.nodes[70], rand)

        self.nodes[241].agregar_salida(self.nodes[71], rand)
        self.nodes[848].agregar_salida(self.nodes[71], rand)

        self.nodes[242].agregar_salida(self.nodes[72], rand)
        self.nodes[847].agregar_salida(self.nodes[72], rand)

        self.nodes[243].agregar_salida(self.nodes[73], rand)
        self.nodes[846].agregar_salida(self.nodes[73], rand)

        self.nodes[244].agregar_salida(self.nodes[74], rand)
        self.nodes[845].agregar_salida(self.nodes[74], rand)

        self.nodes[245].agregar_salida(self.nodes[78], rand)
        self.nodes[844].agregar_salida(self.nodes[78], rand)

        self.nodes[247].agregar_salida(self.nodes[79], rand)
        self.nodes[843].agregar_salida(self.nodes[79], rand)

        self.nodes[248].agregar_salida(self.nodes[80], rand)
        self.nodes[842].agregar_salida(self.nodes[80], rand)

        self.nodes[250].agregar_salida(self.nodes[81], rand)
        self.nodes[841].agregar_salida(self.nodes[81], rand)

        self.nodes[251].agregar_salida(self.nodes[82], rand)
        self.nodes[840].agregar_salida(self.nodes[82], rand)

        self.nodes[839].agregar_salida(self.nodes[83], rand)

        self.nodes[253].agregar_salida(self.nodes[84], rand)
        self.nodes[838].agregar_salida(self.nodes[84], rand)

        self.nodes[254].agregar_salida(self.nodes[85], rand)
        self.nodes[837].agregar_salida(self.nodes[85], rand)

        self.nodes[255].agregar_salida(self.nodes[86], rand)
        self.nodes[836].agregar_salida(self.nodes[86], rand)

        self.nodes[835].agregar_salida(self.nodes[87], rand)

        self.nodes[834].agregar_salida(self.nodes[88], rand)

        self.nodes[833].agregar_salida(self.nodes[89], rand)

        self.nodes[257].agregar_salida(self.nodes[90], rand)

        self.nodes[487].agregar_salida(self.nodes[617], rand)

        self.nodes[488].agregar_salida(self.nodes[616], rand)
        self.nodes[619].agregar_salida(self.nodes[616], rand)

        self.nodes[489].agregar_salida(self.nodes[615], rand)
        self.nodes[620].agregar_salida(self.nodes[615], rand)

        self.nodes[621].agregar_salida(self.nodes[614], rand)
        self.nodes[490].agregar_salida(self.nodes[614], rand)

        self.nodes[622].agregar_salida(self.nodes[613], rand)
        self.nodes[491].agregar_salida(self.nodes[613], rand)

        self.nodes[624].agregar_salida(self.nodes[612], rand)
        self.nodes[492].agregar_salida(self.nodes[612], rand)

        self.nodes[625].agregar_salida(self.nodes[611], rand)
        self.nodes[493].agregar_salida(self.nodes[611], rand)

        self.nodes[626].agregar_salida(self.nodes[610], rand)
        self.nodes[494].agregar_salida(self.nodes[610], rand)

        self.nodes[627].agregar_salida(self.nodes[609], rand)
        self.nodes[495].agregar_salida(self.nodes[609], rand)

        self.nodes[628].agregar_salida(self.nodes[608], rand)
        self.nodes[496].agregar_salida(self.nodes[608], rand)

        self.nodes[629].agregar_salida(self.nodes[607], rand)
        self.nodes[497].agregar_salida(self.nodes[607], rand)

        self.nodes[630].agregar_salida(self.nodes[606], rand)
        self.nodes[498].agregar_salida(self.nodes[606], rand)

        self.nodes[632].agregar_salida(self.nodes[605], rand)
        self.nodes[499].agregar_salida(self.nodes[605], rand)

        self.nodes[633].agregar_salida(self.nodes[604], rand)
        self.nodes[500].agregar_salida(self.nodes[604], rand)

        self.nodes[634].agregar_salida(self.nodes[603], rand)
        self.nodes[501].agregar_salida(self.nodes[603], rand)

        self.nodes[635].agregar_salida(self.nodes[602], rand)
        self.nodes[502].agregar_salida(self.nodes[602], rand)

        self.nodes[636].agregar_salida(self.nodes[601], rand)
        self.nodes[503].agregar_salida(self.nodes[601], rand)

        self.nodes[637].agregar_salida(self.nodes[600], rand)
        self.nodes[504].agregar_salida(self.nodes[600], rand)

        self.nodes[638].agregar_salida(self.nodes[599], rand)
        self.nodes[506].agregar_salida(self.nodes[599], rand)

        self.nodes[639].agregar_salida(self.nodes[598], rand)
        self.nodes[507].agregar_salida(self.nodes[598], rand)

        self.nodes[641].agregar_salida(self.nodes[597], rand)
        self.nodes[508].agregar_salida(self.nodes[597], rand)

        self.nodes[642].agregar_salida(self.nodes[596], rand)
        self.nodes[509].agregar_salida(self.nodes[596], rand)

        self.nodes[643].agregar_salida(self.nodes[595], rand)
        self.nodes[510].agregar_salida(self.nodes[595], rand)

        self.nodes[644].agregar_salida(self.nodes[594], rand)
        self.nodes[511].agregar_salida(self.nodes[594], rand)

        self.nodes[645].agregar_salida(self.nodes[593], rand)
        self.nodes[512].agregar_salida(self.nodes[593], rand)

        self.nodes[646].agregar_salida(self.nodes[592], rand)
        self.nodes[513].agregar_salida(self.nodes[592], rand)

        self.nodes[647].agregar_salida(self.nodes[591], rand)
        self.nodes[514].agregar_salida(self.nodes[591], rand)

        self.nodes[648].agregar_salida(self.nodes[590], rand)
        self.nodes[515].agregar_salida(self.nodes[590], rand)

        self.nodes[649].agregar_salida(self.nodes[589], rand)
        self.nodes[516].agregar_salida(self.nodes[589], rand)

        self.nodes[650].agregar_salida(self.nodes[588], rand)
        self.nodes[517].agregar_salida(self.nodes[588], rand)

        self.nodes[651].agregar_salida(self.nodes[587], rand)
        self.nodes[518].agregar_salida(self.nodes[587], rand)

        self.nodes[653].agregar_salida(self.nodes[586], rand)
        self.nodes[519].agregar_salida(self.nodes[586], rand)

        self.nodes[654].agregar_salida(self.nodes[585], rand)

        self.nodes[655].agregar_salida(self.nodes[584], rand)
        self.nodes[520].agregar_salida(self.nodes[584], rand)

        self.nodes[656].agregar_salida(self.nodes[583], rand)
        self.nodes[521].agregar_salida(self.nodes[583], rand)

        self.nodes[657].agregar_salida(self.nodes[582], rand)
        self.nodes[522].agregar_salida(self.nodes[582], rand)

        self.nodes[658].agregar_salida(self.nodes[581], rand)
        self.nodes[523].agregar_salida(self.nodes[581], rand)

        self.nodes[659].agregar_salida(self.nodes[580], rand)
        self.nodes[524].agregar_salida(self.nodes[580], rand)

        self.nodes[660].agregar_salida(self.nodes[579], rand)
        self.nodes[525].agregar_salida(self.nodes[579], rand)

        self.nodes[661].agregar_salida(self.nodes[578], rand)
        self.nodes[526].agregar_salida(self.nodes[578], rand)

        self.nodes[662].agregar_salida(self.nodes[577], rand)
        self.nodes[527].agregar_salida(self.nodes[577], rand)

        self.nodes[663].agregar_salida(self.nodes[576], rand)
        self.nodes[528].agregar_salida(self.nodes[576], rand)

        self.nodes[664].agregar_salida(self.nodes[575], rand)
        self.nodes[529].agregar_salida(self.nodes[575], rand)

        self.nodes[665].agregar_salida(self.nodes[574], rand)
        self.nodes[530].agregar_salida(self.nodes[574], rand)

        self.nodes[666].agregar_salida(self.nodes[573], rand)
        self.nodes[531].agregar_salida(self.nodes[573], rand)

        self.nodes[667].agregar_salida(self.nodes[572], rand)
        self.nodes[532].agregar_salida(self.nodes[572], rand)

        self.nodes[668].agregar_salida(self.nodes[571], rand)
        self.nodes[533].agregar_salida(self.nodes[571], rand)

        self.nodes[669].agregar_salida(self.nodes[570], rand)
        self.nodes[534].agregar_salida(self.nodes[570], rand)

        self.nodes[670].agregar_salida(self.nodes[569], rand)
        self.nodes[535].agregar_salida(self.nodes[569], rand)

        self.nodes[671].agregar_salida(self.nodes[568], rand)
        self.nodes[536].agregar_salida(self.nodes[568], rand)

        self.nodes[672].agregar_salida(self.nodes[567], rand)
        self.nodes[538].agregar_salida(self.nodes[567], rand)

        self.nodes[673].agregar_salida(self.nodes[566], rand)
        self.nodes[539].agregar_salida(self.nodes[566], rand)

        self.nodes[674].agregar_salida(self.nodes[565], rand)
        self.nodes[540].agregar_salida(self.nodes[565], rand)

        self.nodes[675].agregar_salida(self.nodes[564], rand)
        self.nodes[541].agregar_salida(self.nodes[564], rand)

        self.nodes[676].agregar_salida(self.nodes[563], rand)
        self.nodes[542].agregar_salida(self.nodes[563], rand)

        self.nodes[677].agregar_salida(self.nodes[562], rand)
        self.nodes[543].agregar_salida(self.nodes[562], rand)

        self.nodes[678].agregar_salida(self.nodes[561], rand)
        self.nodes[544].agregar_salida(self.nodes[561], rand)

        self.nodes[679].agregar_salida(self.nodes[560], rand)
        self.nodes[545].agregar_salida(self.nodes[560], rand)

        self.nodes[680].agregar_salida(self.nodes[559], rand)
        self.nodes[546].agregar_salida(self.nodes[559], rand)

        self.nodes[681].agregar_salida(self.nodes[558], rand)
        self.nodes[547].agregar_salida(self.nodes[558], rand)

        self.nodes[682].agregar_salida(self.nodes[557], rand)
        self.nodes[548].agregar_salida(self.nodes[557], rand)

        self.nodes[683].agregar_salida(self.nodes[556], rand)
        self.nodes[549].agregar_salida(self.nodes[556], rand)

        self.nodes[684].agregar_salida(self.nodes[555], rand)
        self.nodes[550].agregar_salida(self.nodes[555], rand)

        self.nodes[685].agregar_salida(self.nodes[554], rand)
        self.nodes[551].agregar_salida(self.nodes[554], rand)

        self.nodes[686].agregar_salida(self.nodes[553], rand)

        self.nodes[618].agregar_salida(self.nodes[748], rand)

        self.nodes[619].agregar_salida(self.nodes[747], rand)
        self.nodes[750].agregar_salida(self.nodes[747], rand)

        self.nodes[751].agregar_salida(self.nodes[746], rand)

        self.nodes[623].agregar_salida(self.nodes[745], rand)
        self.nodes[753].agregar_salida(self.nodes[745], rand)

        self.nodes[754].agregar_salida(self.nodes[744], rand)
        self.nodes[624].agregar_salida(self.nodes[744], rand)

        self.nodes[755].agregar_salida(self.nodes[743], rand)
        self.nodes[625].agregar_salida(self.nodes[743], rand)

        self.nodes[756].agregar_salida(self.nodes[742], rand)

        self.nodes[757].agregar_salida(self.nodes[741], rand)
        self.nodes[627].agregar_salida(self.nodes[741], rand)

        self.nodes[758].agregar_salida(self.nodes[740], rand)

        self.nodes[759].agregar_salida(self.nodes[739], rand)

        self.nodes[760].agregar_salida(self.nodes[738], rand)
        self.nodes[630].agregar_salida(self.nodes[738], rand)

        self.nodes[633].agregar_salida(self.nodes[737], rand)
        self.nodes[761].agregar_salida(self.nodes[737], rand)

        self.nodes[762].agregar_salida(self.nodes[736], rand)
        self.nodes[634].agregar_salida(self.nodes[736], rand)

        self.nodes[764].agregar_salida(self.nodes[735], rand)
        self.nodes[636].agregar_salida(self.nodes[735], rand)

        self.nodes[765].agregar_salida(self.nodes[734], rand)
        self.nodes[637].agregar_salida(self.nodes[734], rand)

        self.nodes[635].agregar_salida(self.nodes[763], rand)

        self.nodes[766].agregar_salida(self.nodes[733], rand)
        self.nodes[638].agregar_salida(self.nodes[733], rand)

        self.nodes[767].agregar_salida(self.nodes[732], rand)
        self.nodes[639].agregar_salida(self.nodes[732], rand)

        self.nodes[768].agregar_salida(self.nodes[731], rand)
        self.nodes[641].agregar_salida(self.nodes[731], rand)

        self.nodes[769].agregar_salida(self.nodes[730], rand)
        self.nodes[642].agregar_salida(self.nodes[730], rand)

        self.nodes[770].agregar_salida(self.nodes[729], rand)
        self.nodes[643].agregar_salida(self.nodes[729], rand)

        self.nodes[771].agregar_salida(self.nodes[728], rand)
        self.nodes[644].agregar_salida(self.nodes[728], rand)

        self.nodes[772].agregar_salida(self.nodes[727], rand)
        self.nodes[645].agregar_salida(self.nodes[727], rand)

        self.nodes[773].agregar_salida(self.nodes[726], rand)
        self.nodes[646].agregar_salida(self.nodes[726], rand)

        self.nodes[774].agregar_salida(self.nodes[725], rand)
        self.nodes[647].agregar_salida(self.nodes[725], rand)

        self.nodes[775].agregar_salida(self.nodes[724], rand)
        self.nodes[648].agregar_salida(self.nodes[724], rand)

        self.nodes[776].agregar_salida(self.nodes[723], rand)
        self.nodes[649].agregar_salida(self.nodes[723], rand)

        self.nodes[778].agregar_salida(self.nodes[722], rand)
        self.nodes[650].agregar_salida(self.nodes[722], rand)

        self.nodes[779].agregar_salida(self.nodes[721], rand)
        self.nodes[651].agregar_salida(self.nodes[721], rand)

        self.nodes[780].agregar_salida(self.nodes[720], rand)
        self.nodes[653].agregar_salida(self.nodes[720], rand)

        self.nodes[781].agregar_salida(self.nodes[719], rand)
        self.nodes[654].agregar_salida(self.nodes[719], rand)

        self.nodes[782].agregar_salida(self.nodes[718], rand)
        self.nodes[655].agregar_salida(self.nodes[718], rand)

        self.nodes[783].agregar_salida(self.nodes[717], rand)
        self.nodes[656].agregar_salida(self.nodes[717], rand)

        self.nodes[784].agregar_salida(self.nodes[716], rand)
        self.nodes[657].agregar_salida(self.nodes[716], rand)

        self.nodes[785].agregar_salida(self.nodes[715], rand)
        self.nodes[658].agregar_salida(self.nodes[715], rand)

        self.nodes[786].agregar_salida(self.nodes[714], rand)
        self.nodes[659].agregar_salida(self.nodes[714], rand)

        self.nodes[787].agregar_salida(self.nodes[713], rand)
        self.nodes[660].agregar_salida(self.nodes[713], rand)

        self.nodes[788].agregar_salida(self.nodes[712], rand)
        self.nodes[661].agregar_salida(self.nodes[712], rand)

        self.nodes[789].agregar_salida(self.nodes[711], rand)
        self.nodes[662].agregar_salida(self.nodes[711], rand)

        self.nodes[790].agregar_salida(self.nodes[710], rand)
        self.nodes[663].agregar_salida(self.nodes[710], rand)

        self.nodes[791].agregar_salida(self.nodes[709], rand)
        self.nodes[664].agregar_salida(self.nodes[709], rand)

        self.nodes[792].agregar_salida(self.nodes[708], rand)
        self.nodes[665].agregar_salida(self.nodes[708], rand)

        self.nodes[793].agregar_salida(self.nodes[707], rand)
        self.nodes[666].agregar_salida(self.nodes[707], rand)

        self.nodes[794].agregar_salida(self.nodes[706], rand)
        self.nodes[667].agregar_salida(self.nodes[706], rand)

        self.nodes[795].agregar_salida(self.nodes[705], rand)
        self.nodes[668].agregar_salida(self.nodes[705], rand)

        self.nodes[796].agregar_salida(self.nodes[704], rand)
        self.nodes[669].agregar_salida(self.nodes[704], rand)

        self.nodes[797].agregar_salida(self.nodes[703], rand)
        self.nodes[670].agregar_salida(self.nodes[703], rand)

        self.nodes[798].agregar_salida(self.nodes[702], rand)
        self.nodes[671].agregar_salida(self.nodes[702], rand)

        self.nodes[799].agregar_salida(self.nodes[701], rand)
        self.nodes[672].agregar_salida(self.nodes[701], rand)

        self.nodes[800].agregar_salida(self.nodes[700], rand)
        self.nodes[673].agregar_salida(self.nodes[700], rand)

        self.nodes[801].agregar_salida(self.nodes[699], rand)
        self.nodes[674].agregar_salida(self.nodes[699], rand)

        self.nodes[802].agregar_salida(self.nodes[698], rand)
        self.nodes[675].agregar_salida(self.nodes[698], rand)

        self.nodes[803].agregar_salida(self.nodes[697], rand)
        self.nodes[676].agregar_salida(self.nodes[697], rand)

        self.nodes[804].agregar_salida(self.nodes[696], rand)
        self.nodes[677].agregar_salida(self.nodes[696], rand)

        self.nodes[805].agregar_salida(self.nodes[695], rand)
        self.nodes[678].agregar_salida(self.nodes[695], rand)

        self.nodes[806].agregar_salida(self.nodes[694], rand)
        self.nodes[679].agregar_salida(self.nodes[694], rand)

        self.nodes[807].agregar_salida(self.nodes[693], rand)
        self.nodes[680].agregar_salida(self.nodes[693], rand)

        self.nodes[808].agregar_salida(self.nodes[692], rand)
        self.nodes[681].agregar_salida(self.nodes[692], rand)

        self.nodes[809].agregar_salida(self.nodes[691], rand)
        self.nodes[682].agregar_salida(self.nodes[691], rand)

        self.nodes[810].agregar_salida(self.nodes[690], rand)
        self.nodes[683].agregar_salida(self.nodes[690], rand)

        self.nodes[684].agregar_salida(self.nodes[689], rand)

        self.nodes[685].agregar_salida(self.nodes[688], rand)

        self.nodes[686].agregar_salida(self.nodes[687], rand)
        self.nodes[811].agregar_salida(self.nodes[687], rand)

        self.nodes[834].agregar_salida(self.nodes[885], rand)
        self.nodes[884].agregar_salida(self.nodes[885], rand)

        self.nodes[835].agregar_salida(self.nodes[886], rand)
        self.nodes[1006].agregar_salida(self.nodes[886], rand)

        self.nodes[836].agregar_salida(self.nodes[887], rand)
        self.nodes[1005].agregar_salida(self.nodes[887], rand)

        self.nodes[837].agregar_salida(self.nodes[888], rand)
        self.nodes[1004].agregar_salida(self.nodes[888], rand)

        self.nodes[838].agregar_salida(self.nodes[889], rand)
        self.nodes[1003].agregar_salida(self.nodes[889], rand)

        self.nodes[839].agregar_salida(self.nodes[890], rand)
        self.nodes[1002].agregar_salida(self.nodes[890], rand)

        self.nodes[840].agregar_salida(self.nodes[891], rand)
        self.nodes[1001].agregar_salida(self.nodes[891], rand)

        self.nodes[841].agregar_salida(self.nodes[892], rand)
        self.nodes[1000].agregar_salida(self.nodes[892], rand)

        self.nodes[842].agregar_salida(self.nodes[893], rand)
        self.nodes[999].agregar_salida(self.nodes[893], rand)

        self.nodes[843].agregar_salida(self.nodes[894], rand)
        self.nodes[998].agregar_salida(self.nodes[894], rand)

        self.nodes[844].agregar_salida(self.nodes[895], rand)
        self.nodes[997].agregar_salida(self.nodes[895], rand)

        self.nodes[845].agregar_salida(self.nodes[896], rand)
        self.nodes[996].agregar_salida(self.nodes[896], rand)

        self.nodes[846].agregar_salida(self.nodes[897], rand)
        self.nodes[995].agregar_salida(self.nodes[897], rand)

        self.nodes[847].agregar_salida(self.nodes[898], rand)
        self.nodes[994].agregar_salida(self.nodes[898], rand)

        self.nodes[994].agregar_salida(self.nodes[870], rand)
        self.nodes[819].agregar_salida(self.nodes[870], rand)

        self.nodes[995].agregar_salida(self.nodes[871], rand)
        self.nodes[820].agregar_salida(self.nodes[871], rand)

        self.nodes[996].agregar_salida(self.nodes[872], rand)
        self.nodes[821].agregar_salida(self.nodes[872], rand)

        self.nodes[997].agregar_salida(self.nodes[873], rand)
        self.nodes[822].agregar_salida(self.nodes[873], rand)

        self.nodes[998].agregar_salida(self.nodes[874], rand)
        self.nodes[823].agregar_salida(self.nodes[874], rand)

        self.nodes[999].agregar_salida(self.nodes[875], rand)

        self.nodes[1000].agregar_salida(self.nodes[876], rand)

        self.nodes[1001].agregar_salida(self.nodes[877], rand)
        self.nodes[824].agregar_salida(self.nodes[877], rand)

        self.nodes[1002].agregar_salida(self.nodes[878], rand)
        self.nodes[825].agregar_salida(self.nodes[878], rand)

        self.nodes[1003].agregar_salida(self.nodes[879], rand)
        self.nodes[826].agregar_salida(self.nodes[879], rand)

        self.nodes[1004].agregar_salida(self.nodes[880], rand)

        self.nodes[1005].agregar_salida(self.nodes[881], rand)
        self.nodes[827].agregar_salida(self.nodes[881], rand)

        self.nodes[1006].agregar_salida(self.nodes[882], rand)
        self.nodes[828].agregar_salida(self.nodes[882], rand)

        self.nodes[884].agregar_salida(self.nodes[883], rand)

        self.nodes[886].agregar_salida(self.nodes[885], rand)
        self.nodes[832].agregar_salida(self.nodes[885], rand)

        self.nodes[888].agregar_salida(self.nodes[887], rand)
        self.nodes[886].agregar_salida(self.nodes[887], rand)

        self.nodes[890].agregar_salida(self.nodes[889], rand)
        self.nodes[888].agregar_salida(self.nodes[889], rand)

        self.nodes[892].agregar_salida(self.nodes[891], rand)
        self.nodes[890].agregar_salida(self.nodes[891], rand)

        self.nodes[894].agregar_salida(self.nodes[893], rand)
        self.nodes[892].agregar_salida(self.nodes[893], rand)

        self.nodes[896].agregar_salida(self.nodes[895], rand)
        self.nodes[894].agregar_salida(self.nodes[895], rand)

        self.nodes[898].agregar_salida(self.nodes[897], rand)
        self.nodes[896].agregar_salida(self.nodes[897], rand)

        self.nodes[831].agregar_salida(self.nodes[884], rand)
        self.nodes[1006].agregar_salida(self.nodes[884], rand)

        self.nodes[830].agregar_salida(self.nodes[883], rand)
        self.nodes[882].agregar_salida(self.nodes[883], rand)

        self.nodes[881].agregar_salida(self.nodes[880], rand)
        self.nodes[879].agregar_salida(self.nodes[880], rand)

        self.nodes[879].agregar_salida(self.nodes[878], rand)
        self.nodes[877].agregar_salida(self.nodes[878], rand)

        self.nodes[877].agregar_salida(self.nodes[876], rand)
        self.nodes[875].agregar_salida(self.nodes[876], rand)

        self.nodes[875].agregar_salida(self.nodes[874], rand)
        self.nodes[873].agregar_salida(self.nodes[874], rand)

        self.nodes[873].agregar_salida(self.nodes[872], rand)
        self.nodes[871].agregar_salida(self.nodes[872], rand)

        self.nodes[871].agregar_salida(self.nodes[870], rand)
        self.nodes[869].agregar_salida(self.nodes[870], rand)

        self.nodes[869].agregar_salida(self.nodes[868], rand)
        self.nodes[867].agregar_salida(self.nodes[868], rand)

        self.nodes[867].agregar_salida(self.nodes[866], rand)
        self.nodes[865].agregar_salida(self.nodes[866], rand)

        self.nodes[865].agregar_salida(self.nodes[864], rand)
        self.nodes[863].agregar_salida(self.nodes[864], rand)

        self.nodes[863].agregar_salida(self.nodes[862], rand)
        self.nodes[687].agregar_salida(self.nodes[862], rand)

        self.nodes[686].agregar_salida(self.nodes[985], rand)
        self.nodes[986].agregar_salida(self.nodes[985], rand)

        self.nodes[986].agregar_salida(self.nodes[987], rand)
        self.nodes[989].agregar_salida(self.nodes[987], rand)

        self.nodes[989].agregar_salida(self.nodes[990], rand)
        self.nodes[991].agregar_salida(self.nodes[990], rand)

        self.nodes[991].agregar_salida(self.nodes[992], rand)
        self.nodes[993].agregar_salida(self.nodes[992], rand)

        self.nodes[993].agregar_salida(self.nodes[994], rand)
        self.nodes[994].agregar_salida(self.nodes[995], rand)
        self.nodes[995].agregar_salida(self.nodes[996], rand)
        self.nodes[997].agregar_salida(self.nodes[996], rand)

        self.nodes[997].agregar_salida(self.nodes[998], rand)
        self.nodes[999].agregar_salida(self.nodes[998], rand)

        self.nodes[999].agregar_salida(self.nodes[1000], rand)
        self.nodes[1001].agregar_salida(self.nodes[1000], rand)

        self.nodes[1001].agregar_salida(self.nodes[1002], rand)
        self.nodes[1003].agregar_salida(self.nodes[1002], rand)

        self.nodes[1003].agregar_salida(self.nodes[1004], rand)
        self.nodes[1005].agregar_salida(self.nodes[1004], rand)

        self.nodes[1005].agregar_salida(self.nodes[1006], rand)

        self.nodes[898].agregar_salida(self.nodes[977], rand)
        self.nodes[978].agregar_salida(self.nodes[977], rand)

        self.nodes[978].agregar_salida(self.nodes[979], rand)
        self.nodes[980].agregar_salida(self.nodes[979], rand)

        self.nodes[980].agregar_salida(self.nodes[981], rand)
        self.nodes[982].agregar_salida(self.nodes[981], rand)

        self.nodes[982].agregar_salida(self.nodes[983], rand)
        self.nodes[984].agregar_salida(self.nodes[983], rand)

        self.nodes[985].agregar_salida(self.nodes[984], rand)
        self.nodes[986].agregar_salida(self.nodes[983], rand)

        self.nodes[987].agregar_salida(self.nodes[982], rand)
        self.nodes[989].agregar_salida(self.nodes[981], rand)

        self.nodes[852].agregar_salida(self.nodes[981], rand)
        self.nodes[989].agregar_salida(self.nodes[980], rand)

        self.nodes[990].agregar_salida(self.nodes[980], rand)
        self.nodes[851].agregar_salida(self.nodes[980], rand)

        self.nodes[991].agregar_salida(self.nodes[979], rand)
        self.nodes[850].agregar_salida(self.nodes[979], rand)

        self.nodes[992].agregar_salida(self.nodes[978], rand)
        self.nodes[849].agregar_salida(self.nodes[978], rand)

        self.nodes[993].agregar_salida(self.nodes[977], rand)
        self.nodes[848].agregar_salida(self.nodes[977], rand)

        self.nodes[985].agregar_salida(self.nodes[862], rand)
        self.nodes[812].agregar_salida(self.nodes[862], rand)

        self.nodes[986].agregar_salida(self.nodes[863], rand)
        self.nodes[813].agregar_salida(self.nodes[863], rand)

        self.nodes[987].agregar_salida(self.nodes[864], rand)

        self.nodes[989].agregar_salida(self.nodes[865], rand)
        self.nodes[814].agregar_salida(self.nodes[865], rand)

        self.nodes[990].agregar_salida(self.nodes[866], rand)

        self.nodes[991].agregar_salida(self.nodes[867], rand)
        self.nodes[815].agregar_salida(self.nodes[867], rand)

        self.nodes[992].agregar_salida(self.nodes[868], rand)
        self.nodes[816].agregar_salida(self.nodes[868], rand)

        self.nodes[993].agregar_salida(self.nodes[869], rand)
        self.nodes[817].agregar_salida(self.nodes[869], rand)

        self.nodes[93].agregar_salida(self.nodes[260], rand)
        self.nodes[95].agregar_salida(self.nodes[260], rand)

        self.nodes[899].agregar_salida(self.nodes[261], rand)
        self.nodes[96].agregar_salida(self.nodes[261], rand)

        self.nodes[900].agregar_salida(self.nodes[263], rand)
        self.nodes[97].agregar_salida(self.nodes[263], rand)

        self.nodes[901].agregar_salida(self.nodes[264], rand)

        self.nodes[902].agregar_salida(self.nodes[265], rand)
        self.nodes[98].agregar_salida(self.nodes[265], rand)

        self.nodes[903].agregar_salida(self.nodes[266], rand)
        self.nodes[99].agregar_salida(self.nodes[266], rand)

        self.nodes[904].agregar_salida(self.nodes[267], rand)
        self.nodes[100].agregar_salida(self.nodes[267], rand)

        self.nodes[905].agregar_salida(self.nodes[268], rand)
        self.nodes[101].agregar_salida(self.nodes[268], rand)

        self.nodes[907].agregar_salida(self.nodes[270], rand)
        self.nodes[102].agregar_salida(self.nodes[270], rand)

        self.nodes[908].agregar_salida(self.nodes[271], rand)

        self.nodes[909].agregar_salida(self.nodes[272], rand)
        self.nodes[103].agregar_salida(self.nodes[272], rand)

        self.nodes[910].agregar_salida(self.nodes[273], rand)
        self.nodes[104].agregar_salida(self.nodes[273], rand)

        self.nodes[911].agregar_salida(self.nodes[274], rand)
        self.nodes[105].agregar_salida(self.nodes[274], rand)

        self.nodes[912].agregar_salida(self.nodes[275], rand)
        self.nodes[107].agregar_salida(self.nodes[275], rand)

        self.nodes[913].agregar_salida(self.nodes[276], rand)

        self.nodes[914].agregar_salida(self.nodes[277], rand)
        self.nodes[108].agregar_salida(self.nodes[277], rand)

        self.nodes[915].agregar_salida(self.nodes[278], rand)
        self.nodes[109].agregar_salida(self.nodes[278], rand)

        self.nodes[916].agregar_salida(self.nodes[279], rand)
        self.nodes[110].agregar_salida(self.nodes[279], rand)

        self.nodes[917].agregar_salida(self.nodes[280], rand)
        self.nodes[111].agregar_salida(self.nodes[280], rand)

        self.nodes[918].agregar_salida(self.nodes[281], rand)
        self.nodes[112].agregar_salida(self.nodes[281], rand)

        self.nodes[919].agregar_salida(self.nodes[282], rand)
        self.nodes[113].agregar_salida(self.nodes[282], rand)

        self.nodes[920].agregar_salida(self.nodes[283], rand)
        self.nodes[114].agregar_salida(self.nodes[283], rand)

        self.nodes[921].agregar_salida(self.nodes[284], rand)
        self.nodes[115].agregar_salida(self.nodes[284], rand)

        self.nodes[922].agregar_salida(self.nodes[285], rand)
        self.nodes[116].agregar_salida(self.nodes[285], rand)

        self.nodes[923].agregar_salida(self.nodes[286], rand)

        self.nodes[924].agregar_salida(self.nodes[287], rand)
        self.nodes[117].agregar_salida(self.nodes[287], rand)

        self.nodes[925].agregar_salida(self.nodes[288], rand)
        self.nodes[118].agregar_salida(self.nodes[288], rand)

        self.nodes[926].agregar_salida(self.nodes[289], rand)
        self.nodes[119].agregar_salida(self.nodes[289], rand)

        self.nodes[927].agregar_salida(self.nodes[290], rand)
        self.nodes[120].agregar_salida(self.nodes[290], rand)

        self.nodes[928].agregar_salida(self.nodes[291], rand)
        self.nodes[121].agregar_salida(self.nodes[291], rand)

        self.nodes[929].agregar_salida(self.nodes[292], rand)
        self.nodes[122].agregar_salida(self.nodes[292], rand)

        self.nodes[930].agregar_salida(self.nodes[293], rand)
        self.nodes[123].agregar_salida(self.nodes[293], rand)

        self.nodes[931].agregar_salida(self.nodes[294], rand)
        self.nodes[124].agregar_salida(self.nodes[294], rand)

        self.nodes[932].agregar_salida(self.nodes[295], rand)
        self.nodes[125].agregar_salida(self.nodes[295], rand)

        self.nodes[1007].agregar_salida(self.nodes[286], rand)
        self.nodes[1009].agregar_salida(self.nodes[271], rand)
        self.nodes[1008].agregar_salida(self.nodes[276], rand)

        self.nodes[296].agregar_salida(self.nodes[933], rand)
        self.nodes[934].agregar_salida(self.nodes[933], rand)
        self.nodes[219].agregar_salida(self.nodes[934], rand)

        self.nodes[901].agregar_salida(self.nodes[900], rand)
        self.nodes[899].agregar_salida(self.nodes[900], rand)

        self.nodes[903].agregar_salida(self.nodes[902], rand)
        self.nodes[901].agregar_salida(self.nodes[902], rand)

        self.nodes[905].agregar_salida(self.nodes[904], rand)
        self.nodes[903].agregar_salida(self.nodes[904], rand)

        self.nodes[907].agregar_salida(self.nodes[906], rand)
        self.nodes[905].agregar_salida(self.nodes[906], rand)

        self.nodes[909].agregar_salida(self.nodes[908], rand)
        self.nodes[907].agregar_salida(self.nodes[908], rand)

        self.nodes[911].agregar_salida(self.nodes[910], rand)
        self.nodes[909].agregar_salida(self.nodes[910], rand)

        self.nodes[913].agregar_salida(self.nodes[912], rand)
        self.nodes[911].agregar_salida(self.nodes[912], rand)

        self.nodes[915].agregar_salida(self.nodes[914], rand)
        self.nodes[913].agregar_salida(self.nodes[914], rand)

        self.nodes[917].agregar_salida(self.nodes[916], rand)
        self.nodes[915].agregar_salida(self.nodes[916], rand)

        self.nodes[919].agregar_salida(self.nodes[918], rand)
        self.nodes[917].agregar_salida(self.nodes[918], rand)

        self.nodes[921].agregar_salida(self.nodes[920], rand)
        self.nodes[919].agregar_salida(self.nodes[920], rand)

        self.nodes[923].agregar_salida(self.nodes[922], rand)
        self.nodes[921].agregar_salida(self.nodes[922], rand)

        self.nodes[925].agregar_salida(self.nodes[924], rand)
        self.nodes[923].agregar_salida(self.nodes[924], rand)

        self.nodes[927].agregar_salida(self.nodes[926], rand)
        self.nodes[925].agregar_salida(self.nodes[926], rand)

        self.nodes[929].agregar_salida(self.nodes[928], rand)
        self.nodes[927].agregar_salida(self.nodes[928], rand)

        self.nodes[931].agregar_salida(self.nodes[930], rand)
        self.nodes[929].agregar_salida(self.nodes[930], rand)

        self.nodes[933].agregar_salida(self.nodes[932], rand)
        self.nodes[931].agregar_salida(self.nodes[932], rand)

        self.nodes[91].agregar_salida(self.nodes[258], rand)
        self.nodes[968].agregar_salida(self.nodes[258], rand)

        self.nodes[968].agregar_salida(self.nodes[967], rand)
        self.nodes[966].agregar_salida(self.nodes[967], rand)

        self.nodes[966].agregar_salida(self.nodes[965], rand)
        self.nodes[964].agregar_salida(self.nodes[965], rand)

        self.nodes[964].agregar_salida(self.nodes[963], rand)
        self.nodes[962].agregar_salida(self.nodes[963], rand)

        self.nodes[962].agregar_salida(self.nodes[961], rand)
        self.nodes[960].agregar_salida(self.nodes[961], rand)

        self.nodes[960].agregar_salida(self.nodes[959], rand)
        self.nodes[958].agregar_salida(self.nodes[959], rand)

        self.nodes[958].agregar_salida(self.nodes[957], rand)
        self.nodes[956].agregar_salida(self.nodes[957], rand)

        self.nodes[956].agregar_salida(self.nodes[955], rand)
        self.nodes[954].agregar_salida(self.nodes[955], rand)

        self.nodes[954].agregar_salida(self.nodes[953], rand)
        self.nodes[952].agregar_salida(self.nodes[953], rand)

        self.nodes[952].agregar_salida(self.nodes[951], rand)
        self.nodes[950].agregar_salida(self.nodes[951], rand)

        self.nodes[950].agregar_salida(self.nodes[949], rand)
        self.nodes[948].agregar_salida(self.nodes[949], rand)

        self.nodes[948].agregar_salida(self.nodes[947], rand)
        self.nodes[946].agregar_salida(self.nodes[947], rand)

        self.nodes[946].agregar_salida(self.nodes[945], rand)
        self.nodes[944].agregar_salida(self.nodes[945], rand)

        self.nodes[944].agregar_salida(self.nodes[943], rand)
        self.nodes[942].agregar_salida(self.nodes[943], rand)

        self.nodes[942].agregar_salida(self.nodes[941], rand)
        self.nodes[940].agregar_salida(self.nodes[941], rand)

        self.nodes[940].agregar_salida(self.nodes[939], rand)
        self.nodes[938].agregar_salida(self.nodes[939], rand)

        self.nodes[938].agregar_salida(self.nodes[937], rand)
        self.nodes[936].agregar_salida(self.nodes[937], rand)

        self.nodes[936].agregar_salida(self.nodes[935], rand)
        self.nodes[934].agregar_salida(self.nodes[935], rand)

        self.nodes[932].agregar_salida(self.nodes[935], rand)
        self.nodes[220].agregar_salida(self.nodes[935], rand)

        self.nodes[931].agregar_salida(self.nodes[936], rand)
        self.nodes[221].agregar_salida(self.nodes[936], rand)

        self.nodes[930].agregar_salida(self.nodes[937], rand)
        self.nodes[222].agregar_salida(self.nodes[937], rand)

        self.nodes[929].agregar_salida(self.nodes[938], rand)
        self.nodes[223].agregar_salida(self.nodes[938], rand)

        self.nodes[928].agregar_salida(self.nodes[939], rand)
        self.nodes[224].agregar_salida(self.nodes[939], rand)

        self.nodes[927].agregar_salida(self.nodes[940], rand)
        self.nodes[225].agregar_salida(self.nodes[940], rand)

        self.nodes[926].agregar_salida(self.nodes[941], rand)
        self.nodes[226].agregar_salida(self.nodes[941], rand)

        self.nodes[925].agregar_salida(self.nodes[942], rand)
        self.nodes[227].agregar_salida(self.nodes[942], rand)

        self.nodes[924].agregar_salida(self.nodes[943], rand)
        self.nodes[228].agregar_salida(self.nodes[943], rand)

        self.nodes[923].agregar_salida(self.nodes[944], rand)
        self.nodes[229].agregar_salida(self.nodes[944], rand)

        self.nodes[922].agregar_salida(self.nodes[945], rand)
        self.nodes[230].agregar_salida(self.nodes[945], rand)

        self.nodes[921].agregar_salida(self.nodes[946], rand)
        self.nodes[231].agregar_salida(self.nodes[946], rand)

        self.nodes[920].agregar_salida(self.nodes[947], rand)
        self.nodes[232].agregar_salida(self.nodes[947], rand)

        self.nodes[919].agregar_salida(self.nodes[948], rand)
        self.nodes[233].agregar_salida(self.nodes[948], rand)

        self.nodes[918].agregar_salida(self.nodes[949], rand)
        self.nodes[234].agregar_salida(self.nodes[949], rand)

        self.nodes[917].agregar_salida(self.nodes[950], rand)
        self.nodes[235].agregar_salida(self.nodes[950], rand)

        self.nodes[976].agregar_salida(self.nodes[951], rand)
        self.nodes[236].agregar_salida(self.nodes[951], rand)
        self.nodes[916].agregar_salida(self.nodes[951], rand)

        self.nodes[975].agregar_salida(self.nodes[952], rand)
        self.nodes[915].agregar_salida(self.nodes[975], rand)

        self.nodes[974].agregar_salida(self.nodes[953], rand)
        self.nodes[239].agregar_salida(self.nodes[953], rand)
        self.nodes[914].agregar_salida(self.nodes[974], rand)

        self.nodes[973].agregar_salida(self.nodes[954], rand)
        self.nodes[240].agregar_salida(self.nodes[954], rand)
        self.nodes[913].agregar_salida(self.nodes[973], rand)

        self.nodes[972].agregar_salida(self.nodes[955], rand)
        self.nodes[241].agregar_salida(self.nodes[955], rand)
        self.nodes[912].agregar_salida(self.nodes[972], rand)

        self.nodes[971].agregar_salida(self.nodes[956], rand)
        self.nodes[242].agregar_salida(self.nodes[956], rand)
        self.nodes[911].agregar_salida(self.nodes[971], rand)

        self.nodes[970].agregar_salida(self.nodes[957], rand)
        self.nodes[243].agregar_salida(self.nodes[957], rand)
        self.nodes[910].agregar_salida(self.nodes[970], rand)

        self.nodes[969].agregar_salida(self.nodes[958], rand)
        self.nodes[244].agregar_salida(self.nodes[958], rand)
        self.nodes[909].agregar_salida(self.nodes[969], rand)

        self.nodes[246].agregar_salida(self.nodes[959], rand)
        self.nodes[908].agregar_salida(self.nodes[959], rand)

        self.nodes[247].agregar_salida(self.nodes[960], rand)
        self.nodes[907].agregar_salida(self.nodes[960], rand)

        self.nodes[248].agregar_salida(self.nodes[961], rand)
        self.nodes[906].agregar_salida(self.nodes[961], rand)

        self.nodes[250].agregar_salida(self.nodes[962], rand)
        self.nodes[905].agregar_salida(self.nodes[962], rand)

        self.nodes[251].agregar_salida(self.nodes[963], rand)
        self.nodes[904].agregar_salida(self.nodes[963], rand)

        self.nodes[903].agregar_salida(self.nodes[964], rand)
        self.nodes[83].agregar_salida(self.nodes[964], rand)

        self.nodes[253].agregar_salida(self.nodes[965], rand)
        self.nodes[902].agregar_salida(self.nodes[965], rand)

        self.nodes[254].agregar_salida(self.nodes[966], rand)
        self.nodes[901].agregar_salida(self.nodes[966], rand)

        self.nodes[255].agregar_salida(self.nodes[967], rand)
        self.nodes[900].agregar_salida(self.nodes[967], rand)

        self.nodes[899].agregar_salida(self.nodes[968], rand)
        self.nodes[256].agregar_salida(self.nodes[968], rand)

        self.nodes[127].agregar_salida(self.nodes[296], rand)
        self.nodes[1010].agregar_salida(self.nodes[297], rand)
        self.nodes[128].agregar_salida(self.nodes[298], rand)
        self.nodes[129].agregar_salida(self.nodes[299], rand)
        self.nodes[130].agregar_salida(self.nodes[301], rand)
        self.nodes[131].agregar_salida(self.nodes[302], rand)
        self.nodes[132].agregar_salida(self.nodes[303], rand)
        self.nodes[133].agregar_salida(self.nodes[304], rand)
        self.nodes[1012].agregar_salida(self.nodes[305], rand)
        self.nodes[134].agregar_salida(self.nodes[306], rand)
        self.nodes[1011].agregar_salida(self.nodes[307], rand)
        self.nodes[135].agregar_salida(self.nodes[308], rand)
        self.nodes[1013].agregar_salida(self.nodes[309], rand)
        self.nodes[136].agregar_salida(self.nodes[310], rand)
        self.nodes[137].agregar_salida(self.nodes[311], rand)
        self.nodes[138].agregar_salida(self.nodes[312], rand)
        self.nodes[139].agregar_salida(self.nodes[313], rand)
        self.nodes[142].agregar_salida(self.nodes[315], rand)
        self.nodes[143].agregar_salida(self.nodes[316], rand)
        self.nodes[144].agregar_salida(self.nodes[317], rand)
        self.nodes[145].agregar_salida(self.nodes[318], rand)
        self.nodes[146].agregar_salida(self.nodes[319], rand)
        self.nodes[147].agregar_salida(self.nodes[320], rand)
        self.nodes[148].agregar_salida(self.nodes[321], rand)
        self.nodes[149].agregar_salida(self.nodes[322], rand)
        self.nodes[150].agregar_salida(self.nodes[323], rand)
        self.nodes[151].agregar_salida(self.nodes[324], rand)
        self.nodes[152].agregar_salida(self.nodes[325], rand)
        self.nodes[153].agregar_salida(self.nodes[326], rand)
        self.nodes[154].agregar_salida(self.nodes[327], rand)
        self.nodes[155].agregar_salida(self.nodes[328], rand)
        self.nodes[156].agregar_salida(self.nodes[329], rand)
        self.nodes[158].agregar_salida(self.nodes[330], rand)
        self.nodes[159].agregar_salida(self.nodes[331], rand)
        self.nodes[160].agregar_salida(self.nodes[332], rand)
        self.nodes[161].agregar_salida(self.nodes[336], rand)
        self.nodes[163].agregar_salida(self.nodes[337], rand)
        self.nodes[164].agregar_salida(self.nodes[338], rand)
        self.nodes[165].agregar_salida(self.nodes[339], rand)
        self.nodes[166].agregar_salida(self.nodes[340], rand)
        self.nodes[167].agregar_salida(self.nodes[341], rand)
        self.nodes[342].agregar_salida(self.nodes[168], rand)
        self.nodes[486].agregar_salida(self.nodes[169], rand)
        self.nodes[416].agregar_salida(self.nodes[486], rand)
        self.nodes[342].agregar_salida(self.nodes[415], rand)

        self.nodes[380].agregar_salida(self.nodes[377], rand)
        self.nodes[377].agregar_salida(self.nodes[380], rand)

        self.nodes[381].agregar_salida(self.nodes[376], rand)
        self.nodes[376].agregar_salida(self.nodes[381], rand)

        self.nodes[381].agregar_salida(self.nodes[450], rand)
        self.nodes[450].agregar_salida(self.nodes[381], rand)

        self.nodes[382].agregar_salida(self.nodes[375], rand)
        self.nodes[375].agregar_salida(self.nodes[382], rand)

        self.nodes[383].agregar_salida(self.nodes[449], rand)
        self.nodes[449].agregar_salida(self.nodes[383], rand)
        self.nodes[383].agregar_salida(self.nodes[374], rand)
        self.nodes[374].agregar_salida(self.nodes[383], rand)

        self.nodes[384].agregar_salida(self.nodes[448], rand)
        self.nodes[448].agregar_salida(self.nodes[384], rand)
        self.nodes[384].agregar_salida(self.nodes[373], rand)
        self.nodes[373].agregar_salida(self.nodes[384], rand)

        self.nodes[385].agregar_salida(self.nodes[372], rand)
        self.nodes[372].agregar_salida(self.nodes[385], rand)

        self.nodes[386].agregar_salida(self.nodes[447], rand)
        self.nodes[447].agregar_salida(self.nodes[386], rand)

        self.nodes[387].agregar_salida(self.nodes[371], rand)
        self.nodes[371].agregar_salida(self.nodes[387], rand)
        self.nodes[387].agregar_salida(self.nodes[446], rand)
        self.nodes[446].agregar_salida(self.nodes[387], rand)

        self.nodes[388].agregar_salida(self.nodes[444], rand)
        self.nodes[444].agregar_salida(self.nodes[388], rand)
        self.nodes[388].agregar_salida(self.nodes[370], rand)
        self.nodes[370].agregar_salida(self.nodes[388], rand)

        self.nodes[389].agregar_salida(self.nodes[369], rand)
        self.nodes[369].agregar_salida(self.nodes[389], rand)
        self.nodes[389].agregar_salida(self.nodes[443], rand)
        self.nodes[443].agregar_salida(self.nodes[389], rand)

        self.nodes[390].agregar_salida(self.nodes[442], rand)
        self.nodes[442].agregar_salida(self.nodes[390], rand)

        self.nodes[391].agregar_salida(self.nodes[368], rand)
        self.nodes[368].agregar_salida(self.nodes[391], rand)
        self.nodes[391].agregar_salida(self.nodes[441], rand)
        self.nodes[441].agregar_salida(self.nodes[391], rand)

        self.nodes[392].agregar_salida(self.nodes[367], rand)
        self.nodes[367].agregar_salida(self.nodes[392], rand)
        self.nodes[392].agregar_salida(self.nodes[440], rand)
        self.nodes[440].agregar_salida(self.nodes[392], rand)
        
        self.nodes[393].agregar_salida(self.nodes[439], rand)
        self.nodes[439].agregar_salida(self.nodes[393], rand)
        self.nodes[393].agregar_salida(self.nodes[366], rand)
        self.nodes[366].agregar_salida(self.nodes[393], rand)

        self.nodes[394].agregar_salida(self.nodes[438], rand)
        self.nodes[438].agregar_salida(self.nodes[394], rand)
        self.nodes[394].agregar_salida(self.nodes[365], rand)
        self.nodes[365].agregar_salida(self.nodes[394], rand)

        self.nodes[395].agregar_salida(self.nodes[437], rand)
        self.nodes[437].agregar_salida(self.nodes[395], rand)
        self.nodes[395].agregar_salida(self.nodes[364], rand)
        self.nodes[364].agregar_salida(self.nodes[395], rand)

        self.nodes[396].agregar_salida(self.nodes[363], rand)
        self.nodes[363].agregar_salida(self.nodes[396], rand)
        self.nodes[396].agregar_salida(self.nodes[436], rand)
        self.nodes[436].agregar_salida(self.nodes[396], rand)

        self.nodes[398].agregar_salida(self.nodes[362], rand)
        self.nodes[362].agregar_salida(self.nodes[398], rand)
        self.nodes[398].agregar_salida(self.nodes[435], rand)
        self.nodes[435].agregar_salida(self.nodes[398], rand)

        self.nodes[399].agregar_salida(self.nodes[434], rand)
        self.nodes[434].agregar_salida(self.nodes[399], rand)

        self.nodes[400].agregar_salida(self.nodes[360], rand)
        self.nodes[360].agregar_salida(self.nodes[400], rand)
        self.nodes[400].agregar_salida(self.nodes[433], rand)
        self.nodes[433].agregar_salida(self.nodes[400], rand)

        self.nodes[401].agregar_salida(self.nodes[432], rand)
        self.nodes[432].agregar_salida(self.nodes[401], rand)
        self.nodes[401].agregar_salida(self.nodes[359], rand)
        self.nodes[359].agregar_salida(self.nodes[401], rand)

        self.nodes[402].agregar_salida(self.nodes[358], rand)
        self.nodes[358].agregar_salida(self.nodes[402], rand)
        self.nodes[402].agregar_salida(self.nodes[431], rand)
        self.nodes[431].agregar_salida(self.nodes[402], rand)

        self.nodes[357].agregar_salida(self.nodes[430], rand)
        self.nodes[430].agregar_salida(self.nodes[357], rand)

        self.nodes[403].agregar_salida(self.nodes[356], rand)
        self.nodes[356].agregar_salida(self.nodes[403], rand)
        self.nodes[403].agregar_salida(self.nodes[429], rand)
        self.nodes[429].agregar_salida(self.nodes[403], rand)

        self.nodes[404].agregar_salida(self.nodes[428], rand)
        self.nodes[428].agregar_salida(self.nodes[404], rand)
        self.nodes[404].agregar_salida(self.nodes[355], rand)
        self.nodes[355].agregar_salida(self.nodes[404], rand)

        self.nodes[405].agregar_salida(self.nodes[427], rand)
        self.nodes[427].agregar_salida(self.nodes[405], rand)
        self.nodes[405].agregar_salida(self.nodes[354], rand)
        self.nodes[354].agregar_salida(self.nodes[405], rand)

        self.nodes[406].agregar_salida(self.nodes[353], rand)
        self.nodes[353].agregar_salida(self.nodes[406], rand)
        self.nodes[406].agregar_salida(self.nodes[426], rand)
        self.nodes[426].agregar_salida(self.nodes[406], rand)

        self.nodes[407].agregar_salida(self.nodes[425], rand)
        self.nodes[425].agregar_salida(self.nodes[407], rand)
        self.nodes[407].agregar_salida(self.nodes[352], rand)
        self.nodes[352].agregar_salida(self.nodes[407], rand)

        self.nodes[408].agregar_salida(self.nodes[424], rand)
        self.nodes[424].agregar_salida(self.nodes[408], rand)
        self.nodes[408].agregar_salida(self.nodes[351], rand)
        self.nodes[351].agregar_salida(self.nodes[408], rand)

        self.nodes[350].agregar_salida(self.nodes[423], rand)
        self.nodes[423].agregar_salida(self.nodes[350], rand)

        self.nodes[409].agregar_salida(self.nodes[349], rand)
        self.nodes[349].agregar_salida(self.nodes[409], rand)
        self.nodes[409].agregar_salida(self.nodes[422], rand)
        self.nodes[422].agregar_salida(self.nodes[409], rand)

        self.nodes[410].agregar_salida(self.nodes[421], rand)
        self.nodes[421].agregar_salida(self.nodes[410], rand)
        self.nodes[410].agregar_salida(self.nodes[348], rand)
        self.nodes[348].agregar_salida(self.nodes[410], rand)

        self.nodes[411].agregar_salida(self.nodes[420], rand)
        self.nodes[420].agregar_salida(self.nodes[411], rand)
        self.nodes[411].agregar_salida(self.nodes[347], rand)
        self.nodes[347].agregar_salida(self.nodes[411], rand)

        self.nodes[412].agregar_salida(self.nodes[419], rand)
        self.nodes[419].agregar_salida(self.nodes[412], rand)
        self.nodes[412].agregar_salida(self.nodes[346], rand)
        self.nodes[346].agregar_salida(self.nodes[412], rand)

        self.nodes[413].agregar_salida(self.nodes[418], rand)
        self.nodes[418].agregar_salida(self.nodes[413], rand)
        self.nodes[413].agregar_salida(self.nodes[345], rand)
        self.nodes[345].agregar_salida(self.nodes[413], rand)

        self.nodes[414].agregar_salida(self.nodes[344], rand)
        self.nodes[344].agregar_salida(self.nodes[414], rand)
        self.nodes[414].agregar_salida(self.nodes[417], rand)
        self.nodes[417].agregar_salida(self.nodes[414], rand)

        self.nodes[417].agregar_salida(self.nodes[485], rand)
        self.nodes[485].agregar_salida(self.nodes[417], rand)

        self.nodes[418].agregar_salida(self.nodes[484], rand)
        self.nodes[484].agregar_salida(self.nodes[418], rand)

        self.nodes[421].agregar_salida(self.nodes[482], rand)
        self.nodes[482].agregar_salida(self.nodes[421], rand)

        self.nodes[422].agregar_salida(self.nodes[481], rand)
        self.nodes[481].agregar_salida(self.nodes[422], rand)

        self.nodes[423].agregar_salida(self.nodes[480], rand)
        self.nodes[480].agregar_salida(self.nodes[423], rand)

        self.nodes[424].agregar_salida(self.nodes[479], rand)
        self.nodes[479].agregar_salida(self.nodes[424], rand)

        self.nodes[425].agregar_salida(self.nodes[478], rand)
        self.nodes[478].agregar_salida(self.nodes[425], rand)

        self.nodes[426].agregar_salida(self.nodes[475], rand)
        self.nodes[475].agregar_salida(self.nodes[426], rand)
        self.nodes[475].agregar_salida(self.nodes[473], rand)
        self.nodes[473].agregar_salida(self.nodes[475], rand)

        self.nodes[427].agregar_salida(self.nodes[473], rand)
        self.nodes[473].agregar_salida(self.nodes[427], rand)
        self.nodes[473].agregar_salida(self.nodes[471], rand)
        self.nodes[471].agregar_salida(self.nodes[473], rand)

        self.nodes[428].agregar_salida(self.nodes[471], rand)
        self.nodes[471].agregar_salida(self.nodes[428], rand)
        self.nodes[471].agregar_salida(self.nodes[469], rand)
        self.nodes[469].agregar_salida(self.nodes[471], rand)

        self.nodes[429].agregar_salida(self.nodes[469], rand)
        self.nodes[469].agregar_salida(self.nodes[429], rand)
        self.nodes[469].agregar_salida(self.nodes[467], rand)
        self.nodes[467].agregar_salida(self.nodes[469], rand)

        self.nodes[430].agregar_salida(self.nodes[467], rand)
        self.nodes[467].agregar_salida(self.nodes[430], rand)

        self.nodes[476].agregar_salida(self.nodes[474], rand)
        self.nodes[474].agregar_salida(self.nodes[476], rand)
        self.nodes[474].agregar_salida(self.nodes[472], rand)
        self.nodes[472].agregar_salida(self.nodes[474], rand)
        self.nodes[472].agregar_salida(self.nodes[470], rand)
        self.nodes[470].agregar_salida(self.nodes[472], rand)
        self.nodes[470].agregar_salida(self.nodes[468], rand)
        self.nodes[468].agregar_salida(self.nodes[470], rand)

        self.nodes[432].agregar_salida(self.nodes[465], rand)
        self.nodes[465].agregar_salida(self.nodes[432], rand)

        self.nodes[433].agregar_salida(self.nodes[464], rand)
        self.nodes[464].agregar_salida(self.nodes[433], rand)

        self.nodes[434].agregar_salida(self.nodes[463], rand)
        self.nodes[463].agregar_salida(self.nodes[434], rand)

        self.nodes[435].agregar_salida(self.nodes[462], rand)
        self.nodes[462].agregar_salida(self.nodes[435], rand)

        self.nodes[436].agregar_salida(self.nodes[461], rand)
        self.nodes[461].agregar_salida(self.nodes[436], rand)

        self.nodes[437].agregar_salida(self.nodes[460], rand)
        self.nodes[460].agregar_salida(self.nodes[437], rand)

        self.nodes[438].agregar_salida(self.nodes[459], rand)
        self.nodes[459].agregar_salida(self.nodes[438], rand)

        self.nodes[441].agregar_salida(self.nodes[457], rand)
        self.nodes[457].agregar_salida(self.nodes[441], rand)

        self.nodes[443].agregar_salida(self.nodes[455], rand)
        self.nodes[455].agregar_salida(self.nodes[443], rand)

        self.nodes[444].agregar_salida(self.nodes[454], rand)
        self.nodes[454].agregar_salida(self.nodes[444], rand)

        self.nodes[445].agregar_salida(self.nodes[453], rand)
        self.nodes[453].agregar_salida(self.nodes[445], rand)

        self.nodes[448].agregar_salida(self.nodes[451], rand)