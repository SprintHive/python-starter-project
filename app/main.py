# SprintHive Pty Ltd
# Python Starter Project ('ground-zero')

# Contact details
# Jonathan Zwart <jz@sprinthive.com>
# Monday 9 April 2018

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<span style='color:red'>I am app 1</span>'

@app.route('/hellofromflask')
def hello():
    return 'Hello World from Flask'

@app.route('/TestImports')
def testImports():

    print 'Hello world'
    try:
        from flask import Flask
        return 'Imports worked'
    except:
        return 'Imports failed'


if __name__ == "__main__":
    # Only for debugging while developing
    # Port is handled by UWSGI internally
    app.run(host='0.0.0.0', debug=True, port=1492)
