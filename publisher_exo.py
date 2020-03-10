# import library PAHO
import paho.mqtt.client as mqtt

# mendefinisikan broker address yang digunakan
broker_address = "127.0.0.1"

# membuat client bernama P1
print("Creating new instance")
client = mqtt.Client("P1")

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

# client loop mulai
client.loop_start()

# Menutup file
print("close file")
my_file.close()
