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
# # Classes and Objects in Python
#%% [markdown]
# 1. Create `Fleet` and `Aircraft` classes that meet the below
#    requirements, instantiate a `Fleet` object, load your new `Fleet`
#    with several `Aircraft` objects, and demonstrate the properties of
#    your `Fleet`
#     * Aircraft
#         * Requires a `status` property which indicates `"In Flight"`,
#           `"Taxiing"`, `"At Gate"`, or `"In Maintenance"`
#         * Requires one or more methods to set the `status` property
#         * Requires one or more engine related properties
#     * Fleet
#         * Must be able to hold multiple `Aircraft`
#         * Must be able to return the count of the aforementioned `Aircraft`
#           using the `len` method
#         * Must have a `ground` method in case of governmental intervention

#%%
# Write your code below:

#%% [markdown]
# 2. Create the following classes with their respective requirements. All
#    classes must validate that only the mentioned property values are
#    mentioned where applicable.
#     * Vehicle
#         * Must have `accelerate` and `decelerate` methods that set and
#           print the vehicle's new speed
#         * Must have a `powerplant` property set to `None`
#     * Train
#         * Must have `accelerate` and `decelerate` methods that set and
#           print the vehicle's new speed
#         * Must have a `powerplant` property
#         * Must set the `powerplant` property during instantiation to
#           `'Steam'`, `'Internal Combustion'`, or `'Hybrid-Electric'`
#         * Must have `conductor` and `engineer` properties set to the
#           names of these operators on instantiation
#     * Car
#         * Must have `accelerate` and `decelerate` methods that set and
#           print the vehicle's new speed
#         * Must have a `powerplant` property set to `'Inline'`, `'V'`, or
#           `'Wankel'` upon instantiation
#         * Must have a `steer` that validates the car's speed is above 0
#           and prints the direction if it is.
#     * Bicycle
#         * Must have `accelerate` and `decelerate` methods that set and
#           print the vehicle's new speed
#         * Must have a `powerplant` property set to the name of the
#           bike's operator on instantiation
#         * Must have a `transmission` property set to `'ratcheting'` or
#           `'fixie'` on instantiation
#         * Must have a `pedalBackwards` method that does nothing if
#           `transmission` is `'ratcheting'` or calls `decelerate` if it
#           is `'fixie'`

#%%
# Write your code below:


#%% [markdown]
# 3. Write a `TreeMaker` class with the following parameters and methods,
#    then create 3 differently configured objects from the class and print
#    2 differently sized trees from each
#     * Parameters
#         * `decoChar`: The characters that act as "decorations" on your
#           tree
#         * `fillChar`: The characters that makeup the bulk of your tree
#         * `treeShape`: This will define what shape the tree takes
#     * Method
#         * `makeTree`: accepts a tree height and returns a string that
#           represents the tree configured per the parameters
#
# ```python
# # Example Test
# tree = TreeMaker(decoChar='*', fillChar='-', treeShape='tiered')
# print(tree.makeTree(15))
#          **
#         *--*
#        *-*--*
#       *---*--*
#         *--*
#        *--*-*
#       *-*--*-*
#      *--*-*--**
#     *-*--*--*--*
#        *--*-*
#       *-*--*-*
#      *--*-*--**
#     *-*--*--*--*
#    **--*--*--*--*
#   *--*--*---*-*--*
#%%
# Write your code below:

#%% [markdown]
# 4. Write a class that can be used in a `with` statement that prints the
#    number of seconds elapsed every 5 seconds. Run `time.sleep(16)` in the `with` block.
#    * [Hint](https://docs.python.org/3/library/threading.html#thread-objects)


#%%
# Write your code below:
