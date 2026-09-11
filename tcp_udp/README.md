# TCP and UDP Student Record Retrieval

**UCS3511 - Networks Laboratory — Assignment 2**

This directory contains the TCP and UDP client-server programs from the assignment. Both applications retrieve a student record from `students.csv` using a Roll Number. The TCP server creates a new thread for each connected client.

## Files

- `tcp_server.py` — TCP server with multithreading
- `tcp_client.py` — TCP client
- `udp_server.py` — UDP server
- `udp_client.py` — UDP client

## Required CSV

Place `students.csv` in this directory when running the programs. The code expects these column names:

```text
RollNumber,Name,Department,Semester,CGPA
```

## Run TCP

Terminal 1:

```bash
python3 tcp_server.py
```

Terminal 2:

```bash
python3 tcp_client.py
```

TCP uses port `5000`.

## Run UDP

Terminal 1:

```bash
python3 udp_server.py
```

Terminal 2:

```bash
python3 udp_client.py
```

UDP uses port `6000`.

## Concepts covered

- TCP client-server communication
- UDP client-server communication
- Socket programming in Python
- CSV-based student record lookup
- Multithreading in a TCP server
- TCP vs UDP communication
