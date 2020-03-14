import pandas as pd 
import argparse
import os


class cidade:
	def __init__(self, nome,fn,gn,cidade_pai):
		self.nome = nome
		self.fn=fn
		self.gn=gn
		self.cidade_pai=cidade_pai
	def __repr__(self):
		return str(self.__dict__)
#h(n): Mostra todas as distancias (estimadas) em linha reta ate bucharest
def pega_hn_ate_destino(arquivo,origem):
	for inex,row in arquivo.iterrows():
		if origem==row['City']:
			return row['DistanceToBucharest']	

def retira_cidade_borda(cidade):
	for row in cidades_borda:
		if row.nome==cidade.nome:
			cidades_borda.remove(row)

def pega_caminho_otimo(origem,destino,visitadas):
	atual=destino
	caminho_invertido = []
	
	while atual!=origem:
		caminho_invertido.append(atual)
		for row in visitadas:
			#print (row.nome,row.fn)
			if(row.nome==atual):
				atual=row.cidade_pai
	caminho_invertido.append(origem)
	caminho=[]
	i=len(caminho_invertido)-1
	while i >=0:
		caminho.append(caminho_invertido[i])	
		i=i-1

	return caminho

def printf (text):
    print(text, end="")

def imprime_cidades(cidades):
	printf('[')
	for row in cidades:
		text=row.nome,row.fn		
		printf(text)
	print(']')

def pega_fn_cidade (cidade):
	for row in cidades_borda:
		if (row.nome==cidade):
			return row.fn 

def pega_cidade_menor_custo_borda (): #menor fn
	menor=pega_menor_custo_borda()
	for row in cidades_borda:
		if(row.fn==menor):
			return row

def pega_menor_custo_borda (): #menor fn
	menor=10000000
	for row in cidades_borda:
		if(row.fn<menor):
			menor=row.fn
	return menor

def pega_gn_cidade_menor_custo_borda (cidade): #menor fn
	for row in cidades_borda:
		if (row.nome==cidade.nome):
			return row.gn

def pega_cidades_adjacentes(cidade):
    lista_cidades = []
    for index, row in grafo.iterrows():
        if cidade == row['OriginCity']:			
            lista_cidades.append(row['FinalCity'])
        
    return lista_cidades



parser = argparse.ArgumentParser()
parser.add_argument('cidade_origem', help='Cidade de origem: De onde voce esta saindo.', type=str)
parser.add_argument('cidade_destino', help='Cidade de destino: Onde voce quer chegar.', type=str)
args = parser.parse_args()

dist_linha_reta = pd.read_csv('distanceToBucharest.csv', delimiter=',')
grafo = pd.read_csv('AcityToBcityDistance.csv',delimiter=',')


origem = args.cidade_origem
destino = args.cidade_destino
visitadas =[]

hn=pega_hn_ate_destino(dist_linha_reta,origem) #custo da cidade, neste caso 


gn=0
#print ('Cidade\t\tg(n)\th(n)\tf(n)\n')
#visitadas.append(origem)

gnAnterior=0 #toda borda que ainda pode ser explorada
cidades_borda= []
cidade_origem=cidade(origem,hn,gn,'0') # neste caso fn=hn
cidades_borda.append(cidade_origem)
visitadas.append(cidade_origem)
while(cidade_origem.nome!=destino):
	print('Cidade atual:',cidade_origem)
	for index, row in grafo.iterrows():
		if(row['OriginCity']==cidade_origem.nome):	
			retira_cidade_borda(cidade_origem)
			hn=pega_hn_ate_destino(dist_linha_reta,row['FinalCity'])#custo estimado de n até o destino
			gn= gnAnterior + row['Distance'] #custo até o momento para alcançar n
			fn=gn+hn	#custo total estimado do caminho até o objetivo
			#print(row['FinalCity'],'\t\t',gn,'\t',hn,'\t',fn)			
			cidade_adjacente=row['FinalCity']

			#if(cidade_adjacente in visitadas):
			#	print('Ja foi visitada', cidade_adjacente)
			#else:
			cidades_borda.append(cidade(cidade_adjacente,fn,gn,cidade_origem.nome))
				
	print('borda: ',end="")
	imprime_cidades(cidades_borda)
	cidade_anterior=cidade_origem
	cidade_origem = pega_cidade_menor_custo_borda()
	gnAnterior=cidade_origem.gn
	visitadas.append(cidade_origem)
	print('\n')		

print('Custo do caminho:',pega_menor_custo_borda())
#print('borda: ',end="")
#imprime_cidades(cidades_borda)
#print('Visitadas: ',end="")
#imprime_cidades(visitadas)

caminho_otimo=pega_caminho_otimo(origem,destino,visitadas)

print('Caminho ótimo: ',caminho_otimo)