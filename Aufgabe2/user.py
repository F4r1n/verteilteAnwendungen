class User:
    def __init__(self, name, password, chatList):
        self.name = name
        self.password = password
        self.chatList = chatList

    def introduce(self):
        print("Hello my name is " + self.name)

    def deleteAccount(self):
        self.name = ""
        self.password = ""
        self.chatList = []

    def changePassword(self, oldPass, newPass):
        if oldPass == self.password:
            self.password = newPass
            print("Password changed.")
            return True
        else:
            print("Old password didnt match. Try again!")
            return False

    def login(self, password, allChats):
        import random
        if self.password == password:
            randChat = random.choice(allChats)
            print("%s successfully logged in and was assigned a random Chat." % self.name)
            randChat.join(self)
            return True
        else:
            print("Password incorrect. Try again!")
            return False
