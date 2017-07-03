from flask import Flask, request
app = Flask(__name__)


@app.route('/', methods=['POST'])
def day_off():
    print(request.form)
    return '請輸入日期'


if __name__ == '__main__':
    app.run()
