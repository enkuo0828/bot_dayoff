from flask import jsonify

from app.service import Service


def dayoff_create(user, text, config):
    times = text.split(' ')
    if len(times) < 2:
        return "錯誤的時間資訊：請輸入日期與時間範圍\n" \
               "範例：201701010800 201701011200 請假理由"
    desc, reason = make_day0ff_result(user, times)
    # TODO 請假
    service = Service.get_service(config, user)
    start_datetime = '{}-{}-{}T{}:{}:00'.format(
        times[0][:4], times[0][4:6], times[0][6:8],
        times[0][8:10], times[0][10:]
    )
    end_datetime = '{}-{}-{}T{}:{}:00'.format(
        times[1][:4], times[1][4:6], times[1][6:8],
        times[1][8:10], times[1][10:]
    )
    event = make_dayoff_event(reason, desc, start_datetime, end_datetime)

    created_event = service.events().insert(
        calendarId=config.get('CALENDAR_ID'),  # config.get('CALENDAR_ID'),
        body=event
    ).execute()

    result = {
        "response_type": "in_channel",
        "text": desc,
    }
    return jsonify(result)


def make_dayoff_event(reason, desc, start_datetime, end_datetime):
    return {
        'summary': reason,
        'description': desc,
        'start': {
            'dateTime': start_datetime,
            'timeZone': 'Asia/Taipei'
        },
        'end': {
            'dateTime': end_datetime,
            'timeZone': 'Asia/Taipei'
        }
    }


def make_day0ff_result(user, times):
    year_a = times[0][:4]
    day_a = times[0][4:8]
    hour_a = times[0][8:]
    year_b = times[1][:4]
    day_b = times[1][4:8]
    hour_b = times[1][8:]
    same_year = False
    same_month = False
    same_day = False
    if year_a == year_b:
        same_year = True
    if day_a[:2] == day_b[:2]:
        same_month = True
    if day_a == day_b:
        same_day = True
    # 有填請假理由
    if len(times) == 3:
        reason = times[2]
    else:
        reason = '{}請假'.format(user)

    if same_year and same_month and same_day:
        time_desc = '@{}-{}-{} from {}:{} to {}:{}'.format(
            year_a, day_a[:2], day_a[2:],
            hour_a[:2], hour_a[2:], hour_b[:2], hour_b[2:])
    elif same_year and not same_day:
        time_desc = '@{} from {}-{} {}:{} to {}-{} {}:{}'.format(
            year_a, day_a[:2], day_a[2:], hour_a[:2], hour_a[2:],
            day_b[:2], day_b[2:], hour_b[:2], hour_b[2:]
        )
    elif not same_year:
        time_desc = 'from {}-{}-{} {}:{} to {}-{}-{} {}:{}'.format(
            year_a, day_a[:2], day_a[2:], hour_a[:2], hour_a[2:],
            year_b, day_b[:2], day_b[2:], hour_b[:2], hour_b[2:]
        )
    desc = reason + ' {}'.format(time_desc)
    return desc, reason


def make_desc(user, start_datetime, end_datetime, reason):
    same_year = False
    same_month = False
    same_day = False
    if start_datetime[:4] == end_datetime[:4]:
        same_year = True
    if start_datetime[5:7] == end_datetime[5:7]:
        same_month = True
    if start_datetime[8:10] == end_datetime[8:10]:
        same_day = True
    if same_year and same_month and same_day:
        time_desc = '@{} from {} to {}'.format(
            start_datetime[:10], start_datetime[11:16], end_datetime[11:16]
        )
    elif same_year and not same_day:
        time_desc = '@{} from {} {} to {} {}'.format(
            start_datetime[:4], start_datetime[5:10], start_datetime[11:16],
            end_datetime[5:10], end_datetime[11:16]
        )
    elif not same_year:
        time_desc = 'from {} to {}'.format(
            start_datetime, end_datetime
        )
    desc = "{} {} {}".format(user, reason, time_desc)
    return desc


def dayoff_list(config):
    pass


def meeting_func(user, text):
    pass
