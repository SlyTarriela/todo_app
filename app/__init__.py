from flask import Flask
from dotenv import load_dotenv
from flask_pymongo import PyMongo
import os

load_dotenv()


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')
app.config["MONGO_URI"] = f"mongodb+srv://{os.getenv('MONGODB_USERNAME')}:{os.getenv('MONGODB_PASSWORD')}@cluster0.tklqmdr.mongodb.net/ToDo_App?retryWrites=true&w=majority"

# setup mongodb
mongodb_client = PyMongo(app)
db = mongodb_client.db


from app import routes