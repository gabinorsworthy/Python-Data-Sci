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
def removeVowels (myStr):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    noVowels = ''

    for char in myStr:
        if char in vowels:
            pass
        else:
            noVowels += char

    print(noVowels)
    
print('Answer 1:')
removeVowels(input('Input a string to remove vowels: '))
print('\n')

#%% [markdown]
# Run the function from the above on the first 10 non-blank lines from Beowulf.txt

#%%
# Write your code below:
f = open('resources/beowulf.txt', 'r')
nonBlankLines = 0

while nonBlankLines < 10:
    line = f.readline().strip()
    if line:
        removeVowels(line)
        nonBlankLines += 1

print('\n')

#%% [markdown]
# 2. Write one or more functions such that the highest level function accepts an integer and returns a string of [Roman Numerals](https://en.wikipedia.org/wiki/Roman_numerals) or accepts Roman Numerals and returns an integer

#%%
# Write your code below:
def romanToDecimal (num):
    romanDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = 0
    newInt = 0

    while i < len(num) - 1:
        currNum = romanDict[num[i]]
        followingNum = romanDict[num[i + 1]]

        if currNum < followingNum:
            newInt += (followingNum - currNum)
            i += 2
        else:
            newInt += currNum
            i +=1
    
    if i != len(num):
        newInt += romanDict[num[i]]
    
    return newInt



def decimalToRoman (num):
    # not sure if this is cheating
    decNum = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    romanSym = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    newRoman = ''

    for i in range(len(decNum) - 1, -1, -1):
        numOfSymbol = num // decNum[i]
        
        for j in range(numOfSymbol):
            newRoman += romanSym[i]
            num -= decNum[i]

    return newRoman



def convertNum (num):
    if isinstance(num, str):
        return romanToDecimal(num)
    else:
        return decimalToRoman(num)

#%% [markdown]
# Run the function from above on each element from the below list and print the results

#%%
convertibles = [125, 'MMXIX', 77, 99, 'MCMLXXXVIII', 'XXII', 623]
# Write your code below:
print("Answer 2:")
for num in convertibles:
    print(convertNum(num))
print('\n')

#%% [markdown]
# 3. Create a function that accepts an abritrary number of integers and a sequence of operators then returns the results of applying those operators to the numbers in order, looping to the beginning of the operator sequence if necessary.
#     * The ops sequence should default to `['*', '\\', '+', '-']`
#     * Example1: Function accepts `(1, 2, 3, 4, 5, 6, 7, ops=['+', '-', '*'])` and returns `((((((1 + 2) - 3) * 4) + 5) - 6) * 7)`

#%%
# Write your code below:
def calculate (nums, ops=['*', '\\', '+', '-']):
    numOps = len(ops)
    ans = nums[0]
    
    for idx, num in enumerate(nums[1:]):
        ops_idx = idx % numOps
        operation = ops[ops_idx]

        if operation == '*':
            ans *= num
        elif operation == '\\':
            ans //= num
        elif operation == '+':
            ans += num
        elif operation == '-':
            ans -= num
        elif operation == '%':
            ans %= num
        else:
            ans **= num   

    return ans

#%% [markdown]
# Run the function from above on the following groups of arguments

#%%
first = ((6, 2, 6, 1, 2, 3, 5), {'ops': ['+', '-', '-', '**']})
second = tuple(range(1,10))
third = (tuple(range(50, 0, -2)), {'ops': ['\\','-', '-', '+', '+', '\\']})
# Write your code below:
print("Answer 3:")
print(calculate(first[0], **first[1]))
print(calculate(second))
print(calculate(third[0], **third[1]))
print('\n')

#%% [markdown]
# 4. Write a function that searches an arbitrarily nested structure of lists and prints the coordinates and values of any non-empty strings or non-0 integer multiples of 10 that it finds

#%%
# Write your code below:
def findingCoord (myList):

    for idx, i in enumerate(myList):
        if not i: continue

        if isinstance(i, list):
            findingCoord(i)

        elif isinstance(i, str):            
            print(i)

        elif not i % 10:
            print(i)


#%% [markdown]
# Run the function from above on the following structures

#%%
first = ['This', 7, 'one', 15, 'is', 'easy.', 40, 44, 25]
second = ['More', 7, ['nesting'], 64, ['here.'], 25,]
third = [8, [45, 23, ['Irregular'], 'nesting', 50], 44, ['on', 27, ''], 0, [[['this', 1], 'one', 7], '!!'], 'Yay!', 65]
# Write your code below:
print('Answer 4:')
findingCoord(first)
print()
findingCoord(second)
print()
findingCoord(third)
print('\n')

#%% [markdown]
# 5. Write a function that creates finds the nth number in the Fibonacci Sequence

#%%
# Write your code below:
def findNthFib (arg):
    if arg == 0:
        return 0
    if arg == 1:
        return 1
    
    return findNthFib(arg - 1) + findNthFib(arg - 2)


#%% [markdown]
# Use the function from above to find the 10th, 20th, 6th, and 17th numbers

#%%
# Write your code below:
print('Answer 5:')
print(f'10th Fibonacci Number: {findNthFib(10)}')
print(f'20th Fibonacci Number: {findNthFib(20)}')
print(f'6th Fibonacci Number: {findNthFib(6)}')
print(f'17th Fibonacci Number: {findNthFib(17)}')

#%%
