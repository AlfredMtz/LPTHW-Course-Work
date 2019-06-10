# This exercise uses pytest instead of nosetest

'''
from python site packages import the framework(package)
pytest, so I can use its functionalities in this current file
'''
import pytest
from gothonweb.planisphere import *
# from gothonweb import planisphere

def test_gothon_game_map():
    
    # TESTS FEATURES ON STARTING ROOM
    start_room = load_room(START)
    assert start_room.name == 'Central Corridor'
    assert start_room.go('shoot!') == Shoot_Death
    assert start_room.go('dodge!') == Dodge_Death 
    # Next room
    room = start_room.go('tell a joke')
    assert room == Laser_Weapon_Armory

#-------
    armory_room = load_room('laser_weapon_armory')
    assert armory_room.name == 'Laser Weapon Armory'
    assert armory_room.go('*') == Exceedtries_Death
    
    # Next room
    assert armory_room.go('123') == The_Bridge

#--------
    bridge_room = load_room('the_bridge')
    assert bridge_room.name == 'The Bridge'
    assert bridge_room.go('throw the bomb') == Bridge_Death

    # Next room
    assert bridge_room.go('slowly place the bomb') == Escape_Pod

#---------
    escape_pod_room = load_room('escape_pod')
    assert escape_pod_room.name == 'Escape Pod'
    assert escape_pod_room.go('2') == The_End_Winner
    assert escape_pod_room.go('end') == The_End_Loser

    generic_d = load_room('death')
    assert generic_d.name == 'death'
    # HOW DO I ASSERT THAT MY OUTPUT IS RANDOM??
    #  --->>  assert generic_d.go()








































