from flask import Flask, render_template
from views import my_view

# initialises flask and the blueprint (template) to be used from views.py
app = Flask(__name__)
app.register_blueprint(my_view)

# how the website will handle 404 page cannot be found errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',e=e)

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html',e=e)

# to run the site with debug settings than the default via running app.py
if __name__ == '__main__':
    app.run(debug=True,port=8000)