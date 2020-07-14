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
# # Control Flow in Python
#%% [markdown]
# 0. Write an import statement for all of the libraries you need.

#%%
# Write your code below:
from random import randint

#%% [markdown]
# 1. Pick a random number between 1 and 20. Print a note that describes if that number is  less than 5, less than 10, less than 15, or greater than or equal to 20.

#%%
# Write your code below:

#%% [markdown]
# 2. Pick a random number between -5 and 5. Assign a variable to 'N' if the number is negative, 'P' if the number is positive, or 0 if the number is 0 and display the value of variable.

#%%
# Write your code below:

#%% [markdown]
# 3. Write a loop that accepts user input until the user submits the string "~END~".

#%%
# Write your code below:

#%% [markdown]
# 4. Create a collection that contains 20 random numbers between 1 and 10. Iterate over that collection printing the even values, multiplying the odds to each other, and summing all numbers then print the resulting product and sum.

#%%
# Write your code below:

#%% [markdown]
# 5. Create a dictionary with the below tuple for keys and random floating point values between 0 and 10 and rounded to 2 digits. Then print the sum of 1 Udon, 2 Lo Mein, 3 Japchae, 4 Pho, and 5 Spaghetti.

#%%
noodles = ('Udon', 'Lo Mein', 'Japchae', 'Pho', 'Spaghetti')
# Write your code below:

#%% [markdown]
# 6. Print the first 10 digits of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) in a comma-delimited string, starting with 0.

#%%
# Write your code below:

#%% [markdown]
# 7. Write a loop that can find the highest value and its index in the `peaked` variable below without using any sort of `max` or `index`/`find` functions.
#     * The list will only have one peak
#         * This means the values will either all ascend, all descend, or ascend to a random point then descend
#     * The list will always have between 5 and 50 values
#     * You are not allowed to use any of the setup variables
#     * Numbers will never be duplicated

#%%
nums = tuple({randint(1, 100) for i in range(randint(5, 50))})
split_idx = randint(0, len(nums) - 1)
peaked = sorted(nums[:split_idx]) + sorted(nums[split_idx:], reverse=True)
# Write your code below:
