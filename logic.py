from googleapiclient.discovery import build
import settings
service = build(
    serviceName=settings.SERVICE_NAME,
    version=settings.SERVICE_VERSION,
    developerKey=settings.DEVELOPER_KEY,
)


def dayoff(user, text):
    times = text.split(' ')
    if len(times) != 3:
        return "錯誤的時間資訊：請輸入日期與時間範圍\n" \
               "範例：1月1日 8點到 12點 0101 0800 1200"
    # TODO 請假

    ans = '{}於{}的{}到{}請假'.format(user, times[0], times[1], times[2])
    return ans


def meeting(user, text):
    pass
