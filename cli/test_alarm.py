import unittest
from alarm import Alarm


class AlarmTest(unittest.TestCase):
    def test_check_below_min(self):
        alarm = Alarm("temperature", 20, 30)
        result = alarm.check(15)
        self.assertEqual(result, -1)

    def test_check_above_max(self):
        alarm = Alarm("temperature", 20, 30)
        result = alarm.check(35)
        self.assertEqual(result, 1)

    def test_check_within_range(self):
        alarm = Alarm("temperature", 20, 30)
        result = alarm.check(25)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
