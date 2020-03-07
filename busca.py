import pandas as pd 
import os
path = os.getcwd()

distToBuch = pd.read_csv('distanceToBucharest.csv', delimiter=';')
aCityToB = pd.read_csv('AcityToBcityDistance.csv')

print(distToBuch['City'])
#print(distToBuch['DistanceToBucharest'])
#for row in distToBuch:
	#print(row)

#for row,index in distToBuch.iterrows():
#	print(row)

for index, row in distToBuch.iterrows():
    print (row['City'], row['DistanceToBucharest'])
 

