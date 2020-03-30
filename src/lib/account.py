from passlib.hash import argon2

from lib import db
from lib.util import random_str


class AuthError(Exception):
    pass


def generate_id():
    return random_str(16)


def hash_password(password):
    return argon2.hash(password)


def get_account_with_password(email, password):
    params = (email, )
    sql = '''SELECT * FROM accounts WHERE
             email = ?'''
    account = db.cursor().execute(sql, params).fetchone()

    if account is None:
        raise AuthError

    if not argon2.verify(password, account['hashed_password']):
        raise AuthError

    return account


def create_account(email, password):
    account_id = generate_id()
    hashed_password = hash_password(password)

    params = (account_id, email, hashed_password)
    sql = '''INSERT INTO accounts
             (id, email, hashed_password, date_created)
             VALUES
             (?, ?, ?, DATETIME('now'))'''
    db.cursor().execute(sql, params)

    return account_id
