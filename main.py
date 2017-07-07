import uuid
from flask import Flask, request
from constants import DAYOFF_HELP_TEXT, MEETING_HELP_TEXT
from logic import dayoff_create, meeting_func

app = Flask(__name__)
app.config.from_object('settings.local.DevelopConfig')
app.secret_key = str(uuid.uuid4())


@app.route('/dayoff/', methods=['POST'])
def dayoff():
    user = request.form['user_name']
    text = request.form['text']
    if '' == text:
        return DAYOFF_HELP_TEXT

    return dayoff_create(user, text, app.config)


@app.route('/meeting/', methods=['POST'])
def meeting_func():
    text = request.form['text']
    if '' == text:
        return MEETING_HELP_TEXT

    if '會議' in text:
        return meeting_func(text)


@app.route('/call_back/', methods=['POST'])
def call_back():
    pass

if __name__ == '__main__':

    app.run()
