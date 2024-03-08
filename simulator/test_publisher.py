import unittest
from unittest.mock import MagicMock
from publisher import Publisher


class PublisherTest(unittest.TestCase):
    def setUp(self):
        self.broker = "localhost"
        self.port = 1891
        self.topic = "sensor/temperature"
        self.publisher = Publisher(self.broker, self.port, self.topic)
        self.publisher.client = MagicMock()

    def test_publish(self):
        message = "test_message"
        self.publisher.publish(message)
        self.publisher.client.publish.assert_called_once_with(self.topic, message)
        print("Test publish passed")

    def test_disconnect(self):
        self.publisher.disconnect()
        self.publisher.client.disconnect.assert_called_once()
        print("Test disconnect passed")


if __name__ == '__main__':
    unittest.main()
