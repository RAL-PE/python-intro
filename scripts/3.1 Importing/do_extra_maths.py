import extra_maths as math

# Python 'import' searches for a .py file with the name specified in:
# - your current directory
# - the python lib directory (if you install stuff, it goes here)


# The import function creates a python 'object' out of what it finds in the .py script
# where the object is called either:
# - the name of the .py file or
# - the name you specify with your 'as' command

# - global variables in the script become parameters of the object
# - functions in the script become methods of the object

# We can then treat the imported code exactly like a python object
# so we can print the parameters
print(math.version)

# And we can call the methods
print(math.add(1,2))

# When importing numpy, matplotlib etc it works exactly the same.

# IMPORTANT NOTE:
# import x.y.z
#  the x. specifies that you want something out of x. Python will check:
#  - if there's a file called x.py it can locate (it will then check for a function, class or variable called y in that script)
#  - if there's a directory called x, inside which is a file called y.py that it can then extract stuff from

# There is a specific order python does this in, but it isn't important as you should avoid having a directory and file with the same name