import random
from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route('/')
def generate_likud_message():
    is_collab = None
    if random.random() > 0.5:
        is_collab = random_line_from_staticfiles('collab.txt')

    return render_template('index.html', before=random_line_from_staticfiles('before.txt'),
                           name=random_line_from_staticfiles('names.txt'),
                           nickname=random_line_from_staticfiles('nickname.txt'),
                           action=random_line_from_staticfiles('actions.txt'),
                           collab=is_collab,
                           ending=random_line_from_staticfiles('ending.txt'))


def random_line_from_staticfiles(filename):
    with open('staticfiles/' + filename, encoding="utf8") as file:
        return random.choice(file.readlines())
