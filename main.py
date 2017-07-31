import uuid
from flask import Flask, request, jsonify, json
from constants import DAYOFF_HELP_TEXT, MEETING_HELP_TEXT, MENU_OPTION
from logic import dayoff_create, meeting_func, make_dayoff_event, make_desc
from service import Service
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
    form = json.loads(request.form['payload'])
    callback_id = form.get('callback_id')
    sel_actions = form.get('actions')[0]

    message = form.get('original_message')

    def check_actions_selected(attachements):
        select_result = {}
        for attach in attachements:
            for act in attach['actions']:
                if act['type'] == 'button':
                    continue
                if not act.get('selected_options'):
                    return False, select_result
                else:
                    select_result[act["name"]] = \
                        act["selected_options"][0]["value"]
        return True, select_result

    def select_return(actions):
        for act in actions:
            if act['name'] == sel_actions.get('name'):
                act["selected_options"] = \
                    sel_actions.get('selected_options')
                act["selected_options"][0]['text'] = \
                    sel_actions.get('selected_options')[0]['value']
        return actions

    if callback_id == 'start_time_selection':
        actions = message['attachments'][0]['actions']
        actions = select_return(actions)
        message['attachments'][0]['actions'] = actions
    elif callback_id == 'end_time_selection':
        actions = message['attachments'][1]['actions']
        actions = select_return(actions)
        message['attachments'][1]['actions'] = actions
    elif callback_id == 'Reason':
        actions = message['attachments'][2]['actions'][0]
        #  actions = select_return(actions)
        # actions['data_source'] = ""
        actions['options'] = [{
            "text": sel_actions.get('selected_options')[0]['value'],
            "value": sel_actions.get('selected_options')[0]['value']
        }]
        actions['selected_options'] = [{
            "text": sel_actions.get('selected_options')[0]['value'],
            "value": sel_actions.get('selected_options')[0]['value']
        }]
        message['attachments'][2]['actions'][0] = actions
    else:
        attachements = message.get('attachments')
        check_result, select_result = check_actions_selected(attachements)
        if check_result:
            reason = select_result['reason']
            def get_dayoff_time(select_result):

                return '{}T{}:00'.format(
                    select_result['start_date'],
                    select_result['start_time']
                ), '{}T{}:00'.format(
                    select_result["end_date"], select_result["end_time"])
            user = form.get('user').get('name')
            start_datetime, end_datetime = get_dayoff_time(select_result)
            desc = make_desc(user, start_datetime, end_datetime, reason)
            event = make_dayoff_event(reason,
                                      desc,
                                      start_datetime,
                                      end_datetime)
            service = Service.get_service(app.config, user)
            created_event = service.events().insert(
                calendarId=app.config.get('CALENDAR_ID'),
                # config.get('CALENDAR_ID'),
                body=event
            ).execute()
            message = {
                "response_type": "in_channel",
                "text": desc,
            }

    return jsonify(message)


@app.route('/dayoff/menu/', methods=['POST'])
def dayoff_menu():
    return jsonify(MENU_OPTION)


@app.route('/dayoff/reason_menu/', methods=['POST'])
def dayoff_reason_select():
    form = json.loads(request.form['payload'])
    result = {
        "options": [
            {
                "text": form.get("value"),
                "value": form.get("value")
            }
        ]
    }
    return jsonify(result)


@app.route('/meeting/', methods=['POST'])
def meeting_func():
    text = request.form['text']
    if '' == text:
        return MEETING_HELP_TEXT

    if '會議' in text:
        return meeting_func(text)


@app.route('/oauth/', methods=['POST'])
def oauth():
    pass


@app.route('/call_back/', methods=['POST'])
def call_back():
    pass

if __name__ == '__main__':

    app.run()
