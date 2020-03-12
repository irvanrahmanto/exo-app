# import dan menggunakan library PAHO
import paho.mqtt.client as mqtt

# menggunakan library time
import time

# import socket
import socket

# buat callback pada saat ada pesan masuk


def on_message(client, userdata, message):
    # print(client)
    socket_name = socket.gethostname()
    host_ip = socket.gethostbyname(socket_name)
    print("Host ip :", host_ip)
    # print("IP : ", )
    # print()
    with open("myidol.jpg", "wb") as f:
        f.write(message.payload)
        # f.write(message)
        f.close()

        print("Success downloaded!")
        print("History subscribe : ", str(message.payload.decode("utf-8")))


# mendefinisikan broker address yang akan digunakan
broker_address = "127.0.0.1"
# broker_address = "192.168.43.160"

# membuat client P2
print("creating new instance")
client = mqtt.Client("P2")

# koneksi P2 ke broker
print("Connecting to broker")
client.connect(broker_address)

print("Subscribing to topic", "photo")
client.subscribe("photo")

# print("Subscribing to topic", "waktu")
client.subscribe("waktu")


# callback diaktifkan
client.on_message = on_message

# client loop forever
while True:
    client.loop(15)
    time.sleep(2)
