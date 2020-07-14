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
print("Answer 1:")
if (47689 % 7 == 0):
    print("7 is a multiple of 47689\n \n")
else:
    print("7 is not a multiple of 47689\n \n")

#%% [markdown]
# 2. Divide 27 by 7 and display the results as-is, rounded to the nearest int, and rounded to 6 decimal places

#%%
# Write your code below:
print("Answer 2:")
result = 27/7
print("standard division: " + str(result))
print("rounded to nearest int: " + str(round(result)))
print("rounded to 6 decimals: " + str(round(result,6)) + "\n")

print("Testing other print methods:")
print("standard division:", result)
print("rounded to nearest int: {}".format(round(result)))
print(f"rounded to 6 decimals: {round(result,6)} \n \n")

#%% [markdown]
# 3. Find the distance between the points (1, 7) and (7, 1) using the equation $\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$

#%%
# Write your code below:
print("Answer 3:")
distance = ((7-1)**2+(1-7)**2)**.5
print("The distance between (1,7) and (7,1) is " + str(distance) + "\n")

print("Testing other print methods")
print("The distance between (1,7) and (7,1) is", distance)
print("The distance between (1,7) and (7,1) is {}".format(distance))
print(f"The distance between (1,7) and (7,1) is {distance} \n \n")

#%% [markdown]
# 4. Create a string that will span several lines when printed, assign it to a variable, and print it.

#%%
# Write your code below:
print("Answer 4:")
myString = """Hello
World!"""
myOtherString = "Hello\nAgain\nWorld!\n"
print(myString)
print(myOtherString)

#%% [markdown]
# 5. Display the below string with all occurences of the word "run" replace with the Unicode character 1F4A9.

#%%
real_exercise = "Sorry, dude; I can't go right now, I have to head home and go for a run."
# Write your code below:
print("Answer 5:")
real_exercise = real_exercise.replace('run','\U0001F4A9')
print(real_exercise + "\n \n")

#%% [markdown]
# 6. Create an empty list then add 6 values into it of any type.

#%%
# Write your code below:
print('Answer 6:')
myList = []
myList.extend([1,'two',(3,4),(5,6),'seven',8])
for i in myList:
    print(i)
print('\n')

#%% [markdown]
# 7. Create an empty tuple then add 6 values into it of any type.

#%%
# Write your code below:
print('Answer 7:')
print('NOTE: Tuples are immutable in Python')
myTuple = ()
myTuple += (1,'two',(3,4),(5,6),'seven',8)
for i in myTuple:
    print(i)
print('\n')

#%% [markdown]
# 8. Create two sets and print or output all of the values that exist in one or the other, but not both.

#%%
# Write your code below:
print('Problem 8:')
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
print(set1 ^ set2)
print('\n')

#%% [markdown]
# 9. Programatically check to see if `'Idle'` exists in the below set.
pythons = {'Chapman', 'Cleese', 'Jones', 'Idle', 'Palin', 'Gilliam'}
#%%

# Write your code below:
print('Problem 9:')
if 'Idle' in pythons:
    print('"Idle" in set\n \n')
else:
    print('"Idle" not in set\n \n')

#%% [markdown]
# 10. Create a dictionary with fruit names for keys and numeric prices for values then output the price of an order that contains 3 apples, 2 bananas, 1 satsuma, and 8% tax.

#%%
# Write your code below:
print('Problem 10:')
myCatalog = {'apples': 3, 'bananas': 1, 'satsuma': 5}
noTaxPrice = myCatalog['apples'] * 3 + myCatalog['bananas'] * 2 + myCatalog['satsuma'] * 1
totalPrice = noTaxPrice * 1.08
print("Your total price is " + str(totalPrice))

#%%
