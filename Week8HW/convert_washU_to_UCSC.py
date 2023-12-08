#!/usr/bin/env python3

import sys
import pandas as pd 

#2.1: Convert the WashU format to UCSC 

baitmap,washU_text, output =sys.argv[1:4]

#create baitmap 
baitmapfile_df=pd.read_csv(baitmap, delim_whitespace=True, names=('CHR', 'BStart','BEnd','ID','Gene'))

#Create WashU data frame 
washU_df=pd.read_csv(washU_text, sep=(',|\t'),names=('chromosome1','start1','end1','chromosome2','start2','end2','score'),engine='python') 
maximum=max(washU_df['score'])
print(washU_df)
#Could do the next part a few ways, easiest way is to make a new dataframe and then loop through it (ugh)

chrom_info=pd.DataFrame(columns=['chrom','chromStart','chromEnd','name','score','value','ex','color','sourceChrom','sourceStart','sourceEnd','sourceName','sourceStrand','targetChrom','targetStart','targetEnd','targetName','targetStrand'])

#First try didn't work for some reason, created an empty targetStrand column 
# for i in WashU_df.index:
#     chrom_info.loc[i, 'chrom'] = WashU_df.loc[i, 'chromosome1']
#     chrom_info.loc[i, 'chromStart'] = min(WashU_df.loc[i, 'start1'], WashU_df.loc[i, 'start2'])
#     chrom_info.loc[i, 'chromEnd'] = max(WashU_df.loc[i, 'end2'], WashU_df.loc[i, 'end1'])
#     chrom_info.loc[i, 'name'] = '.'
#     chrom_info.loc[i, 'score'] = int(int(WashU_df.loc[i, 'score']) / maximum * 1000)  # Maybe wrong, will fix later if wrong
#     chrom_info.loc[i, 'value'] = WashU_df.loc[i, 'score']
#     chrom_info.loc[i, 'ex'] = '.'
#     chrom_info.loc[i, 'color'] = '0'
#     if WashU_df.loc[i, 'start1'] in baitmapfile_df['BStart'].values:
#         x1 = int(baitmapfile_df[baitmapfile_df['BStart'] == WashU_df.loc[i, 'start1']].index.values)
#         chrom_info.loc[i, 'sourceChrom'] = WashU_df.loc[i, 'chromosome1']
#         chrom_info.loc[i, 'sourceStart'] = WashU_df.loc[i, 'start1']
#         chrom_info.loc[i, 'sourceEnd'] = WashU_df.loc[i, 'end1']
#         chrom_info.loc[i, 'sourceName'] = baitmapfile_df.loc[x1, 'Gene']
#         chrom_info.loc[i, 'sourceStrand'] = '+'
#         chrom_info.loc[i, 'targetChrom'] = WashU_df.loc[i, 'chromosome2']
#         chrom_info.loc[i, 'targetStart'] = WashU_df.loc[i, 'start2']
#         chrom_info.loc[i, 'targetEnd'] = WashU_df.loc[i, 'end2']
#     elif WashU_df.loc[i, 'targetStart'] in baitmapfile_df['BStart'].values:
#         x2 = int((baitmapfile_df[baitmapfile_df['BStart'] == WashU_df.loc[i, 'start2']].index.values))
#         chrom_info.loc[i, 'targetName'] = baitmapfile_df.loc[x2, 'Gene']
#         chrom_info.loc[i, 'targetStrand'] = '+'
#     elif WashU_df.loc[i, 'start2'] in baitmapfile_df['BStart'].values:
#         y1 = int(baitmapfile_df[baitmapfile_df['BStart'] == WashU_df.loc[i, 'start2']].index.values)
#         chrom_info.loc[i, 'sourceChrom'] = WashU_df.loc[i, 'chromosome2']
#         chrom_info.loc[i, 'sourceStart'] = WashU_df.loc[i, 'start2']
#         chrom_info.loc[i, 'sourceEnd'] = WashU_df.loc[i, 'end2']
#         chrom_info.loc[i, 'sourceName'] = baitmapfile_df.loc[y1, 'Gene']
#         chrom_info.loc[i, 'sourceStrand'] = '+'
#         chrom_info.loc[i, 'targetChrom'] = WashU_df.loc[i, 'chromosome1']
#         chrom_info.loc[i, 'targetStart'] = WashU_df.loc[i, 'start1']
#         chrom_info.loc[i, 'targetEnd'] = WashU_df.loc[i, 'end1']
#     elif WashU_df.loc[i, 'targetStart'] in baitmapfile_df['BStart'].values:
#         y2 = int(baitmapfile_df[baitmapfile_df['BStart'] == WashU_df.loc[i, 'start1']].index.values)
#         chrom_info.loc[i, 'targetName'] = baitmapfile_df.loc[y2, 'Gene']
#         chrom_info.loc[i, 'targetStrand'] = '+'
#     else:
#         chrom_info.loc[i, 'targetName'] = '.'
#         chrom_info.loc[i, 'targetStrand'] = '-'

for i in washU_df.index: 
	chrom_info.loc[i,'chrom']=washU_df.loc[i,'chromosome1']
	chrom_info.loc[i,'chromStart']=min(washU_df.loc[i,'start1'],washU_df.loc[i,'start2'])
	chrom_info.loc[i,'chromEnd']=max(washU_df.loc[i,'end2'],washU_df.loc[i,'end1'])
	chrom_info.loc[i,'name']='.'
	chrom_info.loc[i,'score']=int(int(washU_df.loc[i,'score'])/maximum*1000) # Maybe wrong, will fix later if wrong
	chrom_info.loc[i,'value']=washU_df.loc[i,'score']
	chrom_info.loc[i,'ex']='.'
	chrom_info.loc[i,'color']='0'
	if washU_df.loc[i,'start1'] in baitmapfile_df['BStart'].values:
		x1=int(baitmapfile_df[baitmapfile_df['BStart'] == washU_df.loc[i,'start1']].index.values)
		chrom_info.loc[i,'sourceChrom']=washU_df.loc[i,'chromosome1']
		chrom_info.loc[i,'sourceStart']=washU_df.loc[i,'start1']
		chrom_info.loc[i,'sourceEnd']=washU_df.loc[i,'end1']
		chrom_info.loc[i,'sourceName']=baitmapfile_df.loc[x1,'Gene']
		chrom_info.loc[i,'sourceStrand']='+'
		chrom_info.loc[i,'targetChrom']=washU_df.loc[i,'chromosome2']
		chrom_info.loc[i,'targetStart']=washU_df.loc[i,'start2']
		chrom_info.loc[i,'targetEnd']=washU_df.loc[i,'end2']
		if chrom_info.loc[i,'targetStart'] in baitmapfile_df['BStart'].values: 
			x2=int((baitmapfile_df[baitmapfile_df['BStart'] == washU_df.loc[i,'start2']].index.values))
			chrom_info.loc[i,'targetName']=baitmapfile_df.loc[x2,'Gene']
			chrom_info.loc[i,'targetStrand']='+'
		else: 
			chrom_info.loc[i,'targetName']='.'
			chrom_info.loc[i,'targetStrand']='-'
	elif washU_df.loc[i,'start2'] in baitmapfile_df['BStart'].values: 
		y1=int(baitmapfile_df[baitmapfile_df['BStart'] == washU_df.loc[i,'start2']].index.values)
		chrom_info.loc[i,'sourceChrom']=washU_df.loc[i,'chromosome2']
		chrom_info.loc[i,'sourceStart']=washU_df.loc[i,'start2']
		chrom_info.loc[i,'sourceEnd']=washU_df.loc[i,'end2']
		chrom_info.loc[i,'sourceName']=baitmapfile_df.loc[y1,'Gene']
		chrom_info.loc[i,'sourceStrand']='+'
		chrom_info.loc[i,'targetChrom']=washU_df.loc[i,'chromosome1']
		chrom_info.loc[i, 'targetStart'] = washU_df.loc[i, 'start1']
		chrom_info.loc[i,'targetEnd']=washU_df.loc[i,'end1']
		if chrom_info.loc[i,'targetStart'] in baitmapfile_df['BStart'].values:
			y2=int(baitmapfile_df[baitmapfile_df['BStart']] == washU_df.loc[i,'start1'].index.values)
			chrom_info.loc[i,'targetName']=baitmapfile_df.loc[y2,'Gene']
			chrom_info.loc[i,'targetStrand'] == '+' 
		else: 
			chrom_info.loc[i,'targetName']='.'
			chrom_info.loc[i,'targetStrand']='-'


with open('output.bed', 'w') as f: 
	f.write('track type=interact name="pCHIC" description="Chromatin interactions" useScore=on maxHeightPixels=200:100:50 visibility=full \n') 
	UCSCdataforgenomebrowser = chrom_info.to_string(header=False, index=False)
	f.write(UCSCdataforgenomebrowser)


#2.2 

baitfragmentinteraction=chrom_info[chrom_info['sourceStrand'] ==chrom_info['targetStrand']]
baitfragmentinteraction=baitfragmentinteraction.sort_values(['score'])
print(baitfragmentinteraction.iloc[:6,:])

baitfragmentnonbaitfragment=chrom_info[chrom_info['sourceStrand'] !=chrom_info['targetStrand']]
baitfragmentnonbaitfragment=baitfragmentnonbaitfragment.sort_values(['score'])
print(baitfragmentnonbaitfragment.iloc[:6,:])



