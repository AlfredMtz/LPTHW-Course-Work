name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 * 2.54 # from inches to centermeters
weight = 180 * .4535 # from lbs to kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} centermeters tall.")
print(f"He's {weight} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = round(age + height + weight,ndigits=2)
print(f"If I add {age}, {height}, and {weight} I get {total}.")
