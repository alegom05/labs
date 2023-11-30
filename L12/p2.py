# from urllib.request import urlopen
# url = ''
# with urlopen(url) as page:
# image_data = page.read() # data como objeto binario
import time
from threading import Thread


def descarga(url,n):
    from urllib.request import urlopen
    with urlopen(url) as page:
        with open(f"./descargas/{(n):02d}.png", 'wb') as destino:
            image_data = page.read()
            destino.write(image_data)

def descarga_multiple(urls, n):
    from urllib.request import urlopen
    for i in range(len(urls)):
        with urlopen(urls[i]) as page:
            with open(f"./descargas/{(i+1):02d}.png", 'wb') as destino:
                image_data = page.read()
                destino.write(image_data)

def arreglo_urls(a,b):
    l=[]
    for i in range(a, b+1):
        l.append(f'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/{i:02d}.png')
    return l

urls_totales= arreglo_urls(1,29)
print(urls_totales)
urls_parciales_1= arreglo_urls(1,10)
urls_parciales_2= arreglo_urls(11,20)
urls_parciales_3= arreglo_urls(21,29)
print(urls_parciales_1)

#a. Tiempo de ejecucion, descarga sincrona
tic1=time.perf_counter()
descarga_multiple(urls_totales,29)
toc1=time.perf_counter()

print(f"Descarga sincrona tardo {toc1-tic1}")

# b. Usando 29 hilos sin iterar

inicio21=time.perf_counter()
t1=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/01.png',))
t2=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/02.png',))
t3=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/03.png',))
t4=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/04.png',))
t5=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/05.png',))
t6=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/06.png',))
t7=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/07.png',))
t8=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/08.png',))
t9=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/09.png',))
t10=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/10.png',))
t11=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/11.png',))
t12=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/12.png',))
t13=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/13.png',))
t14=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/14.png',))
t15=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/15.png',))
t16=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/16.png',))
t17=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/17.png',))
t18=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/18.png',))
t19=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/19.png',))
t20=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/20.png',))
t21=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/21.png',))
t22=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/22.png',))
t23=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/23.png',))
t24=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/24.png',))
t25=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/25.png',))
t26=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/26.png',))
t27=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/27.png',))
t28=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/28.png',))
t29=Thread(target=descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/29.png',))

fin21=time.perf_counter()

print(f"Tiempo de ejecucion para 29 hilos sin iterar: {fin21-inicio21} (igual que el anterior)")

#c. Tiempo de ejecucion, descarga usando 3 hilos

def descarga_multiple(urls, n):
    from urllib.request import urlopen
    for i in range(len(urls)):
        with urlopen(urls[i]) as page:
            with open(f"./descargas/{(i+1):02d}.png", 'wb') as destino:
                image_data = page.read()
                destino.write(image_data)

tic3=time.perf_counter()

t31=Thread(target=descarga_multiple, args=(urls_parciales_1,10))
t32=Thread(target=descarga_multiple, args=(urls_parciales_2,10))
t33=Thread(target=descarga_multiple, args=(urls_parciales_3,9))

t31.start()
t32.start()
t33.start()

t31.join()
t32.join()
t33.join()

toc3=time.perf_counter()

print(f"Tiempo de ejecucion con 3 hilos es {toc3-tic3}")

# inicio2=time.perf_counter()
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/01.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/02.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/03.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/04.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/05.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/06.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/07.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/08.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/09.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/10.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/11.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/12.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/13.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/14.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/15.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/16.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/17.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/18.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/19.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/20.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/21.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/22.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/23.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/24.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/25.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/26.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/27.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/28.png')
# descarga('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/29.png')
#     fin=time.perf_counter()

#     print(f"Tiempo de ejecucion: {fin-inicio}")

#a

#b. Con hilos

# tic2=time.perf_counter()

# t1=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/01.png',))
# t2=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/02.png',))
# t3=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/03.png',))
# t4=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/04.png',))
# t5=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/05.png',))
# t6=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/06.png',))
# t7=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/07.png',))
# t8=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/08.png',))
# t9=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/09.png',))
# t10=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/10.png',))
# t11=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/11.png',))
# t12=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/12.png',))
# t13=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/13.png',))
# t14=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/14.png',))
# t15=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/15.png',))
# t16=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/16.png',))
# t17=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/17.png',))
# t18=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/18.png',))
# t19=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/19.png',))
# t20=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/20.png',))
# t21=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/21.png',))
# t22=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/22.png',))
# t23=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/23.png',))
# t24=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/24.png',))
# t25=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/25.png',))
# t26=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/26.png',))
# t27=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/27.png',))
# t28=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/28.png',))
# t29=Thread(descarga,args=('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/29.png',))

# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# t6.start()
# t7.start()
# t8.start()
# t9.start()
# t10.start()
# t11.start()
# t12.start()
# t13.start()
# t14.start()
# t15.start()
# t16.start()
# t17.start()
# t18.start()
# t19.start()
# t20.start()
# t21.start()
# t22.start()
# t23.start()
# t24.start()
# t25.start()
# t26.start()
# t27.start()
# t28.start()
# t29.start()

# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()
# t6.join()
# t7.join()
# t8.join()
# t9.join()
# t10.join()
# t11.join()
# t12.join()
# t13.join()
# t14.join()
# t15.join()
# t16.join()
# t17.join()
# t18.join()
# t19.join()
# t20.join()
# t21.join()
# t22.join()
# t23.join()
# t24.join()
# t25.join()
# t26.join()
# t27.join()
# t28.join()
# t29.join()

# toc2=time.perf_counter()

# print(f"El tiempo de ejecución de un archivo en cada hilo es {toc2-tic2}")

#c. Usando 3 hilos.

    # url1=[]
    # url1.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/01.png')
    # url1.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/02.png')
    # url1.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/03.png')
    # url1.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/04.png')
    # url1.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/05.png')
    # url1.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/06.png')
    # url1.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/07.png')
    # url1.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/08.png')
    # url1.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/09.png')
    # url1.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/10.png')

    # url2=[]
    # url2.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/11.png')
    # url2.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/12.png')
    # url2.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/13.png')
    # url2.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/14.png')
    # url2.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/15.png')
    # url2.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/16.png')
    # url2.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/17.png')
    # url2.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/18.png')
    # url2.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/19.png')
    # url2.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/20.png')

    # url3=[]
    # url3.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/21.png')
    # url3.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/22.png')
    # url3.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/23.png')
    # url3.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/24.png')
    # url3.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/25.png')
    # url3.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/26.png')
    # url3.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/27.png')
    # url3.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/28.png')
    # url3.append('https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/29.png')




    # t1=Thread(target=descarga_multiple, args=(url1,))
    # t2=Thread(target=descarga_multiple, args=(url2,))
    # t3=Thread(target=descarga_multiple, args=(url3,))



