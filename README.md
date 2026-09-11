# Computer Networks Programs

Python socket programs for learning reliable data transfer protocols.

## Structure

### 1. Stop-and-Wait ARQ — `sw_arq/`
- `server.py` — intentionally withholds ACK 2 once to demonstrate timeout and retransmission.
- `client.py` — waits for ACKs and retransmits packet 2 after a 2-second timeout.

### 2. Sliding Window / Selective Repeat — `sw_sr/`
- `server.py` — sends packets in windows of four and selectively retransmits the configured lost packet.
- `client.py` — receives each window, sends ACKs together, and acknowledges the retransmitted packet.

### 3. Go-Back-N ARQ — `gbn/`
- `sender.py` — sends a window of four packets, tracks the base packet, uses a timer, and retransmits from the unacknowledged base packet after timeout.
- `receiver.py` — receives packets using UDP, sends ACKs, and intentionally loses ACK 2 to demonstrate Go-Back-N retransmission.

> Note: `sw_sr` is a simplified classroom implementation of sliding-window selective retransmission, not a full production-grade Selective Repeat implementation.

## Running

Open two terminals for each program and run the sender/server first.

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

### Go-Back-N
```bash
cd gbn
python receiver.py
```
In another terminal:
```bash
cd gbn
python sender.py
```

## Concepts covered

- TCP and UDP sockets
- IPv4 (`AF_INET`)
- `bind()`, `listen()`, `accept()`, `connect()`
- `send()`, `sendto()`, `recv()`, `recvfrom()`
- Encoding and decoding
- ACKs
- Timeout and retransmission
- Stop-and-Wait ARQ
- Sliding Window
- Selective retransmission
- Go-Back-N ARQ
- Sequence numbers and sender window
