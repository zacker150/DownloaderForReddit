import logging
from PyQt5.QtCore import QObject, pyqtSignal

from ..Utils import Injector


class PostHandler(QObject):

    """
    A class that is responsible for handling Posts and their comments that have been extracted from reddit.  This class
    will handle checking if comments should be extracted from posts, organizing comments with posts as specified by the
    settings, saving both posts and comments to the database, and downloading posts and comments in the manner specified
    by the settings.  This class is designed to be run in it's own thread parallel with the extraction and download
    threads.
    """

    finished = pyqtSignal()

    def __init__(self, reddit_object_queue):
        """
        Initializes a PostHandler instance.

        :param reddit_object_queue: A queue in which reddit objects (users or subreddits) are placed in order for any
                                    Post objects that have been added to them to be handled via this class.
        :type reddit_object_queue: queue.Queue
        """
        super().__init__()
        self.logger = logging.getLogger('DownloaderForReddit.%s' % __name__)
        self.settings_manager = Injector.get_settings_manager()
        self.run = True
        self.queue = reddit_object_queue


