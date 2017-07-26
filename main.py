import uuid
from flask import Flask, request, jsonify, json
from constants import DAYOFF_HELP_TEXT, MEETING_HELP_TEXT, MENU_OPTION
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


@app.route('/dayoff/action/', methods=['POST'])
def dayoff_action():
    temp = json.loads(request.form['payload'])
    print(type(temp))
    print(temp.get('actions'))
    print(temp)
    return jsonify('done')


@app.route('/dayoff/menu/', methods=['POST'])
def dayoff_menu():
    return jsonify(MENU_OPTION)


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
