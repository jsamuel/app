from bottle import redirect

import lib.session


def redirect_if_not_logged_in():
    try:
        lib.session.check_current_session()
    except lib.session.NoSessionError:
        redirect('/login')
