import pandas as pd 
import os
path = os.getcwd()

#h(n): Mostra todas as distancias (estimadas) em linha reta ate bucharest
def custoCiToBu (cidade):	
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
custoAtual=0 #f(n)

custoTotCidade=100000
gn=0
gnAnterior=0
print ('City\t\t gn\t hn\t fn')
proximaCidade=origem
visitadas.append(proximaCidade)


while (origem!='Bucharest'):
	print('\n')
	for index, row in aCityToB.iterrows():
		if(row['OriginCity']==origem):
			hn=custoCiToBu(row['FinalCity'])	#custo estimado de n até o objetivo
			gn = gnAnterior + row['Distance']	#custo até o momento para alcançar n
			fn=gn+hn	#custo total estimado do caminho até o objetivo
						
			print(row['FinalCity'],'\t\t',gn,'\t',hn,'\t',fn)

			if(fn<custoTotCidade):			
				cid=0
				for cidade in visitadas:
					if(cidade==row['FinalCity']):
						cid=1
						print('\tCidade já visitadada')

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