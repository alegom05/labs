import socket
import datetime

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345
SERVER_BUFFER = 1024
N_CLIENTS = 5


if __name__ == '__main__':

    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = (SERVER_HOST, SERVER_PORT)

    socket_server.bind(server_address)

    socket_server.listen(N_CLIENTS)

    print(f"Servidor de tiempo escuchando en {server_address[0]}: {server_address[1]}")

    while (1):

        client_conn, client_addr = socket_server.accept()

        try:
            print(f"Conexión entrante desde ({client_addr[0]}', {client_addr[1]})")

            while(1):
                data_RX = client_conn.recv(SERVER_BUFFER) 

                if data_RX:
                    msg_RX = data_RX.decode('utf-8')
                    if msg_RX == 'get_time':
                        current_time = datetime.datetime.now().strftime('%a %b %d %H:%M:%S %Y')
                        client_conn.send(current_time.encode('utf-8'))
                    else:
                        client_conn.send("Comando no válido".encode('utf-8'))

                else:
                    break

        except KeyboardInterrupt:
            print("Servidor cerrado manualmente por el usuario...")
            #socket_server.close()
