# slack_bot_with_gc

#### 目的
在slack透過簡單的指令 可直接新增 **事件** 在指定的google日曆上
#### 主要 requirement
flask, google-api-python-client, slack-client
#### 使用前提
1. 使用者 都使用同一個google domains
2. 建立**服務帳戶**(service account)的使用者必須是google domains的
**administrator**
#### 使用方式
GCP API 管理員
1. 開啟 Project並啟用 Google Calendar API
2. 建立憑證 > 服務帳戶金鑰 並勾選使用G suite
3. 下載SA的secret.json 檔名長得像：{服務帳戶名稱}-{secret-key}.json

GCP IAM與管理
1. 將頻道使用者以email加入此SA的所屬成員,角色選Project > 編輯者

Google Admin Console
1. 到 http://admin.google.com/
2. Security > Advanced settings > Authentication > Manage API client access
3. Client Name = 上面的secret.json中的client id
4. API Scopes = https://www.googleapis.com/auth/calendar
5. 點擊 Authorize

Google 日曆
1. 新增日曆
2. 新增頻道使用者到日曆中
3. 確認頻道使用者都有 **進行變更並管理共用設定** 的權限
4. 在日曆詳細資料中找到 **日曆 ID**

Service
1. 將secret.json 移到 settings中
2. 新增{config_name}.py 到 settings中
3. 填入下面
```
from .base import BaseConfig

class {config_name}(BaseConfig):
    CALENDAR_ID = "{CALENDAR_ID}"
    SERVICE_JSON_KEY = "./settings/{secret.json}"
    DOMAIN_NAME = "{DOMAIN_NAME}"
```
4. 修改main.py 中的
```app.config.from_object('settings.{py_filename}.{config class name}')```
5. Flask Run Command
```FLASK_APP=main.py flask run```

Slack
1. 登入domain所屬帳號
2. build app
3. 建立 Incoming Webhooks 到你想要連接的聊天室
4. 建立 Slash command 並填入對應的url與說明
5. 就可以開始使用您剛剛建立的 command了