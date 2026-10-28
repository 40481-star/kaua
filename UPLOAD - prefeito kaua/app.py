from flask import Flask
from database.db import init_db
from routes.upload_route import upload_bp
from routes.download_route import download_bp

app = Flask(_name_)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

init_db()

app.register_blueprint(upload_bp, url_prefix='/uploads')
app.register_blueprint(download_bp, url_prefix= '/downloads')

if_name_ == '_main_':
    app.run(debug=True)