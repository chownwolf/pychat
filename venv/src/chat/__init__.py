class ChatRoom:
    def __init__(self):
        self.users = []
        self.messages = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def send_message(self, user, message):
        self.messages.append((user, message))

    def get_messages(self):
        return self.messages