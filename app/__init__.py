from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
from app import views
app.config['SECRET_KEY'] = '6ab1f1d9bf1b73113fbecda5faf88979'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
mail = Mail(app)
from app import views