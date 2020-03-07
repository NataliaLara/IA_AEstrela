import pandas as pd 
import os
path = os.getcwd()

distToBuch = pd.read_csv('distanceToBucharest.csv', delimiter=';')
aCityToB = pd.read_csv('AcityToBcityDistance.csv',delimiter=';')

#print(distToBuch['City']) 
#print(distToBuch['DistanceToBucharest'])
#for row in distToBuch:
	#print(row)

for index, row in distToBuch.iterrows():
    print (row['City'], row['DistanceToBucharest'])

for index, row in aCityToB.iterrows():
    print (row['OriginCity'], row['FinalCity'],row['Distance'])
 

