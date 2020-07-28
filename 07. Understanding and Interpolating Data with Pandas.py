#%%
# Change working directory to data file locations
import os
try:
    old_wd = os.getcwd()
    new_wd = old_wd[:old_wd.rindex('-') + 3] + r'\Notes\Data'
    os.chdir(new_wd)
    print(f'Working Direcotry: {os.getcwd()}')
except:
    pass

#%%
# Obligatory imports
import numpy as np
import pandas as pd

#%% [markdown]
# # Understanding and Interpolating Data with Pandas
#%% [markdown]
# 1. Load in LCOD.csv, store it in a variable, and display the counts of rows and columns
#    along with the first 5 rows of the data and each columns data types
#%%
# Write your code below:
df = pd.read_csv('C://Users/241556/Documents/00 Co-Op/Python-Data-Sci/resources/LCOD.csv')

print('(rows, columns):')
display(df.shape)

display(df.head())

display(df.dtypes)

#%% [markdown]
# 2. What are the unique values in "113 Cause Name"? What the the unique values in "Cause Name"?
#    Do the to map 1:1 or is one of them more detailed?
#%%
# Write your code below:
causeNames1 = df['113 Cause Name'].unique()
print(f'113 Cause Names: {len(causeNames1)} items')
display(causeNames1)

causeNames2 = df['Cause Name'].unique()
print(f'Cause Names: {len(causeNames2)} items')
display(causeNames2)

# It appears that the columns map 1:1 since they each have 11 items.
# 113 Cause Names seems to be a more technical description for reporting purposes,
# whereas Cause Names seems to be a more user-friendly "display name" for the cause.

#%% [markdown]
# 3. How many total deaths were there in each state in 2012? Does the sum match the number in
#    the "United States" row for that year?
#%%
# Write your code below:
# rows where Year == 2012
df2012 = df.loc[(df['Year'] == 2012)  & (df['Cause Name'] =='All causes')]

# Group by state and get total deaths for each
display(df2012.groupby(df2012['State']).agg({'Deaths': 'sum'}))

# United States total vs Everyone else total
print('\nAll States Total vs United States Total:')
display(df2012.groupby(df2012['State'] == 'United States').agg({'Deaths': 'sum'}))

#%% [markdown]
# 4. Print the top 5 causes of death in each state for 2016, not including "All causes".
#%%
# Write your code below:
# rows where Year == 2016
df2016 = df.loc[
    (df['Year'] == 2016)
    & (df['Cause Name'] != 'All causes'),
    ['State','Cause Name','Deaths']
].sort_values(by=['Deaths'], ascending=False)

# sort by deaths
for idx, gdf in df2016.groupby('State'):
    print(f"{idx}'s Top 5 Causes of Death 2016\n")
    print(f"{gdf.loc[:,['Cause Name','Deaths']].head()}\n\n")

#%% [markdown]
# 5. Display the top 5 causes of death for your favorite state for each year available
#%%
# Write your code below:
df2016 = df.loc[
    (df['State'] == 'Texas')
    & (df['Cause Name'] != 'All causes'),
    ['Year','Cause Name','Deaths']
].sort_values(by=['Deaths'], ascending=False)

# sort by deaths
for idx, gdf in df2016.groupby('Year'):
    print(f"Texas' Top 5 Causes of death {idx}\n")
    print(f"{gdf.loc[:,['Cause Name','Deaths']].head()}\n\n")

#%%
