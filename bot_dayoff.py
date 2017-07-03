from flask import Flask, request
from constants import HELP_TEXT
app = Flask(__name__)


@app.route('/', methods=['POST'])
def day_off():
    print(request.form)
    user = request.form['user_name']
    text = request.form['text']
    if '-h' in text:
        #
        return HELP_TEXT

    if '-list' in text:
        # call list
        return HELP_TEXT

    times = text.split(' ')

    if len(times) != 3:
        return "錯誤的時間資訊：請輸入日期與時間範圍\n" \
               "範例：1月1日 8點到 12點 0101 0800 1200"
    # TODO 請假

    ans = '{}於{}的{}到{}請假'.format(user, times[0], times[1], times[2])
    return ans


if __name__ == '__main__':
    app.run()
