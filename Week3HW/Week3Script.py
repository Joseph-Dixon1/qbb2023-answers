#!/usr/bin/env python3

import numpy as np 
import sys
import pandas as pd
from fasta import readFASTA

#1.1 + 1.2 

fasta_file = sys.argv[1]

scoring_matrix = sys.argv[2]

gap_penalty = int(sys.argv[3])

file_name = sys.argv[4]

input_sequences = readFASTA(open(fasta_file))

seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]

scoring_matrix_df = pd.read_csv(scoring_matrix, sep = '\s+')

fmatrix=np.zeros((len(sequence1)+ 1, len(sequence2) +1))

for i in range(len(sequence1)+ 1):
	fmatrix[i, 0]=i*gap_penalty

for j in range(len(sequence2)+ 1):
	fmatrix[0, j]=j*gap_penalty

tmatrix=np.zeros((len(sequence1)+ 1, len(sequence2) +1), dtype='str')

for i in range(1, fmatrix.shape[0]):
	for j in range(1, fmatrix.shape[1]):
		matchscore =  scoring_matrix_df.loc[sequence1[i-1], sequence2[j-1]]
		d = fmatrix[i-1, j-1] + matchscore
		h = fmatrix[i, j-1] + gap_penalty
		v = fmatrix[i-1, j] + gap_penalty
		fmatrix[i, j] = max(d, h, v)

#print(fmatrix)

#1.3: populating the matrices 

i=len(sequence1)
j=len(sequence2)

while i != -1 and j !=-1: 
	d=fmatrix[i-1, j-1]
	h=fmatrix[i,j-1]
	v=fmatrix[i-1,j]
	if max(d, v, h) == d:
		tmatrix[i, j] = 'd'
		i -= 1 
		j -= 1 
	elif max(d, v, h) == v:
		tmatrix[i,j]='v'
		i -= 1
	elif max(d,v,h) == h: 
		tmatrix[i,j]='h'
		j -= 1
	elif max(d,v,h) == d and h: 
		tmatrix[i,j]='d'
		i -= 1
		j -=1 
	elif max(d,v,h) == d and v: 
		tmatrix[i,j]='d'
		i -= 1 
		j -= 1 
	elif max(d,v,h) == v and h: 
		tmatrix[i,j]='h'
		i -= 1

#1.4: Finding optimal alignment 

seq1alignment=''
seq2alignment=''

row=len(sequence1)
column=len(sequence2)

while row > 0 and column >0: 
	if tmatrix[row,column] == 'd': 
		seq1alignment=sequence1[row-1]+ seq1alignment
		seq2alignment=sequence2[column-1]+seq2alignment
		row -= 1
		column -= 1 
	elif tmatrix[row,column] == 'h':
		seq1alignment='-'+ seq1alignment
		seq2alignment=sequence2[column-1] + seq2alignment
		column -= 1
	elif tmatrix[row,column] == 'v': 
		seq1alignment=sequence1[row-1]+ seq1alignment
		seq2alignment='-' +seq2alignment
		row -= 1 
#print(seq1alignment)
#print(seq2alignment)

#1.5 

score=fmatrix[len(sequence1),len(sequence2)]

gapseq1=0
gapseq2=0 

for position in range(len(seq1alignment)):
	if seq1alignment[position] == '-':
		gapseq1 += 1 
		position +=1 

for position in range(len(seq2alignment)): 
	if seq2alignment[position] == '-':
		gapseq2 +=1 
		position +=1 

with open(file_name, 'w') as f: 
	f.write('Seq1 Alignment')
	f.write(seq1alignment)
	f.write('Seq2 Alignment')
	f.write(seq2alignment)
	f.write('Gaps in the first sequence')
	f.write(str(gapseq1))
	f.write('Gaps in Second Sequence')
	f.write(str(gapseq2))
	f.write('Alignment Score')
	f.write(str(score))








