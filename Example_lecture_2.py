# example from p. 154 of the book
## US States
## goal: learning how to merge and combine dataframes

# cleaning memory
for v in dir(): del globals()[v]
pass

# set you directory where the main root folder is (you should create a root folder where scripts are, plus a datasets subfolder where datasets are saved)
import os
os.getcwd()
os.chdir("C:/Users/aguido/Downloads/datasciencewithpython-main/datasciencewithpython-main/Datasets")

# Example code
import pandas as pd

## import the datasets
pop = pd.read_csv('state-population.csv')
areas = pd.read_csv('state-areas.csv')
abbrevs = pd.read_csv('state-abbrevs.csv')
print(pop.head()); print(areas.head()); print(abbrevs.head())

merged = pd.merge(pop, abbrevs, how='outer', left_on='state/region', right_on='abbreviation')
merged = merged.drop(labels='abbreviation', axis=1) # drop duplicate info
merged.head()

merged.isnull().any()
merged[merged['population'].isnull()].head()
merged.loc[merged['state'].isnull(), 'state/region'].unique()

merged.loc[merged['state/region'] == 'PR', 'state'] = 'Puerto Rico'
merged.loc[merged['state/region'] == 'USA', 'state'] = 'United States'
merged.isnull().any()

final = pd.merge(merged, areas, on='state', how='left')
final.head()
final.isnull().any()
final['state'][final['area (sq. mi)'].isnull()].unique()

final.dropna(inplace=True)
 final.head()

import numexpr
data2010 = final.query("year == 2010 & ages == 'total'")
data2010.head()

data2010.set_index('state', inplace=True)
density = data2010['population'] / data2010['area (sq. mi)']

density.sort_values(ascending=False, inplace=True)
density.head()
density.tail()
