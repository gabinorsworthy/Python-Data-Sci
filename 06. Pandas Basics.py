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
#df2 = pd.read_json('http://qj07301287:3000/LastAC')
#df2
df = pd.read_json('C://Users/241556/Documents/00 Co-Op/Python-Data-Sci/resources/exercise06-01.json')
df

# %% [markdown]
# 2. Display the AP_Name, Nose, Station, and Session start and end times (UTC)
#    for only columns with Avg_SNR >= 25
# %%
# Write your code below:
# I'm assuming it meant only for rows with Avg_SNR >= 25
df.loc[
    df['Avg_SNR'] >= 25,
    ['Nose', 'AP_Name', 'Station','Session_start_Time_UTC','Session_End_Time_UTC']
]

# %% [markdown]
# 3. Convert the start, end, and last file time columns to datetime objects
#    with precision to the second
# %%
# Write your code below:\
df['Session_Start_Time_Lcl'] = pd.to_datetime(df['Session_Start_Time_Lcl'],
                                                format="%Y-%m-%d %H:%M:%S",
                                                errors='coerce')

df['Session_start_Time_UTC'] = pd.to_datetime(df['Session_start_Time_UTC'],
                                                format="%Y-%m-%d %H:%M:%S",
                                                errors='coerce',
                                                utc=True)

df['Session_End_Time_LCL'] = pd.to_datetime(df['Session_End_Time_LCL'],
                                                format="%Y-%m-%d %H:%M:%S",
                                                errors='coerce')

df['Session_End_Time_UTC'] = pd.to_datetime(df['Session_End_Time_UTC'],
                                                format="%Y-%m-%d %H:%M:%S",
                                                errors='coerce',
                                                utc=True)

df['LAST_FILE'] = pd.to_datetime(df['LAST_FILE'],
                                                format="%Y-%m-%d %H:%M:%S",
                                                errors='coerce')


df.dtypes

#alternative
#df.loc[:,timeCols] = df.loc[:,timeCols].astype('datetime64[s]')

# %% [markdown]
# 4. Add a new column that holds the length of the connection
#     * If the end time is NA, use the current datetime
# %%
# Write your code below:
df['lenOfConnection'] = df.apply(
    lambda timeDiff: (
            timeDiff.Session_End_Time_UTC
            if pd.notna(timeDiff.Session_End_Time_UTC)
            else pd.Timestamp.utcnow()        
        ) - timeDiff.Session_start_Time_UTC,
        axis=1
)

df['lenOfConnection']

# %% [markdown]
# 5. What is the average connection time?
#    * Only take positive connection times into account
# %%
# Write your code below:
df.loc[
    df['lenOfConnection'].map(lambda x: x.total_seconds()) >= 0,
    ['lenOfConnection']
].mean()

# %%
