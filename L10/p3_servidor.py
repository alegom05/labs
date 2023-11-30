import socket

host = '127.0.0.1'
port = 5001

if __name__=='__main__':

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0',5001)

    print(f"Iniciando servidor en: {server_address[0]}:{server_address[1]}")
    sock.bind((host, port))

    sock.listen(5)

    print(f"Servidor de eco escuchando en {host}:{port}")

    while True:
        conn, client_address = sock.accept()
        print(f"Conexión entrante desde {client_address}")

        while True:
            data = conn.recv(1024)  
            data = data.decode('utf-8')
            if not data:
                break

            notas = data.split(",")
            print(notas)

            labs = 0
            pcs = 0

            for i in range(5, 15):
                labs += int(notas[i])
            labs = labs / 10
            for i in range(1, 5):
                pcs += int(notas[i])
            pcs = pcs / 4
            ta = int(notas[15])

            promedio = pcs * 0.5 + labs * 0.25 + ta * 0.25

            print(f"Promedio: {promedio}")

        conn.close()
