from flask import Flask
#from redis import Redis, RedisError
import os
import socket

# Connect to Redis
#redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/hello")
def hello():
#    print 'Hello World'
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"),\
                        hostname=socket.gethostname(),visits="")

@app.route("/TestImports")
def testImports():

    print "Hello world"
    try:
        import os
        import socket
        from flask import Flask
        return "Imports worked"
    except:
        return "Imports failed"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
