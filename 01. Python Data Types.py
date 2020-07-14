#%%
# Change working directory to data file locations
# This won't actually work until there's a /Notes/Data directory
import os
try:
    old_wd = os.getcwd()
    print('Old WD:', old_wd[:old_wd.rindex('-') + 3])
    new_wd = old_wd[:old_wd.rindex('-') + 3] + r'\Notes\Data'
    os.chdir(new_wd)
    print('New WD:', os.getcwd())
except Exception as e:
    pass

#%% [markdown]
# # Python Data Types and Collections: Assignment
#%% [markdown]
# 1. Check if 47689 is a multiple of 7

#%%
# Write your code below:

#%% [markdown]
# 2. Divide 27 by 7 and display the results as-is, rounded to the nearest int, and rounded to 6 decimal places

#%%
# Write your code below:

#%% [markdown]
# 3. Find the distance between the points (1, 7) and (7, 1) using the equation $\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$

#%%
# Write your code below:

#%% [markdown]
# 4. Create a string that will span several lines when printed, assign it to a variable, and print it.

#%%
# Write your code below:

#%% [markdown]
# 5. Display the below string with all occurences of the word "run" replace with the Unicode character 1F4A9.

#%%
real_exercise = "Sorry, dude; I can't go right now, I have to head home and go for a run."
# Write your code below:

#%% [markdown]
# 6. Create an empty list then add 6 values into it of any type.

#%%
# Write your code below:

#%% [markdown]
# 7. Create an empty tuple then add 6 values into it of any type.

#%%
# Write your code below:

#%% [markdown]
# 8. Create two sets and print or output all of the values that exist in one or the other, but not both.

#%%
# Write your code below:

#%% [markdown]
# 9. Programatically check to see if `'Idle'` exists in the below set.
pythons = {'Chapman', 'Cleese', 'Jones', 'Idle', 'Palin', 'Gilliam'}
#%%

# Write your code below:

#%% [markdown]
# 10. Create a dictionary with fruit names for keys and numeric prices for values then output the price of an order that contains 3 apples, 2 bananas, 1 satsuma, and 8% tax.

#%%
# Write your code below:

#%%
