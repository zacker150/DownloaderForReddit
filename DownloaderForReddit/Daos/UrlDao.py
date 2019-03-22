from sqlite3 import IntegrityError
import time

from ..RedditObjects.Url import Url
from ..Daos.BaseDao import BaseDao


class UrlDao(BaseDao):

    """
    A DAO class responsible for accessing the Url data stored in the database.  This DAO deals exclusively with the url
    table in the database.
    """

    def __init__(self, conn):
        super().__init__(conn)

    def get_all_urls(self):
        """
        Returns a list of all the urls stored in the database.
        :return: A list of all urls.
        :rtype: list
        """
        urls = []
        c = self.get_cursor()
        sql = "SELECT * FROM urls"  # TODO: this will need to have limit and order
        c.execute(sql)
        row = c.fetchone()
        while row is not None:
            urls.append(self.build_url(row))
            row = c.fetchone()
        return urls

    def get_urls_for_post(self, post):
        """
        Returns a list of urls that are associated with the supplied post.  For posts that link to content, this should
        only be a single url.  For self posts it is possible that there will be multiple links associated with the post.
        :param post: The post for which associated urls are to be returned.
        :return: A list of urls associated with the supplied post.
        :type post: Post
        :rtype: list
        """
        sql = "SELECT * FROM urls WHERE id IN (SELECT url_id FROM post_urls WHERE post_id=?)"
        return self.get_urls(sql, (post.id, ))

    def get_urls_for_comment(self, comment):
        """
        Returns a list of urls that are associated with the supplied comment.  This list may contain only one url or
        many urls.
        :param comment: The comment for which associated urls are to be returned.
        :return: A list of urls that are associated with the supplied comment.
        :type comment: Comment
        :rtype: list
        """
        sql = "SELECT * FROM urls WHERE id IN (SELECT url_id FROM comment_urls WHERE comment_id=?)"
        return self.get_urls(sql, (comment.id, ))

    def get_urls_for_user(self, user):
        """
        Returns a list of all urls that have been posted by the supplied user.  This list will most likely be a large
        list of urls.
        :param user: The User who posted the queried urls to reddit.
        :return: A list of Urls that have been posted by the supplied user.
        :type user: User
        :rtype: list
        """
        sql = "SELECT * FROM urls WHERE id IN " \
              "(SELECT url_id FROM post_urls WHERE post_id IN " \
              "(SELECT post_id FROM user_posts WHERE user_id=:id) " \
              "UNION ALL " \
              "SELECT url_id FROM comment_urls WHERE comment_id IN " \
              "(SELECT comment_id FROM user_comments WHERE user_id=:id))"
        return self.get_urls(sql, {'id': user.id})

    def get_urls_for_subreddit(self, subreddit):
        """
        Returns a list of all urls that have been posted to the supplied subreddit.  This list will likely be a very
        large list of urls.
        :param subreddit: The subreddit from which urls are to be queried.
        :return: A list of urls that are associated with the supplied subreddit.
        :type subreddit: Subreddit
        :rtype: list
        """
        sql = "SELECT * FROM urls WHERE id IN " \
              "(SELECT url_id FROM post_urls WHERE post_id IN " \
              "(SELECT post_id FROM subreddit_posts WHERE subreddit_id=:id) " \
              "UNION ALL " \
              "SELECT url_id FROM comment_urls WHERE comment_id IN " \
              "(SELECT comment_id FROM subreddit_comments WHERE subreddit_id=:id))"
        return self.get_urls(sql, {'id': subreddit.id})

    def get_urls(self, sql, value_tup):
        """
        Handles the actual querying of the database for a list of urls based on the supplied sql statement and the
        value tuple.
        :param sql: The sql statement that is to be used to query the database.  Should contain necessary placeholders.
        :param value_tup: A value tuple used to hold the values that placeholders used in the sql statement are to be
                          replaced with.
        :return: A list of urls based on the supplied sql statement.
        :type sql: str
        :type value_tup: tuple/dict
        :rtype: list
        """
        urls = []
        c = self.get_cursor()
        c.execute(sql, value_tup)
        row = c.fetchone()
        while row is not None:
            urls.append(self.build_url(row))
            row = c.fetchone()
        return urls

    def get_url(self, url_id):
        """
        Queries and returns the url with the supplied id.
        :param url_id: The id of the url that is to be returned.
        :return: The Url with the supplied id.
        :type url_id: int
        :rtype: Url
        """
        url = None
        c = self.get_cursor()
        sql = "SELECT * FROM urls WHERE id=?"
        c.execute(sql, (url_id, ))
        row = c.fetchone()
        if row is not None:
            url = self.build_url(row)
        return url

    def check_existing_url(self, url):
        """
        Checks for the existence of the supplied url in the database.
        :param url: The url who's existence is to be checked.
        :return: True if the url is already in the database, False if it is not
        :type url: str
        :rtype: bool
        """
        c = self.get_cursor()
        sql = "SELECT 1 FROM urls WHERE url=?"
        c.execute(sql, (url, ))
        return c.fetchone() is not None

    def build_url(self, row):
        """
        Builds and returns a Url object from the data queried from the database that is stored in the supplied row
        object.
        :param row: The row object which holds the url information queried from the database.
        :return: A url with the information contained in the supplied row.
        :type row: sqlite3.Row
        :rtype: Url
        """
        url = Url(_id=row['id'], url=row['url'], date_added=row['date_added'])
        return url

    def add_url(self, url):
        """
        Adds the supplied url to the database.
        :param url: The url which is to be added to the database.
        :return: True if the url was successfully added, false if it was not.
        :type url: Url
        :rtype: bool
        """
        c = self.get_cursor()
        try:
            sql = "INSERT INTO urls (url, date_added) VALUES (?, ?)"
            c.execute(sql, url.url, time.time())
            return c.rowcount > 0
        except IntegrityError:
            self.logger.error("Failed to add url to database", extra={'url': url.url})
            return False

    def update_url(self, url):
        """
        Updates the supplied urls data in the database.
        :param url: The url which is to be updated in the database.
        :return: True if the url was successfully updated, false if it was not.
        :type url: Url
        :rtype: bool
        """
        c = self.get_cursor()
        try:
            sql = "UPDATE urls SET url=? WHERE id=?"
            c.execute(sql, url.url, url.id)
            return c.rowcount > 0
        except IntegrityError:
            self.logger.error("Failed to update url", extra={'url': url.url})
            return False

    def delete_url(self, url):
        """
        Deletes the supplied url from the database.
        :param url: The url which is to be deleted from the database.
        :return: True if the url was successfully deleted, and false if it was not.
        :type url: Url
        :rtype: bool
        """
        c = self.get_cursor()
        try:
            sql = "DELETE FROM urls WHERE id=?"
            c.execute(sql, (url.id, ))
            return c.rowcount > 0
        except IntegrityError:
            self.logger.error("Failed to delete url from database", extra={'url': url.url})
