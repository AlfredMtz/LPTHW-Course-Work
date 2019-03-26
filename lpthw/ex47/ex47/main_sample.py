# main.py
m room import Room
from character import Enemy, Character
from item import Item

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("What's up, dude! I'm hungry.")
dave.set_weakness("cheese")
dining_hall.set_character(dave)


tabitha = Enemy("Tabitha", "An enormous spider with countless eyes and furry legs.")
tabitha.set_conversation("Sssss....I'm so bored...")
tabitha.set_weakness("book")
ballroom.set_character(tabitha)


cheese = Item("cheese")
cheese.set_description("A large and smelly block of cheese")
ballroom.set_item(cheese)

book = Item("book")
book.set_description("A really good book entitled 'Knitting for dummies'")
dining_hall.set_item(book)



current_room = kitchen
backpack = []

dead = False

while dead == False:
  
  print("\n")
  current_room.get_details()
  
  inhabitant = current_room.get_character()
  if inhabitant is not None:
    inhabitant.describe()
  
  item = current_room.get_item()
  if item is not None:
    item.describe()
  
  command = input("> ")
  
  if command in ["north", "south", "east", "west"]:
    # Move in the given direction
    current_room = current_room.move(command)
  elif command == "talk":
    # Talk to the inhabitant - check whether there is one!
    if inhabitant is not None:
      inhabitant.talk()
  elif command == "fight":
    if inhabitant is not None:
      # Fight with the inhabitant, if there is one
      print("What will you fight with?")
      fight_with = input()
      
      # Do I have this item?
      if fight_with in backpack:
      
        if inhabitant.fight(fight_with) == True:
          # What happens if you win?
          print("Hooray, you won the fight!")
          current_room.character = None
          if inhabitant.get_defeated() == 2:
            print("Congratulations, you have vanquished the enemy horde!")
            dead = True
        else:
          # What happens if you lose?
          print("Oh dear, you lost the fight.")
          print("That's the end of the game")
          dead = True
      else:
        print("You don't have a " + fight_with)
    else:
      print("There is no one here to fight with")
  elif command == "take":
    if item is not None:
      print("You put the " + item.get_name() + " in your backpack")
      backpack.append(item.get_name())
      current_room.set_item(None)
    else:
      print("There's nothing here to take!")
  else:
    print("I don't know how to " + command)

# rooms.py
class Room():
  
  def __init__(self, room_name):
    self.name = room_name
    self.description = None
    self.linked_rooms = {}
    self.character = None
    self.item = None
    
  def set_character(self, new_character):
    self.character = new_character
    
  def get_character(self):
    return self.character 
  
  def set_description(self, room_description):
    self.description = room_description
    
  def get_description(self):
    return self.description
    
  def get_name(self):
    return self.name
    
  def set_name(self, room_name):
    self.name = room_name 
  
  def get_item(self):
    return self.item
    
  def set_item(self, item_name):
    self.item = item_name
  
  def describe(self):
    print( self.description )
    
  def link_room(self, room_to_link, direction):
    self.linked_rooms[direction] = room_to_link
    #print( self.name + " linked rooms: " + repr(self.linked_rooms))
    
  def get_details(self):
    print(self.name)
    print("--------------------")
    print(self.description)
    for direction in self.linked_rooms:
      room = self.linked_rooms[direction]
      print("The " + room.get_name() + " is " + direction)
      
  def move(self, direction):
    if direction in self.linked_rooms:
      return self.linked_rooms[direction]
    else:
      print("You can't go that way")
      return self