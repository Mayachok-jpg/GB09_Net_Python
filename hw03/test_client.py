import json
import unittest
import time

from client import form_message_to_server


class ClientTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.correct_message = {
            "action": 'presence',
            "time": time.ctime(time.time()),
            "type": "status",
            "user": {
                "account_name": "some_user_name",
                "status": "Yep, I am here!"
            }
        }

    def _get_message_to_server(self, action='presence') -> dict:
        """
        формируем сообщение для сервера.
        :param action: передаём в сообщение метод
        :return: словарь, полученный из JSON-объекта
        """
        message_to_server = form_message_to_server(action)
        return json.loads(message_to_server)

    def test_message_type(self):
        self.assertEqual(type(self._get_message_to_server()), type(self.correct_message))

    def test_forming_message_to_server(self):
        self.assertEqual(self._get_message_to_server()['action'], self.correct_message['action'])
        self.assertAlmostEqual(self._get_message_to_server()['time'], self.correct_message['time'], 3)


if __name__ == "__main__":
    unittest.main()

