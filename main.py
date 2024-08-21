import socket

HOST, PORT = '192.168.0.11', 8888

# this variable stores private ip address of the computer
host = socket.gethostbyname(socket.gethostname())

#socket.socket take as parametes two values: first type of socket eg: internet bluetooth
#and second is stream or datagram first is TCP protocol and second is UDP protocol
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print(listen_socket.getsockname()[:2])
print(f'Serving HTTP on port {PORT} ...')
while True:
    client_connection, client_address = listen_socket.accept()
    request_data = client_connection.recv(1024)
    print(request_data.decode('utf-8'))

    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)
    client_connection.close()
    