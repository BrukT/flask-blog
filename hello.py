from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    print("hello there")
    return 'Hello, we are here!'