import os
from flask import Flask
from api import *

app = Flask(__name__)

if __name__ == "__main__":
    app.run()