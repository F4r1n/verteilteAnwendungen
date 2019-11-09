class User:
    def __init__(self, name, password, chatList, firendList):
        self.name = name
        self.password = password
        self.chatList = chatList
        self.friends = firendList

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

    def addFriend(self, anotherUser):
        self.friends.append(anotherUser.name)
        anotherUser.friends.append(self.name)


    def removeFriend(self, anotherUser):
        if anotherUser.name in self.friends:
            userIndex = self.friends.index(anotherUser.name)
            self.friends.pop(userIndex)

            selfIndex = anotherUser.friends.index(self.name)
            anotherUser.friends.pop(selfIndex)
            return True
        else:
            return False
