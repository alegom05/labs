import socket

host = '127.0.0.1'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((host, port))

server_socket.listen(5)

print(f"Servidor de eco escuchando en {host}:{port}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Conexión entrante desde {client_address}")

    while True:
        data = client_socket.recv(1024)  
        if not data:
            break
        
        message = data.decode()

        print(f"Cliente: {message}")

        client_socket.send(data)

        print(f"Servidor: {message}")

        if message == 'exit':
            break

    client_socket.close()

    if message == "exit":
        break

server_socket.close()

