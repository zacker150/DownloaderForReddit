from sqlite3 import IntegrityError
import time

from ..RedditObjects.Comment import Comment
from ..Daos.BaseDao import BaseDao


class CommentDao(BaseDao):

    def __init__(self, conn):
        super().__init__(conn)

    def get_all_comments(self):
        comments = []
        c = self.get_cursor()
        sql = "SELECT * FROM comments"  # TODO: this will need to have a limit and order
        c.execute(sql)
        row = c.fetchone()
        while row is not None:
            comments.append(self.build_comment(row))
            row = c.fetchone()
        return comments

    def get_comments_for_post(self, post):
        sql = "SELECT * FROM comments WHERE id IN (SELECT comment_id FROM post_comments WHERE post_id=?)"
        return self.get_comments(sql, post.id)

    def get_comments_for_user(self, user):
        sql = "SELECT * FROM comments WHERE id IN (SELECT comment_id FROM user_comments WHERE user_id=?)"
        return self.get_comments(sql, user.id)

    def get_comments_for_subreddit(self, subreddit):
        sql = "SELECT * FROM comments WHERE id IN (SELECT comment_id FROM subreddit_comments WHERE subreddit_id=?)"
        return self.get_comments(sql, subreddit.id)

    def get_comments(self, sql, id_value):
        comments = []
        c = self.get_cursor()
        c.execute(sql, (id_value, ))
        row = c.fetchone()
        while row is not None:
            comments.append(self.build_comment(row))
            row = c.fetchone()
        return comments

    def get_comment_by_id(self, comment_id):
        comment = None
        c = self.get_cursor()
        sql = "SELECT * FROM comments WHERE id=?"
        c.execute(sql, (comment_id, ))
        row = c.fetchon()
        if row is not None:
            comment = self.build_comment(row)
        return comment

    def build_comment(self, row):
        comment = Comment(
            _id=row['id'],
            author_id=row['author_id'],
            author=row['author_name'],
            subreddit_id=row['subreddit_id'],
            subreddit=row['subreddit_name'],
            score=row['score'],
            creation_date=row['creation_date'],
            text=row['text'],
            date_added=row['date_added'],
            parent_comment=row['parent_comment']
        )
        return comment

    def add_comment(self, comment):
        c = self.get_cursor()
        try:
            sql = "INSERT INTO comments (author_id, author_name, subreddit_id, subreddit_name, score, " \
                  "creation_date, text, parent_comment, date_added) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
            c.execute(sql, (comment.author_id, comment.author_name, comment.subreddit_id, comment.subreddit,
                            comment.score, comment.created, comment.text, comment.parent_comment, time.time()))
            return c.rowcount > 0
        except IntegrityError:
            self.logger.error("Failed to add comment to database", extra={'author': comment.user,
                                                                          'subreddit': comment.subreddit,
                                                                          'post_date': comment.created})
            return False

    def update_comment(self, comment):
        if comment.id is not None:
            c = self.get_cursor()
            try:
                sql = "UPDATE comments SET author_id=?, author_name=?, subreddit_id=?, subreddit_name=?, score=?, " \
                      "creation_date=?, text=?, parent_comment=? WHERE id=?"
                c.execute(sql, (comment.author_id, comment.author, comment.subreddit_id, comment.subreddit,
                                comment.score, comment.created, comment.text, comment.parent_comment, comment.id))
                return c.rowcount > 0
            except IntegrityError:
                self.logger.error("Failed to update comment to database", extra={'author': comment.user,
                                                                                 'subreddit': comment.subreddit,
                                                                                 'post_date': comment.created})

    def delete_comment(self, comment):
        c = self.get_cursor()
        try:
            sql = "DELETE FROM comments WHERE id=?"
            c.execute(sql, (comment.id, ))
            return c.rowcount > 0
        except IntegrityError:
            self.logger.error("Failed to delete comment", extra={'author': comment.author,
                                                                  'subreddit': comment.subreddit,
                                                                  'post_date': comment.created})
