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

from urllib.parse import urlparse

from DownloaderForReddit.Utils.SystemUtil import epoch_to_str


class Post:

    """
    A class representing a post made on Reddit.

    Holds information about an actual post made to reddit such as the title, score, text, etc.  This class is used as
    both a database model class and as a way to save and use post information in other parts of the application.

    Attributes:
        text: The actual text part of a post if it is a self-post.  Value will be None if the post is not a self-post.
        score: The karma score that the post had at the time of download.
        date_added: Value used by the database to keep a record of the date and time that post data was entered into
                    the database.  Should only be set by the post dao.
    """

    def __init__(self, _id, title, author_id, author, subreddit_id, subreddit, created, url=None, status='good',
                 domain=None, score=None):
        """
        Initializes the post object with necessary data.
        :param _id: The id of the post as assigned by the database.
        :param title: The title of the post.
        :param author_id: The id of the author as stored in the database if the author is in fact stored in the
                          database, otherwise None
        :param author: The user who made the post to reddit.
        :param subreddit_id: The id of the subreddit as stored in the databse if the subreddit is in fact stored in the
                             database, otherwise None
        :param subreddit: The subreddit in which the post was made.
        :param created: The epoch time that the post was made.
        :param url: The url that the post links to.
        :param status: The status of the post.  This is used to hold status information about the post, including the
                       reason the post failed to download if necessary.  Defaults to "good".
        :param domain: The domain name of the site hosting the post.  This can be supplied by reddit but defaults to
                       None.  If the default value is taken, this class will determine the domain name based on the
                       supplied url.
        :type _id: int
        :type title: str
        :type author_id: int
        :type author: str
        :type subreddit_id: int
        :type subreddit: str
        :type created: long
        :type url: str
        :type status: str
        :type domain: str
        """
        self.id = _id
        self.title = title
        self.author_id = author_id
        self.author = author
        self.subreddit_id = subreddit_id
        self.subreddit = subreddit
        self.created = created
        self.url = url

        self.text = None
        self.score = score
        self.date_added = None
        self.domain = domain if domain is not None else self.get_domain()

        self.status = status
        self.save_status = 'Not Saved'

    def __str__(self):
        return self.format_failed_text()

    @property
    def date_posted(self):
        return epoch_to_str(self.created)

    def get_domain(self):
        parsed_url = urlparse(self.url)
        self.domain = '{url.netloc}'.format(url=parsed_url)

    def format_failed_text(self):
        return 'Failed to download content:\nUser: %s  Subreddit: %s  Title: %s\nUrl:  %s\n%s\nSave Status: %s\n' % \
               (self.author, self.subreddit, self.title, self.url, self.status, self.save_status)
