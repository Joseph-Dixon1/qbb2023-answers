#!/usr/bin/env python 

#EXERCISE 1

import numpy as np
import matplotlib.pyplot as plt
#Get a starting frequency and a population size 
frequency=.4
popn_size=1000000
#input parameters for function 
def generational_af(frequency, popn_size):

	#Make a list to store our allele frequencies 
	af_list=[] #While our allele frequency is between 0 and 1: 
	while  0 < frequency < 1:
	#Get the new allele frequency for next geneartion (random)
		frequency=np.random.binomial(popn_size, frequency)/popn_size
	#by drawing from the binomial distribution (conver number of successes into a frequency)
	#Store our allele frequency in the AF list 
		af_list.append(frequency)
		print(frequency)
	#Return a list of allele frequency at each time point 
	return(af_list)
	
af_list=generational_af(.4,100)
#Number of generations to fixation is the length of your list
print("Number of Generations is:", len(af_list))

#Create the figure 
fig, ax=plt.subplots()
#x axis is generations so len(af_list)
# y axis is the frequency of the allele so function 
for i in range(1):
	fqs= generational_af(.4,100)
	ax.plot(fqs)
plt.show() 


np.random.seed(12)

def randomMotion(numberSteps):
	x=0
	y=0

	x_list=[x]
	y_list=[y]

	for timePoint in range(numberSteps):
		# how far do we move 
		y_displacement = np.random.uniform(-1,1)
		x_displacement=np.random.uniform(-1,1)

		x=x+x_displacement
		y=y+y_displacement

		x_list.append(x)
		y_list.append(y)

	return(x_list, y_list)


fig, ax=plt.subplots()
for i in range(20):
	trajectory = randomMotion(200)

	x_positions=trajectory[0]
	y_position=trajectory[1]
	ax.plot(x_positions,y_position)
plt.show()


#EXERCISE 2 

fig, ax=plt.subplots()
#x axis is generations so len(af_list)
# y axis is the frequency of the allele so function 
for i in range(30):
	fqs= generational_af(.4,100)
	ax.plot(fqs)
#plt.show() 


fig, ax=plt.subplots()
#x axis is generations so len(af_list)
# y axis is the frequency of the allele so function 
histo=[]
for i in range(1000):
	fqs= generational_af(.4,100)
	num_freqs=len(fqs)
	histo.append(num_freqs)
plt.hist(histo)
# x axis is number of generations 
# y is your count 
plt.xlabel("Number of Generations")
plt.ylabel("Counts")
plt.show()


# telling matlib that everything you did you should so 
#plt.show()


#EXERCISE 3 

#Changing population size affects the time to fication 
# pick 5 ppulation sizes greater than or equal to 50 
# for each run at least 50 times, find the average time to fixation 

pop50avg=[]
pop100avg=[]
pop150avg=[]
pop200avg=[]
pop250avg=[]
popn_averages=[]
for i in range(50):
	fqs50= generational_af(.4,100)
	num_freqs50=len(fqs50)
	pop50avg.append(num_freqs50)
	Fiftyavg=np.mean(pop50avg)
popn_averages.append(Fiftyavg)
for i in range(100):
	fqs100= generational_af(.4,100)
	num_freqs100=len(fqs100)
	pop100avg.append(num_freqs100)
	Hundredavg=np.mean(num_freqs100)
popn_averages.append(Hundredavg)
for i in range(150): 
	fqs150= generational_af(.4,100)
	num_freqs150=len(fqs150)
	pop150avg.append(num_freqs150)
	OneFiftyavg=np.mean(num_freqs150)
popn_averages.append(OneFiftyavg)
for i in range(200): 
	fqs200= generational_af(.4,100)
	num_freqs200=len(fqs200)
	pop200avg.append(num_freqs200)
	TwoHundavg=np.mean(num_freqs200)
popn_averages.append(TwoHundavg)
for i in range(250): 
	fqs250= generational_af(.4,100)
	num_freqs250=len(fqs250)
	pop250avg.append(num_freqs250)
	TwoFiftyavg=np.mean(num_freqs250)
popn_averages.append(TwoFiftyavg)
plt.scatter( popn_averages, [50,100,150,200,250])
plt.xlabel("Average Time to Fixation")
plt.ylabel("Population Size")
plt.show()



#Do the same but for allele frequencies 
pop50avg=[]
pop100avg=[]
pop150avg=[]
pop200avg=[]
pop250avg=[]
popn_averages=[]
for i in range(250):
	fqs50= generational_af(.1,10)
	num_freqs50=len(fqs50)
	pop50avg.append(num_freqs50)
	Fiftyavg=np.mean(pop50avg)
popn_averages.append(Fiftyavg)
for i in range(250):
	fqs100= generational_af(.2,10)
	num_freqs100=len(fqs100)
	pop100avg.append(num_freqs100)
	Hundredavg=np.mean(num_freqs100)
popn_averages.append(Hundredavg)
for i in range(250): 
	fqs150= generational_af(.3,10)
	num_freqs150=len(fqs150)
	pop150avg.append(num_freqs150)
	OneFiftyavg=np.mean(num_freqs150)
popn_averages.append(OneFiftyavg)
for i in range(250): 
	fqs200= generational_af(.4,10)
	num_freqs200=len(fqs200)
	pop200avg.append(num_freqs200)
	TwoHundavg=np.mean(num_freqs200)
popn_averages.append(TwoHundavg)
for i in range(250): 
	fqs250= generational_af(.5,10)
	num_freqs250=len(fqs250)
	pop250avg.append(num_freqs250)
	TwoFiftyavg=np.mean(num_freqs250)
popn_averages.append(TwoFiftyavg)
plt.scatter( popn_averages, [50,100,150,200,250])
plt.xlabel("Average Time to Fixation")
plt.ylabel("Allele Frequency")
plt.show()










