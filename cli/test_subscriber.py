import unittest
from unittest.mock import MagicMock
from subscriber import Subscriber


class SubscriberTest(unittest.TestCase):
    def test_listen(self):
        broker = "localhost"
        port = 1891
        topic = "sensor/temperature"
        callback = MagicMock()
        subscriber = Subscriber(broker, port, topic, callback)

        subscriber.listen()

        callback.assert_called_once()


if __name__ == '__main__':
    unittest.main()
