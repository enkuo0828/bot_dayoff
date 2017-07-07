from flask import jsonify
from service import Service


def dayoff_create(user, text, config):
    times = text.split(' ')
    if len(times) < 6:
        return "錯誤的時間資訊：請輸入日期與時間範圍\n" \
               "範例：2017 0101 0800 2017 0101 1200 請假理由"
    desc_head = '{}請假'.format(user)
    desc_end = '{}-{}-{}~{}-{}-{}'.format(
        user, times[0], times[1], times[2], times[3], times[4], times[5])
    if len(times) >= 7:
        reason = times[6]
        desc = desc_head + reason + desc_end
    else:
        reason = '{}請假'.format(user)
        desc = desc_head + desc_end
    # TODO 請假
    service = Service.get_service(config, user)
    event = {
        'summary': reason,
        'description': desc,
        'start': {
            'dateTime': '{}-{}-{}T{}:{}:00'.format(
                times[0], times[1][:2], times[1][2:], times[2][:2], times[2][2:]
            ),
            'timeZone': 'Asia/Taipei'
        },
        'end': {
            'dateTime': '{}-{}-{}T{}:{}:00'.format(
                times[3], times[4][:2], times[4][2:], times[5][:2], times[5][2:]
            ),
            'timeZone': 'Asia/Taipei'
        }
    }
    created_event = service.events().insert(
        calendarId=config.get('CALENDAR_ID'),  # config.get('CALENDAR_ID'),
        body=event
    ).execute()
    result = {
        "response_type": "in_channel",
        "text": desc,
    }
    return jsonify(result)


def dayoff_list(config):
    pass


def meeting_func(user, text):
    pass
