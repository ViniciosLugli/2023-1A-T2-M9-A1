import unittest
import json
from serializer import Serializer


class SerializerTest(unittest.TestCase):
    def test_serialize(self):
        _id = 1
        _type = "temperature"
        temperature = 25
        timestamp = "2022-01-01 12:00:00"

        expected_result = json.dumps({
            "id": _id,
            "type": _type,
            "temperature": temperature,
            "timestamp": timestamp
        })

        result = Serializer.serialize(_id, _type, temperature, timestamp)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
