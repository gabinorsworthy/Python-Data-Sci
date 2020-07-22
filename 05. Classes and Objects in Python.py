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

from warnings import warn

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
class Aircraft:
    def __init__(self, engine, status="In Maintenance"):
        self.status = status
        self.engine = engine
    
    def getEngine(self):
        return self.engine
    
    def getStatus(self):
        return self.status
        
    def statusChange(self, status):
        self.status = status
    
    def takingOff(self):
        if self.status == "Taxiing":
            self.status = "In Flight"
            print('Taking off...now in flight.')
        else:
            warn(f'Aircraft needs to be taxiied before taking off.')
    
    def landing(self):
        if self.status == "In Flight":
            self.status = "Taxiing"
            print('Landing...now being taxiied.')
        else:
            warn(f'Aircraft cannot be landing if it is not in flight.')

    def taxiing(self):
        if self.status == "At Gate" or self.status == "In Maintenance":
            self.status = "Taxiing"
            print('Taxiing aircraft...')
        else:
            warn(f'Cannot begin taxiing if aircraft is not parked. Is the plane landing?')

    def parking(self, location):
        if location == "Gate":
            self.status = "At Gate"
            print('Parking aircraft at gate...')
        elif location == "Maintenance Center":
            self.status = "In Maintenance"
            print('Aircraft in for maintenance...')
        else:
            warn(f'Aircraft must be parked At Gate or at Maintenance Center')


class Fleet:
    def __init__ (self, *args):
        self.aircrafts = []
        for aircraft in args:
            self.aircrafts.append(aircraft)
    
    def __len__ (self):
        return(len(self.aircrafts))
    
    def ground(self):
        for aircraft in self.aircrafts:
            aircraft.parking("Maintenance Center")

    def statusOfAircrafts(self):
        for aircraft in self.aircrafts:
            print(aircraft.getStatus())

print("ANSWER 1:")
eng = "123"
aircraft1 = Aircraft(eng, "In Maintenance")
aircraft2 = Aircraft(eng, "At Gate")
aircraft3 = Aircraft(eng, "In Flight")

b777 = Fleet(aircraft1, aircraft2, aircraft3)
print(f'Number of aircrafts in fleet: {len(b777)}\n')

print('Current status of aircrafts:')
b777.statusOfAircrafts()
print()
b777.ground()
print('\nAircrafts after grounding fleet:')
b777.statusOfAircrafts()

print()
aircraft1.taxiing()
aircraft1.parking("Gate")
aircraft1.takingOff()
aircraft1.taxiing()
aircraft1.takingOff()
print(f'Aircraft 1 status: {aircraft1.getStatus()}\n\n')

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
trainPowerplants = ('Steam', 'Internal Combustion', 'Hybrid-Electric')
carPowerplants = ('Inline', 'V', 'Wankel')
bikeTransmissions = ('ratcheting', 'fixie')

class Vehicle:
    def __init__ (self):
        self.powerplant = None
        self.speed = 0
    
    def getPowerplant(self):
        return self.powerplant
    
    def getSpeed(self):
        return self.speed
    
    def accelerate(self, increase):
        self.speed += increase
        print(f'Your new speed is {self.speed} mph')
    
    def decelerate(self, decrease):
        if self.speed == 0:
            print('You cannot go slower than 0 mph')
        elif self.speed - decrease < 0:
            print(f'You cannot go slower than 0 mph. Your new speed is 0 mph, but you decreased {self.speed} mph instead of {decrease} mph')
            self.speed = 0
        else:
            self.speed -= decrease
            print(f'Your new speed is {self.speed} mph')


class Train(Vehicle):
    def __init__ (self, engineer, conductor, powerplant="Steam"):
        self.engineer = engineer
        self.conductor = conductor
        self.speed = 0

        if powerplant not in trainPowerplants:
            warn('Not a valid powerplant value. Defaulted to Steam')
            self.powerplant = "Steam"
        else:
            self.powerplant = powerplant

    def getEngineer(self):
        return self.engineer
    
    def getConductor(self):
        return self.conductor


class Car(Vehicle):
    def __init__(self, powerplant="Inline"):
        self.speed = 0

        if powerplant not in carPowerplants:
            warn('Not a valid powerplant value. Defaulted to Inline')
            self.powerplant = "Inline"
        else:
            self.powerplant = powerplant

    def steer(self, direction):
        if self.speed > 0:
            print(f'Turning {direction}')
        else:
            print("Cannot turn. You're not moving!!")


class Bicycle(Vehicle):
    def __init__(self, operator, transmission="ratcheting"):
        self.powerplant = operator
        self.operator = operator
        self.speed = 0

        if transmission not in bikeTransmissions:
            print(f'Not a valid transmission. Defaulting to ratcheting.')
            self.transmission = "ratcheting"
        else:
            self.transmission = transmission
    
    def pedalBackwards(self, amount):
        if self.transmission == 'fixie':
            self.decelerate(amount)

print('ANSWER 2 TEST:')

print('Testing vehicle class...')
vehicle = Vehicle()
vehicle.accelerate(4)
vehicle.decelerate(5)
vehicle.decelerate(1)
print(vehicle.getPowerplant())

print('\nTesting train class...')
#train = Train('Joe','Gabi','hello')
train = Train('Joe','Gabi')
print(f'Powerplant: {train.getPowerplant()}')
print(f'Conductor: {train.getConductor()}')
print(f'Engineer: {train.getEngineer()}')

print('\nTesting car class...')
car = Car('V')
print(f'Powerplant: {car.getPowerplant()}')
car.steer('left')
car.accelerate(30)
car.steer('left')
car.decelerate(40)

print('\nTesting bicycle class...')
bicycle = Bicycle('Gabi','fixie')
bicycle.accelerate(10)
bicycle.pedalBackwards(5)
bicycle.accelerate(5)

print('\n')

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
from random import randint

class TreeMaker:
    def __init__(self, decoChar, fillChar, treeShape):
        self.deco = decoChar
        self.fill = fillChar
        self.shape = treeShape

    def makeStandard(self, height):
        decorationSpacing = randint(2, 5)

        for i in range(1, height + 1):
            
            level = ' ' * (height - i)
            for j in range((i * 2) - 1):
                if j % decorationSpacing == 0:
                    level += self.deco
                else:
                    level += self.fill
            print(f'{level}')


    def makeUpsideDown(self, height):
        decorationSpacing = randint(2, 5)

        for i in range(1, height + 1):
            
            level = ' ' * (i - 1)
            for j in range(((height-i + 1) * 2) - 1):
                if j % decorationSpacing == 0:
                    level += self.deco
                else:
                    level += self.fill
            print(f'{level}')


    def makeTiered(self, height):
        if height < 4:
            self.makeStandard(height)
            return 0
        elif height < 9:
            numofTiers = 2
        else:
            numofTiers = 3
        decorationSpacing = randint(2, 5)
        tierBreak = height // numofTiers
        
        startIteration = 1
        currIteration = 1
        tierNum = 1

        for i in range(1, height + 1):
            
            level = ' ' * (height - currIteration)
            for j in range((currIteration * 2) - 1):
                if j % decorationSpacing == 0:
                    level += self.deco
                else:
                    level += self.fill
            print(f'{level}')

            if tierBreak != 0 and not i % tierBreak and tierNum < numofTiers:
                currIteration = ((i - startIteration) // 2) + 1
                startIteration = currIteration
                tierNum += 1
            else:
                currIteration += 1

    
    def makeTree(self,height):
        if self.shape == "tiered":
            self.makeTiered(height)
        elif self.shape == "standard":
            self.makeStandard(height)
        elif self.shape == "upside-down":
            self.makeUpsideDown(height)


tree1 = TreeMaker('*','-','standard')
tree2 = TreeMaker('`','^','upside-down')
tree3 = TreeMaker('#','~','tiered')

("ANSWER 3 TEST:")
tree1.makeTree(15)
print('\n')
tree1.makeTree(5)
print('\n')

tree2.makeTree(7)
print('\n')
tree2.makeTree(14)
print('\n')

tree3.makeTree(10)
print('\n')
tree3.makeTree(17)
print('\n\n\n')

#%% [markdown]
# 4. Write a class that can be used in a `with` statement that prints the
#    number of seconds elapsed every 5 seconds. Run `time.sleep(16)` in the `with` block.
#    * [Hint](https://docs.python.org/3/library/threading.html#thread-objects)


#%%
# Write your code below:
from threading import Thread
import time

class TimeKeeper(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.finished = False
        self.daemon = True

    def run(self):
        startTime = time.perf_counter()

        while not self.finished:
            print(f'{time.perf_counter() - startTime:.2f} seconds')
            time.sleep(5)

    def __enter__(self):
        self.start()

    def __exit__(self, type, value, traceback):
        self.finished = True
        self.join()

print("ANSWER FOUR TEST:")
with TimeKeeper():
    time.sleep(16)

# %%
