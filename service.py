import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

scopes = ['https://www.googleapis.com/auth/calendar']


class Service(object):

    @classmethod
    def get_service(cls, config, user):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            config.get('SERVICE_JSON_KEY'), scopes)
        delegate_creds = credentials.create_delegated(
            '{}@{}'.format(user, config.get('DOMAIN_NAME'))
        )
        http = delegate_creds.authorize(httplib2.Http())
        return build(
            serviceName=config.get('SERVICE_NAME'),
            version=config.get('SERVICE_VERSION'),
            http=http
        )
