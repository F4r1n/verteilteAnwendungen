class User:
    def __init__(self, name, password, chatList):
        self.name = name
        self.password = password
        self.chatList = chatList

    def introduce(self):
        print("Hello my name is " + self.name)
