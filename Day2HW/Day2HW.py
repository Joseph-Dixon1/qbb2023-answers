#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# Get dataset to recreate Fig 3B from Lott et al 2011 PLoS Biology https://pubmed.gov/21346796
# wget https://github.com/bxlab/cmdb-quantbio/raw/main/assignments/lab/bulk_RNA-seq/extra_data/all_annotated.csv

transcripts = np.loadtxt( "/Users/cmdb/Desktop/swc-python/all_annotated.csv", delimiter=",", usecols=0, dtype="<U30", skiprows=1 )
print( "transcripts: ", transcripts[0:5] )

samples = np.loadtxt( "/Users/cmdb/Desktop/swc-python/all_annotated.csv", delimiter=",", max_rows=1, dtype="<U30" )[2:]
print( "samples: ", samples[0:5] )

data = np.loadtxt( "/Users/cmdb/Desktop/swc-python/all_annotated.csv", delimiter=",", dtype=np.float32, skiprows=1, usecols=range(2, len(samples) + 2) )
print( "data: ", data[0:5, 0:5] )

# Find row with transcript of interest for gene 033
for i in range(len(transcripts)):
    if transcripts[i] == 'FBtr0073461':
        row = i
    
# Find columns with samples of interest
cols = []
#colsMale=[]

#i just an index, just positions
for i in range(len(samples)):
    if "female" in samples[i]:
        cols.append(i)
    #else: 
        #colsMale.append(i)


# Subset data of interest
expression = data[row, cols]

# Prepare data
x = samples[cols]
#xmales=samples[colsmale]
y = expression


# Plot data
fig, ax = plt.subplots()
ax.set_title( "FBtr0331261" )
ax.plot( x, y )
fig.savefig( "FBtr0331261.png" )
#plt.close( fig )
plt.show()
fig.savefig('MaleDataExercise1')

