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

      print("%s joined the room. Current users: %s" % (user.name, str(self.userList)))

  def sendMessage(self, message, user):
      from chatMessage import ChatMessage

      message = ChatMessage(message, user.name)
      message.print()
      self.chatMessages.append(message)
