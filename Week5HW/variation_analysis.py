#!/usr/bin/env python3

import matplotlib.pyplot as plt 

#Data for each graph 

distribution_read_depth=[]
genotype_quality=[]
allele_frequency=[]
variant_effects=[]

for line in open('annotated_variants.vcf'):
    if line.startswith('#'):
        continue
    fields=line.rstrip('\n').split('\t')
    data=fields[7]
    datalist=data.split(';')
    for item in datalist: 
   		if item.startswith('DP='): 
   			distribution_read_depth.append(item[3: ])
   		elif item.startswith('GQ='):
   			if float(GQ) > 0:
   				genotype_quality.append(float(item[3: ]))
   		elif item.startswith('AF='):
   			allele_frequency.append(item[3: ])
   		elif item.startswith('ANN='):
   			variant_list=item.split("|")
   			variant_effects.append(variant_list[1])

print(genotype_quality)
   ##3.1 

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize = (10,6)) 
ax1.hist(distribution_read_depth, bins = 300)
ax1.set_xlim(0,100)
ax1.set_xlabel("Read Depth")
ax1.set_ylabel("Frequency (sample)")
ax1.set_title("Distribution of read depth")
fig.savefig('ThreePointOne.png')

   #3.2 

ax2.hist(genotype_quality, bins = 300)
ax2.set_xlabel("Quality of Gene")
ax2.set_ylabel("Frequency of Sample")
ax2.set_title("Genotype Quality Distribution")

   #3.3 

ax3.hist(allele_frequency, bins = 20)
ax3.set_xlabel("Allele Frequency (Distribution)")
ax3.set_ylabel("Frequency of Sample")
ax3.set_title(" Allele Frequency Distribution")

   ##3.4 

#make a dictionary or whatever 

variant_dict={}
for i in set(variant_effects):
	variant_dict[i] = variant_effects.count(i)

variant_key = list(variant_dict.keys())
variant_value = list(variant_dict.values())

ax4.bar(range(len(variant_dict)), variant_value)
ax4.set_xlabel("Predicted Effects")
ax4.set_ylabel("Frequency of Allele)")
ax4.set_title("Predicted Effects of Variants")
ax4.set_xticks(range(len(variant_key)))
ax4.set_xticklabels(variant_key, rotation = 'vertical',  fontsize = 7)

fig.suptitle('Variant Patterns')
fig.tight_layout()
fig.savefig("ThreePointFour.png")
