"""
*Map
    - next_scene
    - opening_scene
*Engine
    -play
*Scene
    - Intro
    - Freesa world
    - Cell world
    - Majimbu world
    - One star dragon world
    - Making a wish
    - Death
"""
from textwrap import dedent
class Scene(object):
    pass

class Intro(Scene):
    
    def enter(self):
        print(dedent("""

        WELCOME TO DRAGONBZ TEXT GAME!!!

        This story begins in a very, very far planet named Vegeta which
        is about to be destroyed by powerful evil forces. A desperate
        father with little to no time puts his son into a spaceship 
        and sends it over into space and arrives into a new planetary
        destination named earth. 

        Years later he grows up, starts a family, and as he seems to be much
        stronger than average humans he finds a passion for helping people 
        escape the hands of evil villains. One day, returning home, he sees
        his entire village wiped out including his family.

        A survivor informs him that an evil dragon monster came in and took 
        the seven dragon balls which grand a single wish once a year.So, Goku 
        the warrior goes out to locate all seven dragon balls to bring them back 
        home and make a wish to have his family and village back to normality.

        Do you want to help by being Goku and start the quest of saving your 
        village and bring your family back to life?
        
        [ Yes / No ]

        """))

        action = input("> ")

        if action == "Yes":
            print(dedent("""
            Great!!!  You lose no time and start investigating where to find
            this evil dragon one and get back the dragon balls. You get informed
            that the evil dragon distributed two of the dragon balls to each of
            his best soldiers to keep them safe while he only held one.

            You quickly go out and find out that two of the dragon balls are
            held by one of this dragon's soldiers by the name of Freeza.
            
            Bravely you set out to space, find Freeza's planet and get ready to
            face him.
            """))
            Player()
            return 'Freeza_world'
        
        else:
            print('GAME EXITED!')
            exit(1)

class Freezaworld(Scene):

    def enter(self):
        print('next')

class Cellworld(Scene):
    pass

class Majimbuworld(Scene):
    pass

class Dragonworld(Scene):
    pass

class Makingwish(Scene):
    pass

class Death(Scene):
    pass

class Completed(Scene):
    pass

class Engine(object):
    # Contructor for class to take arguments and assign them
    # to variables, and be run inside as commanded.
    def __init__(self, scene_map):
        self.scene_map = scene_map
        print(self.scene_map)

    # Function will run automatically if not any other parameters
    # are given besides itself.
    def play(self):
        # first run returns backs to the same scene 'Intro()'
        # since it is the first run.
        current_scene = self.scene_map.open_scene()
        # Last message when yo finish the whole game succesfully
        last_scene = self.scene_map.next_scene('Completed')
        print("current_scene and last_scene before while-loop:")
        print(current_scene)
        print(last_scene) 

        # while this statement is true keep running the loop
        # otherwise exit the loop
        while current_scene != last_scene:
            # The enter() function needs to get define on
            # each scene class so it can be implemented here.
            next_scene_name = current_scene.enter() 
            # Current scene calls the next_scene function inheritaded
            # from Map() and the value on next_scene_name is given as
            # input
            current_scene = self.scene_map.next_scene(next_scene_name)
            # The enter() function is call to start executing the code
            # and it is enter inside of the play() fucntion, it only gets
            # executed when the play function get executed.
            current_scene.enter() 



class Map(object):
    # Reference scenes via diccionary values
    scenes = {
        'Intro': Intro(),
        'Player': Player(),
        'Freeza_world': Freezaworld(),
        'Cell_world': Cellworld(),
        'Majimbu_world': Majimbuworld(),
        'One_start_dragon_world': Dragonworld(),
        'Making_a_wish': Makingwish(),
        'Death': Death(),
        'Completed': Completed(),
    }
    # Initialize a constructor
    def __init__(self, start_scene):
        self.start_scene = start_scene

    # Define next scene fucntion
    def next_scene(self, scene_name):
        # Take specefic key value from scenes diccionary
        val = Map.scenes.get(scene_name)
        return val

    # Runs next_scene function() for opening scene
    def open_scene(self):
        return self.next_scene(self.start_scene)

# Intro class becomes an object of the Map class
# a_map becomes an instance of a Map class
# At this point
a_map = Map('Intro')
print(a_map)
a_game = Engine(a_map)
a_game.play()









