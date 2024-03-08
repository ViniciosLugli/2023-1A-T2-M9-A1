import json


class Serializer:
    @staticmethod
    def serialize(_id, _type, temperature, timestamp):
        return json.dumps({
            "id": _id,
            "type": _type,
            "temperature": temperature,
            "timestamp": timestamp
        })
