from sqlite3 import IntegrityError
import time

from DownloaderForReddit.RedditObjects.RedditObjects import Subreddit
from ..Daos.BaseDao import BaseDao


class SubredditDao(BaseDao):

    """
    A DAO class responsible for accessing Subreddit data stored in the database.  This DAO deals exclusively with the
    subreddit table in the database.
    """

    def __init__(self, conn):
        super().__init__(conn)

    def get_all_subreddits(self):
        """
        Returns a list of Subreddit objects built from data stored in the subreddit database table.
        :return: A list of Subreddit objects stored in the database.
        :rtype: list
        """
        subs = []
        sql = "SELECT * FROM subreddits"
        c = self.get_cursor()
        c.execute(sql)
        row = c.fetchone()
        while row is not None:
            subs.append(self.build_sub(row))
            row = c.fetchone()
        return subs

    def get_subreddit(self, sub_name):
        """
        Builds and returns a Subreddit object from the database selected by the supplied subreddit name.
        :param sub_name: The name of the Subreddit which is to be queried from the database.
        :return: A Subreddit object built from data stored in the database which has the supplied subreddit name.
        :type sub_name: str
        :rtype: Subreddit
        """
        sub = None
        sql = "SELECT * FROM subreddits WHERE name=?"
        c = self.get_cursor()
        c.execute(sql, (sub_name, ))
        row = c.fetchone()
        if row is not None:
            sub = self.build_sub(row)
        return sub

    def build_sub(self, row):
        """
        Builds a Subreddit out of the data provided in the supplied row.
        :param row: A row returned from an sqlite query.
        :return: A Subreddit with the attributes contained in the supplied row.
        :type row: sqlite3.Row
        :rtype: Subreddit
        """
        sub = Subreddit(
            row['id'],
            row['version'],
            row['name'],
            row['save_path'],
            row['post_limit'],
            row['avoid_duplicates'],
            row['download_videos'],
            row['download_images'],
            row['download_self_posts'],
            row['download_comments'],
            row['nsfw_filter'],
            row['subreddit_save_method'],
            row['date_added']
        )
        sub.date_limit = row['date_limit']
        sub.custom_date_limit = row['custom_date_limit']
        sub.save_undownloaded_content = row['save_unfinished']
        sub.enable_download = row['enable_download']
        sub.lock = row['lock']
        return sub

    def add_subreddit(self, sub):
        """
        Adds the supplied subreddit to the database.
        :param sub: The Subreddit which is to be added to the database
        :return: True if the insert operation was successful, False if it was not.
        :type sub: Subreddit
        :rtype: bool
        """
        c = self.get_cursor()
        try:
            sql = "INSERT INTO subreddits (name, save_path, post_limit, avoid_duplicates, download_videos, " \
                  "download_images, download_self_posts, download_comments, nsfw_filter, date_limit, " \
                  "custom_date_limit, save_unfinished, enable_download, lock, date_added, subreddit_save_method) " \
                  "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            c.execute(sql, (sub.name, sub.save_path, sub.post_limit, sub.avoid_duplicates, sub.download_videos,
                            sub.download_images, sub.download_self_posts, sub.download_comments, sub.nsfw_filter,
                            sub.date_limit, sub.custom_date_limit, sub.save_undownloaded_content, sub.enable_download,
                            sub.lock, time.time(), sub.subreddit_save_method))
            sub.id = c.lastrow
            return sub.id is not None
        except IntegrityError:
            self.logger.error("Failed to add subreddit to database", extra={'subreddit': sub.name})
            return False

    def update_subreddit(self, sub):
        """
        Updates the stored values for the supplied subreddit.
        :param sub: The Subreddit who's values are to be updated in the database.
        :return: True if the update operation was successful, False if it was not.
        :type sub: Subreddit
        :rtype: bool
        """
        c = self.get_cursor()
        try:
            sql = "UPDATE subreddits SET version=?, name=?, save_path=?, post_limit=?, avoid_duplicates=?," \
                  "download_videos=?, download_images=?, download_self_posts=?, download_comments=?, nsfw_filter=?," \
                  "date_limit=?, custom_date_limit=?, save_unfinished=?, enable_download=?, lock=?, date_added=?," \
                  "subreddit_save_method=? WHERE id=?"
            c.execute(sql, (sub.version, sub.name, sub.save_path, sub.post_limit, sub.avoid_duplicates,
                            sub.download_videos, sub.download_images, sub.download_self_posts, sub.download_comments,
                            sub.nsfw_filter, sub.date_limit, sub.custom_date_limit, sub.save_undownloaded_content,
                            sub.enable_download, sub.lock, time.time(), sub.subreddit_save_method, sub.id))
            return c.rowcount > 0
        except IntegrityError:
            self.logger.error("Failed to update subreddit", extra={'subreddit': sub.name})
            return False

    def delete_subreddit(self, sub):
        """
        Delets the supplied subreddit from the database.
        :param sub: The subreddit which is to be deleted.
        :return: True if the operation was successful, False if it was not.
        :type sub: Subreddit
        :rtype: bool
        """
        c = self.get_cursor()
        try:
            sql = "DELETE FROM subreddits WHERE id=?"
            c.execute(sql, (sub.id, ))
            return c.rowcount > 0
        except IntegrityError:
            self.logger.error("Failed to delete subreddit", extra={'subreddit': sub.name})
            return False
