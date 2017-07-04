from service import Service
import rfc3339


def dayoff_func(user, text, config):
    times = text.split(' ')
    if len(times) != 3:
        return "錯誤的時間資訊：請輸入日期與時間範圍\n" \
               "範例：1月1日 8點到 12點 0101 0800 1200"
    ans = '{}於{}的{}到{}請假'.format(user, times[0], times[1], times[2])
    # TODO 請假
    service = Service.get_service(config)
    created_event = service.events().quickAdd(
        calendarId=config.get('CALENDAR_ID'),
        text=ans
    ).execute()
    print(created_event)
    return ans + ' event_id:{}'.format(created_event['id'])


def meeting_func(user, text):
    pass
