from flask import Flask, request
from constants import DAYOFF_HELP_TEXT, MEETING_HELP_TEXT
from logic import dayoff_func, meeting_func
app = Flask(__name__)
app.config.from_object('settings.local.DevelopConfig')


@app.route('/dayoff/', methods=['POST'])
def dayoff():
    print(request.form)
    user = request.form['user_name']
    text = request.form['text']
    if '' == text:
        return DAYOFF_HELP_TEXT

    print(app.config)
    return dayoff_func(user, text, app.config)


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
