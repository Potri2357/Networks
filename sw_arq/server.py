import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5000))
server.listen(1)

client, client_addr = server.accept()
print("Connected", client_addr)

buffer = []
packet2lost = False

while True:
    data = client.recv(1024).decode()

    if not data:
        break

    if data not in buffer:
        buffer.append(data)

    pckt = int(data)
    print("Packet Received:", pckt)

    if pckt == 2 and packet2lost is False:
        print("ACK 2 intentionally not sent")
        packet2lost = True
        continue

    ack = "ACK " + str(pckt)
    client.send(ack.encode())

print("BUFFER")

for packet in buffer:
    print("Packet", packet)

client.close()
server.close()
