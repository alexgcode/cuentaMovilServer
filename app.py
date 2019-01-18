from flask import Flask
from sqlalchemy import create_engine

app = Flask(__name__)

@app.route('/')
def index():
    return 'hola mundoss'

app.run()