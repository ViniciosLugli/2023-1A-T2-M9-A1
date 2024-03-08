from sensor import FakeTemperatureSensor
from publisher import Publisher
from serializer import Serializer
import time

freezer_sensor = FakeTemperatureSensor("S1", "freezer", -30, -10)
fridge_sensor = FakeTemperatureSensor("S2", "fridge", -3, 15)


def main():
    sensors = [
        freezer_sensor,
        fridge_sensor
    ]

    publisher = Publisher("localhost", 1891, "sensor/temperature")

    while True:
        for sensor in sensors:
            message = Serializer.serialize(sensor.get_id(), sensor.get_type(), sensor.read(), time.strftime("%d/%m/%Y %H:%M:%S"))
            publisher.publish(message)

        time.sleep(1)


if __name__ == "__main__":
    main()
