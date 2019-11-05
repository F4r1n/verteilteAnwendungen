class ChatMessage:
    def __init__(self, message, sender):
        import datetime
        self.message = message
        self.sender = sender
        self.time = datetime.datetime.now()

    def delete(self):
        self.message = ""

    def print(self):
        print("%s: \"%s\" sent by %s" %
              (self.time, self.message, self.sender))
