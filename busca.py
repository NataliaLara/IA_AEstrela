import pandas as pd 
import os

#h(n): Mostra todas as distancias (estimadas) em linha reta ate bucharest
def dist_linha_reta (cidade):	
	for index, row in distToBuch.iterrows():
		if(row['City']==cidade):
			return row['DistanceToBucharest']
	    #print (row['City'], row['DistanceToBucharest'])	

distToBuch = pd.read_csv('distanceToBucharest.csv', delimiter=',')
aCityToB = pd.read_csv('AcityToBcityDistance.csv',delimiter=',')

#print(aCityToB)
origem = 'Arad'
destino = 'Bucharest'
visitadas =[]

custoAtual=distToBuch.loc[0,'DistanceToBucharest'] #custo de arad
custoTotCidade=100000
gn=0
gnAnterior=0
print ('Cidade\t\t g(n)\t h(n)\t f(n)')
visitadas.append(origem)
proximaCidade=origem

while (origem!='Bucharest'):
	print('\n')
	for index, row in aCityToB.iterrows():
		if(row['OriginCity']==origem):
			hn=dist_linha_reta(row['FinalCity'])	#custo estimado de n até o objetivo
			gn = gnAnterior + row['Distance']	#custo até o momento para alcançar n
			fn=gn+hn	#custo total estimado do caminho até o objetivo
						
			print(row['FinalCity'],"\t\t",gn,"\t",hn,"\t",fn)

			if(fn<custoTotCidade):			
				cid=0
				for cidade in visitadas:
					if(cidade==row['FinalCity']):
						cid=1
						print('\tCidade ja visitadada')

				if(cid==0):
					custoTotCidade=fn
					gnFuturo = gn
					proximaCidade = row['FinalCity']
					#print ('Cid',row['OriginCity'], row['FinalCity'],row['Distance']) 

	origem=proximaCidade
	gnAnterior = gnFuturo
	custoAtual = custoAtual + custoTotCidade 
	visitadas.append(proximaCidade)	
	custoTotCidade=100000
	#print (row['OriginCity'], row['FinalCity'],row['Distance']) 

print('\ncaminho:')   		
for cidade in visitadas:
	print(cidade)		

print('Custo: ',custoAtual) # precisa revisar o conceito do custo geral
