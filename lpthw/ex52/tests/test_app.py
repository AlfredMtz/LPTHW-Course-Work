#from nose.tools import *
import pytest 
# import the whole application from the app module
from gothonweb.app import app

# Set the file to test mode
app.config['TESTING'] = True
# Imitates the web app as shown to the user.
web = app.test_client()


def test_index():
    rv = web.get('/', follow_redirects=True)
    assert rv.status_code == 200


    
    # rv = web.get('/hello', follow_redirects=True)
    # assert_equal(rv.status_code, 200)
    # assert_in(b"Fill Out This Form", rv.data)

    # data = {'name': 'Zed', 'greet': 'Hola'}
    # rv = web.post('/hello', follow_redirects=True, data=data)
    # assert_in(b"Zed", rv.data)
    # assert_in(b"Hola", rv.data)

