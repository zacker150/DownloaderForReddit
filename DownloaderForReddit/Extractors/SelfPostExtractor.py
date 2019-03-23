from ..Extractors.BaseExtractor import BaseExtractor


class SelfPostExtractor(BaseExtractor):

    def __init__(self, post, reddit_object, content_display_only=False):
        super().__init__(post, reddit_object, content_display_only)
