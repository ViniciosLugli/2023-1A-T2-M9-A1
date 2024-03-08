import random


class FakeTemperatureSensor:
    def __init__(self, _id, _type, _min, _max):
        self._min = _min
        self._max = _max
        self._id = _id
        self._type = _type
        self._current = 0

    def read(self):
        self._current = round(random.uniform(self._min, self._max))
        return self._current

    def get_id(self):
        return self._id

    def get_type(self):
        return self._type
