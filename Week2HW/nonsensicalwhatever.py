#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import statsmodels.formula.api as smf
import statsmodels.api as sm
import sys


# 1.2 
def simulation(coverage, genome_length, read_length, figname):
	coverage_array = np.zeros(genome_length)
	minimum=0 
	maximum=genome_length - read_length 

	reads=int(coverage * genome_length/read_length)

	position0=np.random.randint(low=minimum, high= maximum +1 ,size=reads)

	for start in position0: 
		coverage_array[start:start +read_length] +=1 

	x=np.arange(0,max(coverage_array)+1)

	zero_coverage=genome_length -np.count_nonzero(coverage_array)
	zero_coverage_percent=100*zero_coverage/genome_length 

	poisson1=(stats.poisson.pmf(x, mu=coverage)) * genome_length

	normal1=stats.norm.pdf(x, loc=coverage, scale=np.sqrt(coverage)*genome_length)

	fig, ax = plt.subplots()
	ax.hist(coverage_array, bins=x, align='left',label='Coverage Simulation')
	ax.plot(x,poisson1, label='Poisson')
	ax.plot(x,normal1, label='Normal')
	ax.set_xlabel('Number of Reads')
	ax.set_ylabel('Base Pair Frequency')
	ax.legend()
	fig.tight_layout()
	plt.show()


simulation(3, 1000000, 100, 'ex1_3x_cov.png')
simulation(10, 1000000, 100, 'ex1_10x_cov.png')
simulation(30, 1000000, 100, 'ex1_30x_cov.png')
print(simulation)

#2.1 

nuc_reads = ['ATTCA', 'ATTGA', 'CATTG', 'CTTAT', 'GATTG', 'TATTT', 'TCATT', 'TCTTA', 'TGATT', 'TTATT', 'TTCAT', 'TTCTT', 'TTGAT']

graph = set()
 
 
kmers =  []
 

for reads in range(len(nuc_reads)):
	for i in range(len(nuc_reads[reads]) - 3):
		kmer1 = nuc_reads[reads][i: i + 3]
		print(kmer1)
		kmer2 = nuc_reads[reads][i + 1: i+ 4]
		edge = kmer1 + " -> "+ kmer2
		graph.add(edge)
		i+=1
	reads+=1

for edge in graph: 
	print(edge)


#2.2 


with open('Graph.txt', 'w') as f: 
	f.write('digraph {\n')
	f.write('\n'.join(graph))
	f.write('\n}')


