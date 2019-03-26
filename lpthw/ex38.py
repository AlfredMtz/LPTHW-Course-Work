ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
                "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    # pop(more_stuff)
    # call pop on more_stuff
    # call pop with argument more_stuff
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    # append(stuff)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
# pop(stuff)
print(stuff.pop())
# attaches all items in the list as a single string
print(' '.join(stuff)) # what? cool!
# attaches the # symbol on the specified space
print('#'.join(stuff[3:5])) # super stellar!