class Post:
    def __init__(self, user_id: int, post_id: int, title: str, body: str):
        self.user_id = user_id
        self.post_id = post_id
        self.title = title
        self.body = body
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'post_id': self.post_id,
            'title': self.title,
            'body': self.body
        }