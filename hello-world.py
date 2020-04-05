from flask import Flask
import sys
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!<br>Python Version: %s' % '.'.join(['%d'%k for k in sys.version_info[:3]])


