import socket
import csv

HOST = '0.0.0.0'
PORT = 6000


def find_student(roll_no):
    with open('students.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['RollNumber'].upper() == roll_no.upper():
                return row
    return None


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print("UDP Server started on port", PORT)

while True:
    data, addr = server.recvfrom(1024)
    roll_no = data.decode()
    print("Request from", addr, ":", roll_no)

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

    server.sendto(response.encode(), addr)
