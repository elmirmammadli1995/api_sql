from flask import jsonify, Flask
from flask-cors import CORS
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)

CORS(app)