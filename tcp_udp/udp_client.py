import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 6000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

roll_no = input("Enter your Roll Number: ")
client.sendto(roll_no.encode(), (SERVER_HOST, SERVER_PORT))

response, addr = client.recvfrom(1024)
print("\n" + response.decode())

client.close()
