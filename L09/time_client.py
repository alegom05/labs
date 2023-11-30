import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345
CLIENT_BUFFER = 1024

if __name__ == '__main__':

    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = (SERVER_HOST, SERVER_PORT)

    socket_client.connect(server_address)

    # TX
    msg_TX = "get_time"
    data_TX = msg_TX.encode('utf-8')
    socket_client.sendall(data_TX)

    # RX
    data_RX = socket_client.recv(CLIENT_BUFFER)
    print(f"Hora actual del servidor: {data_RX.decode('utf-8')}")

    socket_client.close()