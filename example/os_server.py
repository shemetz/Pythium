import socket
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("127.0.0.1", 50505))
server.listen(999)

print("---OS server is now up, listening---")

while True:
    conn, addr = server.accept()
    buffer = b''
    msg = "..."
    while msg:
        msg = conn.recv(1024)
        buffer += msg
    data = json.loads(buffer.decode())
    if data["kind"] == "LOG":
        print(data["name"], "-", data["message"])
    elif data["kind"] == "BANISHED":
        print(data["name"], "has been banished from this mortal coil.")
    else:
        print(f"Unrecognized kind of message:", data.get('kind', '<no kind>'))