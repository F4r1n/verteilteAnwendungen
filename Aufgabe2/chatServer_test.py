import sys
import unittest
import io
from Aufgabe2.chatServer import Chat
from Aufgabe2.chatMessage import ChatMessage
from Aufgabe2.user import User

class ChatServerTest(unittest.TestCase):
    def test_join(self):
        u1 = User("test", "test123", [])
        u2 = User("test2", "test123", [])
        c1 = Chat("Chat01", u1.name, [], [])

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        c1.join(u1)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(),
                         "%s joined the room. Current users: %s\n" % (u1.name, str(c1.userList)))
        self.assertEqual(u1.chatList, [c1])
        self.assertEqual(c1.userList, [u1.name])

        c1.join(u2)
        self.assertEqual(c1.userList, [u1.name, u2.name])

    def test_sendMessage(self):
        u1 = User("test", "test123", [])
        c1 = Chat("Chat01", u1.name, [], [])

        res1 = c1.sendMessage("Hi!", u1)
        self.assertEqual(len(res1), 2)
        self.assertEqual(res1[0].message, "Hi!")
        self.assertEqual(res1[1], 0)
        self.assertEqual(len(c1.chatMessages), 1)
        self.assertEqual(c1.chatMessages[0].message, "Hi!")

        res2 = c1.sendMessage("Are you there?", u1)
        self.assertEqual(len(res2), 2)
        self.assertEqual(res2[0].message, "Are you there?")
        self.assertEqual(res2[1], 1)
        self.assertEqual(len(c1.chatMessages), 2)
        self.assertEqual(c1.chatMessages[1].message, "Are you there?")
         
    def test_removeMessage(self):
        u1 = User("test", "test123", [])
        c1 = Chat("Chat01", u1.name, [], [])

        message1 = c1.sendMessage("Hi!", u1)[0]
        c1.sendMessage("It's me!", u1)

        c1.removeMessage(message1, 0)
        self.assertEqual(len(c1.chatMessages), 1)
        self.assertEqual(c1.chatMessages[0].message, "It's me!")
        self.assertEqual(message1.message, "")

    def test_removeUser(self):
        u1 = User("test", "test123", [])
        c1 = Chat("Chat01", u1.name, [], [])
        c1.join(u1)

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        c1.removeUser(u1)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(),
                         "%s left the room. Current users: %s\n" % (u1.name, str(c1.userList)))
        self.assertNotIn(c1, u1.chatList)
        self.assertNotIn(u1, c1.userList)
