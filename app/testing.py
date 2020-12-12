# All module materials will be archived in Moodle & on the module website: http://siwells.github.io/teaching_set09103/
# All code examples are at https://github.com/siwells/set09103

# Running on 127.0.0.1:5000 currently
from flask import Flask, redirect, url_for, abort, request

app = Flask(__name__)

@app.route('/')
@app.route('/home/')
def hello_world():
    return('Hello, World! \nWelcome to my homepage!')

@app.route('/about-me/')
@app.route('/about/')
def aboutme():
    return('All about me!')

@app.route('/about-you/', methods=['GET', 'POST'])
def aboutyou():
    if request.method == 'POST':
        print(request.form)
        name = request.form['name']
        return("Hello, {}".format(name))
    else:
        page = '''
        <html><body>
            <form action="" method="post" name="form">
                <label for="name">Name:</label>
                <input type="text" name="name" id="name"/>
                <input type="submit" name="submit" id="submit"/>
            </form>
        </body></html>'''
        return page

@app.route('/say-hello/<name>')
def sayhello(name):
    return "Hello there {}!".format(name)

@app.route('/add/<int:num1>/<int:num2>/')
def add(num1, num2):
    return "Number is {}".format(num1+num2)

# Looking for /try-get-name/?name=my%20name%20is%20slim%20shady
@app.route('/try-get-name/')
def try_get_name():
    name = request.args.get('name', '')
    if name == "":
        return "Enter a name pls sirr!"
    else:
        return "Oh, I didn't see you there {}".format(name)

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
