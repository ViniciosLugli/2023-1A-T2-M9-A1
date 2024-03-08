import paho.mqtt.client as mqtt


class Subscriber:
    def __init__(self, broker, port, topic, callback):
        self.broker = broker
        self.port = port
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "subscriber")
        self.client.connect(self.broker, self.port)
        self.client.subscribe(topic)
        self.client.on_message = callback

    def listen(self):
        self.client.loop_forever()
