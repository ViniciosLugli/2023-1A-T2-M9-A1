import paho.mqtt.client as mqtt


class Publisher:
    def __init__(self, broker, port, topic):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "publisher")
        self.client.connect(self.broker, self.port)

    def publish(self, message):
        self.client.publish(self.topic, message)
        print("Message published: ", message)

    def disconnect(self):
        self.client.disconnect()
        print("Disconnected from broker")
