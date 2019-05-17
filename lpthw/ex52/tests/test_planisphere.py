# This exercise uses pytest instead of nosetest

'''
from python site packages import the framework(package)
pytest, so I can use its functionalities in this current file
'''
import pytest
from gothonweb.planisphere import *


def test_gothon_game_map():
    
    # TESTS FEATURES ON STARTING ROOM
    start_room = load_room(START)
    assert start_room.name == 'Central Corridor'
    assert start_room.go('shoot!') == generic_death
    assert start_room.go('dodge!') == generic_death 
    # Next room
    room = start_room.go('tell a joke')
    assert room == laser_weapon_armory

#-------
    armory_room = load_room('laser_weapon_armory')
    assert armory_room.name == 'Laser Weapon Armory'
    assert armory_room.go('*') == generic_death
    
    # Next room
    assert armory_room.go('0132') == the_bridge

#--------
    bridge_room = load_room('the_bridge')
    assert bridge_room.name == 'The Bridge'
    assert bridge_room.go('throw the bomb') == generic_death

    # Next room
    assert bridge_room.go('slowly place the bomb') == escape_pod

#---------
    escape_room = load_room('escape_pod')
    assert escape_pod.name == 'Escape Pod'
    assert escape_pod.go('2') == the_end_winner
    assert escape_pod.go('*') == the_end_loser








































