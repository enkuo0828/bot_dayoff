from googleapiclient.discovery import build


class Service(object):

    @classmethod
    def get_service(cls, config):
        return build(
            serviceName=config.get('SERVICE_NAME'),
            version=config.get('SERVICE_VERSION'),
            developerKey=config.get('DEVELOPER_KEY'),
        )
