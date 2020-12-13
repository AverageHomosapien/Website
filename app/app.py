from flask import Flask, redirect, url_for, abort, request, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/home/')
@app.route('/index/')
@app.route('/')
def home():
    print("Url for {}".format(url_for('static', filename='owl-carousel/owl.carousel.css')))
    return render_template('index.jinja')

@app.route('/contact/')
@app.route('/contact-us/')
def contact():
    return render_template('contact.jinja')

@app.route('/about/')
@app.route('/about-me/')
def about():
    return render_template('about.jinja')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
