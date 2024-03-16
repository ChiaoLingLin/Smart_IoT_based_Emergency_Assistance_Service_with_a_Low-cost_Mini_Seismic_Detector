from paho.mqtt import client as mqtt_client
import uuid

class MQTT:
    def __init__(self, host="127.0.0.1", port="1883", username=None, password=None):
        self.HOST = host
        self.PORT = port
        self.client_id = "EQB-" + str(uuid.uuid4())[:6]
        self.client = mqtt_client.Client(self.client_id)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        if username is not None and password is not None:
            self.client.username_pw_set(username, password)
        self.client.connect(self.HOST, int(self.PORT))
    
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    def publish(self, topic, text):   
        msg = f"{text}"
        result = self.client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        #time.sleep(100)

    def on_message(self, client, userdata, msg):
        pass