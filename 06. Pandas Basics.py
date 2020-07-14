#%%
# Change working directory to data file locations
import os
try:
    old_wd = os.getcwd()
    print(old_wd[:old_wd.rindex('-') + 3])
    new_wd = old_wd[:old_wd.rindex('-') + 3] + r'\Notes\Data'
    os.chdir(new_wd)
    print(os.getcwd())
except:
    pass

# %%
import pandas as pd

# %% [markdown]
# # Pandas Basics
# * Any calculations involving time should be done using UTC data.
# %% [markdown]
# 1. Read the data from http://qj07301287:3000/LastAC into a Pandas DataFrame
#    and store it in a variable
#     * Hint: The URL returns JSON data
#     * Note: This link will only work on-network or through VPN
# %%
# Write your code below:

# %% [markdown]
# 2. Display the AP_Name, Nose, Station, and Session start and end times (UTC)
#    for only columns with Avg_SNR >= 25
# %%
# Write your code below:

# %% [markdown]
# 3. Convert the start, end, and last file time columns to datetime objects
#    with precision to the second
# %%
# Write your code below:

# %% [markdown]
# 4. Add a new column that holds the length of the connection
#     * If the end time is NA, use the current datetime
# %%
# Write your code below:

# %% [markdown]
# 5. What is the average connection time?
#    * Only take positive connection times into account
# %%
# Write your code below:

# %%
