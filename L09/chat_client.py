import socket

host = '127.0.0.1'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((host, port))

while True:
    message = input("Cliente: ")
    client_socket.send(message.encode())  
    data = client_socket.recv(1024)  
    print(f"Servidor: {data.decode()}")
    if message == 'exit':
            break

client_socket.close()