# Builds a parent class
class Parent(object):

    # Builds a fucntion named 'override'
    def override(self):
        print("PARENT override()")
    # Builds a function named 'implicit'
    def implicit(self):
        print("PARENT implicit")

    # Builds a function named 'altered'
    def altered(self):
        print("PARENT altered()")

# Builds a class named 'Child' which has
# Inheritance from its parent class 'Parent'
class Child(Parent):

    # overwrites the override functions inherenced
    # from the parent class 'Parent'
    def override(self):
        print("CHILD override()")

    # overwrites the altered function from its
    # parent class 'Parent'
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        # call the 'super' method which is aware of 
        # inheritance and will get and call the original
        # Parent class 'Functions' for you.
        super(Child, self).altered()
        print("CHILD, AFTER PARENT alrered()")

dad = Parent()
son = Child()

# Not an overwrite
dad.implicit()
# Not an overwrite, inheritance
son.implicit()

# Not an overwrite
dad.override()
# Yes an override
son.override()

# Not an override
dad.altered()
# Yes an override, but aslo
# origianl fucntion brough 
# back from parent.
son.altered()



