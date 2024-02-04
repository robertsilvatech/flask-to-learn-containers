import os
from flask import Flask
from flask import render_template
from flask import request
import logging
import logging.config

def create_app():
    app = Flask(__name__)
    if 'FLASK_CONFIG' in os.environ.keys():
        app.config.from_object('app.settings.' + os.environ['FLASK_CONFIG'])
    else:
        app.config.from_object('app.settings.Development')

    @app.route('/')
    def home():
        color = os.getenv('COLOR')
        return render_template('index.html', color=color)
    

    return app

LOGLEVEL = os.getenv('LOGLEVEL', 'INFO').upper()

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(module)s %(process)d %(thread)d %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        }
    },
    'loggers': {
        '': {
            'level': LOGLEVEL,
            'handlers': ['console'],
            'propagete': True,
        },
    },
})

logger = logging.getLogger('')
level = logging.getLevelName('DEBUG')
logger.setLevel(level)

app = Flask(__name__)
