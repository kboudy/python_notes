"""
Inheritance example
"""


class Bird:
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


# child class
class Penguin(Bird):
    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")


peggy = Penguin()  # Bird is ready  Penguin is ready
peggy.whoisThis()  # Penguin
peggy.swim()  # Swim faster
peggy.run()  # Run faster

"""
Polymorphism example
"""


class Parrot:
    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can not swim")


class Penguin:
    def fly(self):
        print("Penguin can not fly")

    def swim(self):
        print("Penguin can swim")


# common interface
def flying_test(bird):
    bird.fly()


# instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)


"""
class method & variable
"""


class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print("(Initializing {})".format(self.name))
        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))

    def say_hi(self):
        """Greeting by the robot.
        Yeah, they can do that."""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")  # (Initializing R2-D2)
droid1.say_hi()  # Greetings, my masters call me R2-D2.
Robot.how_many()  # We have 1 robots.
droid2 = Robot("C-3PO")  # (Initializing C-3PO)
droid2.say_hi()  # Greetings, my masters call me C-3PO.
Robot.how_many()  # We have 2 robots.
droid1.die()  # R2-D2 is being destroyed!  # There are still 1 robots working.
droid2.die()  # C-3PO is being destroyed!  # C-3PO was the last one.
Robot.how_many()  # We have 0 robots.

"""
delattr:

Deletes the named attribute from the given object.

delattr(x, 'y') is equivalent to `del x.y''
"""


class SomeClass:
    name = "Keith"


delattr(SomeClass, "name")
sc = SomeClass()

print(sc.name)  # AttributeError: 'SomeClass' object has no attribute 'name'
