import socket
import time

SOCK_BUFFER = 1024

def factorial(x):
    f=1
    for i in range (1,x+1):
        f=f*i
    return f

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', 5001)

    sock.bind(server_address)
    sock.listen(1)

    while True:
        try:
            conn, client_address = sock.accept()
            dato = conn.recv(SOCK_BUFFER)
            dato = dato.decode('utf-8')
            print(f"Recibi {dato}")
            dato = int(dato)
            fact = factorial(dato)
            conn.sendall(str(fact).encode('utf-8'))
        except ConnectionResetError:
                print("El cliente cerro la conexion de manera abrupta")
        finally:
            conn.close()
            fin_conexion = time.perf_counter()
            print("Cerrando la conexion")