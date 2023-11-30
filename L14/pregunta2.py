import time
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool
from multiprocessing import Process

"""
Función: calcular_histograma
Entrada: El archivo de la imagen en formato .npy
Salida: El arreglo del histograma
"""
def calcular_histograma(filename_npy):
    # Cargamos la imagen .npy a un arreglo bidimensional
    imagen = np.load(filename_npy)  # La variable imagen viene a ser un arreglo bidimensional como cualquier otro

    #Información útil: Calcular las filas y columnas de la matriz (largo y ancho de la imagen)
    M = len(imagen)     # Número de filas
    N = len(imagen[0])  # Número de columnas

    """
    Escriba aquí su algoritmo para calcular el histograma
    """
    imagen_aplanada=imagen.flatten()

    histograma, bins = np.histogram(imagen_aplanada, bins=256, range=(0, 256))

    graficar_histograma(histograma,f"./histogramas/{filename_npy[11:]}.png",'red')

def calcular_histograma_p(filename_npy):
    # Cargamos la imagen .npy a un arreglo bidimensional
    imagen = np.load(filename_npy)  # La variable imagen viene a ser un arreglo bidimensional como cualquier otro

    #Información útil: Calcular las filas y columnas de la matriz (largo y ancho de la imagen)
    M = len(imagen)     # Número de filas
    N = len(imagen[0])  # Número de columnas

    """
    Escriba aquí su algoritmo para calcular el histograma
    """
    imagen_aplanada=imagen.flatten()

    histograma, bins = np.histogram(imagen_aplanada, bins=256, range=(0, 256))

    graficar_histograma(histograma,f"./histogramas_p/{filename_npy[11:]}.png",'red')
"""
Función: graficar_histograma
Entradas:
- histograma_list: Su histograma que quiere graficar
- filename: Cadena de texto con el nombre del archivo para su gráfico que va a generar. Debe terminar en .png
- color: Cadena de texto con el color en inglés para su gráfico, 
Salida: Genera un gráfico de su histograma en formato .png
"""
def graficar_histograma(histograma_list, filename, color):
    plt.plot(range(0, len(histograma_list)), histograma_list, color=color)
    plt.savefig(filename, bbox_inches='tight')
    plt.close()


if __name__ == '__main__':

    imagenes=[
    './imagenes/goldhill_x2.npy',
    './imagenes/hong kong_x2.npy',
    './imagenes/lena_x2.npy',
    './imagenes/stonehenge_x2.npy'
    ]

    imagenes2=[
    './imagenes/goldhill.npy',
    './imagenes/hong kong.npy',
    './imagenes/lena.npy',
    './imagenes/stonehenge.npy'        
    ]

    imagenes3=[
    ['./imagenes/goldhill_x2.npy'],
    ['./imagenes/hong kong_x2.npy'],
    ['./imagenes/lena_x2.npy'],
    ['./imagenes/stonehenge_x2.npy']
    ]

    imagenes4=[
    './imagenes/goldhill_x2.npy',
    './imagenes/hong kong_x2.npy',
    './imagenes/lena_x2.npy',
    './imagenes/stonehenge_x2.npy'
    ]

    # # Parte a: Calculo del histograma en serial
    inicio=time.perf_counter()
    for imagen in imagenes:
        calcular_histograma(imagen)
    fin=time.perf_counter()
    print(f"Tiempo total en serie: {fin-inicio}")
    # #matrices, numpy

    #Parte b: Calculo del histograma en paralelo
    inicio1=time.perf_counter()
    proc=4
    args=imagenes
    p=Pool(processes=proc)
    p.map(calcular_histograma_p,args)
    p.close()
    p.join()
    fin1=time.perf_counter()
    print(f'Tiempo de ejecucion en paralelo: {fin1-inicio1}')


    #Cálculo del SpeedUp:
    SpeedUP=(fin-inicio)/(fin1-inicio1)
    print(f"SpeedUp:{SpeedUP}")

    ##c: Cálculo del histograma imagenes pequeñas
    inicio3=time.perf_counter()
    for imagen in imagenes2:
        calcular_histograma(imagen)
    fin3=time.perf_counter()
    print(f"Tiempo total en serie de imágenes pequeñas: {fin3-inicio3}")

    # Parte d: Calculo del histograma en paralelo de imagenes pequeñas
    inicio4=time.perf_counter()
    proc=4
    args=[[imagen] for imagen in imagenes2]
    p=Pool(processes=proc)
    p.starmap(calcular_histograma_p,args)
    p.close()
    p.join()
    fin4=time.perf_counter()
    print(f'Tiempo de ejecucion en paralelo de imagenes pequeñas: {fin4-inicio4}')

    # # Calculo del SpeedUp:
    SpeedUP=(fin3-inicio3)/(fin4-inicio4)
    print(f"SpeedUp:{SpeedUP}")

    # Nota: Las gráficas del cálculo de los histogramas en serie y en paralelo deben salir iguales.