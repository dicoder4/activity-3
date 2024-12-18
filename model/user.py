class User:
    def __init__(self, user_id, name, borrowed_books=None):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = borrowed_books if borrowed_books else []

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "borrowed_books": self.borrowed_books
        }

    @staticmethod
    def from_dict(data):
        return User(data["user_id"], data["name"], data["borrowed_books"])
