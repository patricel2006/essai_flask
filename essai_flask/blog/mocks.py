from flask import abort


class Post():
    """classe qui simule une base de données"""

    POSTS = [
        {'id': 1, 'title': 'First Post', 'content': 'this is my first post'},
        {'id': 2, 'title': 'Second Post', 'content': 'this is my second post'},
        {'id': 3, 'title': 'Third Post', 'content': 'this is my third post'},
    ]

    @classmethod
    def all(cls):
        """Fetch all posts"""
        return cls.POSTS

    @classmethod
    def find(cls, id):
        """Fetch a single post"""
        try:
            return cls.POSTS[int(id) - 1]
        except IndexError:
            abort(404)