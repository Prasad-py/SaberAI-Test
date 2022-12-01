from distutils.log import error
from flask import Flask
from flask_mail import Mail
import saberai.config as config
import openai
import pymongo

openai.api_key = config.OPENAI_API_KEY
GPT_Engine = "text-davinci-003"

#Mongodb configuration
client = pymongo.MongoClient(config.MONGO_URL)
db = client.get_database('saberAI')

app = Flask(__name__)
app.config.from_object(config.config['development'])

app.config['MAIL_SERVER']='smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'dummyaditya22@gmail.com'
app.config['MAIL_PASSWORD'] = 'xadafnzuxtlugpgq'
app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

from saberai import routes