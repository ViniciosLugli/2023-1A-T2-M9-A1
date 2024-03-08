import unittest
from unittest.mock import patch
from main import watcher, main
from sensor import FakeTemperatureSensor
from publisher import Publisher
from serializer import Serializer
import time


class MainTest(unisttest.TestCase):
    @patch('builtins.print')
    def test_watcher_alarm_below_min(self, mock_print):
        message = {
            "timestamp": "2022-01-01 12:00:00",
            "id": "sensor1",
            "type": "freezer",
            "temperature": -30
        }
        watcher(None, None, message)
        mock_print.assert_called_with("2022-01-01 12:00:00|sensor1: freezer | -30°C [ALARM temperature too LOW]")

    @patch('builtins.print')
    def test_watcher_alarm_above_max(self, mock_print):
        message = {
            "timestamp": "2022-01-01 12:00:00",
            "id": "sensor2",
            "type": "fridge",
            "temperature": 15
        }
        watcher(None, None, message)
        mock_print.assert_called_with("2022-01-01 12:00:00|sensor2: fridge | 15°C [ALARM temperature too HIGH]")

    @patch('builtins.print')
    def test_watcher_no_alarm(self, mock_print):
        message = {
            "timestamp": "2022-01-01 12:00:00",
            "id": "sensor3",
            "type": "freezer",
            "temperature": -20
        }
        watcher(None, None, message)
        mock_print.assert_called_with("2022-01-01 12:00:00|sensor3: freezer | -20°C")

    def test_main(self):
        freezer_sensor = FakeTemperatureSensor("S1", "freezer", -30, -10)
        fridge_sensor = FakeTemperatureSensor("S2", "fridge", -3, 15)

        publisher = Publisher("localhost", 1891, "sensor/temperature")

        serializer = Serializer()

        with patch('time.sleep') as mock_sleep:
            main()

            self.assertEqual(mock_sleep.call_count, 1)
            self.assertEqual(serializer.serialize.call_count, 2)
            self.assertEqual(publisher.publish.call_count, 2)


if __name__ == '__main__':
    unittest.main()
