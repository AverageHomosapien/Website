# All module materials will be archived in Moodle & on the module website: http://siwells.github.io/teaching_set09103/
# All code examples are at https://github.com/siwells/set09103

# Running on 127.0.0.1:5000 currently
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home/')
def hello_world():
    return('Hello, World!')

@app.route('/profile/')
def profile():
    return('Welcome to my profile!')

@app.route('/about-me/')
@app.route('/about/')
def aboutme():
    return('All about me!')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
