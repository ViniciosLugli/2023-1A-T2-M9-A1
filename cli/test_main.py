import unittest
from unittest.mock import patch
from main import watcher
import json


class Data:
    def __init__(self, payload):
        self.payload = json.dumps(payload)


class MainTest(unittest.TestCase):
    @patch('builtins.print')
    def test_watcher_alarm_below_min(self, mock_print):
        message = Data({
            "timestamp": "2022-01-01 12:00:00",
            "id": "sensor1",
            "type": "freezer",
            "temperature": -30
        })
        watcher(None, None, message)
        mock_print.assert_called_with("2022-01-01 12:00:00|sensor1: freezer | -30°C [ALARM temperature too LOW]")

    @patch('builtins.print')
    def test_watcher_alarm_above_max(self, mock_print):
        message = Data({
            "timestamp": "2022-01-01 12:00:00",
            "id": "sensor2",
            "type": "fridge",
            "temperature": 15
        })
        watcher(None, None, message)
        mock_print.assert_called_with("2022-01-01 12:00:00|sensor2: fridge | 15°C [ALARM temperature too HIGH]")

    @patch('builtins.print')
    def test_watcher_no_alarm(self, mock_print):
        message = Data({
            "timestamp": "2022-01-01 12:00:00",
            "id": "sensor3",
            "type": "freezer",
            "temperature": -20
        })
        watcher(None, None, message)
        mock_print.assert_called_with("2022-01-01 12:00:00|sensor3: freezer | -20°C")


if __name__ == '__main__':
    unittest.main()
