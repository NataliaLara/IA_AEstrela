import pandas as pd

def pega_distancia_ate_destino(cidade):
    for row, index in dist_linha_reta.iterrows():
        if cidade == row:
            return index['DistanceToBucharest']

def pega_distancia_cidadeAtual_cidadeAdjacente(cidade_origem, cidade_atual):
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
        dist = pre_gn+pre_hn
        #print("Cidade: ", cidade)
        #print("Distancia total: ", dist)
        for row, index in grafo.iterrows():
            if cidade == row and aux >= dist:
                aux = dist
                cidade_atual = cidade
                gn = pega_distancia_cidadeAtual_cidadeAdjacente(cidade_origem=origem, cidade_atual=cidade_atual)
                hn = pega_distancia_ate_destino(cidade_atual)
    
    return cidade_atual, gn, hn

def verifica_outro_caminho(cidade_atual, lista_cidades, custo):
    for cidade in lista_cidades:
        if cidade != cidade_atual:
            proxima_cidade, gn, hn = visita_menor_distancia(cidade_atual, lista_cidades)
            fn = gn+hn+pega_distancia_cidadeAtual_cidadeAdjacente(cidade_atual, proxima_cidade)
            if custo > fn:
                lista_cidades += pega_cidades_adjacentes(proxima_cidade)
                return lista_cidades, fn, True
            else:
                return False
        

def busca(cidade_origem, cidades_adj, destino, custo_total):
    cidade_atual, gn_1, hn_1 = visita_menor_distancia(origem=cidade_origem,lista_cidades=cidades_adj)
    print('Cidade Atual: ', cidade_atual)
    print('g(n): ', gn_1)
    print('h(n): ', hn_1)
    cidades_adj += pega_cidades_adjacentes(cidade_atual)
    fn_1 =custo_total+gn_1+hn_1
    print(cidades_adj)
    print(fn_1)
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



