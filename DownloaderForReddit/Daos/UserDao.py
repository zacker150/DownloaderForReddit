from sqlite3 import IntegrityError
import time

from ..Core.RedditObjects import User
from ..Daos.BaseDao import BaseDao


class UserDao(BaseDao):

    """
    A DAO class responsible for accessing User data stored in the database.  This DAO deals exclusively with the user
    table in the database.
    """

    def __init__(self, conn):
        super().__init__(conn)

    def get_all_users(self):
        """
        Returns a list of all users stored in the database.
        :return: A list of all users stored in the database.
        :rtype: list
        """
        users = []
        sql = "SELECT * FROM users"
        c = self.get_cursor()
        c.execute(sql)
        row = c.fetchone()
        while row is not None:
            users.append(self.build_user(row))
            row = c.fetchone()
        return users

    def get_user(self, user_name):
        """
        Builds a returns a user object from the database selected by the supplied user name.
        :param user_name: The name of the user object that is to be returned.
        :return: A User from the database with the supplied name. Returns None if there is no user with the supplied
                 name
        :type user_name: str
        :rtype: User
        """
        user = None
        sql = "SELECT * FROM users WHERE name=?"
        c = self.get_cursor()
        c.execute(sql, (user_name, ))
        row = c.fetchone()
        if row is not None:
            user = self.build_user(row)
        return user

    def build_user(self, row):
        """
        Builds a User out of the data provided in the supplied row.
        :param row: A row returned from an sqlite query.
        :return: A User with the attributes contained in the supplied row.
        :type row: sqlite3.Row
        :rtype: User
        """
        user = User(
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
            row['date_added']
        )
        user.date_limit = row['date_limit']
        user.custom_date_limit = row['custom_date_limit']
        user.save_undownloaded_content = row['save_unfinished']
        user.enable_download = row['enable_download']
        user.lock = row['lock']
        return user

    def add_user(self, user):
        """
        Adds the supplied user to the database.
        :param user: A User containing the values that are to be added to the database.
        :return: True if the insert operation was successful, False if not.
        :type user: User
        :rtype: bool
        """
        c = self.get_cursor()
        try:
            sql = "INSERT INTO users (name, save_path, post_limit, avoid_duplicates, download_videos, " \
                  "download_images, download_self_posts, download_comments, nsfw_filter, date_limit, " \
                  "custom_date_limit, save_unfinished, enable_download, lock, date_added) VALUES " \
                  "(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            c.execute(sql, (user.name, user.save_path, user.post_limit, user.avoid_duplicates,
                            user.download_videos, user.download_images, user.download_self_posts,
                            user.download_comments, user.nsfw_filter, user.date_limit, user.custom_date_limit,
                            user.save_undownloaded_content, user.enable_download, user.lock, time.time()))
            user.id = c.lastrow
            return user.id is not None
        except IntegrityError:
            self.logger.error("Failed to add user to database", extra={'user_name': user.name})
            return False

    def update_user(self, user):
        """
        Updates the stored values for the supplied user.
        :param user: The User who's database values are to be updated.
        :return: True if the update operation was successful, False if it was not.
        :type user: User
        :rtype: bool
        """
        c = self.get_cursor()
        try:
            sql = "UPDATE users SET version=?, name=?, save_path=?, post_limit=?, avoid_duplicates=?, " \
                  "download_videos=?, download_images=?, download_self_posts=?, download_comments=?, nsfw_filter=?," \
                  "date_limit=?, custom_date_limit=?, save_unfinished=?, enable_download=?, lock=? WHERE id=?"
            c.execute(sql, user.version, user.name, user.save_path, user.post_limit, user.avoid_duplicates,
                      user.download_videos, user.download_images, user.download_self_posts, user.download_comments,
                      user.nsfw_filter, user.date_limit, user.custom_date_limit, user.save_undownloaded_content,
                      user.enable_download, user.lock, user.id)
            return c.rowcount > 0
        except IntegrityError:
            self.logger.error("Failed to update user entry in database", extra={'user_name': user.name})
            return False

    def delete_user(self, user):
        """
        Deletes the supplied user from the database.
        :param user: The User that is to be deleted from the database.
        :return: True if the update operation was successful, False if it was not.
        :type user: User
        :rtype: bool
        """
        c = self.get_cursor()
        try:
            sql = "DELETE FROM users WHERE id=?"
            c.execute(sql, (user.id, ))
            return c.rowcount > 0
        except IntegrityError:
            self.logger.error("Failed to delete user from database", extra={'user_name': user.name})
            return False
