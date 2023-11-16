#!/bin/python




import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
import seaborn as sns 

#Print top 10 principal components here because idk what's going on in the terminal 

with open('/Users/cmdb/qbb2023-answers/Week6HW/gwas_data/plink.eigenvec', 'r') as file: 
	for i, line in enumerate(file):
		if i < 10: 
			components = line.strip().split()[2:12]
			print('\t'.join(components))

#1.2 

# eigenvec_file= 'gwas_data/plink.eigenvec'

# data=np.loadtxt(eigenvec_file)

# PC1=data[:, 2]
# PC2=data[:,3]

# plt.figure(figsize=(8,6))
# plt.scatter(PC1,PC2, alpha=0.5)
# plt.title('Principle Component Analysis')
# plt.xlabel('PC1')
# plt.ylabel('PC2')
# plt.grid(True)
# plt.savefig('PCAGraph1')

# plt.close()

# #Exercise 2 

# allele_frequencies='gwas_data/allele_frequencies.frq'

# data2=pd.read_csv(allele_frequencies, delim_whitespace=True)

# variable=data2.loc[:, 'MAF']

# fig9, ax9=plt.subplots()
# ax9.hist(variable, bins=20, color='blue', alpha=0.7)
# ax9.set_ylabel('Occurence')
# ax9.set_xlabel('Allele Frequency')
# ax9.title("AFS of Variants in Samples")
# plt.savefig('Exercise2Week6Histogram')


#Exercise 3.2 

variable2=pd.read_csv('gwas_data/PHENO1.assoc.linear', delim_whitespace=True)
print(variable2)

variable3=pd.read_csv('gwas_data/PHENO2.assoc.linear', delim_whitespace=True)
print(variable3)

variable2part2=variable2.loc[:, 'P']
variable3part2=variable3.loc[:, 'P']


plt2 = variable2part2[variable2part2 < 1e-5]
x = variable2part2.index[variable2part2 < 1e-5]

plt3 = variable3part2[variable3part2 < 1e-5]
x2 = variable3part2.index[variable3part2 < 1e-5]


fig,(ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12,6))
ax1.scatter(range(len(variable2part2)), -np.log10(variable2part2), marker='o', color='blue')
ax1.scatter(x, -np.log10(plt2), c='red')
ax1.set_xlabel('Position of SNP')
ax1.set_ylabel('P-value SNP')
ax2.scatter(range(len(variable3part2)), -np.log10(variable3part2), marker='o', color='blue')
ax2.scatter(x2, -np.log10(plt3), c='red')
ax2.set_xlabel('Position of SNP')
ax2.set_ylabel('P-value SNP')
plt.savefig('3point2Histogram.png')

plt.show()

#Exercise 3.3 


# threepointthree=variable2.loc[variable2part2 == variable2part2.min(), 'SNP']
# threepointthree = threepointthree.values[0]

# for line in open("gwas_data/genotypes.vcf"):
# 	if line.startswith('#'):
# 		continue 
# 	variable4=line.rstrip('\n').split('\t')
# 	#print(variable4[2])
# 	if variable4[2] == threepointthree: 
# 		info=variable4[9: ] 
# 		INFOTHISONE=variable4[:9]
# print('THIS IS INFO',INFOTHISONE)

# phenotype=[]
# for line in open('gwas_data/CB1908_IC50.txt'):
# 	variable4=line.rstrip('\n').split()
# 	if variable4[2] != 'CB1908_IC50':
# 		if variable4[2] == 'NA':
# 			phenotype.append('NA')
# 		else: 
# 			phenotype.append(float(variable4[2]))
# 		#else: 
# 		#	continue 


# zerozero=[]
# onezero=[]
# oneone=[]

# for i in range(0, len(info)):
# 	if info[i] == '0/0': 
# 		if phenotype[i] == 'NA': 
# 			continue 
# 		else:
# 			zerozero.append(phenotype[i])
# 	if info[i] == '0/1':
# 		if phenotype[i] == 'NA':
# 			continue
# 		else: 
# 			onezero.append(phenotype[i])
# 	elif info[i] == '1/1': 
# 		if phenotype[i] == 'NA': 
# 			continue 
# 		else: 

# 			oneone.append(phenotype[i]) 
# 	else: 
# 		continue 

# cumulative=[]
# cumulative.append(zerozero) 
# cumulative.append(onezero)
# cumulative.append(oneone)

# labels=['0/0', '0/1', '1/1']

# fig, ax3=plt.subplots()
# ax3.boxplot(cumulative, labels=labels)
# ax3.set_xlabel('Genotype')
# ax3.set_ylabel('Phenotype')
# ax3.set_title('Genotype vs Phenotype for rs10876043')
# fig.savefig('BoxPlot')
# fig.tight_layout()

# plt.show()


