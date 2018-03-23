"""
This script runs the isensweb application using a development server.
"""

from os import environ
from isensweb import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        #PORT = 8000
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    #app.run("192.168.8.189",8000,debug=True)
    app.run(HOST, PORT)
