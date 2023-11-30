import socket
import time

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000
CLIENT_BUFFER = 1024

def estado_servidor(SERVER_HOST, SERVER_PORT):

    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (SERVER_HOST, SERVER_PORT)
    socket_client.connect(server_address)

    # TX
    msg_TX = "get_status"
    data_TX = msg_TX.encode('utf-8')
    socket_client.sendall(data_TX)

    # RX
    data_RX = socket_client.recv(CLIENT_BUFFER)
    status= data_RX.decode('utf-8')

    socket_client.close()
    return status

if __name__ == '__main__':

    SERVER_HOST1 = '127.0.0.1'
    SERVER_HOST2 = '127.0.0.1'

    SERVER_PORT1 = 50000
    SERVER_PORT2 = 50001

    estado_serv1= estado_servidor(SERVER_HOST1, SERVER_PORT1)
    estado_serv2= estado_servidor(SERVER_HOST2, SERVER_PORT2)

    while(1):

        print(f"Informacion del uso del servidor: {SERVER_HOST1}:{SERVER_PORT1} {estado_serv1}")
        print(f"Informacion del uso del servidor: {SERVER_HOST2}:{SERVER_PORT2} {estado_serv2}")

        time.sleep(5)

