from csc_319 import db
from datetime import datetime

class students(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	first_name_db = db.Column(db.String(20), nullable=False)
	last_name_db = db.Column(db.String(20), nullable=False)
	email_db = db.Column(db.String(50), nullable = False, unique = True)
	date_of_birth_db = db.Column(db.String(20), nullable=False)
	course_db = db.Column(db.String(60), nullable = False)
	gender_db = db.Column(db.String(30), nullable = False)
	phone_no_db = db.Column(db.String(300), nullable= False)
	#password_hash=db.Column(db.String(400), #nullable=False)
	date_added = db.Column(db.DateTime, default=datetime.utcnow)
	
	#@property
	#def password(self):
		#raiseAttributeError("Password is not a readable attribute")
	#@password.setter
	#def password(self, password):
		#self.password_hash = generate_password_hash(password)
	#def verify_password(self, password):
		#return check_password_hash(self.password_hash, password)