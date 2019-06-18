
import pytest
from gothonweb.planisphere import *

# Testing room directions
@pytest.mark.parametrize('current_room, direction, new_room',
                        [
                            (Rest_Area, 'south', Spaceship_Bathroom),
                            (Spaceship_Bathroom, 'north', Rest_Area),
                            (Rest_Area, 'east', Main_Lobby),
                            (Main_Lobby, 'west', Rest_Area),
                            (Main_Lobby, 'east', Central_Corridor),
                            (Central_Corridor, 'shoot!', Shoot_Death),
                            (Central_Corridor, 'dodge!', Dodge_Death),
                            (Central_Corridor, 'tell a joke', Laser_Weapon_Armory),
                            (Laser_Weapon_Armory, '123', The_Bridge),
                            (Laser_Weapon_Armory, '*', Exceedtries_Death),
                            (The_Bridge, 'throw the bomb', Bridge_Death),
                            (The_Bridge, 'slowly place the bomb', Escape_Pod),
                            (Escape_Pod, '2', The_End_Winner),
                            (Escape_Pod, 'end', The_End_Loser)
                        ]
                        )
def test_gothon_game_map(current_room, direction, new_room):
    assert current_room.go(direction) == new_room









































