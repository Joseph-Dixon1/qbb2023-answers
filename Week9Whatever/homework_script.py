#!/usr/bin/env python3

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats import multitest
from pydeseq2 import preprocessing
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats
import matplotlib.pyplot as plt


# read in data
counts_df = pd.read_csv("/Users/cmdb/qbb2023-answers/Week9Stuff/gtex_whole_blood_counts_formatted.txt", index_col = 0)

# read in metadata
metadata = pd.read_csv("/Users/cmdb/qbb2023-answers/Week9Stuff/gtex_metadata.txt", index_col = 0)


counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]

counts_df_normed = np.log2(counts_df_normed + 1)


full_design_df = pd.concat([counts_df_normed, metadata], axis=1)

model = smf.ols(formula = 'Q("DDX11L1") ~ SEX', data=full_design_df)
results = model.fit()

slope = results.params[1]
pval = results.pvalues[1]


#1.5 

#need to store name of gene, slope, and p-value 
all_genes={}

for gene in counts_df.columns:
	model = smf.ols(formula = 'Q("' + gene +'") ~ SEX', data=full_design_df)
	results = model.fit()
	slope = results.params[1]
	pval = results.pvalues[1]
	all_genes[gene] = [slope, pval]
data_store= pd.DataFrame.from_dict(all_genes, orient='index', columns=['slope', 'pval'])
data_store.index.name = 'gene'

data_store.to_csv('gene_sex_regression_results.txt', header=True, index=True, sep='\t')


pvalues=[]
for gene in all_genes: 
	#call a dictionary with the right key, second paranthesis is the pvalue
	pvalues.append(all_genes[gene][1])


fdr_true=multitest.fdrcorrection(pvalues, alpha=0.10, method='indep', is_sorted=False)[0]
gene_names=list(all_genes.keys())
homemade_DE_results=[]

f= open('homemade_DE_results','w', encoding='utf-8')
with open('homemade_DE_results','w',encoding='utf-8') as f: 
	for idx in range(len(gene_names)):
		if fdr_true[idx]:
			gene_good=gene_names[idx]
			homemade_DE_results.append(gene_good)
			f.write(gene_good+ '\n')



#Exercise 2 

dds = DeseqDataSet(
    counts=counts_df,
    metadata=metadata,
    design_factors="SEX",
    )

dds.deseq2()
stat_res = DeseqStats(dds)
stat_res.summary()
results = stat_res.results_df


# genes=[]
# for lines in open('gene_sex_regression_results.txt'):
# 	all_genes=tuple(lines.rstrip('\n').split('\t'))
# 	genes.append(all_genes)
# #print(genes)

# genes_1=[]
# for lines in open('gtex_whole_blood_counts_formatted.txt'): 
# 	gene_1=tuple(lines.split(','))
# 	genes_1.append(gene_1)
# geneset_sex=set(genes)
# geneset_blood=set(genes_1)
# intersect=geneset_sex.intersection(geneset_blood)

results=results.dropna(subset=['padj'])
log2fold= results['log2FoldChange']
padj=results['padj']
log10pvalue= -1 * (np.log10(padj))
DEG_filter=(padj < 0.1) & (abs(log2fold) > 1)
DEG=results[DEG_filter]

f2= open('DEseq2_results.txt','w', encoding='utf-8')
with open('DEseq2_results.txt','w',encoding='utf-8') as f2: 
	f2.write(DEG)

homemade_DE_set = set(homemade_DE_results)
DESEQ2_set=set(DEG.index)
intersect=homemade_DE_set.intersection(DESEQ2_set)
union=homemade_DE_set.union(DESEQ2_set)
index= len(intersect)/len(union)*100
print("This is what you're looking for", index)

fig,ax = plt.subplots()
ax.scatter(log2fold,log10pvalue, color='blue', alpha=0.5, label='Not DE')
ax.scatter(log2fold[DEG_filter], log10pvalue[DEG_filter], color='green', alpha=0.7, label='DEG')
ax.set_xlabel('log2FoldChange')
ax.set_ylabel('P-value-Log10')
ax.set_title('DifferentialGeneExpression')
fig.tight_layout()
plt.show()

fig.savefig('Differential_Gene_Expression.png')