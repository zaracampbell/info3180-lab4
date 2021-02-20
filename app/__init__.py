from flask import Flask
from .config import Config

app = Flask(__name__)
app.config.from_object(__name__)
from app import views
