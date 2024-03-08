class Alarm:
    def __init__(self, _type, _min, _max):
        self._type = _type
        self.min = _min
        self.max = _max

    def check(self, value):
        if value < self.min:
            return -1
        elif value > self.max:
            return 1
        else:
            return 0
