# import library PAHO
import paho.mqtt.client as mqtt

# import library time sebagai waktu
import time

# import library datetime sebagai waktu
import datetime

# import socket
import socket

# def on_message(client, userdata, message):
#     socket_name = socket.gethostname()
#     host_ip = socket.gethostbyname(socket_name)
#     print("Host ip :", host_ip)
#     # print pesan
#     print("History publish : ", str(message.payload.decode("utf-8")))


def on_publish(client, userdata, result):
    # print pesan data terpublish
    print("data published")

    # print ip address publisher
    socket_name = socket.gethostname()
    host_ip = socket.gethostbyname(socket_name)
    print("Host ip :", host_ip)

    # print pesan history
    print("History publish : ", str(result.payload.decode("utf-8")))


# mendefinisikan broker address yang digunakan
broker_address = "127.0.0.1"
# broker_address = "192.168.43.160"

# membuat client bernama P1
print("Creating new instance")
client = mqtt.Client("P1")

# callback diaktifkan
client.on_publish = on_publish

# client terkoneksi ke broker
print("Connecting to broker")
client.connect(broker_address)

# Membuka file
print("read file")
my_file = open("ronaldo.jpg", 'rb')

# membaca semua isi file
my_file_content = my_file.read()

# mengubah file ke dalam bentuk byte menggunakan fungsi byte()
byte_conv = bytes(my_file_content)


# publish dengan topik photo dan data yang dipublish adalah file
print("publish foto")
client.publish("photo", byte_conv)

# publish dengan topik waktu yang dipublish adalah waktu
client.publish("waktu", datetime.datetime.now().strftime("%Y:%m:%D:%H:%M:%S"))

# client loop mulai
client.loop_start()

# Menutup file
print("close file")
my_file.close()

client.loop_stop()
