from flask import render_template, redirect, url_for, Blueprint, abort

# creates the blueprint
my_view = Blueprint('my_view',__name__)

# setting up the structure of the backend
@my_view.route('/')
def home():
    #### abort(500)    # Only uncomment this if wanting to test the 500 error page
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

@my_view.route('/Naming')
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

# redirect for page 4 for some obvious similar names (pun intended)
# in practice could make a long list of all the different potential pages to
# for each individual page, due to similar names or typos, trying to reduce the 
# amount of errors caused by the user where they'd end up on the 404 page instead
@my_view.route('/Names')
@my_view.route('/Name')
def p4_redirect():
    return redirect(url_for('my_view.page4'))

