#PREGUNTA 2. CON HILOS

import time
import requests
from concurrent.futures import ThreadPoolExecutor
import statistics


def obtener_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
    return response


if __name__=='__main__':

    urls = [
    "https://www.wikipedia.org/",
    "https://www.nytimes.com/",
    "https://www.bbc.com/",
    "https://www.python.org/",
    "https://www.reddit.com/",
    "https://www.instagram.com/",
    "https://www.twitter.com/",
    "https://www.cnn.com/",
    "https://www.github.com/",
    "https://www.spotify.com/",
    ]

def descarga(url,n) -> bool:
    response = requests.get(url)

    if response.status_code != 200:
        return False
    
    with open(f'./images2/{n+1}.html', 'wb') as f:
        f.write(response.content)
    
    return True

if __name__ == "__main__":

    # inicio = time.perf_counter()
   
    # for url1 in urls:
    #     descarga(url1,10)

    # inicio2=time.perf_counter()

    tiempos=[]
    s=0

    for i in range(5):

        workers = 3
        inicio2 = time.perf_counter()
        with ThreadPoolExecutor(max_workers=workers) as executor:
            for i, url in enumerate(urls):
                executor.submit(descarga, url, i)
        fin = time.perf_counter()

        tiempos.append(fin-inicio2)


    me=statistics.median(tiempos)

    # print(f"El tiempo de ejecución sincrónico es {inicio2-inicio}")
    print(f"El tiempo de ejecución con hilos es {me} s")
