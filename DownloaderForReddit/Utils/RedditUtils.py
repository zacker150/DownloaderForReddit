"""
Downloader for Reddit takes a list of reddit users and subreddits and downloads content posted to reddit either by the
users or on the subreddits.


Copyright (C) 2017, Kyle Hickey


This file is part of the Downloader for Reddit.

Downloader for Reddit is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Downloader for Reddit is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Downloader for Reddit.  If not, see <http://www.gnu.org/licenses/>.
"""

import praw
import prawcore
from PyQt5.QtCore import QObject, pyqtSignal
import logging

from DownloaderForReddit.RedditObjects.Post import Post
from ..version import __version__


reddit_instance = None


def get_reddit_instance():
    global reddit_instance
    if not reddit_instance:
        reddit_instance = praw.Reddit(user_agent='python:DownloaderForReddit:%s (by /u/MalloyDelacroix)' % __version__,
                                      client_id='frGEUVAuHGL2PQ', client_secret=None)
    return reddit_instance


def convert_praw_posts(praw_post_list, reddit_object):
    """
    Converts the list of praw post objects (raw praw Post objects as extracted directly from reddit using praw) to Post
    model objects that can be stored to the application database.
    :param praw_post_list: A list of praw.Post objects.
    :param reddit_object: The Reddit object that is associated with the supplied posts.  Either a User or a Subreddit.
    :return: A list of Post model objects containing pertinent information from the original praw post object that can
             be saved to the database.
    """
    posts = [convert_post(x, reddit_object) for x in praw_post_list]
    return posts


def convert_post(praw_post, reddit_object):
    """
    Makes a Post model object out of the supplied praw post.  The post is converted here to a Post object to get the
    important data from the praw post object and convert it into a post model that can be saved to the database at
    a later point.  This post will also have variables that are used throughout the application and will have a
    uniform structure.
    :param praw_post: The praw.Post object as it was extracted from reddit.
    :param reddit_object: The reddit object that the post is associated with.  Should be either User or Subreddit.
    :return: A RedditObjects.Post object containing the pertinent information taken from the raw reddit post.
    :type praw_post: praw.Post
    :type reddit_object: RedditObject
    :rtype: Post
    """
    if reddit_object.object_type == 'USER':
        author_id = reddit_object.id
        author = reddit_object.name
        subreddit_id = None
        subreddit = praw_post.subreddit
    else:
        author_id = None
        author = praw_post.author
        subreddit_id = reddit_object.id
        subreddit = reddit_object.name

    post = Post(title=praw_post.title, author_id=author_id, author=author, subreddit_id=subreddit_id,
                subreddit=subreddit, created=praw_post.created, url=praw_post.url, self_post=praw_post.is_self,
                domain=praw_post.domain, score=praw_post.score, text=praw_post.selftext,
                html_text=praw_post.selftext_html, nsfw=praw_post.over_18, reddit_id=praw_post.id)
    return post


class NameChecker(QObject):

    """
    This class is to check for the existence of a reddit object name using praw, then report back whether the name
    exists or not.  This class is intended to be ran in a separate thread.
    """

    name_validation = pyqtSignal(tuple)
    finished = pyqtSignal()

    def __init__(self, object_type, queue):
        """
        Initializes the NameChecker and establishes its operation setup regarding whether to target users or subreddits.
        :param object_type: The type of reddit object (USER or SUBREDDIT) that the supplied names will be.
        :param queue: The queue established by the caller in which names to be checked will be deposited.
        :type object_type: str
        :type queue: Queue
        """
        super().__init__()
        self.logger = logging.getLogger('DownloaderForReddit.%s' % __name__)
        self.r = get_reddit_instance()
        self.continue_run = True
        self.object_type = object_type
        self.queue = queue

    def run(self):
        """
        Continuously checks the queue for a new name then calls the check name method when one is extracted from the
        queue.  Responsible for emitting the finished signal when the class is done and is to be destroyed.
        """
        while self.continue_run:
            name = self.queue.get()
            if name is not None:
                self.check_name(name)
        self.finished.emit()

    def stop_run(self):
        """
        Switches off the run cycle.  None is added to the queue because the run method will block until it receives
        something from the queue.
        """
        self.continue_run = False
        self.queue.put(None)

    def check_name(self, name):
        if self.object_type == 'USER':
            self.check_user_name(name)
        else:
            self.check_subreddit_name(name)

    def check_user_name(self, name):
        user = self.r.redditor(name)
        try:
            test = user.fullname
            self.name_validation.emit((name, True))
        except (prawcore.exceptions.NotFound, prawcore.exceptions.Redirect, AttributeError):
            self.name_validation.emit((name, False))
        except:
            self.logger.error('Unable to validate user name', extra={'user_name': name}, exc_info=True)

    def check_subreddit_name(self, name):
        sub = self.r.subreddit(name)
        try:
            test = sub.fullname
            self.name_validation.emit((name, True))
        except (prawcore.exceptions.NotFound, prawcore.exceptions.Redirect, AttributeError):
            self.name_validation.emit((name, False))
        except:
            self.logger.error('Unable to validate subreddit name', extra={'subreddit_name': name}, exc_info=True)
