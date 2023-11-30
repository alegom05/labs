#PREGUNTA2. SINCRONICA
import time
import requests
from concurrent.futures import ThreadPoolExecutor
import statistics

def descarga(url,n) -> bool:
    response = requests.get(url)

    if response.status_code != 200:
        return False

    with open(f'./pages/{n+1}.html', 'wb') as f:
        f.write(response.content)
    
    return True

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
    
    inicio=time.perf_counter()
    for i,url in enumerate(urls):
        descarga(url,i)
    fin=time.perf_counter()

    print(f"Tiempo de ejecucion sincronico {fin-inicio}")

