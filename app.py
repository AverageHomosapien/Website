# All module materials will be archived in Moodle & on the module website: http://siwells.github.io/teaching_set09103/
# All code examples are at https://github.com/siwells/set09103

# Running on 127.0.0.1:5000 currently
from flask import Flask, redirect, url_for, abort

app = Flask(__name__)

@app.route('/')
@app.route('/home/')
def hello_world():
    return('Hello, World!')
    return('Welcome to my homepage!')

@app.route('/profile/')
def profile():
    return('Welcome to my profile!')

@app.route('/about-me/')
@app.route('/about/')
def aboutme():
    return('All about me!')

@app.route('/private/')
def private():
    return redirect(url_for('login'))

@app.route('/login/')
def login():
    return('Please enter a username and password:')

@app.route('/image/')
@app.route('/picture/')
def image():
    return ('<img src=https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Breathe-face-smile.svg/1200px-Breathe-face-smile.svg.png>', 200)



@app.route('/force404/')
def force404():
    abort(404)

@app.errorhandler(404)
def error_page_not_found(error):
    return("Sorry, that page doesn't exist I'm afraid!", 404)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
