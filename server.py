from flask import Flask
from random import randint

app = Flask(__name__)


def make_h1(function):
    def wrapper():
        return f'<h1>{function()}</h1>'
    return wrapper


@app.route('/')
def home_page():
    return '<h1>Guess a number between 0 and 9</h1> ' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


num = randint(0, 9)


@app.route('/<guessed_num>')
def results(guessed_num):
    gnum = int(guessed_num)
    if gnum == num:
        return f'<h1 style="color:green">{gnum} is the right number congratulations !!!</h1> ' \
               f'<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif gnum > num:
        return f'<h1 style="color:red">{gnum} is too high, please try again :p</h1>' \
               f'<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif gnum < num:
        return f'<h1 style="color:red">{gnum} is too low, please try again :p</h1>' \
               f'<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'


if __name__ == '__main__':
    app.run(debug=True)
