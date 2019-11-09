import sys
import unittest
from Aufgabe2.chatMessage import ChatMessage
import io


class ChatMessageTest(unittest.TestCase):
    def test_delete(self):
        m1 = ChatMessage("HI. It's me - a test!", "test")

        m1.delete()
        self.assertEqual("", m1.message)

    def test_print(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        m1 = ChatMessage("HI. It's me - a test!", "test")
        m1.print()

        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "%s: \"%s\" sent by %s\n" % (
            m1.time, m1.message, m1.sender))
