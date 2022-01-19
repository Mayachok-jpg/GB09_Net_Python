import json
import unittest
import time

from client import enc_message, dec_message


class ServerTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.test_message = {
                "action": 'presence',
                "time": time.ctime(time.time()),
                "type": "status",
                "user": {
                        "account_name": "C0deMaver1ck",
                        "status": "Yep, I am here!"
                }
        }

        self.answer = {
        "response": 200,
        "alert":"Необязательное сообщение/уведомление",
        "time": time.ctime(time.time()),
        }

    def test_message_type(self):
        result = enc_message('presence')
        print(type(json.dumps(self.test_message)))
        self.assertEqual(type(result), type(json.dumps(self.test_message)))

    def test_answer_type(self):
        result = dec_message(json.dumps(self.answer))
        # print(type(json.loads(self.answer)))
        self.assertEqual(type(result), type((self.answer)))


if __name__ == '__main__':
    unittest.main()
