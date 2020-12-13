from flask import Flask, redirect, url_for, abort, request, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)


@app.route('/print/<int:number>/')
@app.route('/print-to/<int:number>/')
def print_to(number):
    numbers = []
    for i in range(number+1):
        numbers.append(i)
    return render_template('/examples/print_to.jinja', numbers = numbers)

@app.route('/users/')
@app.route('/names/')
def names():
    names = ['Duncan', 'Donald', 'Mary', 'Sally', 'Susan', 'Francesca', 'Jenny', 'Joesph', 'Andrew']
    return render_template('/examples/names.jinja', names=names)

@app.route('/do_like/')
@app.route('/like/')
def like():
    return render_template('/examples/people_i_like.jinja', names = ['Duncan', 'Donald', 'Mary', 'Sally', 'Susan', 'Francesca', 'Jenny', 'Joesph', 'Andrew'])

@app.route('/dont_like/')
@app.route('/dislike/')
def dislike():
    return render_template('/examples/people_i_dislike.jinja', names = ['Duncan', 'Donald', 'Mary', 'Sally', 'Susan', 'Francesca', 'Jenny', 'Joesph', 'Andrew'])

@app.route('/joking/')
def joking():
    return render_template('/examples/joking.jinja', names = ['Duncan', 'Donald', 'Mary', 'Sally', 'Susan', 'Francesca', 'Jenny', 'Joesph', 'Andrew'])

@app.route('/parent/')
def parent():
    return render_template('/examples/parent.jinja')

@app.route('/child/')
def child():
    return render_template('/examples/child.jinja')

@app.route('/grandchild/')
def grandchild():
    return render_template('/examples/grandchild.jinja')

@app.route('/greatgrandchild/')
@app.route('/great-grandchild/')
def super_grandchild():
    return render_template('/examples/greatgrandchild.jinja')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
