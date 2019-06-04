from models import User


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
            return render_template("show_room.html", room=room, n_count=count,
                                   g_death=g_death, title='Gothons From Planet Percal #25')
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


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html", title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template("login.html", title='Login', form=form)
