from flask import Flask, request
from constants import HELP_TEXT
from logic import dayoff, meeting
app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    print(request.form)
    user = request.form['user_name']
    text = request.form['text']
    if '' == text:
        return HELP_TEXT

    if '-h' in text:
        return HELP_TEXT

    if '-list' in text:
        # call list
        return HELP_TEXT

    if '請假' in text:
        return dayoff(user, text)

    if '會議' in text:
        return meeting(text)


@app.route('/call_back/', methods=['POST'])
def call_back():
    pass

if __name__ == '__main__':
    app.run()
