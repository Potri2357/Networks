import socket
import threading
import csv

HOST = '0.0.0.0'
PORT = 5000


def find_student(roll_no):
    with open('students.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['RollNumber'].upper() == roll_no.upper():
                return row
    return None


def handle_client(conn, addr):
    print("Connected:", addr)
    roll_no = conn.recv(1024).decode()
    student = find_student(roll_no)

    if student:
        response = (
            f"Roll Number: {student['RollNumber']}\n"
            f"Name: {student['Name']}\n"
            f"Department: {student['Department']}\n"
            f"Semester: {student['Semester']}\n"
            f"CGPA: {student['CGPA']}"
        )
    else:
        response = "Student Record Not Found."

    conn.send(response.encode())
    conn.close()
    print("Connection closed:", addr)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print("TCP Server started on port", PORT)

while True:
    conn, addr = server.accept()
    threading.Thread(target=handle_client, args=(conn, addr)).start()
