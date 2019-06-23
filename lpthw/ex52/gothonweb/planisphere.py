import random
from sys import exit
from random import randint

class Room(object):

    def __init__(self, name, description, helpsystem):
        self.name = name
        self.description = description
        self.helpsystem = helpsystem
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)




# GAME1    [Gothons From Planet Percal #25 Game] ------------------------------
Rest_Area = Room("Rest Area",
"""
You are in your spaceship sleeping and waiting to get back home after saving 
a struggling planet that was in the hands of evil invaders. Suddenly, you hear
a loud sound as if someone had fired a gun laser somewhere within the spaceship. 
You wake up, and carefully start investigating around the room.

What direction do you want to go?
""", "You can go either right or down")

Spaceship_Bathroom = Room("Spaceship Bathroom",
                          """
You accessed your bathroom, there is nothing specially here
Which way do you want to go now?
""", "You can go up")

Main_Lobby = Room("Main Lobby",
"""
You are at the spaceship main lobby, and something feels suspicious, is quite,
too quite indeed. Suddenly, you hear another blast and this time is much louder,
quickly you start to investigate and try to find out where is coming from.

Which way do you want to go now?
""", "You can either right or left")


Central_Corridor = Room("Central Corridor",
"""
The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew.  You are the last surviving member and your last
mission is to get the neutron destruct bomb from the Weapons Armory, put
it in the bridge, and blow the ship up after getting into an escape pod.

You're running down the central corridor to the Weapons Armory when a
Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown
costume flowing around his hate filled body.  He's blocking the door to
the Armory and about to pull a weapon to blast you.

What would you like to do?
Type in the word/pharse:
""", "You can eihter shoot, dodge or tell a joke")


Shoot_Death = Room("death",
"""
Quick on the draw you yank out your blaster and fire
it at the Gothon.  His clown costume is flowing and
moving around his body, which throws off your aim.
Your laser hits his costume but misses him entirely.
This completely ruins his brand new costume his mother
bought him, which makes him fly into an insane rage
and blast you repeatedly in the face until you are
dead.  Then he eats you.
""", None)

Dodge_Death = Room("death", 
"""
Like a world class boxer you dodge, weave, slip and
slide right as the Gothon's blaster cranks a laser
past your head.  In the middle of your artful dodge
your foot slips and you bang your head on the metal
wall and pass out.  You wake up shortly after only to
die as the Gothon stomps on your head and eats you.
""", None)

Laser_Weapon_Armory = Room("Laser Weapon Armory",
"""
Lucky for you they made you learn Gothon insults in the academy.  You
tell the one Gothon joke you know: Lbhe zbgure vf fb sng, jura fur fvgf
nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.  The Gothon stops, tries
not to laugh, then busts out laughing and can't move.  While he's
laughing you run up and shoot him square in the head putting him down,
then jump through the Weapon Armory door.

You do a dive roll into the Weapon Armory, crouch and scan the room for
more Gothons that might be hiding.  It's dead quiet, too quiet.  You
stand up and run to the far side of the room and find the neutron bomb
in its container.  There's a keypad lock on the box and you need the
code to get the bomb out.  If you get the code wrong 10 times then the
lock closes forever and you can't get the bomb.  The code is 3 digits.
""", "The three digit code is an easy tree sequence number")

Exceedtries_Death = Room("Bomb Death",
"""
The lock buzzes one last time and then you hear a
sickening melting sound as the mechanism is fused
together.  You decide to sit there, and finally the
Gothons blow up the ship from their ship and you die.
""", None)

The_Bridge = Room("The Bridge",
"""
The container clicks open and the seal breaks, letting gas out.  You
grab the neutron bomb and run as fast as you can to the bridge where you
must place it in the right spot.

You burst onto the Bridge with the netron destruct bomb under your arm
and surprise 5 Gothons who are trying to take control of the ship.  Each
of them has an even uglier clown costume than the last.  They haven't
pulled their weapons out yet, as they see the active bomb under your arm
and don't want to set it off.

What would you like to do?
""", "You can either throw the bomb or slowly place the bomb")

Escape_Pod = Room("Escape Pod",
"""
You point your blaster at the bomb under your arm and the Gothons put
their hands up and start to sweat.  You inch backward to the door, open
it, and then carefully place the bomb on the floor, pointing your
blaster at it.  You then jump back through the door, punch the close
button and blast the lock so the Gothons can't get out.  Now that the
bomb is placed you run to the escape pod to get off this tin can.

You rush through the ship desperately trying to make it to the escape
pod before the whole ship explodes.  It seems like hardly any Gothons
are on the ship, so your run is clear of interference.  You get to the
chamber with the escape pods, and now need to pick one to take.  Some of
them could be damaged but you don't have time to look.  There's 5 pods,
which one do you take?

Input the number of your chosen pod (1-5):
""", "Think about a peace sign")

Bridge_Death = Room('Bridge Death',
"""
In a panic you throw the bomb at the group of Gothons
and make a leap for the door.  Right as you drop it a
Gothon shoots you right in the back killing you.  As
you die you see another Gothon frantically try to
disarm the bomb. You die knowing they will probably
blow up when it goes off.
""", None)

The_End_Winner = Room("The End Winner",
"""
You jump into pod 2 and hit the eject button.  The pod easily slides out
into space heading to the planet below.  As it flies to the planet, you
look back and see your ship implode then explode like a bright star,
taking out the Gothon ship at the same time.  You won!
""", None)


The_End_Loser = Room("The End Loser",
"""
You jump into a random pod and hit the eject button.  The pod escapes
out into the void of space, then implodes as the hull ruptures, crushing
your body into jam jelly.
""", None)


quips = [
    "You died.  You kinda suck at this.",
    "Your Mom would be proud...if she were smarter.",
    "Such a luser.",
    "I have a small puppy that's better at this.",
    "You're worse than your Dad's jokes."
]
Generic_Death = Room("death", quips[randint(0, len(quips)-1)], None)


Rest_Area.add_paths({
    'right': Main_Lobby,
    'down': Spaceship_Bathroom
})

Spaceship_Bathroom.add_paths({
    'up': Rest_Area
})

Main_Lobby.add_paths({
    'right': Central_Corridor,
    'left': Rest_Area
})

Central_Corridor.add_paths({
    'shoot': Shoot_Death,
    'dodge': Dodge_Death,
    'tell a joke': Laser_Weapon_Armory
})

Laser_Weapon_Armory.add_paths({
  '123': The_Bridge,
  '*': Exceedtries_Death
})

The_Bridge.add_paths({
    'throw the bomb': Bridge_Death,
    'slowly place the bomb': Escape_Pod
})

Escape_Pod.add_paths({
    '2': The_End_Winner,
    'end': The_End_Loser
})

START_GAME1 = 'game1_start'
GENERIC_DEATH = 'death'
right_choices = ['tell a joke', '123', 'slowly place the bomb', '2']






# GAME2 [A second game example] --------------------------------------------------------
Another_Game = Room("Another Game Sample",
                 """
THIS IS A SAMPLE FOR ANOTHER GAME, TO LET PEOPLE CHOOSE A GAME THEY WANT TO PLAY
""", "You can go either east or south")

START_GAME2 = 'game2_start'





# GAMES' MAP -------------------------------------------------------------------
# Mapping for games
scences = {'game1_start': Rest_Area,
           'game2_start': Another_Game,
           'main_lobby': Main_Lobby,
           'spaceship_bathroom': Spaceship_Bathroom,
           'rest_area': Rest_Area,
           'central_corridor': Central_Corridor,
           'shoot': Shoot_Death,
           'dodge': Dodge_Death,
           'laser_weapon_armory': Laser_Weapon_Armory,
           '*': Exceedtries_Death,
           'the_bridge': The_Bridge,
           'bridge_death': Bridge_Death,
           'escape_pod': Escape_Pod,
           'the_end_winner': The_End_Winner,
           'end': The_End_Loser,
           'death': Generic_Death
           }



# GAME FUNCTIONS ---------------------------------------------------------------
# Gets key value
def load_room(name):
    val = scences.get(name)
    return val


# returns specific scenes key if given room/parameter 
# equals to a scenes' key value
def name_room(room):
    for key, value in scences.items():
        if value == room:
            return key
