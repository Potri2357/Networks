# Computer Networks Programs

Python socket programs for learning reliable data transfer protocols.

## Structure

### 1. Stop-and-Wait ARQ — `sw_arq/`
- `server.py` — intentionally withholds ACK 2 once to demonstrate timeout and retransmission.
- `client.py` — waits for ACKs and retransmits packet 2 after a 2-second timeout.

### 2. Sliding Window / Selective Repeat — `sw_sr/`
- `server.py` — sends packets in windows of four and selectively retransmits the configured lost packet.
- `client.py` — receives each window, sends ACKs together, and acknowledges the retransmitted packet.

> Note: `sw_sr` is a simplified classroom implementation of sliding-window selective retransmission, not a full production-grade Selective Repeat or Go-Back-N implementation.

## Running

Open two terminals for each program and run the server first.

### Stop-and-Wait
```bash
cd sw_arq
python server.py
```
In another terminal:
```bash
cd sw_arq
python client.py
```

### Sliding Window
```bash
cd sw_sr
python server.py
```
In another terminal:
```bash
cd sw_sr
python client.py
```

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
