from flask import Flask
import sys
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!\n\tPython Version: %s' % sys.version_info


