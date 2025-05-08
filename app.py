from flask import Flask
from flaskr.token import token

app = Flask(__name__)
app.register_blueprint(token)
