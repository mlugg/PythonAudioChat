# Server
import socket
HOST = ""
PORT = 50007
PACKETSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(2)
conn1, addr1 = sock.accept()
conn2, addr2 = sock.accept()
print("Connected the following IPs: " + addr1 + " ," + addr2)
while True:
    from1 = conn1.recv(PACKETSIZE)
    from2 = conn2.recv(PACKETSIZE)
    if (not from1) or (not from2): break
    conn2.sendall(from1)
    conn1.sendall(from2)
conn1.close()
conn2.close()
# Incredibly simplistic - should relay the messages of two client back to the other client. Will stop if wither connection fails or terminates.