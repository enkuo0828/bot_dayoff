import uuid

from flask import Flask

app = Flask(__name__)
app.config.from_object('settings.local.DevelopConfig')
app.secret_key = str(uuid.uuid4())

from app import views

if __name__ == '__main__':
    app.run()
