import pandas as pd

def pega_distancia_ate_destino(cidade):
    distancia = 0
    for row, index in dist_linha_reta.iterrows():
        if cidade == row:
            distancia = index['DistanceToBucharest']
    if distancia is not None: return distancia
    else: return 0

def pega_distancia_cidadeAtual_cidadeAdjacente(cidade_origem, cidade_atual):
    distancia = 0
    if cidade_origem == cidade_atual:
        return 0
    for row, index in grafo.iterrows():
        if cidade_origem == row and index['FinalCity'] == cidade_atual:
            distancia = index['Distance']
    
    if distancia is None: return 0
    else: return distancia

def pega_cidades_adjacentes(cidade):
    lista_cidades = []
    for row, index in grafo.iterrows():
        if cidade == row:
            lista_cidades.append(index['FinalCity'])
        
    return lista_cidades

def visita_menor_distancia(origem, lista_cidades):
    aux = 100000
    for cidade in lista_cidades:
        pre_gn = pega_distancia_cidadeAtual_cidadeAdjacente(cidade_origem=origem, cidade_atual=cidade)
        pre_hn = pega_distancia_ate_destino(cidade)
        if pre_gn is not None:
            dist = pre_gn+pre_hn 
        else:
            dist=-1
        #print("Cidade: ", cidade)
        #print("Distancia total: ", dist)
        for row, index in grafo.iterrows():
            if dist > 0:
                if cidade == row and aux >= dist and pre_gn is not None:
                    aux = dist
                    cidade_atual = cidade
                    gn = pega_distancia_cidadeAtual_cidadeAdjacente(cidade_origem=origem, cidade_atual=cidade_atual)
                    hn = pega_distancia_ate_destino(cidade_atual)
        
    return cidade_atual

def verifica_cidade_anterior (cidade_atual, cidade_anterior, l_cidades_adj, l_cidades_vis):
    custo_anterior = 0
    custo = pega_distancia_ate_destino(cidade_anterior) #hn
    possivel_cidade = 'Null'
    #print('\t\t--Verificando cidade anterior--\t\t')
    #print("Cidade Anterior: ", cidade_anterior)
    for cidade in l_cidades_adj:
        gn = pega_distancia_cidadeAtual_cidadeAdjacente(cidade_anterior, cidade)
        hn = pega_distancia_ate_destino(cidade)
        if cidade != cidade_atual and gn is not None and cidade and cidade in l_cidades_vis:
            custo += gn
            fn = gn+hn
            print("f(n): ", fn)
            print("Custo: ", custo)
            if custo > fn:
                possivel_cidade = cidade
                custo_anterior = custo
            else:
                possivel_cidade = 'Null'
                custo_anterior = 0
        
    #print("Cidade Anterior: ", possivel_cidade)
    #print("Custo Anterior: ", custo_anterior)
    return possivel_cidade, custo_anterior

def verifica_outro_caminho(cidade_origem, cidade_atual, cidade_anterior, l_cidades_adj, l_cidades_vis, acumulo):
    #print("ANTERIOR: ", cidade_anterior)
    #print("TOTAL: ", total)
    custo = pega_distancia_ate_destino(cidade_atual) #hn
    possivel_cidade = 'Null'
    custo_anterior = 0
    #print("Acumulo: ", acumulo)
    if cidade_atual != cidade_anterior:
        menor_cidade_anterior, custo_anterior = verifica_cidade_anterior(cidade_atual, cidade_anterior, l_cidades_adj, l_cidades_vis)
    #print('\t\t--Verificando outro caminho--\t\t')
    #print("Cidade Atual: ", cidade_atual)
    #print("Custo: ", custo)
    #print("Lista Adj: ", l_cidades_adj)
    for cidade in l_cidades_adj:
        #print("Cidade: ", cidade)
        gn = pega_distancia_cidadeAtual_cidadeAdjacente(cidade_origem=cidade_anterior, cidade_atual=cidade_atual)
        hn = pega_distancia_ate_destino(cidade)
        #print("g(n): ", gn)
        if cidade != cidade_atual and gn is not None and cidade not in l_cidades_vis:
            #proxima_cidade, gn, hn = visita_menor_distancia(cidade_atual, l_cidades_adj)
            custo += gn
            fn = gn+hn
            #print("f(n): ", fn)
            if custo > fn:
                possivel_cidade = cidade
            elif custo_anterior < fn and custo_anterior != 0:
                possivel_cidade = cidade_anterior
            else:
                possivel_cidade = 'Null'
    #print("Possivel_cidade: ", possivel_cidade)
    return possivel_cidade
        

def busca(cidade_origem, cidades_adj, destino, custo_total):
    custo_total = 0
    cidade_anterior = cidade_origem
    fn_1 = 0
    fn_2 = 0
    fn = 0
    cidades_visitadas = [cidade_origem]
    cidade_atual = visita_menor_distancia(cidade_origem, cidades_adj)
    gn = 0
    cont = 0
    while cidade_atual != destino:
        cont +=1
        if cont == 1: gn_1 = 0
        else:
            gn_1 = gn+pega_distancia_cidadeAtual_cidadeAdjacente(cidade_anterior, cidade_atual)
        hn_1 = pega_distancia_ate_destino(cidade_atual)
        print('Cidade Origem: ', cidade_anterior)
        print('Cidade Atual(busca): ', cidade_atual)
        print('g(n): ', gn)
        cidade_anterior = cidades_visitadas[0]
        cidades_visitadas.insert(0, cidade_atual)
        print('g1(n): ', gn_1)
        print('h1(n): ', hn_1)
        fn_1 =gn_1+hn_1
        print(cidades_adj)
        print('f1(n): ',fn_1)
        outra_cidade = verifica_outro_caminho(cidade_origem=cidade_origem,cidade_atual=cidade_atual, cidade_anterior=cidade_anterior, l_cidades_adj=cidades_adj, l_cidades_vis=cidades_visitadas, acumulo=gn)
        print("Possivel Cidade: ", outra_cidade)
        gn_2 = gn+pega_distancia_cidadeAtual_cidadeAdjacente(cidade_origem=cidade_anterior, cidade_atual=outra_cidade)
        if outra_cidade is not 'Null' and gn_2 is not None:
            hn_2 = pega_distancia_ate_destino(cidade=outra_cidade)
            fn_2 = gn_2+hn_2
            print('g2(n): ', gn_2)
            print('h2(n): ', hn_2)
            print("f2(n): ", fn_2)

            if fn_1 > fn_2:
                cidade_atual = outra_cidade
                fn = fn_2
                gn +=gn_2 
            else:
                fn = fn_1
                gn +=gn_1
        else:
            fn = fn_1
            gn +=gn_1
        #cidade_atual, gn_1, hn_1 = visita_menor_distancia(origem=cidade_origem,lista_cidades=cidades_adj)
        if cidade_atual in cidades_adj:
            cidades_adj.remove(cidade_atual)
        cidades_adj += pega_cidades_adjacentes(cidade=cidade_atual)
        print("fn_TOTAL", fn)
        custo_total += fn+gn
        print('Custo(busca): ', custo_total)  
        f1_n = 0
        f2_n = 0  
       
dist_linha_reta = pd.read_csv('distanceToBucharest.csv', index_col=['City'])
grafo = pd.read_csv('AcityToBcityDistance.csv', index_col=['OriginCity'])

#valores iniciais
origem = 'Arad'
destino = 'Bucharest'
fn = pega_distancia_ate_destino(cidade=origem)
cidades_adjacentes = pega_cidades_adjacentes(cidade=origem)
busca(cidade_origem=origem,cidades_adj=cidades_adjacentes, destino=destino, custo_total=fn)



