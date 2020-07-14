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

#%% [markdown]
# # Functions in Python
#%% [markdown]
# 1. Write a function that accepts a string and prints it with all of the vowels removed.

#%%
# Write your code below:

#%% [markdown]
# Run the function from the above on the first 10 non-blank lines from Beowulf.txt

#%%
# Write your code below:

#%% [markdown]
# 2. Write one or more functions such that the highest level function accepts an integer and returns a string of [Roman Numerals](https://en.wikipedia.org/wiki/Roman_numerals) or accepts Roman Numerals and returns an integer

#%%
# Write your code below:

#%% [markdown]
# Run the function from above on each element from the below list and print the results

#%%
convertibles = [125, 'MMXIX', 77, 99, 'MCMLXXXVIII', 'XXII', 623]
# Write your code below:

#%% [markdown]
# 3. Create a function that accepts an abritrary number of integers and a sequence of operators then returns the results of applying those operators to the numbers in order, looping to the beginning of the operator sequence if necessary.
#     * The ops sequence should default to `['*', '\\', '+', '-']`
#     * Example1: Function accepts `(1, 2, 3, 4, 5, 6, 7, ops=['+', '-', '*'])` and returns `((((((1 + 2) - 3) * 4) + 5) - 6) * 7)`

#%%
# Write your code below:

#%% [markdown]
# Run the function from above on the following groups of arguments

#%%
first = ((6, 2, 6, 1, 2, 3, 5), {'ops': ['+', '-', '-', '**']})
second = tuple(range(1,10))
third = (tuple(range(50, 0, -2)), {'ops': ['\\','-', '-', '+', '+', '\\']})
# Write your code below:

#%% [markdown]
# 4. Write a function that searches an arbitrarily nested structure of lists and prints the coordinates and values of any non-empty strings or non-0 integer multiples of 10 that it finds

#%%
# Write your code below:

#%% [markdown]
# Run the function from above on the following structures

#%%
first = ['This', 7, 'one', 15, 'is', 'easy.', 40, 44, 25]
second = ['More', 7, ['nesting'], 64, ['here.'], 25,]
third = [8, [45, 23, ['Irregular'], 'nesting', 50], 44, ['on', 27, ''], 0, [[['this', 1], 'one', 7], '!!'], 'Yay!', 65]
# Write your code below:

#%% [markdown]
# 5. Write a function that creates finds the nth number in the Fibonacci Sequence

#%%
# Write your code below:

#%% [markdown]
# Use the function from above to find the 10th, 20th, 6th, and 17th numbers

#%%
# Write your code below:


#%%
