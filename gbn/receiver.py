import socket

HOST = "127.0.0.1"
PORT = 5000

receiver = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

receiver.bind((HOST, PORT))

print("======================================")
print("        GO-BACK-N RECEIVER")
print("======================================")
print(f"Listening on {HOST}:{PORT}")
print("Waiting for packets...\n")

expected_packet = 1
received_packets = {}
ack2_lost = False
retransmission_started = False

while True:
    data, sender_address = receiver.recvfrom(1024)

    packet = data.decode()
    sequence_number, message = packet.split("|", 1)
    sequence_number = int(sequence_number)

    print("--------------------------------------")
    print(f"Received Packet {sequence_number}")
    print(f"Message: {message}")

    if not retransmission_started:
        if sequence_number == expected_packet:
            received_packets[sequence_number] = message

            print(f"Packet {sequence_number} accepted.")

            if sequence_number == 2 and not ack2_lost:
                print("ACK 2 intentionally lost!")
                ack2_lost = True
            else:
                ack = f"ACK|{sequence_number}"

                receiver.sendto(
                    ack.encode(),
                    sender_address
                )

                print(f"ACK {sequence_number} sent.")

            expected_packet += 1

        else:
            print(
                f"Packet {sequence_number} received, "
                f"but expected Packet {expected_packet}."
            )

            received_packets[sequence_number] = message

            ack = f"ACK|{sequence_number}"

            receiver.sendto(
                ack.encode(),
                sender_address
            )

            print(f"ACK {sequence_number} sent.")

    else:
        print(
            f"Retransmitted Packet {sequence_number} received."
        )

        received_packets[sequence_number] = message

        ack = f"ACK|{sequence_number}"

        receiver.sendto(
            ack.encode(),
            sender_address
        )

        print(f"ACK {sequence_number} sent.")

    if len(received_packets) == 4:
        if (
            ack2_lost
            and sequence_number == 2
            and not retransmission_started
        ):
            retransmission_started = True

            print("\nAll packets are buffered.")
            print("Waiting for retransmitted packets...\n")

            continue

        if retransmission_started:
            print("\n======================================")
            print("All 4 packets received successfully.")
            print("======================================")

            print("\nReceiver displays:")

            for i in range(1, 5):
                print(
                    f"Packet {i} -> "
                    f"{received_packets[i]}"
                )

            print("\nReceiver finished.")
            break

receiver.close()
