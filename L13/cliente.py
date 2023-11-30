import socket

SOCK_BUFFER = 1024

if __name__ == '__main__':

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5001)

    print(f"Conectando al servidor {server_address[0]}:{server_address[1]}")
    sock.connect(server_address)

    print('Ingrese el nombre de un electrodomestico:')
    nombre=input()

    #envia
    nombre=nombre.encode('utf-8')
    sock.sendall(nombre)

    #recibe
    rpta=sock.recv(SOCK_BUFFER).decode('utf-8')

    print(rpta)

    if rpta=="1":
        msg="Producto en stock. Pedido procesado"
    else:
        msg="Producto agotado. Pedido no procesado"

    print(msg)


    # if not rpta:
    #   break

    # sock.close()

    #convertir a cadena de texto
    # str()
