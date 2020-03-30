from bottle import get, response, redirect

import lib.session
from lib.template import render


@get('/')
def home():
    try:
        lib.session.check_current_session()
    except lib.session.NoSessionError:
        redirect('/login')

    return render('home.html')
