from flask install Flask
from flask_bootstrap import flask_bootstrap


bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    