"""
* Map
 - next_scene
 - opening_scene
* Engine
 - play
* Scene
    * Intro
    * Unavailable Product
    * Living Room
    * Bedroom
    * Diningroom
    * Mattresses
* Payment
    * Cash
    * Financing
    * Layaway
* GoodBye
"""
from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        pass

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
        print("first scene:", self.scene_map)

    def play(self):
        current_scene = self.scene_map.opening_scene()
        print("current_scene:", current_scene)
        last_scene = self.scene_map.next_scene('GoodBye')
        print("last_scene:", last_scene)


        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            print("next_scene_name:", next_scene_name)
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Intro(Scene):

    def enter(self):
        print(dedent("""
        Hellooo!!!
        Welcome to my virtual store!
        What brings you in today?
        """))

        
        while True:
            customer = input(dedent("""
            Choose an option:
            living room
            bed room
            dinning room
            mattresses

            Answer: """))

            if customer == 'living room':
                print("Great!")
                return 'LivingRoom'
            
            elif customer == 'bed room':
                print("Great!")
                return  'BedRoom'

            elif customer == 'dinning room':
                print("Great")
                return 'DinningRoom'

            elif customer == 'mattresses':
                print("Great")
                return 'Mattresses'

            else:
                print(dedent("""
                Sorry, as of rightnow I am not program yet
                to answer any further questions, So you are
                going to have to deal with my limited
                abilities for now and give me one of the
                options I am giving you to choose from :-(.
                Now, that is not the saddest thing yet, but
                I actually need you to give me an swear
                exactly as you see the options typed.
                Thank you for your patience, I look foward
                to improve and keep learning within time! :-)
                """
                ))
                continue

class LivingRoom(Scene):

    def enter(self):
        
        while True:
            customer = input(dedent("""
            Are you looking for:
            sofas
            single recliners
            media stands
            set of tables
            or lamps
            
            Answer: """))

            if customer == 'sofas' or customer == 'single recliners':
                print("We are going to stope here this can be endless")
                return 'GoodBye'

            elif customer == 'media stands' or customer == 'set of tables' or customer == 'lamps':
                print("We are going to stop here this can be endless and never ending")
                return 'GoodBye'

            else:
                print(dedent("""
                Sorry, as of rightnow I can only accept answers
                given exactly the way they appear as for the
                options. Thank you for your patience!
                """))
                continue

class Bedroom(Scene):

    def enter(self):
        pass

class DinningRoom(Scene):

    def enter(self):
        pass

class Mattresses(Scene):

    def enter(self):
        pass

class Payment(object):

    def enter(sefl):
        pass

class Cash(Payment):

    def enter(self):
        pass

class GoodBye(Scene):

    def enter(self):
        pass

class Financing(Payment):

    def enter(self):
        pass

class GoodBye(object):

    def enter(self):
        pass

class Map(object):
    scenes = {
        'Intro': Intro(),
        'LivingRoom': LivingRoom(),
        'BedRoom': Bedroom(),
        'DinningRoom': DinningRoom(),
        'Mattresses': Mattresses(),
        'GoodBye': GoodBye(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
        
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('Intro')
a_game = Engine(a_map)
a_game.play()