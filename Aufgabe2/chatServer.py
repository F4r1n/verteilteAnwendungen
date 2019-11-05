class Chat:
  def __init__(self, name, user, userList, chatMessages):
    self.name = name
    self.user = user
    self.userList = userList
    self.chatMessages = chatMessages

  def join(self, user):
      userList = self.userList
      userList.append(user.name)
      self.userList = userList
      user.chatList.append(self)

      print("%s joined the room. Current users: %s" % (user.name, str(self.userList)))

  def sendMessage(self, message, user):
      from chatMessage import ChatMessage

      message = ChatMessage(message, user.name)
      message.print()
      self.chatMessages.append(message)

      return self.chatMessages.index(message)

  def removeMessage(self, message, messageIndex):
      self.chatMessages.pop(messageIndex)
      message.delete()

  def removeUser(self, user):
    userIndex = self.userList.index(user.name)
    self.userList.pop(userIndex)
    user.chatList.pop(user.chatList.index(self))

    print("%s left the room. Current users: %s" %
          (user.name, str(self.userList)))
