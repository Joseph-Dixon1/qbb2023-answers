#!/usr/bin/env python 



import numpy as np 
def take_patient_row(fname,index):
	arthritis=open(fname,"r")
	arthritis_data=arthritis.readlines()
	poi=arthritis_data[index]
	poi=poi.rstrip('\n')
	poi=poi.split(',')
	poi_int=[]
	for item in poi: 
		poi_int.append(int(item))
	return np.mean(poi_int)

print(take_patient_row("/Users/cmdb/Desktop/swc-python/inflammation-01.csv", 12))


'''
data_dictionary={}
for lines in arthritis_data: 
	arthritis_data_stripped=lines.rstrip('\n')
	arthritis_data_split=arthritis_data_stripped.split(',')
	data_dictionary[+1]=int(arthritis_data_split)
print(data_dictionary)
'''

#take_patient_row("/Users/cmdb/Desktop/swc-python/inflammation-02.csv", 12)
#take_patient_row("/Users/cmdb/Desktop/swc-python/inflammation-03.csv", 12)
#take_patient_row("/Users/cmdb/Desktop/swc-python/inflammation-04.csv", 12)