# To perform testing
from nose.tools import *
# from folder ex47 and file game.py import
# the class Room and its functionalityies to
# be tested
from ex47.game import Room


def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a
                door to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})
    # Asserting that function go will go to north variable
    assert_equal(center.go('north'), north)
    # Asserting that functin ago will go to south variable
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")
    #up = Room("north", "There is a rock here, you can go")


    # If user hits 'west' key return west variable value anf bias versa.
    start.add_paths({'west': west, 'down': down})
    # If west value return then add key-value 'east': start
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)          






































