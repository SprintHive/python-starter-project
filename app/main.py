# SprintHive Pty Ltd
# Python Starter Project ('ground-zero')

# Contact details
# Jonathan Zwart <jz@sprinthive.com>
# Monday 9 April 2018

from flask import Flask
app = Flask(__name__)

import logging
from utils import logging_utils
logging_utils.setup_logging()
logging.info('Logging enabled in %s' % __name__)

@app.route('/')
def index():
    return 'Base URL!'

@app.route('/HelloWorld')
def hello():
    return 'Hello World!'

@app.route('/TestImports')
def testImports():
    try:
        from flask import Flask
        import logging
        import utils
        return 'Imports worked'
    except:
        return 'Imports failed'

@app.route('/TestLogging')
def testLogging():
    try:
        import logging
        from utils import logging_utils
        logging_utils.setup_logging()
        logging.info('Logging enabled in %s' % __name__)
        logging_utils.test_logging()
        return 'Logging worked'
    except:
        return 'Logging failed'


if __name__ == "__main__":
    # Only for debugging while developing
    # Port is handled by UWSGI internally
    app.run(host='0.0.0.0', debug=True, port=1492)
