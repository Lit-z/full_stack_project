from flask import render_template, redirect, url_for, Blueprint

# creates the blueprint
my_view = Blueprint('my_view',__name__)

# setting up the structure of the backend
@my_view.route('/')
def home():
    return render_template('home.html')

@my_view.route('/admin')
def admin():
    return render_template('admin.html')

@my_view.route('/Detection')
def page1():
    return render_template('page1.html')

@my_view.route('/Types')
def page2():
    return render_template('page2.html')

@my_view.route('/Stars')
def page3():
    return render_template('page3.html')

@my_view.route('/Data')
def page4():
    return render_template('page4.html')

@my_view.route('/Gallery')
def page5():
    return render_template('page5.html')

# redirects of url's that will send user to the homepage
@my_view.route('/js')
@my_view.route('/javascript')
@my_view.route('/home')
@my_view.route('/index')
def home_redirect():
    return redirect(url_for('my_view.home'))