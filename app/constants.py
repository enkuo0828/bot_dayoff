import calendar as ca
import datetime


DAYOFF_HELP_TEXT = "請假時間格式:YYYYMMDDhhmm YYYYMMDDhhmm"
MEETING_HELP_TEXT = "會議時間格式:YYYYMMDDhhmm YYYYMMDDhhmm @someone ... #roomname"
DAY_RANGE = [
    datetime.date.today() + datetime.timedelta(days=x) for x in range(-7, 30)
]
DAY_OPTION = [
    '{}-{}-{}'.format(day.year, str(day.month).zfill(2), str(day.day).zfill(2))
    for day in DAY_RANGE
]
today = datetime.date.today()
TODAY = '{}-{}-{}'.format(today.year,
                          str(today.month).zfill(2),
                          str(today.day).zfill(2))
TIME_OPTION = []
for hour in range(8, 20):
    for min in ['00', '30']:
        TIME_OPTION.append(':'.join((str(hour).zfill(2), min)))

MENU_OPTION = {
    "response_type": "in_channel",
    # "replace_original": "true",
    "attachments": [
        {
            "text": "Choose Start Date Time",
            "color": "#3AA3E3",
            "callback_id": "start_time_selection",
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
            ]
        },
        {
            "text": "Choose End Date Time",
            "color": "#3AA3E3",
            "callback_id": "end_time_selection",
            "actions": [
                {
                    "text": "Pick End Date...",
                    "name": "end_date",
                    "type": "select",
                    "options": [
                        {"text": y, "value": y} for y in DAY_OPTION
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
            ]
        },
        {
            "text": "Input Reason",
            "color": "#3AA3E3",
            "callback_id": "Reason",
            "actions": [
                {
                    "text": "請輸入請假事由",
                    "name": "reason",
                    "type": "select",
                    "data_source": "external"
                },

            ]
        },
        {
            "text": "",
            "color": "#3AA3E3",
            "callback_id": "submit",
            "actions": [
                {
                    "text": "Submit",
                    "name": "Submit",
                    "type": "button",
                    "style": "primary"
                }
            ]
        }
    ]
}


