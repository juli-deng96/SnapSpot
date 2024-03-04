from flask_app import app
from flask import render_template, redirect, session, request, flash 
from flask_app.models.photospot import Photospot
from flask_app.models.user import User

@app.route ('/home')
def show_all_photospots():
    if 'user_id' not in session:
        return redirect ('/')
    data = {
        'id': session['user_id']
    }
    user = User.get_by_id(data)
    photospot = Photospot.get_all_photospots_with_host()
    return render_template('homepage.html', photospot =photospot, user = user)

#create photospot route
@app.route('/add')
def create_photospot():
    if 'user_id' not in session:
        return redirect ('/')
    return render_template('create_photospot.html')

@app.route('/add', methods= ['POST'])
def create_new_photospot():
    if 'user_id' not in session:
        return redirect ('/')
    if Photospot.create_photospot(request.form):
        return redirect('/home')
    return redirect ('/add')

#read photospot route 
@app.route('/view/<int:id>')
def view_photospot(id):
    if 'user_id' not in session:
        return redirect ('/')
    this_photospot = Photospot.get_all_photospots_with_host()
    return render_template ('view_photospot.html', photospot = this_photospot)

#update photospot route 
@app.route('/edit/<int:id>')
def edit_photospot_page(id):
    if 'user_id' not in session:
        return redirect ('/')
    this_photospot = Photospot.get_photospot_by_id_w_host(id)
    return render_template('edit_photospot.html', photospot = this_photospot)

@app.route('/edit', methods=['POST'])
def edit_photospot():
    if 'user_id' not in session:
        return redirect ('/')
    if Photospot.edit_photospot(request.form):
        return redirect('/home')
    return redirect(f'/edit/{request.form["id"]}')

#delete photospot route 
@app.route('/delete/<int:id>')
def delete_photospot(id):
    if 'user_id' not in session:
        return redirect ('/')
    Photospot.delete_photospot(id)
    return redirect('/home')
