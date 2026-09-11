import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5000))
server.listen(1)

print("Server started")

conn, addr = server.accept()
print("Client connected:", addr)

total_packets = 8
window_size = 4
lost_packet = 2

start = 1

while start <= total_packets:
    end = min(start + window_size - 1, total_packets)

    print("\nSending:", start, "to", end)

    # Send the current window.
    for i in range(start, end + 1):
        if i == lost_packet:
            print("Packet", i, "Lost")
            continue

        print("Sending Packet", i)
        conn.send(str(i).encode())
        time.sleep(0.2)

    # Receive ACKs together.
    ack = conn.recv(1024).decode()
    print("Received:", ack)

    # Selectively retransmit the missing packet.
    if lost_packet >= start and lost_packet <= end:
        print("\nPacket", lost_packet, "was not received")
        print("Retransmitting only Packet", lost_packet)

        conn.send(str(lost_packet).encode())

        ack = conn.recv(1024).decode()
        print("Received:", ack)

        lost_packet = -1

    start = end + 1

conn.close()
server.close()

print("\nAll packets sent successfully")
print("Server closed")
