#!/usr/bin/env python 
import numpy as np 
def list_average(mylist): 
	total=0
	for i in mylist: 
		total += i 
	#take it out of the loop because add together before taking the avg 
	avg=total/len(mylist)
	return avg

series_of_integers=open("my_integers.txt",'r')
integer_data=series_of_integers.readlines()

integer_list=[]
for lines in integer_data: 
	integer_data1=lines.rstrip('\n')
	integer_data1=int(integer_data1)
	integer_list.append(integer_data1)

print(integer_list)

# print(integer_data)

print(list_average(integer_list))
