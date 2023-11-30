import asyncio
import matplotlib.pyplot as plt
import time
import aiofiles

#a. funcion genera_archivos en la carpeta ./original/

def genera_archivos(M,N):
    for i in range(M):
        with open(f"./original/texto{i+1}.txt", "w+") as f:
            cabecera = "a"*N
            cabecera += "\n"
            f.write(cabecera)

genera_archivos(3,1024)

#b. Copia síncrona

def copia_s(n):
    for i in range (n):
        with open(f'./original/texto{i+1}.txt',"r") as archivo:
            with open(f'./copia/texto{i+1}.txt', "w+") as destino:
                cont=archivo.read()
                destino.write(cont)

#c. Copia asíncrona

async def copia_a(n):
    for i in range (n):
        async with aiofiles.open(f'./original/texto{i+1}.txt',"r") as archivo:
            async with aiofiles.open(f'./copia/texto{i+1}.txt', "w+") as destino:
                cont= await archivo.read()
                await destino.write(cont)

inicio=time.perf_counter()
copia_s(3)
inicio2=time.perf_counter()
asyncio.run(copia_a(3))
fin=time.perf_counter()

print(f"El tiempo de ejecucion de la copia sincronica n=3 es {inicio2-inicio}")
print(f"El tiempo de ejecucion de la copia asincronica n=3 es {fin-inicio2}")

#asíncrona tarda más

#d. Gráfica

lista_N = [2**i for i in range(10,26)]
tiempos_sync = []
tiempos_async = []
# Inserte aqui el codigo que haga falta

for N in lista_N:
# Inserte aqui el codigo que haga falta
    genera_archivos(3,N)
    ##modificar
    inicio=time.perf_counter()
    copia_s(3)
    inicio2=time.perf_counter()
    asyncio.run(copia_a(3))
    fin=time.perf_counter()

    tiempo_medido_s=inicio2-inicio
    tiempo_medido_a=fin-inicio2

    tiempos_sync.append((tiempo_medido_s)*1000)
    tiempos_async.append((tiempo_medido_a)*1000)

plt.plot(lista_N,tiempos_sync)
plt.plot(lista_N,tiempos_async)
plt.xlabel('File size [bytes]')
plt.ylabel('Copy time [ms]')
plt.legend(['Sync','Async'])
plt.savefig('SizeVsTime.png')
plt.cla()

#asíncrona es más rápida a mayor número de bytes

#e. M: nro de archivos, N: nro de bytes

N2=2**20

lista_M2=[i for i in range (2,11)]
tiempos_sync = []
tiempos_async = []

for M2 in lista_M2:
    genera_archivos(M2,N2)

    inicio=time.perf_counter()
    copia_s(M2)
    inicio2=time.perf_counter()
    asyncio.run(copia_a(M2))
    fin=time.perf_counter()

    tiempo_medido_s= (inicio2-inicio)*1000
    tiempos_sync.append(tiempo_medido_s)

    tiempo_medido_a= (fin-inicio2)*1000
    tiempos_async.append(tiempo_medido_a)

plt.plot(lista_M2,tiempos_sync)
plt.plot(lista_M2,tiempos_async)
plt.xlabel('File size [bytes]')
plt.ylabel('Copy time [ms]')
plt.legend(['Sync','Async'])
plt.savefig('SizeVsTime2.png')
plt.cla()

#Asíncrona es más rápida a mayor número de archivos.
#La operación se complica cuando hay más de 3 archivos,
#en este caso de 2 a 10, de cada uno 2**10 bytes
#En cambio, el número de bytes no hace más compleja
#la tarea, porque solo se están usando 3 archivos.


