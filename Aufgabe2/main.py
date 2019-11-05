from user import User
from chatMessage import ChatMessage
from chatServer import Chat

allChats = []

#User 1
u1 = User("Jonas", "test123", [])
u1.changePassword("incorrectOldPassword", "newPass")
u1.changePassword("test123", "newPass")

#User 2
u2 = User("Victor", "test321", [])

#Chatroom
c1 = Chat("Chat01", u1.name, [], [])
allChats.append(c1)

#User login
u1.login("newPass", allChats)
#User 2 manually joins chat
c1.join(u2)

#Chatting
c1.sendMessage("Hey!", u1)
c1.sendMessage("Hi Jonas.", u2)

#remove User
c1.removeUser(u1)
c1.removeUser(u2)
