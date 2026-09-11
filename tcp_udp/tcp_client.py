import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_HOST, SERVER_PORT))

roll_no = input("Enter your Roll Number: ")
client.send(roll_no.encode())

response = client.recv(4096).decode()
print("\n" + response)

client.close()
print("\nConnection closed.")
