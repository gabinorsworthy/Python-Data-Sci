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
# # Strings and String Methods
#%% [markdown]
# 1. Create a string and count the number of spaces or newlines characters in it.

#%%
# Write your code below:
myStr = "This is my string. I am very proud of my string.\n"
spaces = myStr.count(' ')
newlines = myStr.count('\n')

print("Answer 1:")
print("Original string:")
print(myStr)
print("The number of spaces is: {}".format(spaces))
print(f"The number of newline characters is: {newlines}\n\n")

#%% [markdown]
# 2. Display all of the text between and including the first and last occurences of the `~` character in the below string.

#%%
s = "This is~the whacky~string dance~is it not?"
# Write your code below:
startIndex = s.find('~')
endIndex = s.rfind('~')

print("Answer 2: display all of the text between first and last '~', inclusive")
print("Original string:")
print(f"{s}\n")
print("Substring:")
print(f"{s[startIndex:endIndex + 1]}\n\n")

#%% [markdown]
# 3. Display a grid of numbers from 1 to 100 in 10 rows of 10 and `|` between each column.

#%%
# Write your code below:
grid = '\n'.join(
    '|'.join(
        f'{(column + (row * 10)):3}' for column in range(1,11)
    )
    for row in range(10)
)

print("Answer 3: display grid af numbers 1 to 100, 10 rows of 10, '|' between each column")
print(f"{grid}\n\n")

#%% [markdown]
# 4. Display the second word of the third line in the below string.

#%%
s = """line 1
this is also a line
New lines everywhere!
so many lines!"""
# Write your code below:
thirdLine = s.split('\n')[2]
secondWord = thirdLine.split(' ')[1]

print("Answer 4: display second word of third line")
print("Original string:")
print(f"{s}\n")
print("Third line, second word:")
print(f"{secondWord}\n\n")

#%% [markdown]
# 5. The below variable, `beowulf`, is a text document containing the epic poems anout the advanetures of Beowulf. Casefold it, strip the punctuation and numbers, and store it in another variable.

#%%
with open('resources/beowulf.txt') as f:
    beowulf = f.read()
# Write your code below:
beowulfCF = beowulf.casefold()
noNumorPunc = ''.join(
    char for char in beowulfCF
    if char.isalpha() or char.isspace()
)

with open('e2q5.txt', 'w') as write_file:
    write_file.write(noNumorPunc)
write_file.close()

print("Answer 5: removal of punctuation and numbers and switch to lowercase")
print("See e2q5.txt\n\n")

#%% [markdown]
# 6. Get the initial term frequencies, create a set of stops, and store them in a set.

#%%
# Write your code below:
from collections import Counter

stops = {'with', 'then', 'that', 'from', 'when', 'they', 'this', 'them', 'have', 'where', 'were', 'their', 'would',
            'thou', 'there', 'thee', 'many', 'shall', 'should', 'after', 'will', 'came', 'some', 'neath', 'till',
            'been', 'ever', 'very', 'which', 'twas', 'more', 'though', 'each', 'your', 'under'}

print("Answer 6: Stop words, found from most common words (commented out)")
#print(Counter(noNumorPunc.split()).most_common(100))
print(f"\nStops: {stops}\n\n")

#%% [markdown]
# 7. Using your variables from #5 and #6, strip your stop words from the document and display the top 25 most common words.

#%%
# Write your code below:
no_stops = ' '.join(
    word for word in noNumorPunc.split()
    if len(word) > 3 and word not in stops
)

print("Answer 7: 25 most common words after removing 'stops'")
print(Counter(no_stops.split()).most_common(25))
print("\n")

#%% [markdown]
# 8. Using only the initial variable, print a string with the number displayed with 6, 4, and 2 decimal places with no trailing 0s and all of the decimal points lined up vertically.

#%%
import random
num = random.random()
# Write your code below:
print("Question 8: print string with number displayed with 6, 4, and 2 decimal places, no trailing 0s, decimal points aligned vertically")

print(f"{num:.6f}")
print(f"{num:.4f}")
print(f"{num:.2f}")

#%%



