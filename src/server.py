from bottle import run
import configparser
import os

from lib import db

# Importing the files that define the request handlers is what registers the
# handlers with bottle.
from handlers import auth
from handlers import index
from handlers import samplequiz


CONFIG_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'app.conf')

DEFAULT_DB_FILE = '/tmp/database.sqlite'


if __name__ == '__main__':
    if os.path.exists(CONFIG_FILE):
        config = configparser.ConfigParser()
        config.read_dict({
            'db': {
                'filepath': DEFAULT_DB_FILE,
            },
        })
        config.read([CONFIG_FILE])
        filepath = config.get('db', 'filepath')
    else:
        filepath = DEFAULT_DB_FILE

    db.init(filepath)
    run(host='0.0.0.0', port=80, server='paste')
