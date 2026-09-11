import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))

print("Client connected to server")

total_packets = 8
window_size = 4
lost_packet = 2

start = 1

while start <= total_packets:
    end = min(start + window_size - 1, total_packets)

    print("\nReceiving:", start, "to", end)

    acks = ""

    # Receive packets that were sent in the current window.
    for i in range(start, end + 1):
        if i == lost_packet:
            continue

        data = client.recv(1024).decode()
        print("Received Packet:", data)
        acks = acks + "ACK " + data + " "

    # Send all ACKs together.
    print("Sending:", acks)
    client.send(acks.encode())

    # Receive the missing packet after selective retransmission.
    if lost_packet >= start and lost_packet <= end:
        data = client.recv(1024).decode()
        print("Received Retransmitted Packet:", data)

        client.send(("ACK " + data).encode())
        lost_packet = -1

    start = end + 1

client.close()
print("\nAll packets received")
print("Client closed")
