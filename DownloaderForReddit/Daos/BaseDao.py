import logging


class BaseDao:

    def __init__(self, connection):
        self.logger = logging.getLogger('DownloaderForReddit.%s' % __name__)
        self.conn = connection

    def get_cursor(self):
        return self.conn.cursor()

    def commit(self):
        self.conn.commit()
