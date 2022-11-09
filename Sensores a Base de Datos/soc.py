from http import server
import socket

HOST = "172.20.10.4"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
s = socket.socket()
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()
print("Connection from: " + str(addr))
while True:
    # receive data stream. it won't accept data packet greater than 1024 bytes
    data = conn.recv(1024).decode()
    if not data:
        # if data is not received break
        break
    print("from connected user: " + str(data))
    data = input(' -> ')
    conn.send(data.encode())  # send data to the client

conn.close()  # close the connection


'''with conn:
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.sendall(data.encode())
        '''