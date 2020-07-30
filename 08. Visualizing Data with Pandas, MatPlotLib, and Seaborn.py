# %%
# Change working directory to data file locations
import os
try:
    old_wd = os.getcwd()
    new_wd = old_wd[:old_wd.rindex('-') + 3] + r'\Notes\Data'
    os.chdir(new_wd)
    print(f'Working Direcotry: {os.getcwd()}')
except:
    pass

# %%
# Obligatory imports
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sbn

# %% [markdown]
# # Visualizing Data with Pandas, MatPlotLib, and Seaborn
# %% [markdown]
# 1. Load aalStock.csv, store it in a variable with the index set to the
#    'date' column, and with the rows sorted on the same
# %%
# Write your code below:
stocks = pd.read_csv('C://Users/241556/Documents/00 Co-Op/Python-Data-Sci/resources/aalStock.csv')

stocks = stocks.set_index(
    stocks.date
).sort_index(ascending=True)

stocks.head()

# %% [markdown]
# 2. Show the daily, 7-day rolling average, and 30-day rolling average
#    lines for the 'high' column
#     * The rolling windows should have data only where the statistic can
#       be fully calculated. The 7-day average, for example should only
#       have data starting on the 7th day.
# %%
# Write your code below:
stocks['7-Day Avg'] = stocks.rolling(7).high.mean()
stocks['30-Day Avg'] = stocks.rolling(30).high.mean()

#display(stocks.head(40))

stocks.loc[:, ['high', '7-Day Avg', '30-Day Avg']].plot()
plt.show()

# %% [markdown]
# 3. Make a vertical 3 plot figure with the x-axes lined up. The first
#    plot will have the volume, the second will have close and open, and
#    the third will have high and low
#%%
# Write your code below:
numItems = stocks.shape[0]

sp = plt.subplot(311)
stocks.volume.plot()

plt.subplot(312, sharex=sp)
plt.plot(stocks.loc[:, ['close', 'open']])

plt.subplot(313, sharex=sp)
plt.plot(stocks.loc[:, ['high', 'low']])

# limits x ticks (wasn't doing by default)
sp.set_xticks(np.arange(0, numItems, 60))

plt.show()

#%% [markdown]
# 4. Load tips.csv to a variable, add a column for tip percentage, and
#    display the first five rows
#%%
# Write your code below:
tips = pd.read_csv('C://Users/241556/Documents/00 Co-Op/Python-Data-Sci/resources/tips.csv')
tips.head()

tips['tip percentage'] = tips.apply(
    lambda tipPerc:
        (tipPerc.tip / tipPerc.total_bill) * 100,
        axis=1
)

tips.head()

#%% [markdown]
# 5. Make a swarm plot comparing tip percentages on each day with the
#    markers colored by smoker or non-smoker
#%%
# Write your code below:
ax = sbn.swarmplot(x="day", y="tip percentage", hue="smoker", data=tips)

plt.show()

#%%
