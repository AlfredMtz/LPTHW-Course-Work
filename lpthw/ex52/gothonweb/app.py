import os
from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
import planisphere
import pdb

app = Flask(__name__)

@app.route("/")
def index():
    # this is used to "setup" the session with starting values
    session['room_name'] = planisphere.START
    session['count'] = 0
    return redirect(url_for("game"))

@app.route("/game", methods=['GET', 'POST'])
def game():
    # starting room
    room_name = session.get('room_name')
    # secret code counts
    count = session.get('count')

    g_death = planisphere.GENERIC_DEATH
    bomb_death = planisphere.BOMB_DEATH
    

    # GET method is to ask the user for data
    if request.method == "GET":

        if room_name in ['central_corridor','laser_weapon_armory', 'the_bridge','escape_pod', 'the_end_winner']:
            # key value, which are classes
            room = planisphere.load_room(room_name)
            # laser_weapon_armory counter variable
            n_count = count
            #pdb.set_trace()
            return render_template("show_room.html", room=room, count=n_count)


        elif room_name in ['shoot!', 'dodge!', 'bomb_death', 'bridge_death','pod_death']:
            room = planisphere.load_room(room_name)
            # General death room
            g_deathroom = planisphere.load_room(g_death)
            return render_template("show_room.html", room=room, g_deathroom=g_deathroom)


        else:
            # Do I even need this???
            return render_template("you_died.html")

    else:
        # request inputed data in client's web page. Form is a diccionary object containing
        # key and value pairs of form parameters and their values. Ex: 'action' is the Key/
        action = request.form.get('action')

        if room_name == 'central_corridor':
            #Central_Corridor class
            room = planisphere.load_room(room_name)
            # Go to the next room 'laser_weapon_armory' or 'death'
            next_room = room.go(action)

            if action == 'tell a joke':
                # Go to the next room 'laser_weapon_armory'
                session['room_name'] = planisphere.name_room(next_room)
            elif action in ['dodge!', 'shoot!']:
                # Go to the next room 'death'
                session['room_name'] = planisphere.name_room(next_room)
            else:
                # Go back to the same room
                session['room_name'] = planisphere.name_room(room)


        elif room_name == 'laser_weapon_armory':
            # Laser_Weapon_Aromory class
            room = planisphere.load_room(room_name)
            next_room = room.go(action)
        
            while count < 3:

                if action == '123':
                    # next room 'the_bridge'
                    session['room_name'] = planisphere.name_room(next_room)
                    break
                else:
                    # Count each tried and go back to the same room
                    session['count'] += 1
                    session['room_name'] = planisphere.name_room(room)
                    break
            else:
                # Exceed tries and to the death room
                room = planisphere.load_room(bomb_death)
                session['room_name'] = planisphere.name_room(room)


        elif room_name == 'the_bridge':
            # The Bridge class
            room = planisphere.load_room(room_name)
            next_room = room.go(action)

            if action == 'slowly place the bomb':
                # Goes to next room
                session['room_name'] = planisphere.name_room(next_room)
            elif action == 'throw the bomb':
                # Goes to death room
                session['room_name'] = planisphere.name_room(next_room)
            else:
                # Back to same room
                session['room_name'] = planisphere.name_room(room)


        elif room_name == 'escape_pod':
            # Scape Pod class
            room = planisphere.load_room(room_name)
            next_room = room.go(action)
            #pdb.set_trace()
            if action == '2':
                session['room_name'] = planisphere.name_room(next_room)
                #pdb.set_trace()
            # This is not working! Why?????
            elif action in ['1','3','4','5']:
                next_room = room.go('*')
                session['room_name'] = planisphere.name_room(next_room)
                #pdb.set_trace()
            else:
                session['room_name'] = planisphere.name_room(room)
                
        # Back to /game url function
        return redirect(url_for("game"))


# YOU SHOULD CHANGE THIS IF YOU PUT ON THE INTERNET
app.secret_key = os.environ.get('MY_LPTHW_SECRETKEY')

if __name__ == "__main__":
    app.run()
