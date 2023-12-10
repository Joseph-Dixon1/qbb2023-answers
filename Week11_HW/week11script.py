#!/usr/bin/env python

import scanpy as sc
import matplotlib.pyplot as plt 

adata = sc.read_h5ad("variable_data.h5")
adata.uns['log1p']['base'] = None # This is needed due to a bug in scanpy 

#1.1 
sc.pp.neighbors(adata, n_neighbors =10, n_pcs=40)

#1.2
sc.tl.leiden(adata)

#1.3
fig, axes = plt.subplots(ncols=2, figsize=(12, 5))
# plt.savefig(Figure_one_point_three.png)

# Plot UMAP
sc.tl.umap(adata, maxiter=900)
sc.pl.umap(adata, color='leiden', ax=axes[0], title='UMAP Visualization', show=False)

# Plot t-SNE
sc.tl.tsne(adata)
sc.pl.tsne(adata, color='leiden', ax=axes[1], title='t-SNE Visualization', show=False)

plt.savefig('Figure_one_point_three.png', dpi=300)

# Show the figure
# plt.show()

#2.1

wilcoxon_adata = sc.tl.rank_genes_groups(adata, groupby='leiden', method='wilcoxon', use_raw=True, copy=True)

logreg_adata = sc.tl.rank_genes_groups(adata, groupby='leiden', method='logreg', use_raw=True, copy=True, max_iter=900)

#2.2 

fig, ax = plt.subplots(figsize=(12, 8), ncols=5, nrows=5, sharex=True, sharey=False)

sc.pl.rank_genes_groups(wilcoxon_adata, n_genes=25,  title='Wilcoxon Rank-Sum', use_raw=True, show=False, save='_wilcoxon.png')

# fig.suptitle('Top 25 Genes for Each Cluster (Wilcoxon Rank-Sum)', fontsize=16)
# plt.subplots_adjust(top=0.9)  
# plt.savefig('Figure_two_point_two.png', dpi=300)



fig, ax = plt.subplots(figsize=(12, 8), ncols=5, nrows=5, sharex=True, sharey=False)

sc.pl.rank_genes_groups(logreg_adata, n_genes=25, title='Logistic Regression', use_raw=True, show=False, save='_logreg.png')

# fig.suptitle('Top 25 Genes for Each Cluster (Logistic Regression)', fontsize=16)
# plt.subplots_adjust(top=0.9)  

# plt.savefig('figure_two_point_two_logs.png', dpi=300)




leiden = adata.obs['leiden']
umap = adata.obsm['X_umap']
tsne = adata.obsm['X_tsne']
adata = sc.read_h5ad('filtered_data.h5')
adata.obs['leiden'] = leiden
adata.obsm['X_umap'] = umap
adata.obsm['X_tsne'] = tsne

adata.write('filtered_clustered_data.h5')

adata = sc.read_h5ad("filtered_clustered_data.h5")
adata.uns['log1p']['base'] = None 

#3.2/3.3

marker_genes = ['S100A8','leiden','CD79A','leiden','GNLY','leiden'] 
sc.pl.umap(adata, save='Three_point_two.png',color=marker_genes, cmap='viridis', ncols=3, title=marker_genes, legend_loc='on data')
adata.rename_categories('leiden',['N/A1', 'Neutrophil','B-Cell','N/A2','N/A3','Human Cytotoxic T Lymphocytes','N/A4','N/A5']) 
sc.pl.umap(adata, save='Three_point_three.png',color=marker_genes, cmap='viridis', ncols=3, title=marker_genes, legend_loc='on data')

#S100A8 is Neutrophil 
#CD79A is B-cell 
#Human Cytotoxic T Lymphocytes

# plt.suptitle('Expression of Marker Genes in UMAP', fontsize=16)
# plt.subplots_adjust(top=0.9) 

# plt.savefig('Figure_three_point_two.png', dpi=300)
# plt.show()



#adata.rename_categories(['N/A', 'Neutrophil','B-Cell','N/A','N/A','Human Cytotoxic T Lymphocytes','N/A','N/A'])
