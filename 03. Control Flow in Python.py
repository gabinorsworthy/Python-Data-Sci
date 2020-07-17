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
from random import uniform

#%% [markdown]
# 1. Pick a random number between 1 and 20. Print a note that describes if that number is  less than 5, less than 10, less than 15, or greater than or equal to 20.

#%%
# Write your code below:
print("Answer 1:")
random_int = randint(1,20)

print(f'Your number is {random_int}')
if random_int < 5:
    print(f'{random_int} is less than 5')
if random_int < 10:
    print(f'{random_int} is less than 10')
if random_int < 15:
    print(f'{random_int} is less than 15')
if random_int >= 20:
    print(f'{random_int} is greater than or equal to 20')

print('\n')

#%% [markdown]
# 2. Pick a random number between -5 and 5. Assign a variable to 'N' if the number is negative, 'P' if the number is positive, or 0 if the number is 0 and display the value of variable.

#%%
# Write your code below:
print('Answer 2:')
random_int = randint(-5,5)

if random_int < 0:
    ans = 'N'
elif random_int > 0:
    ans = 'P'
else:
    ans = 0

print(f'{random_int} returns value {ans}\n\n')

#%% [markdown]
# 3. Write a loop that accepts user input until the user submits the string "~END~".

#%%
# Write your code below:
print("Answer 3:")
user_input = ''

while user_input != '~END~':
    user_input = input("Enter ~END~ to end loop: ")

print('\n')

#%% [markdown]
# 4. Create a collection that contains 20 random numbers between 1 and 10. Iterate over that collection printing the even values, multiplying the odds to each other, and summing all numbers then print the resulting product and sum.

#%%
# Write your code below:
myList = [randint(1,10) for i in range(0,20)]

totalSum = 0
product = 1

for item in myList:
    if not item % 2:
        print(item)
    else:
        product *= item
    
    totalSum += item

print("Answer 4:")
print(f'\n{myList}\n')
print(f'The product of odd numbers is {product}.')
print(f'The total sum of numbers is {totalSum}.\n\n')

#%% [markdown]
# 5. Create a dictionary with the below tuple for keys and random floating point values between 0 and 10 and rounded to 2 digits. Then print the sum of 1 Udon, 2 Lo Mein, 3 Japchae, 4 Pho, and 5 Spaghetti.

#%%
noodles = ('Udon', 'Lo Mein', 'Japchae', 'Pho', 'Spaghetti')
# Write your code below:
print("Answer 5:")
food_menu = {}

for food in noodles:
    random_val = round(uniform(0,10),2)
    food_menu.update( {food:random_val})

bill = 1 * food_menu['Udon'] + 2 * food_menu['Lo Mein'] + 3 * food_menu['Japchae'] + 4 * food_menu['Pho'] + 5 * food_menu['Spaghetti']
print(f'The total is ${bill}')

#%% [markdown]
# 6. Print the first 10 digits of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) in a comma-delimited string, starting with 0.

#%%
# Write your code below:
print('Answer 6: first 10 digits of the Fibonacci sequence')

f_1 = 0
f_2 = 1
print(f_1)
print(f_2)

for i in range(0,8):
    f_3 = f_1 + f_2
    print(f_3)

    f_1 = f_2
    f_2 = f_3

print('\n')

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
