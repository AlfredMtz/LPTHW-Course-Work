'''
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print(f"Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly")
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
'''

def dog_description(size, color):
    print(f"So it was a {size} dog, with {color} hair!")
    print("Well that sounds like a nice dog")

# 1
dog_description('small', 'brown')

# 2
size_of_dog = 'small'
color_of_dog = 'brown'

dog_description(size_of_dog, color_of_dog)

#3
dog_description('sma'+'ll', 'bro'+'wn')

#4
print("Once again, what was the size of the dog?")
size = input()
print("How about the color of the dog?")
color = input()

dog_description(size, color)

