from user import User
from chatMessage import ChatMessage
from chatServer import Chat

u1 = User("Jonas", "test123", [])
u2 = User("Victor", "test321", [])

c1 = Chat("Chat01", u1.name, [], [])
c1.join(u1)
c1.join(u2)
c1.sendMessage("Hey!", u1)
c1.sendMessage("Hi Jonas.", u2)
