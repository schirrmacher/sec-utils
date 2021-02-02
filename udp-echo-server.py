import socket
from datetime import datetime
from hexdump import *

PORT = 1319
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(("8.8.8.8", 80))
host = sock.getsockname()[0]
sock.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((host, PORT))

print(f"{host}:{PORT}")

while True:
    data, addr = sock.recvfrom(BUFFER_SIZE)
    print(f"{datetime.now()}")
    hexdump(data)
    print("")