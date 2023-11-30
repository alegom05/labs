import socket
import time

SOCK_BUFFER = 1024


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5001)

    sock.connect(server_address)

    a=input("Ingrese un numero ")

    sock.sendall(a.encode('utf-8'))

    rpta = sock.recv(SOCK_BUFFER)

    print(f"El factorial del numero es: {rpta.decode('utf-8')}")

