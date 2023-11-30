import socket
import numpy as np

#Diccionario de donde se escoge palabras al azar para el juego
dictionary = ["hola", "pucp", "ciclo", "arquitectura", "ingenieria", "servidor", "computadora", "amazon", "peru", "universidad", "jazz"]

SOCK_BUFFER = 1024

if __name__ == '__main__':

    #random_word = "ingenieria"
	#hidden_word = "**********"
	#client_guess = 'i'

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', 5000)
    print(f"Iniciando servidor en: {server_address[0]}:{server_address[1]}")
    sock.bind(server_address)
    sock.listen(1)
    print("Esperando una nueva conexion de un  cliente...")

    while True:
        conn, client_address = sock.accept()
        print(f"...conexion de: ({client_address[0]}:{client_address[1]})")
        try:
            call=conn.recv(1024)
            call=call.decode('utf-8')
            if call == 'start':
                print(f"Recibi comando {call}")

                random_word=np.random.choice(dictionary)
                print(f"Elegida: {random_word}")
                hidden_word='*'*len(random_word)
                conn.send(hidden_word.encode())
                arreglo=list(random_word)

                while(1):
                    letra=conn.recv(1024).decode()
                    print(f"Client guess: {letra}")

                    for idx in range(0, len(random_word)):
                        if arreglo[idx] == letra:
                            hidden_word = hidden_word[:idx] + letra + hidden_word[idx+1:]
                    print("Hidden word: ", hidden_word)
                    
                    for idx in range(len(random_word)):
                            aux=0
                            if arreglo[idx] == letra:
                                aux=1
                                hidden_word = hidden_word[:idx] + letra + hidden_word[idx+1:]
                                arreglo[idx]='*'
                                if hidden_word==random_word:
                                    conn.sendall(f'¡Lo conseguiste! La palabra correcta es: {hidden_word}')
                                break
                            if aux==1:
                                conn.sendall(hidden_word.encode())
                            else:
                                conn.sendall(b'Intento Incorrecto')

        finally:
            conn.close()
            #print("Cerrando la conexion")
