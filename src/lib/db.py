import sqlite3


_private = {
    'filepath': None
}


def init(filepath):
    _private['filepath'] = filepath
    _create_tables()


def _create_tables():
    _create_accounts_table()
    _create_sessions_table()


def _create_accounts_table():
    sql = '''CREATE TABLE IF NOT EXISTS accounts (
                 id TEXT PRIMARY KEY,
                 email TEXT NOT NULL UNIQUE,
                 hashed_password TEXT NOT NULL,
                 date_created TEXT NOT NULL
             )'''
    cursor().execute(sql)


def _create_sessions_table():
    sql = '''CREATE TABLE IF NOT EXISTS sessions (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 account_id TEXT NOT NULL,
                 hashed_session_id TEXT NOT NULL UNIQUE,
                 date_created TEXT NOT NULL,
                 date_accessed TEXT NOT NULL
             )'''
    cursor().execute(sql)


def cursor():
    # A new connection is made for each request as a connection can't be shared
    # between threads.
    # Setting isolation_level to None enables autocommit.
    filepath = _private['filepath']
    conn = sqlite3.connect(filepath, isolation_level=None)
    conn.row_factory = sqlite3.Row
    return conn.cursor()
