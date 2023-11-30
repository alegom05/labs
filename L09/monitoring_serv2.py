import socket
import psutil
import datetime

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 50001
SERVER_BUFFER = 1024
N_CLIENTS = 5

def get_system_status():
    cpu_usage = psutil.cpu_percent(interval=1)  # Uso de la CPU en el último segundo
    ram = psutil.virtual_memory()
    return f"Uso del CPU: {cpu_usage}%, Uso de la RAM: {ram.percent}%"

if __name__ == '__main__':

    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = (SERVER_HOST, SERVER_PORT)

    socket_server.bind(server_address)

    socket_server.listen(N_CLIENTS)

    print(f"Servicio de monitoreo escuchando en {server_address[0]}:{server_address[1]}")

    while (1):

        client_conn, client_addr = socket_server.accept()

        try:

            while(1):
                data_RX = client_conn.recv(SERVER_BUFFER) 

                if data_RX:
                    msg_RX = data_RX.decode('utf-8')
                    if msg_RX == 'get_status':
                        system_status = get_system_status()
                        client_conn.send(system_status.encode('utf-8'))
                    else:
                        client_conn.send("Comando no válido".encode('utf-8'))

                else:
                    break

        except KeyboardInterrupt:
             print("Servidor cerrado manualmente por el usuario...")