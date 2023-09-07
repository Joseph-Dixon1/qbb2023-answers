#!/usr/bin/env python 
# input needs to be all the integers divided by the sum 

def list_average(mylist): 
	total=0
	for i in mylist: 
		total += i 
	#take it out of the loop because add together before taking the avg 
	avg=total/len(mylist)
	return avg

random_list_of_integers=[2,4,6,8,10]

print(list_average(random_list_of_integers))




