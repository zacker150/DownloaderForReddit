from ..Utils.SystemUtil import epoch_to_str


class Comment:

    def __init__(self, _id=None, author_id=None, author=None, subreddit_id=None, subreddit=None, score=None,
                 creation_date=None, text=None, date_added=None, parent_comment=None, parent_post=None):
        self.id = _id
        self.author_id = author_id
        self.author = author
        self.subreddit_id = subreddit_id
        self.subreddit = subreddit
        self.score = score
        self.created = creation_date
        self.text = text
        self.date_added = date_added

        self.parent_comment = parent_comment
        self.parent_post = parent_post
        self.sub_comments = []
        self.urls = []

    @property
    def date_posted(self):
        return epoch_to_str(self.created)
