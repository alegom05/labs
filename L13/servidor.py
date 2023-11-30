import socket
import time

host = '127.0.0.1'
port = 5001

if __name__=='__main__':


    lavadora =['lavadora',5]
    refrigerador = ['refrigerador', 3]
    aspiradora =['aspiradora',2]
    licuadora =['licuadora', 4]

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0',5001)

    print(f"Iniciando servidor en: {server_address[0]}:{server_address[1]}")
    sock.bind((host, port))

    sock.listen(10)

    print(f"Servidor escuchando en {host}:{port}")

    while True:
        conn, client_address = sock.accept()
        print(f"Conexión entrante desde {client_address}")

        dato=conn.recv(1024).decode('utf-8')
        
        time.sleep(3)

        s=1

        if dato=="lavadora":
            if lavadora[1]>0:
                lavadora[1]-=1
                s=1
            else:
                s=0#stock
        if dato=="refrigerador":
            if refrigerador[1]>0:
                refrigerador[1]-=1
                s=1
            else:
                s=0
        if dato=="aspiradora":
            if aspiradora[1]>0:
                aspiradora[1]-=1
                s=1
            else:
                s=0
        if dato=="licuadora":
            if licuadora[1]>0:
                licuadora[1]-=1
                s=1
            else:
                s=0

        conn.sendall(str(s).encode('utf-8'))

        #try:
        #except KeyboardInterrupt:
        #   print("Interrupción")
        #finally:
        #   conn.close

    #conn.close()


    #envia
    # conn.sendall(codigo.encode('utf-8'))

    #recibe
    # dato=conn.recv(1024).decode('utf-8')