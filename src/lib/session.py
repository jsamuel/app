from bottle import request, response
import hashlib

from lib import db
from lib.util import random_str


class NoSessionError(Exception):
    pass


ACCOUNT_ID_COOKIE = 'account_id'

SESSION_ID_COOKIE = 'session_id'


def get_session_cookies():
    account_id = request.get_cookie(ACCOUNT_ID_COOKIE)
    session_id = request.get_cookie(SESSION_ID_COOKIE)
    return account_id, session_id


def set_session_cookies(account_id, session_id):
    response.set_cookie(ACCOUNT_ID_COOKIE, account_id, path='/')
    response.set_cookie(SESSION_ID_COOKIE, session_id, path='/')


def delete_session_cookies():
    response.delete_cookie(ACCOUNT_ID_COOKIE, path='/')
    response.delete_cookie(SESSION_ID_COOKIE, path='/')


def generate_session_id():
    return random_str(32)


def hash_session_id(session_id):
    return hashlib.sha224(session_id.encode()).hexdigest()


def create_session(account_id):
    session_id = generate_session_id()
    hashed_session_id = hash_session_id(session_id)

    params = (account_id, hashed_session_id)
    sql = '''INSERT INTO sessions
             (account_id, hashed_session_id, date_created, date_accessed)
             VALUES
             (?, ?, DATETIME('now'), DATETIME('now'))'''
    db.cursor().execute(sql, params)

    return session_id


def check_current_session():
    account_id, session_id = get_session_cookies()
    if not account_id or not session_id:
        raise NoSessionError

    hashed_session_id = hash_session_id(session_id)

    params = (account_id, hashed_session_id)
    sql = '''SELECT * FROM sessions WHERE
             account_id = ? AND hashed_session_id = ?'''
    session = db.cursor().execute(sql, params).fetchone()

    if session is None:
        raise NoSessionError

    return session['account_id']


def delete_current_session():
    # TODO: implement
    pass
