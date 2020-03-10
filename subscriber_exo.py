# import dan menggunakan library PAHO
import paho.mqtt.client as mqtt

# menggunakan library time
import time

# buat callback pada saat ada pesan masuk


def on_message(client, userdata, message):
    with open("myidol.jpg", "wb") as f:
        f.write(message.payload)
        f.close()
        print("Downloaded")


# mendefinisikan broker address yang akan digunakan
broker_address = "127.0.0.1"

# membuat client P2
print("creating new instance")
client = mqtt.Client("P2")

# koneksi P2 ke broker
print("Connecting to broker")
client.connect(broker_address)

print("Subscribing to topic", "photo")
client.subscribe("photo")

# callback diaktifkan
client.on_message = on_message

# client loop forever
while True:
    client.loop(15)
    time.sleep(2)
