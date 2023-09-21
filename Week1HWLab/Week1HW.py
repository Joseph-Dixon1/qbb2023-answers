#!/usr/bin/env python 

#Step 1.1

#Load data into a pandas dataframe 
import pandas as pd 
data=pd.read_csv('/Users/cmdb/cmdb-quantbio/assignments/bootcamp/statistical_modeling/extra_data/aau1043_dnm.csv')

# rows as probands, columns with number of paternally inherited DNM, maternally inherited DNM, also father age and mother age 
# do linear regressions on these data 
# each row is  DNM, column tell you proband ID and other is what parent it's from 

#Step 1.2 

#Create an empty dictionary to add values to 
deNovoCount={}
#Create a dictionary, keys are proband IDs value is list of length 2, # of maternal DNM, paternal DNMs 
#Loop through the indices not the entire data frame 
for i in  range(len(data)):
	#.loc is row index, and a column name, putting in i will put in to each row 
	proband_id=data.loc[i, 'Proband_id']
	parent=data.loc[i,'Phase_combined']
	if proband_id not in  deNovoCount: 
		deNovoCount[proband_id]=[0,0]
	if parent == 'mother': 
		deNovoCount[proband_id][0]+= 1 
	elif parent == 'father':
		#add each new number to the dictionary 
		deNovoCount[proband_id][1]+= 1 

#Step 1.3

deNovoCountDF = pd.DataFrame.from_dict(deNovoCount, orient = 'index', columns = ['maternal_dnm', 'paternal_dnm'])
print(deNovoCountDF)
#Step 1.4 

parental_data=pd.read_csv('/Users/cmdb/cmdb-quantbio/assignments/bootcamp/statistical_modeling/extra_data/aau1043_parental_age.csv', index_col='Proband_id')

#Step 1.5

# if they don't match up ( join) do inner or outer, if there are disagreements, do the union or intersection
combined_data=pd.concat([deNovoCountDF,parental_data], axis=1, join='inner')

print(combined_data)

#Step 2.1 
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt 

#row is column, then on the right it's maternal_age 
#add in all the matplotlib stuff from bootcamp 
# doing all the rows w/ the maternal age 

fig, ax=plt.subplots()
combined_data.loc[: , 'Mother_age']
m_dnm=combined_data.loc[: , 'maternal_dnm']
ax.scatter(combined_data.loc[: , 'Mother_age'], combined_data.loc[: , 'maternal_dnm'])
plt.xlabel("Maternal Age")
plt.ylabel("Maternal De Novo Mutations")
fig.savefig('ex2_a.png')
plt.show()


fig, ax=plt.subplots()
combined_data.loc[: , 'Father_age']
p_dnm=combined_data.loc[: , 'paternal_dnm']
ax.scatter(combined_data.loc[: , 'Father_age'], combined_data.loc[: , 'paternal_dnm'])
plt.xlabel("Paternal Age")
plt.ylabel("Paternal De Novo Mutations")
fig.savefig('ex2_b.png')
plt.show()


#Step 2.2 
import statsmodels.formula.api as smf 
maternal_leastsquares=smf.ols(formula='maternal_dnm ~ 1 + Mother_age', data=combined_data)
results=maternal_leastsquares.fit()
print(results.summary())


#Step 2.3
import statsmodels.formula.api as smf 
paternal_leastsquares=smf.ols(formula='paternal_dnm ~ 1 + Father_age', data=combined_data)
results=paternal_leastsquares.fit()
print(results.summary())

#Step 2.5
fig, ax=plt.subplots()
ax.hist(m_dnm, label='Maternal Inherited DNMs', bins=30, alpha=0.5)
ax.hist(p_dnm, label='Paternal Inherited DNMs',bins=30, alpha=0.5)
ax.legend()
ax.set_ylabel("Number of Inherited De Novo Mutations")
fig.savefig('ex2_c.png')
plt.show()

#Step 2.6
from scipy import stats
ttest=stats.ttest_ind(m_dnm,p_dnm)
print(ttest)


 