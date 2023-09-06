#!/usr/bin/env python


#EXERCISE 1 
print('Exercise 1')
arthritis=open("inflammation-01.csv","r")
arthritis_data=arthritis.readlines()

# Approaching the first problem 
#take entire data set, for loop to split it up so each patient had it's own list, call up fourth element of large list, values for fifth patient and call specific days. A nested list. 


# takes it from the row whatever 
fifth_patient=arthritis_data[4]
#remove \n from the row of string 
fifth_patient1=fifth_patient.rstrip('\n')
# check if line disappears that \n creates 
#splitting based on commas, working with string at this point 
# can't use rstrip on lists, only with lines of string, or integers to strip of specific
#things 
fifth_patient2=fifth_patient1.split(',')
#Pull out first, 10th, and last of data 
print('First day is', fifth_patient2[0], '\n10th Day is', fifth_patient2[9],' \nLast day is', fifth_patient2[-1])



#Calculate averages for every given patient 
#Very similar to code we did with Rajiv, import numpy and create an empty list. For each patient in range 10, find the mean and add that to the list 
#Don't always need to create a list, as you loop through you could just print 


#EXERCISE 2
print('Exercise 2')
#set up an empty list to fill up with row averages 
# need a nested for loop because as you loop through rows, save 
# as variable and then find the average 

flare_avg=[]
#parse through data 

for line in arthritis_data: 
	line1=line.rstrip('\n')
	line2=line1.split(',')
	sum=0
	for day in line2:
		day_int=int(day)
		sum += day_int
	avg=sum/len(line)
	flare_avg.append(avg)
print(flare_avg[0:9])

	
		

'''
for line in arthritis_data: 
	line=line.rstrip()
	line_list=line.split()
	avg=int(line_list)
	flare_avg.append(avg)
print(numpy.mean(flare_avg))
'''

#Find highest and lowest w/max and min functions of numpy 

#EXERCISE 3
print('Exercise 3')
import numpy
print(numpy.max(flare_avg))
print(numpy.min(flare_avg))


#extract flare ups for patient 1 and 5 in list. create a second loop over the range of days, within that loop index the two lists and take the difference 


#EXERCISE 4
print('Exercise 4')
#define patient variables and create empty lists for later comparison 
patient1=[]
patient5=[]

#already paresed patient 5 in exercise 1 
for day in fifth_patient2:
	#making an integer I guess? for a reason I don't know 
	five_int=int(day)
	#adding to the empty patient 5 list 
	patient5.append(five_int)

#parse through patient 1 data 
first_patient=arthritis_data[0]
first_patient1=first_patient.rstrip('\n')
first_patient2=first_patient1.split(',')

#now add to patient 1 empty list 
for day in first_patient2:
	#need to convert the str data to integers for the computation part 
	one_int=int(day)
	patient1.append(one_int)

#add to the patient data 
Patient_Data=[]
#range is the length of one of the patients, they both have same # of columns 
for i in range(len(patient5)):
	difference_in_data=patient5[i]-patient1[i]
	#add to the empty patient comparison list 
	Patient_Data.append(difference_in_data)
print(Patient_Data)




#Exercise 1
#First day is 0 
#10th Day is 4  
#Last day is 1

# I had a max of 7 and a min of 2 before I started messing with it to get the first 10 values and suddenly I couldn't figure out what was happening 

#Exercise 2
#[2.5348837209302326, 2.465909090909091, 2.7111111111111112, 2.6818181818181817, 2.5813953488372094, 2.8295454545454546, 2.7471264367816093, 2.9555555555555557, 2.849462365591398]

#Exercise 3
#3.10752688172043
#2.375

#Exercise 4
#[0, 1, 0, 0, 2, -1, -1, -2, -6, 1, 1, 4, -4, 0, -4, 6, 1, 3, -6, -1, 3, 1, -2, -4, 6, 2, 8, 0, -1, -1, 5, 2, -2, -5, -1, 0, 0, -3, 1, 1]





