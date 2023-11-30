import random

def funcion(num_muestras_circulo1, num_muestras_totales1):
    area_circulo=(num_muestras_circulo1/num_muestras_totales1)*4
    pi_aprox1=area_circulo
    return pi_aprox1

num_muestras_totales=10_000_000
cont=0
for i in range (num_muestras_totales):
    a=random.uniform(-1,1)
    b=random.uniform(-1,1)
    if (a**2+b**2)**0.5<1:
        cont+=1
pi_aprox=funcion(cont, num_muestras_totales)

print(f"El valor de pi aproximado es {pi_aprox}")