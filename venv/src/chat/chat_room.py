class ChatRoom:
    def __init__(self):
        self.users = []
        self.messages = []

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)

    def send_message(self, user, message):
        if user in self.users:
            self.messages.append((user, message))

    def get_messages(self):
        return self.messages.copy()