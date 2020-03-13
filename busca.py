import pandas as pd 
import os


class cidade:
	def __init__(self, nome,fn,gn):
		self.nome = nome
		self.fn=fn
		self.gn=gn
	def __repr__(self):
		return str(self.__dict__)
	def setNome(self, nome):
		self.nome = nome
	def setGn(self, gn):
		self.gn = gn
	def setFn(self, fn):
		self.fn = fn
	def getGn(self):
		return self.gn
	def getFn(self):
		return self.fn
	def getNome(self):
		return self.nome

#h(n): Mostra todas as distancias (estimadas) em linha reta ate bucharest
def pega_distancia_ate_destino (cidade):	
	for index, row in dist_linha_reta.iterrows():
		if(row['City']==cidade):
			return row['DistanceToBucharest']
	    #print (row['City'], row['DistanceToBucharest'])	

def retira_cidade_borda(cidade):
	for row in cidades_borda:
		if row.nome==cidade:
			cidades_borda.remove(row)

def printf (text):
    print(text, end="")

def imprime_borda():
	printf('[')
	for row in cidades_borda:
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
			return row.nome

def pega_menor_custo_borda (): #menor fn
	menor=10000000
	for row in cidades_borda:
		if(row.fn<menor):
			menor=row.fn
	return menor

def pega_gn_cidade_menor_custo_borda (cidade): #menor fn
	for row in cidades_borda:
		if (row.nome==cidade):
			return row.gn

def pega_cidades_adjacentes(cidade):
    lista_cidades = []
    for index, row in grafo.iterrows():
        if cidade == row['OriginCity']:			
            lista_cidades.append(row['FinalCity'])
        
    return lista_cidades


dist_linha_reta = pd.read_csv('distanceToBucharest.csv', delimiter=',')
grafo = pd.read_csv('AcityToBcityDistance.csv',delimiter=',')

origem = 'Arad'
destino = 'Bucharest'
visitadas =[]

fn=dist_linha_reta.loc[0,'DistanceToBucharest'] #custo de arad
menorCusto=100000
gn=0
print ('Cidade\t\tg(n)\th(n)\tf(n)\n')
visitadas.append(origem)
proximaCidade=origem
gnAnterior=0 #toda borda que ainda pode ser explorada
cidades_borda= []
cidades_borda.append(cidade(origem,fn,gn))

while(origem!=destino ):
	print('Cidade atual:',origem)
	for index, row in grafo.iterrows():
		if(row['OriginCity']==origem):	
			retira_cidade_borda(origem)
			hn=pega_distancia_ate_destino(row['FinalCity'])#custo estimado de n até o destino
			gn= gnAnterior + row['Distance'] #custo até o momento para alcançar n
			fn=gn+hn	#custo total estimado do caminho até o objetivo
			print(row['FinalCity'],'\t\t',gn,'\t',hn,'\t',fn)			
			cidade_adjacente=row['FinalCity']
			if(cidade_adjacente in visitadas):
				print('Ja foi visitada', cidade_adjacente)
			else:
				cidades_borda.append(cidade(cidade_adjacente,fn,gn))
				
	print('borda: ',end="")
	imprime_borda()
	origem = pega_cidade_menor_custo_borda()
	gnAnterior=pega_gn_cidade_menor_custo_borda(origem)	
	visitadas.append(origem)
	print('\n')		


print('Custo do caminho:',pega_menor_custo_borda())
print('borda: ',end="")
imprime_borda()
print('visitadas: ',visitadas)
