import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5000))

packets = [1, 2, 3, 4, 5]

for packet in packets:
    pck = str(packet).encode()
    client.send(pck)

    if packet == 2:
        print("Waiting for ACK 2:")
        client.settimeout(2)

        try:
            ack = client.recv(1024).decode()
            print(ack)

        except socket.timeout:
            print("Timeout for Packet 2")
            print("Retransmitting Packet 2")

            client.send(pck)

            ack = client.recv(1024).decode()
            print(ack)

        client.settimeout(None)

    else:
        ack = client.recv(1024).decode()
        print(ack)

print("\nAll packets successfully transmitted")
client.close()
