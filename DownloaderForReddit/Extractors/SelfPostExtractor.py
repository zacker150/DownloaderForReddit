from bs4 import BeautifulSoup

from ..Extractors.BaseExtractor import BaseExtractor
from ..Utils.RedditUtils import convert_post


class SelfPostExtractor(BaseExtractor):

    def __init__(self, praw_post, reddit_object, content_display_only=False):
        super().__init__(praw_post, reddit_object, content_display_only)
        self.praw_post = praw_post

    def extract_content(self):
        if self.settings_manager.extract_self_posts:
            post = convert_post(self.praw_post, self.reddit_object)
            self.reddit_object.new_posts.append(post)
            if self.settings_manager.extract_links_from_text_posts:
                self.extract_links_from_text(post)

    def extract_links_from_text(self, post):
        pass
        # TODO: figure out how to extract links from text posts.  To be extracted in current system, links must be urls
        #   found in Praw.Post objects.  This obviously will not work in this case.  Extractor may need to be re-written
