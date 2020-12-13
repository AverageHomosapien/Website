from flask import Flask, redirect, url_for, abort, request, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
@app.route('/home/')
def home():
    #return render_template('second_home.jinja')
    return render_template('index.jinja')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
