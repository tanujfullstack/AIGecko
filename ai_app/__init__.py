import os
from flask import Flask
from ai_app.config import Config
UPLOAD_FOLDER = './ai_app/uploads/'

if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__, static_url_path='/uploads', static_folder='uploads')
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from ai_app import routes