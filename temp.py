import pandas as pd

def pega_distancia_ate_destino(cidade):
    for row, index in dist_linha_reta.iterrows():
        if cidade == row:
            return index['DistanceToBucharest']

def pega_distancia_cidadeAtual_cidadeAdjacente(cidade_origem, cidade_atual):
    if cidade_origem == cidade_atual:
        return 0
    for row, index in grafo.iterrows():
        if cidade_origem == row and index['FinalCity'] == cidade_atual:
            return index['Distance']

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
        
    return cidade_atual, gn, hn

def verifica_cidade_anterior (cidade_atual, cidade_anterior, l_cidades_adj, l_cidades_vis):
    custo_anterior = 0
    custo = pega_distancia_ate_destino(cidade_anterior) #hn
    possivel_cidade = 'Null'
    print('\t\t--Verificando cidade anterior--\t\t')
    print("Cidade Anterior: ", cidade_anterior)
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
        
    print("Cidade Anterior: ", possivel_cidade)
    print("Custo Anterior: ", custo_anterior)
    return possivel_cidade, custo_anterior

def verifica_outro_caminho(cidade_origem, cidade_atual, cidade_anterior, l_cidades_adj, l_cidades_vis):
    print("ANTERIOR: ", cidade_anterior)
    #print("TOTAL: ", total)
    gn = pega_distancia_cidadeAtual_cidadeAdjacente(cidade_anterior, cidade_atual)
    hn = pega_distancia_ate_destino(cidade_atual)
    custo = gn+hn
    print("GN: ", gn)
    custo = pega_distancia_ate_destino(cidade_atual) #hn
    possivel_cidade = 'Null'
    custo_anterior = 0
    if cidade_atual != cidade_anterior:
        menor_cidade_anterior, custo_anterior = verifica_cidade_anterior(cidade_atual, cidade_anterior, l_cidades_adj, l_cidades_vis)
    print('\t\t--Verificando outro caminho--\t\t')
    print("Cidade Atual: ", cidade_atual)
    print("Custo: ", custo)
    print("Lista Adj: ", l_cidades_adj)
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
    cidade_anterior = cidade_origem
    fn_1 = custo_total
    fn_2 = custo_total
    fn = 0
    cidades_visitadas = [cidade_origem]
    cidade_atual, gn_1, hn_1 = visita_menor_distancia(origem=cidade_origem,lista_cidades=cidades_adj)
    while cidade_atual != destino:
        print('Cidade Atual(busca): ', cidade_atual)
        cidade_anterior = cidades_visitadas[0]
        cidades_visitadas.insert(0, cidade_atual)
        #print('g(n): ', gn_1)
        #print('h(n): ', hn_1)
        fn_1 +=gn_1+hn_1
        #print(cidades_adj)
        #print(fn_1)
        outra_cidade = verifica_outro_caminho(cidade_origem=cidade_origem,cidade_atual=cidade_atual, cidade_anterior=cidade_anterior, l_cidades_adj=cidades_adj, l_cidades_vis=cidades_visitadas)
        print("Possivel Cidade: ", outra_cidade)
        gn_2 = pega_distancia_cidadeAtual_cidadeAdjacente(cidade_origem=cidade_atual, cidade_atual=outra_cidade)
        if outra_cidade is not 'Null' and gn_2 is not None:
            hn_2 = pega_distancia_ate_destino(cidade=outra_cidade)
            fn_2 += gn_2+hn_2
            #print("Custo 2: ", fn_2)

            if fn_1 > fn_2:
                cidade_atual = outra_cidade
                fn = fn_2 
            else:
                fn = fn_1
        else:
            fn += fn_1
        #cidade_atual, gn_1, hn_1 = visita_menor_distancia(origem=cidade_origem,lista_cidades=cidades_adj)
        if cidade_atual in cidades_adj:
            cidades_adj.remove(cidade_atual)
        cidades_adj += pega_cidades_adjacentes(cidade=cidade_atual)
        
        custo_total += fn
        print('Custo(busca): ', custo_total)    
        '''
        ----IDEIA:---- 
        *add na lista os adjacentes de cada cidade
        *olhar na lista se ha alguma cidade cujo custo eh menor do que o que se calculou
        *se tiver, ir por essa cidade
        *se nao tiver, continuar a busca normalmente
        '''
        '''
        while(cidade_atual != destino):
            lista_cidades_aux, custo_aux, nova_verificacao = verifica_outro_caminho(cidade_atual=cidade_atual, 
                                                                                    lista_cidades=cidades_adj,custo=fn_1)
            if(nova_verificacao):
                fn_1 = custo_aux
                cidades_adj += lista_cidades_aux

        
            print(cidade_atual)
        '''

dist_linha_reta = pd.read_csv('distanceToBucharest.csv', index_col=['City'])
grafo = pd.read_csv('AcityToBcityDistance.csv', index_col=['OriginCity'])

#valores iniciais
origem = 'Arad'
destino = 'Bucharest'
fn = pega_distancia_ate_destino(cidade=origem)
cidades_adjacentes = pega_cidades_adjacentes(cidade=origem)
busca(cidade_origem=origem,cidades_adj=cidades_adjacentes, destino=destino, custo_total=fn)



