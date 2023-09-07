#!/usr/bin/env python 

import numpy as np 
'''
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
'''

def patient_difference(fname, index1, index2):
	arthritis=open(fname, 'r')
	arthritis_data=arthritis.readlines()
	poi1=arthritis_data[index1]
	poi2=arthritis_data[index2]
	poi1=poi1.rstrip('\n')
	poi1=poi1.split(',')
	poi2=poi2.rstrip('\n')
	poi2=poi2.split(',')
	poi1list=[]
	for item in poi1:
		poi_int1=int(item)
		poi1list.append(poi_int1)
	poi2list=[]
	for item in poi2:
		poi_int2=int(item)
		poi2list.append(poi_int2)
	return(np.array(poi2list)-np.array(poi1list))

print(patient_difference("/Users/cmdb/Desktop/swc-python/inflammation-01.csv", 2, 3))




