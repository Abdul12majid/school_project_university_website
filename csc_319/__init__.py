from flask import Flask, render_template, url_for, request, flash, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

#app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:Non12$ense@localhost/csc_319_db"
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///csc_319.db'
app.config["SECRET_KEY"]="app_py"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from csc_319 import routes