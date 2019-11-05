import sys
import unittest
from user import User
from chatServer import Chat

class UserTest(unittest.TestCase):
    def test_changePassword(self):
        u1 = User("test", "test123", ["chat1", "chat2"])
        
        self.assertFalse(u1.changePassword("wrong", "newPass"))
        self.assertTrue(u1.changePassword("test123", "newPass"))
        self.assertEqual(u1.password, "newPass")
    
    def test_introduce(self):
        import io

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        u1 = User("test", "test123", ["chat1", "chat2"])
        u1.introduce()
                                       
        sys.stdout = sys.__stdout__                   
        self.assertEqual(capturedOutput.getvalue(), "Hello my name is test\n")

    def test_deleteAccount(self):
        u1 = User("test", "test123", ["chat1", "chat2"])
        u1.deleteAccount()

        self.assertEqual(u1.name, "")
        self.assertEqual(u1.password, "")
        self.assertEqual(u1.chatList, [])


    def test_login(self):
        u1 = User("test", "test123", [])
        c1 = Chat("chatTest", u1, [], [])
        chatList = [c1]

        self.assertFalse(u1.login("wrongPass", []))
        self.assertTrue(u1.login("test123", chatList))
        self.assertEqual(c1.userList, [u1.name])
        self.assertEqual(u1.chatList, [c1])
