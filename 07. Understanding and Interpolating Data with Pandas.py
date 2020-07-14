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

#%% [markdown]
# 2. What are the unique values in "113 Cause Name"? What the the unique values in "Cause Name"?
#    Do the to map 1:1 or is one of them more detailed?
#%%
# Write your code below:

#%% [markdown]
# 3. How many total deaths were there in each state in 2012? Does the sum match the number in
#    the "United States" row for that year?
#%%
# Write your code below:

#%% [markdown]
# 4. Print the top 5 causes of death in each state for 2016, not including "All causes".
#%%
# Write your code below:

#%% [markdown]
# 5. Display the top 5 causes of death for your favorite state for each year available
#%%
# Write your code below:

#%%
