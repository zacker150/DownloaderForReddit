import os
import sqlite3

from DownloaderForReddit.Core import Const
from DownloaderForReddit.Utils import SystemUtil


class DatabaseCreator:

    """
    Responsible for creating the sqlite database and the required tables for the application.
    """

    def __init__(self):
        self.db_path = os.path.join(SystemUtil.get_data_directory(), Const.DB_NAME)
        print(self.db_path)

        self.conn = None

    def connect_to_db(self):
        self.conn = sqlite3.connect(self.db_path)

    def close_connection(self):
        if self.conn is not None:
            self.conn.close()

    def execute(self, sql):
        if self.conn is not None:
            self.conn.execute(sql)

    def create_database(self):
        self.connect_to_db()
        self.create_tables()

    def create_tables(self):
        self.create_user_table()
        self.create_subreddit_table()
        self.create_post_table()
        self.create_comments_table()
        self.create_urls_table()
        self.create_user_posts_table()
        self.create_subreddit_posts_table()
        self.create_user_comments_table()
        self.create_subreddit_comments_table()
        self.create_posts_comments_table()
        self.create_post_urls_table()
        self.create_comment_urls_table()

    def create_user_table(self):
        self.execute(
            """
            CREATE TABLE "users" 
                ( `id` INTEGER, 
                `name` TEXT UNIQUE, 
                `save_path` TEXT, 
                `post_limit` INTEGER, 
                `avoid_duplicates` INTEGER NOT NULL DEFAULT 1, 
                `download_vidoes` INTEGER NOT NULL DEFAULT 1, 
                `download_images` INTEGER NOT NULL DEFAULT 1, 
                `download_self_posts` INTEGER NOT NULL DEFAULT 0, 
                `download_comments` INTEGER NOT NULL DEFAULT 0, 
                `nsfw_filter` INTEGER NOT NULL DEFAULT 1, 
                `date_limit` INTEGER NOT NULL DEFAULT 86400, 
                `custom_date_limit` INTEGER, 
                `save_unfinished` INTEGER NOT NULL DEFAULT 1, 
                `enable_download` INTEGER NOT NULL DEFAULT 1, 
                `date_added` INTEGER, 
            PRIMARY KEY(`id`) )
            """
        )

    def create_subreddit_table(self):
        self.execute(
            """
            CREATE TABLE "subreddit" 
                ( `id` INTEGER, 
                `name` TEXT NOT NULL UNIQUE, 
                `save_path` TEXT, 
                `post_limit` INTEGER, 
                `avoid_duplicates` INTEGER NOT NULL DEFAULT 1, 
                `download_videos` INTEGER NOT NULL DEFAULT 1, 
                `download_images` INTEGER NOT NULL DEFAULT 1, 
                `download_self_posts` INTEGER NOT NULL DEFAULT 0, 
                `download_comments` INTEGER NOT NULL DEFAULT 0, 
                `nsfw_filter` INTEGER NOT NULL DEFAULT 1, 
                `date_limit` INTEGER NOT NULL DEFAULT 86400, 
                `custom_date_limit` TEXT, 
                `save_unfinished` INTEGER NOT NULL DEFAULT 1, 
                `enable_download` INTEGER NOT NULL DEFAULT 1, 
                `date_added` INTEGER, 
                `subreddit_save_method` TEXT,
            PRIMARY KEY ('id') )
            """
        )

    def create_post_table(self):
        self.execute(
            """
            CREATE TABLE `posts` 
                ( `id` INTEGER, 
                `title` TEXT NOT NULL, 
                `author_id` INTEGER, 
                `author_name` TEXT, 
                `subreddit_id` INTEGER, 
                `subreddit_name` TEXT, 
                `score` INTEGER, 
                `creation_date` INTEGER, 
                `text` TEXT,
            PRIMARY KEY ('id') )
            """
        )

    def create_comments_table(self):
        self.execute(
            """
            CREATE TABLE "comments" 
                ( `id` INTEGER, 
                `user_id` INTEGER, 
                `user_name` TEXT, 
                `subreddit_id` INTEGER, 
                `subreddit_name` TEXT, 
                `score` INTEGER, 
                `creation_date` INTEGER, 
                `text` TEXT, 
            PRIMARY KEY(`id`) )
            """
        )

    def create_urls_table(self):
        self.execute(
            """
            CREATE TABLE `urls` 
                ( `id` INTEGER, 
                `url` TEXT NOT NULL UNIQUE, 
            PRIMARY KEY(`id`) )
            """
        )

    def create_user_posts_table(self):
        self.execute(
            "CREATE TABLE `user_posts` ( `user_id` INTEGER, `post_id` INTEGER )"
        )

    def create_subreddit_posts_table(self):
        self.execute(
            "CREATE TABLE `subreddit_posts` ( `subreddit_id` INTEGER, `post_id` INTEGER )"
        )

    def create_user_comments_table(self):
        self.execute(
            "CREATE TABLE `user_comments` ( `user_id` INTEGER, `comment_id` INTEGER )"
        )

    def create_subreddit_comments_table(self):
        self.execute(
            "CREATE TABLE `subreddit_comments` ( `subreddit_id` INTEGER, `comment_id` INTEGER )"
        )

    def create_posts_comments_table(self):
        self.execute(
            "CREATE TABLE `post_comments` ( `post_id` INTEGER, `comment_id` INTEGER )"
        )

    def create_post_urls_table(self):
        self.execute(
            "CREATE TABLE `post_urls` ( `post_id` INTEGER, `url_id` INTEGER )"
        )

    def create_comment_urls_table(self):
        self.execute(
            "CREATE TABLE `comment_urls` ( `comment_id` INTEGER, `url_id` INTEGER )"
        )
