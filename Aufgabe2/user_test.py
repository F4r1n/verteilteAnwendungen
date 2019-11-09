import sys
import unittest
from Aufgabe2.user import User
from Aufgabe2.chatServer import Chat
import io

class UserTest(unittest.TestCase):
    def test_changePassword(self):
        u1 = User("test", "test123", ["chat1", "chat2"], [])

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.assertFalse(u1.changePassword("wrong", "newPass"))
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "Old password didnt match. Try again!\n")

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.assertTrue(u1.changePassword("test123", "newPass"))
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(),
                         "Password changed.\n")
        self.assertEqual(u1.password, "newPass")
    
    def test_introduce(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        u1 = User("test", "test123", ["chat1", "chat2"], [])
        u1.introduce()
                                       
        sys.stdout = sys.__stdout__                   
        self.assertEqual(capturedOutput.getvalue(), "Hello my name is test\n")

    def test_deleteAccount(self):
        u1 = User("test", "test123", ["chat1", "chat2"], [])
        u1.deleteAccount()

        self.assertEqual(u1.name, "")
        self.assertEqual(u1.password, "")
        self.assertEqual(u1.chatList, [])


    def test_login(self):
        u1 = User("test", "test123", [], [])
        c1 = Chat("chatTest", u1, [], [])
        chatList = [c1]

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.assertFalse(u1.login("wrongPass", []))
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(),
                         "Password incorrect. Try again!\n")

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.assertTrue(u1.login("test123", chatList))
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(),
                         "test successfully logged in and was assigned a random Chat.\ntest joined the room. Current users: ['test']\n")
        self.assertEqual(c1.userList, [u1.name])
        self.assertEqual(u1.chatList, [c1])

    def test_addfriend(self):
        u1 = User("test", "test123", [], [])
        u2 = User("test2", "test123", [], [])

        u1.addFriend(u2)
        self.assertEqual(u1.friends[0], u2.name)
        self.assertEqual(u2.friends[0], u1.name)

    def test_removefriend(self):
        u1 = User("test", "test123", [], [])
        u2 = User("test2", "test123", [], [])

        u1.addFriend(u2)
        self.assertTrue(u1.removeFriend(u2))
        self.assertNotIn(u1.name, u2.friends)
        self.assertNotIn(u2.name, u1.friends)

        self.assertFalse(u1.removeFriend(u2))
