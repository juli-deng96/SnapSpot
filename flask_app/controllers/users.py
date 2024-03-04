from flask_app import app
from flask import render_template, redirect, session, request, flash 
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#root route 
@app.route('/')
def index():
    return render_template('index.html')

#create user route
@app.route('/register', methods = ['POST'])
def register_user():
    if not User.validate_registration(request.form):
        return redirect('/')
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.create_user(data)
    session['user_id'] = id 
    return redirect('/home')

 #login user route 
@app.route('/login', methods=['POST'])
def login_user ():
    user = User.get_by_email(request.form)
    if not user:
        flash("Invalid Email", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash ("Invalid Password", "login")
        return redirect('/')
    session['user_id']= user.id
    return redirect('/home')

#logout route 
@app.route('/logout')
def logout_user():
    session.clear()
    return redirect('/')
