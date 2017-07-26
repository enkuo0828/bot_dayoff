import datetime

DAYOFF_HELP_TEXT = "請假時間格式:YYYYMMDDhhmm YYYYMMDDhhmm"
MEETING_HELP_TEXT = "會議時間格式:YYYYMMDDhhmm YYYYMMDDhhmm @someone ... #roomname"
DAY_RANGE = [
    datetime.date.today() + datetime.timedelta(days=x) for x in range(-7, 30)
]
DAY_OPTION = [
    '{}-{}-{}'.format(day.year, day.month, day.day) for day in DAY_RANGE
]
today = datetime.date.today()
TODAY = '{}-{}-{}'.format(today.year, today.month, today.day)
TIME_OPTION = []
for hour in range(8, 20):
    for min in ['00', '30']:
        TIME_OPTION.append(':'.join((str(hour), min)))
MENU_OPTION = {
    "response_type": "ephemeral",
    # "replace_original": "true",
    "attachments": [
        {
            "text": "Choose Day Off Time",
            "color": "#3AA3E3",
            "callback_id": "day_off_time_selection",
            "actions": [
                {
                    "text": "Pick Start Date...",
                    "name": "start_date",
                    "type": "select",
                    "options": [
                        {"text": y, "value": y} for y in DAY_OPTION
                    ],
                    "selected_options": [
                        {"text": TODAY, "value": TODAY}
                    ]
                },
                {
                    "name": "start_time",
                    "text": "Pick Start Time...",
                    "type": "select",
                    "options": [
                        {"text": m, "value": m} for m in TIME_OPTION
                    ]
                },
                {
                    "name": "end_date",
                    "text": "Pick End Date...",
                    "type": "select",
                    "options": [
                        {'text': y, 'value': y} for y in DAY_OPTION
                    ],
                    "selected_options": [
                        {"text": TODAY, "value": TODAY}
                    ]
                },
                {
                    "name": "end_time",
                    "text": "Pick End Time...",
                    "type": "select",
                    "options": [
                        {"text": m, "value": m} for m in TIME_OPTION
                    ]
                },
                {
                    "text": "Submit",
                    "name": "Submit",
                    "type": "button",
                    "style": "primary"
                }
            ]
        },
    ]
}


