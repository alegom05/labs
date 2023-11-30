import random
from multiprocessing import Pool

def funcion(num_muestras_circulo1, num_muestras_totales1, area1):
    area_circulo=(num_muestras_circulo1/num_muestras_totales1)*area1
    pi_aprox1=area_circulo
    return pi_aprox1

def funcion_p(area2):
    num_muestras_totales=10_000_000
    cont=0
    for i in range (num_muestras_totales):
        a=random.uniform(0,1)
        b=random.uniform(0,1)
        if (a**2+b**2)**0.5<1:
            cont+=1
    pi_aprox_parcial=funcion(cont,num_muestras_totales,area2)
    return pi_aprox_parcial

if __name__ == '__main__':

    #Usando multiprocessing para llamar a la función_p:
    area=1
    args=[area]*4
    p=Pool(processes=4)
    px=p.map(funcion_p,args)
    p.close()
    p.join()

    s=0
    for i in range (len(px)):
        s=s+px[i]
    print(f"El valor de pi aproximado con multiprocessing es {s}")


