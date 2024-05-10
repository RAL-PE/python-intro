## Variable types 

# x is declared with a value of 1
x = 1
# python interprets this to mean x is an integer variable,
# but it is not explicitly defined

# x can then be reassigned with a new value which is not
# an integer
x = 'helloworld'
# python interprets this as a variable reassignment
# and x becomes a string

# Python also allows for data conversion between types,
# i.e integer to string, or string to int (with restrictions)

y = '1'
print(int(y))
# python is capable of interpreting this as a conversion
# from string to int, where other languages do not have this
# capability - more flexible but greater risk of user error.

print(int('Hi'))
# An example of where python will fail, as 'Hi' cannot be converted to int

## Variable scope
global_var = 'version1'

def do_something(input1, input2):
    # input1 and input2 are local to this function
    # to get the values of these outside of the function, 
    # it is best practice to return them
    
    local_var = 'version1.1'
    # local_var only exists within this function

    global_var = local_var
    # This variable reassignment does not extend outside the function

    return local_var
    # Value of local_var continues outside the function - all other 
    # variables cease to have meaning


## Functions and procedures

def add(A, B):    # A typical function with inputs and an output
    return A + B  # This is a single return value, although python (unlike other languages) allows for multiple returns

def hello():      # In other languages this would be a procedure with different syntax
    print('Hi!')  # No return value - doesn't matter for python

## Python interpreting

# subtract will not be recognised by the interpreter
# my environment has recognised this, hence the highlight
x = subtract(3,1)

def subtract(A, B):
    return A - B

# Functions can only be used ('called') after the declaration
x = subtract(3,1)

