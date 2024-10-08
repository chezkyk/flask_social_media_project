class Company:
    def __init__(self, name: str, catch_phrase: str, bs: str):
        self.name = name
        self.catch_phrase = catch_phrase
        self.bs = bs

    def to_dict(self):
        return {
            'name': self.name,
            'catch_phrase': self.catch_phrase,
            'bs': self.bs
        }