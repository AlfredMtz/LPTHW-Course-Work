from flask import Flask
from flask import session
from flask import redirect
from flask import url_for
from flask import escape
from flask import request
import pdb

from flask import render_template
import planisphere

app = Flask(__name__)

# routes browser url link extension "/" to the below function
@app.route("/")
def index():
    # this is use to "setup" the session with starting values
    session['room_name'] = planisphere.START
    # generates url for game() function and redirects users to the game page
    return redirect(url_for("game"))

@app.route("/game", methods = ['GET', 'POST'])
def game():
    # Saves value from given key in diccionary{"key": 'value'}
    room_name = session.get('room_name')
    # IF METHOD = "GET", RUN THIS BLOCK(Standard starting method
    # is 'GET')
    if request.method == "GET":
        # room_name = 'central_corridor'
        # if statements seems unnecessary.
        if room_name:
            # saves Room() object ---> central_corridor
            room = planisphere.load_room(room_name)
            return render_template("show_room.html", room=room)
        else:
            # why is there here? do I need it?
            return render_template("you_died.html")
        

    # eLSE IF METHOD = "POST", THEN RUN THIS BLOCK
    else: 
        action = request.form.get('action')
        
        if room_name == 'central_corridor' and action == 'tell a joke':
            room = planisphere.load_room(room_name)
            next_room = room.go(action)
            #pdb.set_trace() 
            if not next_room:
                # saves planisphere scenes' key 'central_corridor' as value for session's key 'room_name'
                session['room_name'] = planisphere.name_room(room)
            else:
                session['room_name'] = planisphere.name_room(next_room)
                
        elif room_name == 'laser_weapon_armory':
            room = planisphere.load_room(room_name)
            next_room = room.go(action)
            pdb.set_trace()
            #s = session.get('guesses', None)

            if not session['guesses']:
                session['guesses'] = 0
                pdb.set_trace()
            # If input is the right code
            elif action == '123':
                session['room_name'] = planisphere.name_room(next_room)
            # if input not equals to code and tries are less then 10
            elif action != '123' and session['guesses'] < 3:
                session['guesses'] = session['guesses'] + 1
                pdb.set_trace()
                session['room_name'] = planisphere.name_room(room)
            else:
                session.clear()
                return render_template("you_died.html")
        
        pdb.set_trace()
        return redirect(url_for("game"))
          
            
            
# YOU SHOULD CHANGE THIS IF YOU PUT ON THE INTERNET
app.secret_key = 'AOZr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ =="__main__":
    app.run()
            