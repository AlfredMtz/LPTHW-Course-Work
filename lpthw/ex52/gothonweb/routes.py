from flask import render_template, session, redirect, url_for, escape, request, flash
from gothonweb import app, db, bcrypt
from gothonweb.forms import RegistrationForm, LoginForm
from gothonweb.models import User
from gothonweb import planisphere, lexicon, parser
from flask_login import login_user, current_user, logout_user, login_required
import pdb



@app.route("/")
def index():
    return redirect(url_for("home"))


@app.route("/game1")
def game1():
    # this is used to "setup" the session with starting values
    session['room_name'] = planisphere.START_GAME1
    session['count'] = 0

    # if logged user
    if current_user.is_authenticated:
        session['score'] = current_user.score
    # if playing as a guess
    else:
        session['score'] = 0
    return redirect(url_for("game"))


@app.route("/game2")
def game2():
    # this is used to "setup" the session with starting values
    session['room_name'] = planisphere.START_GAME2
    session['count'] = 0
    #pdb.set_trace()
    # if logged user
    if current_user.is_authenticated:
        session['score'] = current_user.score
    # if playing as a guess
    else:
        session['score'] = 0
    return redirect(url_for("game"))


@app.route("/game", methods=['GET', 'POST'])
def game():
    # starting room
    room_name = session.get('room_name')
    # secret code counts for 'laser_weapon_armory" room
    count = session.get('count')
    # score game system for users, starts at 0
    score = session.get('score')
    pdb.set_trace()

    if request.method == "GET":
        if room_name:
            room = planisphere.load_room(room_name)
            # random death message
            g_death = planisphere.load_room(planisphere.GENERIC_DEATH)
            pdb.set_trace()
            return render_template("show_room.html", room=room, n_count=count, score=score, 
                                    g_death=g_death, title='Gothons From Planet Percal #25')
        else:
            # Do I even need this???
            return render_template("you_died.html")

    else:
        # request inputed data in client's side web page.
        # word_list = lexicon.scan(request.form.get('action'))
        # action = parser.parse_sentence(word_list)
        # pdb.set_trace()
        action = request.form.get('action')
        pdb.set_trace()
        # if logged user
        if action in planisphere.right_choices and current_user.is_authenticated:
            current_user.score = score + 2
            
            # User's score get updated on database
            db.session.commit()
            session['score'] = current_user.score

        # playing as a guess
        elif action in planisphere.right_choices:
            session['score'] += 2

        # Skip and run upcoming lines of code
        else:
            pass

        
        if room_name and action:
            room = planisphere.load_room(room_name)
            # Not from scences, but rooms' paths
            next_room = room.go(action)
            pdb.set_trace()
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
            #pdb.set_trace()
        pdb.set_trace()
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template("login.html", title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template("account.html", title='Account')


@app.route("/help")
def help():
    room_name = session.get('room_name')
    room = planisphere.load_room(room_name)
    return render_template("help.html", room=room)
