from bottle import get, post, request, redirect

from lib.template import render
import lib.account
import lib.session


@get('/signup')
def get_signup():
    try:
        lib.session.check_current_session()
    except lib.session.NoSessionError:
        pass
    else:
        redirect('/')

    return render('signup.html')


@post('/signup')
def post_signup():
    email = request.POST['email']
    password = request.POST['password']

    account_id = lib.account.create_account(email, password)
    session_id = lib.session.create_session(account_id)
    lib.session.set_session_cookies(account_id, session_id)

    redirect('/')


@get('/login')
def get_login():
    try:
        lib.session.check_current_session()
    except lib.session.NoSessionError:
        pass
    else:
        redirect('/')

    return render('login.html')


@post('/login')
def post_login():
    email = request.POST['email']
    password = request.POST['password']

    try:
        account = lib.account.get_account_with_password(email, password)
    except lib.account.AuthError:
        return "Login failed. Press 'back' to try again."

    session_id = lib.session.create_session(account['id'])
    lib.session.set_session_cookies(account['id'], session_id)

    redirect('/')


@get('/logout')
def logout():
    lib.session.delete_current_session()
    lib.session.delete_session_cookies()
    redirect('/login')
