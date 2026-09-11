import socket
import time

HOST = "127.0.0.1"
PORT = 5000

WINDOW_SIZE = 4
TIMEOUT = 3

sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sender.settimeout(0.5)

packets = [
    (1, "Message 1"),
    (2, "Message 2"),
    (3, "Message 3"),
    (4, "Message 4")
]

base = 1
next_sequence_number = 1
timer_start = None

print("======================================")
print("         GO-BACK-N SENDER")
print("======================================")
print(f"Window Size : {WINDOW_SIZE}")
print(f"Timeout     : {TIMEOUT} seconds\n")

print("Sending initial window...\n")

while next_sequence_number <= WINDOW_SIZE:
    sequence_number, message = packets[next_sequence_number - 1]
    packet = f"{sequence_number}|{message}"

    sender.sendto(packet.encode(), (HOST, PORT))

    print(f"Sent Packet {sequence_number} -> {message}")

    if base == next_sequence_number:
        timer_start = time.time()
        print(f"Timer started for Packet {base}")

    next_sequence_number += 1

print("\nAll 4 packets sent.")
print("Waiting for ACKs...\n")

while base <= WINDOW_SIZE:
    try:
        data, receiver_address = sender.recvfrom(1024)
        ack = data.decode()
        ack_type, ack_number = ack.split("|")
        ack_number = int(ack_number)

        print(f"Received ACK {ack_number}")

        if ack_number < base:
            print(f"ACK {ack_number} already processed.")
            continue

        if ack_number == base:
            print(f"Packet {ack_number} acknowledged.")
            base += 1

            if base <= WINDOW_SIZE:
                timer_start = time.time()
                print(f"Timer restarted for Packet {base}")
            else:
                timer_start = None
                print("All packets have been acknowledged.")

        else:
            print(
                f"ACK {ack_number} received, "
                f"but Packet {base} is still unacknowledged."
            )
            print(f"Base remains at Packet {base}.")

    except socket.timeout:
        if timer_start is not None:
            elapsed_time = time.time() - timer_start

            if elapsed_time >= TIMEOUT:
                print("\n======================================")
                print("*** TIMER EXPIRED ***")
                print("======================================")

                print(f"Packet {base} is not acknowledged.")
                print(
                    f"Go-Back-N retransmission "
                    f"starts from Packet {base}.\n"
                )

                for i in range(base, WINDOW_SIZE + 1):
                    sequence_number, message = packets[i - 1]
                    packet = f"{sequence_number}|{message}"

                    sender.sendto(
                        packet.encode(),
                        (HOST, PORT)
                    )

                    print(
                        f"Retransmitted Packet {sequence_number}"
                    )

                print()

                timer_start = time.time()
                print(f"Timer restarted for Packet {base}\n")

print("\n======================================")
print("      TRANSMISSION COMPLETED")
print("======================================")
print("All 4 packets successfully acknowledged.")

sender.close()
