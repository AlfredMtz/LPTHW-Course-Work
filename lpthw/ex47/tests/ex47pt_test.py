# This exercise uses pytest instead of nosetest

'''
from python site packages import the framework(package)
pytest, so I can use its functionalities in this current file
'''
import pytest
'''
from project(diccionary) ex47 import the
# functionalities from the file game.py
'''
from ex47 import game

'''
Now I will be testing if the class Room() works, which is
inside of the file game.py
'''
def test_Room():
    room = game.Room('GoldRoom',
    """This room has gold in it. There is a door
    to the right.""")

    # Here I am just testing my attributes where defined as
    # intended inside of the Room() class
    assert room.name == 'GoldRoom'
    assert room.paths == {}

'''
Now I will be testing if the fucntion [.add_paths] and [.go()]
from the Room() class actually works as intended.
'''
def test_room_paths():
    center = game.Room('Center', 'Test room in the center')
    north = game.Room('North','Test room in the norht')
    south = game.Room('South', 'Test room in the south')
    center.add_paths({'north': north, 'south': south})

    # Here I am just testing using pytest whether the fucntion
    # [.add_paths] and [.go()] from the class Room() works or not.
    assert center.go('south') == south
    assert center.go('north') == north

'''
Now I will be testing a while map with all three fucntionalities
working together as a beautiful  Beethoven's symphony!
'''
def test_map():
    start = game.Room("Start", "You can go west and fall down in a cave")
    west = game.Room("Trees", "There are only trees here, you can go east.")
    down = game.Room("Dungeon", "how did you get here? Get back up to the game!")

    # Adding paths to each room
    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    # Here I am testing how from room to room and being able
    # to come back to previous rooms without a problem.

    assert start.go('west') == west
    assert start.go('west').go('east') == start
    assert start.go('down').go('up') == start

