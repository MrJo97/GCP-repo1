from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to python Flask world - V1.0'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
