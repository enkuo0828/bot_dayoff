import time
from service import Service
from werkzeug.wrappers import Response
import rfc3339


def dayoff_create(user, text, config):
    times = text.split(' ')
    if len(times) != 3:
        return "錯誤的時間資訊：請輸入日期與時間範圍\n" \
               "範例：1月1日 8點到 12點 0101 0800 1200"
    ans = '{}於{}的{}到{}請假'.format(user, times[0], times[1], times[2])
    # TODO 請假
    service = Service.get_service(config, user)
    tm_year = time.localtime().tm_year
    event = {
        'summary': ans,
        'start': {
            'dateTime': '{}-{}-{}T{}:{}:00'.format(
                tm_year, times[0][:2], times[0][2:], times[1][:2], times[1][2:]
            ),
            'timeZone': 'Asia/Taipei'
        },
        'end': {
            'dateTime': '{}-{}-{}T{}:{}:00'.format(
                tm_year, times[0][:2], times[0][2:], times[2][:2], times[2][2:]
            ),
            'timeZone': 'Asia/Taipei'
        }
    }
    created_event = service.events().insert(
        calendarId=config.get('CALENDAR_ID'),  # config.get('CALENDAR_ID'),
        body=event
    ).execute()
    return ans + ' event_id:{}'.format(created_event['id'])


def meeting_func(user, text):
    pass
