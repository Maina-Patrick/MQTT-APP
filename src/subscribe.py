import random

from paho.mqtt import client as mqtt_client

# Setting up the MQTT broker details
broker = 'broker.emqx.io'
port = 1883
topic = "university/ip"

# Generate a Client ID with the subscribe prefix.
client_id = f'subscribe-{random.randint(0, 100)}'

# Callback when connected to the broker
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

# Callback when subscribed to the broker
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message

# Coonecting and subscribing to the broker
def run():
    client = connect_mqtt()
    client.loop_start()
    subscribe(client)
    #client.loop_stop()
    client.loop_forever()


if __name__ == '__main__':
    run()
