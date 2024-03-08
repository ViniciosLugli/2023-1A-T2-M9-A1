import unittest
from sensor import FakeTemperatureSensor


class FakeTemperatureSensorTest(unittest.TestCase):
    def test_read_within_range(self):
        sensor = FakeTemperatureSensor(1, "temperature", 20, 30)
        value = sensor.read()
        self.assertGreaterEqual(value, 20)
        self.assertLessEqual(value, 30)

    def test_get_id(self):
        sensor = FakeTemperatureSensor(1, "temperature", 20, 30)
        self.assertEqual(sensor.get_id(), 1)

    def test_get_type(self):
        sensor = FakeTemperatureSensor(1, "temperature", 20, 30)
        self.assertEqual(sensor.get_type(), "temperature")


if __name__ == '__main__':
    unittest.main()
