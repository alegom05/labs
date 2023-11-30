import socket

SOCK_BUFFER = 1024

def busca_codigo(pos: int) -> str:
    with open("notas.csv", "r") as f:
        contenido = f.read()
    c_lista = contenido.split("\n")
    print("Tengo la lista")

    if pos >= len(c_lista):
        return None
    cod = c_lista[pos]

    return cod

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5001)
    print(f"Conectando al servidor {server_address[0]}:{server_address[1]}")
    sock.connect(server_address)

    try:

        with open("notas.csv", "r") as f:
            contenido = f.read()
            cont = contenido.split("\n")
            print(cont)

            # print(f"Recibimos posicion: {dato}")
            
            codigo = busca_codigo(1)
            #codigo = '\n'.join(cont)
            codigo = codigo.encode('utf-8')
            print(f"mensaje: {codigo}")
            sock.sendall(codigo)

    finally:
        sock.close()

