# Python allows you to make Object Templates called 'Classes' that define what parameters and methods your object will have

class Car: # Our class is called 'Car'

    # When we create a Car 'Instance' we define some parameters using the __init__ function
    def __init__(self, make, model, colour, age):
        # 'self' is how you reference THIS car, not ALL cars - the current instance of car

        # set the parameters of THIS car instance using the ones you pass into __init__
        # Note: Javascript uses 'this' instead of 'self'

        self.make   = make
        self.model  = model
        self.colour = colour
        self.age    = age

        # On creation, all cars start with the engine off and speed at zero
        self.is_on  = False
        self.speed  = 0

    # switch on engine method - changes the engine is_on parameter of THIS car to True
    def switch_on_engine(self):
        self.is_on = True

    def accelerate(self, how_much_pedal):
        # Do some stuff to my car depending on how much 'pedal' you're giving.
        self.speed += how_much_pedal

    def brake(self, how_much_brake):
        # Do some stuff to my car depending on how much 'brake' you're applying.
        self.speed -= how_much_brake

dans_audi = Car('Audi','Latest model','Grey','11')

# We can access object methods or parameters using
# dans_audi.<method> or dans_audi.<parameter>

# Switch on my engine
dans_audi.switch_on_engine()

# Add 10 to my speed
dans_audi.accelerate(10)
