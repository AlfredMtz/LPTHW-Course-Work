import pytest 
# import the whole application from the app module
from gothonweb import app
from gothonweb import __init__

# Set the file to test mode
app.config['TESTING'] = True
# Imitates the web app as shown to the user.
web = app.test_client()


def test_index():
    rv = web.get('/')
    # Redirection code for /home
    assert rv.status_code == 302

    rv = web.get('/home')
    assert rv.status_code == 200
    # Ensuring these strings are part of /home page display output
    assert b"Gothons From Planet Percal #25 Game" in rv.data
    assert b"Click here to start the game!" in rv.data

    # Dictionary variable
    data = {
            'action': 'shoot!', 'action': 'dodge!', 'action': 'tell a joke',
            'action': '123', 'action': '*', 'action': 'throw the bomb', 
            'action': 'slowly place the bomb', 'action': '2', 'action': 'end'
            }
    # Send POST request using the post() method and give the form data as
    # dictionary, which is this case is the above variable define 'data'
    rv = web.post('/game', follow_redirects=True , data=data)
    assert b'shoot!', rv.data
    assert b'dodge!', rv.data
    assert b'tell a joke!', rv.data
    assert b'123', rv.data
    assert b'*', rv.data
    assert b'throw the bomb', rv.data
    assert b'slowly place the bomb', rv.data
    assert b'2', rv.data
    assert b'end', rv.data
















