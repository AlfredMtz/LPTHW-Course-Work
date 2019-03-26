class Animal(object):

    def __init__(self, name, gender, color):
        
        self.name = name
        self.gender = gender
        self.color = color
    
    def new_name(self, new_name):

        self.name = new_name

    def kind(self, description):

        print(f"I'am a {description}")


class Dog(Animal):

    def __init__(self, gender, name, color):

        super(Dog, self).__init__(gender)
        self.name = name
        self.color = color
    
    def action(self, input):

        print(f"{input}")

class Cat(Animal):

    def __init__(self, name):

        self.name = name

    def sound(self):
        print("Miaooouww")

    def hungry(self, inpt):

        if inpt == 'yes':
            print("Let's feed him rightnow")
        elif inpt == 'no':
            print("Ok, Just pet him then")
        else:
            print('Error')


class Person(object):

    def __init__(self, name, race):

        self.name = name
        self.race = race
        self.pet = None
        

    def new_name(self, new_name):

        self.name = new_name
    
    def introduction(self):

        print("Hi, I'am a sample")

class Employee(Person):

    def __init__(self, name, race, salary):

        super().__init__(name, race)

        self.salary = salary

class Fish(object):
    
    def __init__(self, name):
        self.name = name 

    def speak(self):
        print("Gluck!" * 3)

class Salmon(Fish):
    def __init__(self, color):
        self.color = color 

    def count(self, x):
        return x * 3



