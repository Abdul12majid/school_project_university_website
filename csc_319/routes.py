from csc_319 import app
from flask import render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from csc_319.my_database import students

db = SQLAlchemy(app)

@app.route("/")
def home():
	return render_template("index.html")
	
@app.route("/facilities")
def facilities():
	all_info = students.query.order_by(students.date_added)
	return render_template("facilities.html", all_info=all_info)
	
@app.route("/courses")
def courses():
	return render_template('courses.html')
	
	#student registration form
@app.route("/register", methods=["POST", "GET"])
def register():
	if request.method == "POST":
		user = students.query.filter_by(email_db = request.form.get("email")).first()
		if user is None:
			first_name = request.form.get("surname")
			last_name = request.form.get("lname")
			birth_day = request.form.get("bdate")
			gen_der = request.form.get("gender")
			mail = request.form.get("email")
			phone = request.form.get("pnumber")
			dept = request.form.get("course")
			#password = request.form.get("course")
			#hashed = generate_password_hash(password)
			info = students(first_name_db = first_name, last_name_db = last_name, email_db = mail, date_of_birth_db = birth_day, course_db = dept, gender_db = gen_der, phone_no_db = phone)
			db.session.add(info)
			db.session.commit()
			return redirect(url_for('admin'))
			
		else:
			return redirect(url_for("register"))
			
	return render_template("admission.html")
		
@app.route("/admin")
def admin():
	all_info = students.query.order_by(students.date_added)
	return render_template("admin.html", all_info=all_info)
	
@app.route("/delete_user/<int:id>", methods=["POST", "GET"])
def delete_user(id):
	user_to_delete = students.query.get_or_404(id)
	try:
		db.session.delete(user_to_delete)
		db.session.commit()
		return redirect(url_for('admin'))
	except:
		return ("Error deleting user")
		
@app.route("/update_user/<int:id>", methods=["POST", "GET"])
def update_user(id):
	update_user = students.query.get_or_404(id)
	if request.method == "POST":
		update_user.first_name_db = request.form.get("surname")
		update_user.last_name_db = request.form.get("lname")
		update_user.email_db = request.form.get("email")
		update_user.date_of_birth_db = request.form.get("bdate")
		update_user.course_db = request.form.get("course")
		update_user.gender_db = request.form.get("gender")
		update_user.phone_no = request.form.get("pnumber")
		try:
			db.session.add(update_user)
			db.session.commit()
			return redirect(url_for('admin'))
		except:
			pass
	return render_template("update_user.html", update_user=update_user)