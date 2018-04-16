# SprintHive Pty Ltd
# Python Starter Project ('ground-zero')

# Contact details
# Jonathan Zwart <jz@sprinthive.com>
# Monday 16 April 2018

from flask import Flask

app = Flask(__name__)

import logging
from utils import logging_utils

logging_utils.setup_logging()
logging.info('Logging enabled in %s' % __name__)

from utils import config_utils

config = config_utils.load_yaml_config()


@app.route('/')
def index():
    return 'Base URL!'


# ----------------------------------------------------------------------------------------


@app.route('/ping')
def ping():
    """Required by the Kubernetes pod health check"""
    return 'OK'


# ----------------------------------------------------------------------------------------


@app.route('/hello-world')
def hello():
    return config['example']['hello_world_string']


# ----------------------------------------------------------------------------------------


@app.route('/test-imports')
def test_imports():
    try:
        from flask import Flask
        import logging
        from utils import logging_utils
        return 'Imports worked'
    except:
        return 'Imports failed'


# ----------------------------------------------------------------------------------------


@app.route('/test-logging')
def test_logging():
    try:
        logging_utils.test_logging()
        return 'Logging test worked'
    except:
        return 'Logging test failed'


# ----------------------------------------------------------------------------------------


if __name__ == "__main__":
    # Only for debugging while developing
    # Port is handled by UWSGI internally
    app.run(host=config['flask']['host'], debug=config['flask']['debug'], port=config['flask']['port'])
