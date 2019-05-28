#from nose.tools import *
import pytest 
# import the whole application from the app module
from gothonweb.app import app

# Set the file to test mode
app.config['TESTING'] = True
# Imitates the web app as shown to the user.
web = app.test_client()


def test_index():
    # Sends an HTTP GET request to the application with the given path.
    # The '/' page redirects to '/game' so we use the argument 'follow_redirects=True.
    rv = web.get('/', follow_redirects=True)
    # Request was received and understood
    assert rv.status_code == 200

    #
    rv = web.get('/game', follow_redirects=True)
    assert rv.status_code == 200
    assert b"Central Corridor" in rv.data

    # Dictionary variable
    data = {'action': 'tell a joke'}
    # Send POST request using the post() method and give the form data as
    # dictionary, which is this case is the above variable define 'data'
    rv = web.post('/hello', follow_redirects=True , data=data)
    assert b'tell a joke', rv.data


