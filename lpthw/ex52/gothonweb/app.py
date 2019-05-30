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
    

    if request.method == "GET":
        if room_name:
            room = planisphere.load_room(room_name)
            # random death message
            g_death = planisphere.load_room(planisphere.GENERIC_DEATH)
            return render_template("show_room.html", room=room, n_count=count, g_death=g_death)
        else:
            # Do I even need this???
            return render_template("you_died.html")

    else:
        # request inputed data in client's side web page.
        action = request.form.get('action')

        if room_name and action:
            room = planisphere.load_room(room_name)
            next_room = room.go(action)

            while room_name == 'laser_weapon_armory' and action != '123':
                if count < 3:
                    session['count'] += 1
                    break
                else:
                    break

            if not next_room:
                # Exceed passcode tries
                if room_name == 'laser_weapon_armory' and count == 2:
                    next_room = room.go('*')
                    session['room_name'] = planisphere.name_room(next_room)
                # Wrong pod number
                elif room_name == 'escape_pod' and action != '2':
                    next_room = room.go('end')
                    session['room_name'] = planisphere.name_room(next_room)
                else:
                    # Go back to the same room
                    session['room_name'] = planisphere.name_room(room)
            else:
                session['room_name'] = planisphere.name_room(next_room)

        # Back to /game url function
        return redirect(url_for("game"))


app.secret_key = os.environ.get('MY_LPTHW_SECRETKEY')

if __name__ == "__main__":
    app.run()
