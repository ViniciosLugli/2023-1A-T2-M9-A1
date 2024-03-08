from alarm import Alarm
from subscriber import Subscriber
import json

freezer_alarm = Alarm("freezer", -25, -15)
fridge_alarm = Alarm("fridge", 2, 10)


alarm_vault = {
    "freezer": freezer_alarm,
    "fridge": fridge_alarm
}


def watcher(client, userdata, message):
    json_message = json.loads(message.payload)
    output = f'{json_message["timestamp"]}|{json_message["id"]}: {json_message["type"]} | {json_message["temperature"]}°C'

    alarm = alarm_vault[json_message["type"]].check(json_message["temperature"])

    if alarm != 0:
        output += " [ALARM temperature"
        if alarm == 1:
            output += " too HIGH]"
        else:
            output += " too LOW]"
    print(output)


def main():
    subscriber = Subscriber("localhost", 1891, "sensor/temperature", watcher)
    subscriber.listen()


if __name__ == "__main__":
    main()
