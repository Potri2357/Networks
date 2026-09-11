# Computer Networks Programs

Python socket programs for learning reliable data transfer protocols.

## Structure

### 01 — Stop-and-Wait ARQ
- `01_stop_and_wait_arq/server.py` — TCP server that intentionally withholds ACK 2 once to demonstrate timeout and retransmission.
- `01_stop_and_wait_arq/client.py` — TCP client that waits for ACKs and retransmits packet 2 after a 2-second timeout.

### 02 — Sliding Window / Selective Repeat Concept
- `02_sliding_window_selective_repeat/server.py` — Sends packets in windows of four and selectively retransmits the configured lost packet.
- `02_sliding_window_selective_repeat/client.py` — Receives each window, sends ACKs together, and acknowledges the retransmitted packet.

> Note: Program 2 demonstrates a simplified classroom implementation of sliding-window selective retransmission. It is not a full production-grade Selective Repeat or Go-Back-N implementation.

## Running

Open two terminals for each program.

### Stop-and-Wait ARQ

Terminal 1:
```bash
python server.py
```

Terminal 2:
```bash
python client.py
```

Run the server first.

### Sliding Window

Terminal 1:
```bash
python server.py
```

Terminal 2:
```bash
python client.py
```

Again, run the server first.

## Concepts covered

- TCP sockets
- IPv4 (`AF_INET`)
- `bind()`, `listen()`, `accept()`, `connect()`
- `send()` and `recv()`
- Encoding and decoding
- ACKs
- Timeout and retransmission
- Stop-and-Wait ARQ
- Sliding Window
- Selective retransmission
