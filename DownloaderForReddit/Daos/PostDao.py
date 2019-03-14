from sqlite3 import IntegrityError
import time

from ..RedditObjects.Post import Post
from ..Daos.BaseDao import BaseDao


class PostDao(BaseDao):

    def __init__(self, conn):
        super().__init__(conn)
        self.limit = 100
        self.sort_method = 'title'
        self.sort_order = 'asc'

    def get_all_posts(self):
        posts = []
        sql = "SELECT * FROM posts"  # TODO: this will need to have a limit and order
        c = self.get_cursor()
        c.execute(sql)
        row = c.fetchone()
        while row is not None:
            posts.append(self.build_post(row))
            row = c.fetchone()
        return posts

    def get_post_from_id(self, _id):
        return self.search_post('id', _id)

    def get_post_from_title(self, title):
        return self.search_post('title', title)

    def search_post(self, column, value):
        post = None
        c = self.get_cursor()
        sql = "SELECT * FROM posts WHERE ?=?"
        c.execute(sql, (column, value))
        row = c.fetchone()
        if row is not None:
            post = self.build_post(row)
        return post

    def build_post(self, row):
        post = Post(
            row['id'],
            row['title'],
            row['author_id'],
            row['author_name'],
            row['subreddit_id'],
            row['subreddit_name'],
            row['creation_date'],
        )
        post.text = row['text']
        post.score = row['score']
        post.date_added = row['date_added']
        return post

    def add_post(self, post):
        c = self.get_cursor()
        try:
            sql = "INSERT INTO posts (title, author_id, author_name, subreddit_id, subreddit_name, score, " \
                  "creation_date, text) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            c.execute(sql, (post.title, post.author_id, post.author, post.subreddit_id, post.subreddit, post.score,
                            post.created))
            return c.rowcount > 0
        except IntegrityError:
            self.logger.error("Failed to add post to database", extra={'post_title': post.title})
            return False

    def update_post(self, post):
        c = self.get_cursor()
        try:
            sql = "UPDATE posts SET title=?, author_id=?, author_name=?, subreddit_id=?, subreddit_name=?, score=?, " \
                  "creation_date=?, text=? WHERE id=?"
            c.execute(sql, post.title, post.author_id, post.author, post.subreddit_id, post.subreddit, post.score,
                      post.created, post.text, post.id)
            return c.rowcount > 0
        except IntegrityError:
            self.logger.error("Failed to update post", extra={'post_title': post.title})
            return False

    def delete_post(self, post):
        c = self.get_cursor()
        try:
            sql = "DELETE FROM posts WHERE id=?"
            c.execute(sql, (post.id, ))
            return c.rowcount > 0
        except IntegrityError:
            self.logger.error("Failed to delete post", extra={'post_title': post.title})
            return False
