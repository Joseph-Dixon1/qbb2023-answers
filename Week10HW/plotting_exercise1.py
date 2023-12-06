#!/usr/bin/env python3

import numpy as np
import pandas as pd
from pydeseq2 import preprocessing
from matplotlib import pyplot as plt


# read in data
counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)

# read in metadata
metadata = pd.read_csv("gtex_metadata.txt", index_col = 0)

# normalize
counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]

# log
counts_df_logged = np.log2(counts_df_normed + 1)

# merge with metadata
full_design_df = pd.concat([counts_df_logged, metadata], axis=1)
print(full_design_df)

#1.1

# Extract expression data for the specified subject
subject_data = full_design_df.loc['GTEX-113JC', : 'MT-TP']
subject_data.astype(int)


#[full_design_df['SUBJECT_ID'] == 'GTEX-113JC']


# Exclude genes with 0 counts
non_zero_expression = subject_data[subject_data > 0] 


# Plot the distribution
plt.figure(figsize=(10, 6))
plt.hist(non_zero_expression.values.flatten(), bins=50, edgecolor='black')
plt.xlabel('Logged Normalized Counts')
plt.ylabel('Frequency')
plt.title(f'Distribution of Gene Expression for GTEX-113JC')
plt.show()

#1.2
male=full_design_df.loc[full_design_df['SEX'] == 1, 'MXD4' ]
female=full_design_df.loc[full_design_df['SEX'] == 2,'MXD4' ]

plt.figure(figsize=(10, 6))
plt.hist(male, bins=50, edgecolor='blue')
plt.hist(female, bins=50, edgecolor='red')
plt.xlabel('MXD4 Expression')
plt.ylabel('Frequency')
plt.title(f'Distribution of Gene Expression Between Male and Females')
plt.show()

#1.3 
ages=full_design_df['AGE'].unique()
print(ages)
yresults=full_design_df['AGE'].value_counts()

plt.figure(figsize=(10, 6))
plt.bar(x=ages, height=yresults, edgecolor='blue')
plt.xlabel('Ages')
plt.ylabel('Number of Subjects in Each Age')
plt.title(f'Number of Subjects in Each Age Category')
plt.show()

#1.4
male_LPXN=full_design_df.loc[full_design_df['SEX'] == 1, 'LPXN' ]
male_ages=full_design_df.loc[full_design_df['SEX']== 1, 'AGE']
male=pd.concat([male_LPXN,male_ages], axis=1)
female_LPXN=full_design_df.loc[full_design_df['SEX'] == 2,'LPXN' ]
female_ages=full_design_df.loc[full_design_df['SEX']== 2, 'AGE']
female=pd.concat([female_LPXN,female_ages], axis=1)
male_20s=male.loc[male['AGE']== '20-29','LPXN']
male_30s=male.loc[male['AGE']== '30-39','LPXN']
male_40s=male.loc[male['AGE']== '40-49','LPXN']
male_50s=male.loc[male['AGE']== '50-59','LPXN']
male_60s=male.loc[male['AGE']== '60-69','LPXN']
male_70s=male.loc[male['AGE']== '70-79','LPXN']
female_20s=female.loc[female['AGE']== '20-29','LPXN']
female_30s=female.loc[female['AGE']== '30-39','LPXN']
female_40s=female.loc[female['AGE']== '40-49','LPXN']
female_50s=female.loc[female['AGE']== '50-59','LPXN']
female_60s=female.loc[female['AGE']== '60-69','LPXN']
female_70s=female.loc[female['AGE']== '70-79','LPXN']

more_males=[male_20s,male_30s,male_40s,male_50s,male_60s,male_70s]
more_females=[female_20s,female_30s,female_40s,female_50s,female_60s,female_70s]

male_median=[]
female_median=[]

for data in more_males: 
	male_median.append(data.median())

for data in more_females: 
	female_median.append(data.median())

more_ages=['20-29','30-39','40-49','50-59','60-69','70-79']

plt.figure(figsize=(10, 6))
plt.scatter(x=more_ages, y=male_median)
plt.scatter(x=more_ages, y=female_median)
plt.xlabel('Ages')
plt.ylabel('Median Expression')
plt.title(f'Median Expression of LPXN over time in males vs. females')
plt.show()








	

