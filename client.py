import socket 

HOST = ""
PORT = 8888

socket_listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_listen.connect((HOST,PORT))


socket.send("GOSHARI".encode("utf-8"))
print(socket_listen.recv(1024))