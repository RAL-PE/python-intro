## Variables
x        = 1         # integer
name     = 'Me'      # string
is_alive = False     # boolean
height   = 182.5     # float

## Lists
shopping = ['Bread','Milk','Carrots'] 

# add to list
shopping.append('Cookies') # Adds to the end of the list
# remove from list
shopping.pop()             # Removes last list item

# index items in the list
print(shopping[1]) # Will print 'Milk'

# slicing items out of the list - also works for strings
shopping[0:2] # ':' effectively means were looking for the 0th to 2nd items in the list

              #     the start of our slice is 'inclusive' - 0th item WILL be included
              #     the end of our slice is 'exclusive' - 2nd item WILL NOT be included


## Dictionaries
# storing key-value pairs
my_passwords = {
    'Facebook': 'password',
    'Netflix': '123456',
    'Amazon': 'fluffytherabbit'
}

# If we know the 'key' we can find the 'value'
print(my_passwords['Facebook'])

## Conditionals
mode = 'Pirate'
if mode == 'Pirate': # Our primary branch
    print('Arrr, welcome me hearties!')
elif mode == 'Alien': # Alternative branch (you can have lots of these)
    print('Squiggle blarg, arty barnag whadoo!')
else: # Fallback branch (if no other condition is met)
    print('Hello there!')

## Conditionals - extended
# Python also has a form of conditional specifically for errors

try:
    # Do something that we're worried will cause the program to crash
    x = 1 + '2'
except:
    print('Cant add ints and strings together')

# Note you can specify multiple 'except' branches depending on the error
#    except KeyError: - If we try to get an item in a dictionary but use an invalid key
#    except IndexError: - If we try to access the 12th item in a list of 10 items (for example)

## For Loops
# iterate over all items in a list or string
my_name = 'Daniel'
char_counter = 0
for character in my_name:
    print(character)
    char_counter += 1

# python for loops come with a built_in way of having a character/item counter
# a simpler way of doing the item indexing of characters in my name
for char_counter, character in enumerate(my_name):
    print(character)

# We can also iterate over a range of numbers 
# - and we can use a len() argument
for char_counter in range(0, len(my_name)):
    # here we specify a range from 0 to some number. 
    # The number we give it is the length of 'my_name'
    print(character[char_counter])
    # So now we're using the char_counter to index the string 
    # (indexing is a fancy way of saying 'take item x and do something')

## While Loops
# loop until something happens

# if we're trying to find an item in a list of 10 items, 
# we don't want to iterate over all of them 
# if we find the item in position 2

letters = ['A','B','C','D','E','F','G','H','I']

is_found = False
letter_count = 0
while is_found == False: 
    # Also equivalent is saying 'while not is_found' as 'not' is a keyword
    if letters[letter_count] == 'B':
        # Found the letter we're looking for!
        print(letter_count)
        is_found = True
        # The loop will end right after we've found the item
    letter_count += 1

## Functions

# in the 'combine' function:
#    A and B are mandatory - they must be supplied
#    mode is optional - you can supply an override 
#           but otherwise it has a default value

def combine(A, B, mode='add'): # Parameters given in the brackets
    if mode == 'add':
        return A + B
    else: # Do a different thing
        return None # Return specifies the function output

# Note: any new variables defined (declared) in a function
#       or any data changes to existing variables are only
#       valid within the function. The return function allows you 
#       to pass changes out of the function. Functions are therefore 
#       a small pocket area where you can define all sorts of temporary
#       variables that don't affect the rest of the code

# To call a function, the syntax is:
result = combine(1,2)
other  = combine('1','2',mode='concat')
# but I haven't defined the new mode 'concat' so 
# I'll get a 'None' value for 'other'

## In-built functions
print('Hello World')  # Prints to terminal

type(1)               # Gets the type of a parameter

enumerate(shopping)   # Returns a range covering the items in the list as part of a loop

## Special cases

# import              # Imports a different python script (.py)
#                       as a python object - global variables become parameters
#                                          - functions become methods

# assert              # Used in error checking to cause an error if a condition is not true

def function_name(arguments, do_return=False):
    print(arguments)
    if do_return:
        return True

# In general python functions have the format:
function_name(arguments)                          # no return value
result = function_name(arguments, do_return=True) # do return using optional variable
