#!/usr/bin/env python

import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

##3A 

def parse_bedgraph(file_path):
 
    columns = ['chrom', 'start', 'end', 'methylation_level', 'coverage']
    df = pd.read_csv(file_path, sep='\t', header=None, names=columns)
    return df

def compare_methylation_calls(bismark_file, nanopore_file):
   
    bismark_df= parse_bedgraph(bismark_file)
    nanopore_df = parse_bedgraph(nanopore_file)

    bismark_only = len(bismark_df[~bismark_df['start'].isin(nanopore_df['start'])])
    nanopore_only = len(nanopore_df[~nanopore_df['start'].isin(bismark_df['start'])])


    shared_sites = len(bismark_df[bismark_df['start'].isin(nanopore_df['start'])])

    
    total_sites = len(set(bismark_df['start']).union(set(nanopore_df['start'])))
    percentage_shared = (shared_sites / total_sites) * 100

    return bismark_only, nanopore_only, shared_sites, percentage_shared


bismark_file_path = 'bisulfite.cpg.chr2.bedgraph'
nanopore_file_path = 'ONT.cpg.chr2.bedgraph'


bismark_only, nanopore_only, shared_sites, percentage_shared = compare_methylation_calls(
    bismark_file_path, nanopore_file_path
)


print(f"Number of sites present only in Bismark file: {bismark_only}")
print(f"Number of sites present only in Nanopore file: {nanopore_only}")
print(f"Number of shared sites: {shared_sites}")
print(f"Percentage of total sites shared: {percentage_shared:.2f}%")


##3B

def coverage(bismark_file, nanopore_file):
 
    bismark_df = pd.read_csv(bismark_file, sep='\t', header=None, names=['chrom', 'start', 'end', 'methylation_level', 'coverage'])
    nanopore_df = pd.read_csv(nanopore_file, sep='\t', header=None, names=['chrom', 'start', 'end', 'methylation_level', 'coverage'])

   
    x_range = (0, 100)  


    plt.hist(bismark_df['methylation_level'], bins=50, alpha=0.5, label='Bismark', range=x_range)
    plt.hist(nanopore_df['methylation_level'], bins=50, alpha=0.5, label='Nanopore', range=x_range)

    plt.xlabel('Methylation Level')
    plt.ylabel('Frequency')
    plt.title('Distribution of Coverages Across CpG Sites')
    plt.legend()
    plt.savefig('Figure_three_B.png')
    plt.close()

   
 

bismark_file_path = 'bisulfite.cpg.chr2.bedgraph'
nanopore_file_path = 'ONT.cpg.chr2.bedgraph'


coverage(bismark_file_path, nanopore_file_path)

##3C

def histogram2d_and_log_transform(bismark_file, nanopore_file):
    bismark_df = parse_bedgraph(bismark_file)
    nanopore_df = parse_bedgraph(nanopore_file)

    # Ensure that both arrays have the same length
    common_sites = set(bismark_df['start']).intersection(set(nanopore_df['start']))
    #bismark_levels = bismark_df[bismark_df['start'].isin(common_sites)]['methylation_level']
    #nanopore_levels = nanopore_df[nanopore_df['start'].isin(common_sites)]['methylation_level']

    bismark_levels = bismark_df.loc[bismark_df['start'].isin(common_sites), 'methylation_level']
    nanopore_levels = nanopore_df.loc[nanopore_df['start'].isin(common_sites), 'methylation_level']

    # Calculate Pearson correlation coefficient for non-transformed data
    correlation_coefficient = np.corrcoef(bismark_levels, nanopore_levels)[0, 1]

    print(bismark_df)
    print(nanopore_df)

    # Create a 2D histogram using numpy.histogram2d
    hist, x_edges, y_edges = np.histogram2d(bismark_levels, nanopore_levels, bins=50, range=[[0, 100], [0, 100]])

    # Transform the histogram using a log10(data + 1) transformation
    hist_transformed = np.log10(hist + 1)

    return hist_transformed, x_edges, y_edges, correlation_coefficient


# File paths for bedgraph files
bismark_file_path = 'bisulfite.cpg.chr2.bedgraph'
nanopore_file_path = 'ONT.cpg.chr2.bedgraph'

# Run the histogram2d_and_log_transform function
hist_transformed, x_edges, y_edges, correlation_coefficient = histogram2d_and_log_transform(bismark_file_path, nanopore_file_path)

# Plot the transformed histogram using imshow
plt.imshow(hist_transformed.T, origin='lower', extent=[x_edges[0], x_edges[-1], y_edges[0], y_edges[-1]], cmap='viridis')
plt.colorbar(label='log10(Count + 1)')

plt.xlabel('Bismark Methylation Level')
plt.ylabel('Nanopore Methylation Level')

# Include Pearson correlation coefficient in the title
plt.title(f'2D Histogram of Methylation Levels\n(log10 transformed)\nPearson R = {correlation_coefficient:.3f}')

plt.savefig('Figure_three_C.png')
plt.close()#while:
    #pass


##3D 

tumor_df=parse_bedgraph("tumor.ONT.chr2.bedgraph")
normal_df=parse_bedgraph("normal.ONT.chr2.bedgraph")

thing1 = tumor_df["methylation_level"].subtract(normal_df["methylation_level"])
thing1 = thing1.loc[thing1.notnull()]

please_dont_take_my_man=[]
for i in thing1: 
    if i != 0:
        please_dont_take_my_man.append(i)

tumor_bisulfite_df=parse_bedgraph("tumor.bisulfite.chr2.bedgraph")
normal_bisulfite_df=parse_bedgraph("normal.bisulfite.chr2.bedgraph")

thing2 = tumor_bisulfite_df["methylation_level"].subtract(normal_bisulfite_df["methylation_level"])
thing2 = thing2.loc[thing2.notnull()]

jolene=[]
for i in thing2: 
    if i != 0:
        jolene.append(i)

common_sites_tumor = set(tumor_bisulfite_df['start']).intersection(set(normal_bisulfite_df['start']))

thing1.head()

thing1_corr = tumor_bisulfite_df.loc[tumor_bisulfite_df['start'].isin(common_sites_tumor), 'methylation_level']
thing2_corr = normal_bisulfite_df.loc[normal_bisulfite_df['start'].isin(common_sites_tumor), 'methylation_level']

R_value_violin = np.corrcoef(thing1_corr, thing2_corr)[0, 1]
print(R_value_violin)

plt.violinplot([jolene, please_dont_take_my_man], showmeans=True, showextrema=True)
plt.xticks([1, 2], ['ONT', 'bisulfite'])
plt.ylabel('Change in CpG Methylation')
plt.title('Distribution of Methylation Changes ' + str(R_value_violin))
plt.savefig('Figure_Three_D.png')
plt.show()

#def compare_methylation_calls(, ):


#4

indexed_tumor= samtools index tumor.ONT.chr2.bam
indexed_normal= samtools index normal.ONT.chr2.bam



