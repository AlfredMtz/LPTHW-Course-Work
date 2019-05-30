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
    

    # GET method is to ask the user for data
    if request.method == "GET":

        if room_name:
            # key value, which are classes
            room = planisphere.load_room(room_name)
            # laser_weapon_armory counter variable
            n_count = session['count']
            g_death = planisphere.load_room(g_death)
            #pdb.set_trace()
            return render_template("show_room.html", room=room, n_count=n_count, g_death=g_death)
        else:
            # Do I even need this???
            return render_template("you_died.html")

    else:
        # request inputed data in client's web page. Form is a diccionary object containing
        # key and value pairs of form parameters and their values. Ex: 'action' is the Key/
        action = request.form.get('action')

        if room_name and action:
            #Central_Corridor class
            room = planisphere.load_room(room_name)
            # Go to the next room 'laser_weapon_armory' or 'death'
            next_room = room.go(action)

            while room_name == 'laser_weapon_armory' and action != '123':
                if count < 3:
                    session['count'] += 1
                    break
                else:
                    break

            #.set_trace()
            if not next_room:
                if room_name == 'laser_weapon_armory' and count == 2:
                    next_room = room.go('*')
                    #pbd.set_trace()
                    session['room_name'] = planisphere.name_room(next_room)
                elif room_name == 'escape_pod' and action != '2':
                    next_room = room.go('end')
                    session['room_name'] = planisphere.name_room(next_room)
                else:
                    # Go back to the same room
                    session['room_name'] = planisphere.name_room(room)
                    #pdb.set_trace()
            else:
                session['room_name'] = planisphere.name_room(next_room)
                #pdb.set_trace()

        # Back to /game url function
        return redirect(url_for("game"))


# key
app.secret_key = os.environ.get('MY_LPTHW_SECRETKEY')

if __name__ == "__main__":
    app.run()
