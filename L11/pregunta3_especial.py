import time as t
import asyncio as a
import random

def buscar(x):
    with open('players.csv',"r") as archivo:
        cont=archivo.read()#1. Leyendo archivo players.csv
    lines=cont.split("\n")
    segunda_linea=lines[x].strip()
    campos=segunda_linea.split(";")
    a=campos[0]
    b=campos[1]
    l=[a,b,0]
    return l

magnus=buscar(1)#cada nombre es un arreglo con el nombre y el puntaje asignado
vladimir=buscar(2)
peter=buscar(3)
levon=buscar(4)
boris=buscar(5)
alexander=buscar(6)

print(magnus)

def ronda(a,b):
    if a[1]>b[1]:
        a[2]+=1
    else:
        b[2]+=1

def rondaf(a,b):#ronda final
    c=random.randint(0,2)
    if c==0:
        a[2]+=1
    elif c==1:
        a[2]+=0.5
        b[2]+=0.5
    else:
        b[2]=1

async def rondaa(a,b):
    if a[1]>b[1]:
        a[2]+=1
    else:
        b[2]+=1

def fase_rondas_sync():
    ronda11 = ronda(magnus,vladimir)
    t.sleep(0.15)
    ronda12 = ronda(alexander,peter)
    t.sleep(0.15)
    ronda13 = ronda(levon,boris)
    t.sleep(0.15)

    ronda21 = ronda(magnus,vladimir)
    t.sleep(0.15)
    ronda22 = ronda(alexander,peter)
    t.sleep(0.15)
    ronda23 = ronda(levon,boris)
    t.sleep(0.15)

    ronda31 = ronda(boris,magnus)
    t.sleep(0.15)
    ronda32 = ronda(peter,levon)
    t.sleep(0.15)
    ronda33 = ronda(vladimir,alexander)
    t.sleep(0.15)

    ronda41 = ronda(magnus,alexander)
    t.sleep(0.15)
    ronda42 = ronda(levon,vladimir)
    t.sleep(0.15)
    ronda43 = ronda(boris,peter)
    t.sleep(0.15)

    ronda51 = ronda(peter,magnus)
    t.sleep(0.15)
    ronda52 = ronda(vladimir,boris)
    t.sleep(0.15)
    ronda53 = ronda(alexander,levon)
    t.sleep(0.15)

async def ronda1():
    ronda11 = await rondaa(magnus,vladimir)
    await a.sleep(0.15)
    ronda12 = await rondaa(alexander,peter)
    await a.sleep(0.15)
    ronda13 = await rondaa(levon,boris)
    await a.sleep(0.15)

async def ronda2():
    ronda21 = await rondaa(magnus,vladimir)
    await a.sleep(0.15)
    ronda22 = await rondaa(alexander,peter)
    await a.sleep(0.15)
    ronda23 = await rondaa(levon,boris)
    await a.sleep(0.15)

async def ronda3():
    ronda31 = await rondaa(boris,magnus)
    await a.sleep(0.15)
    ronda32 = await rondaa(peter,levon)
    await a.sleep(0.15)
    ronda33 = await rondaa(vladimir,alexander)
    await a.sleep(0.15)

async def ronda4():
    ronda41 = await rondaa(magnus,alexander)
    await a.sleep(0.15)
    ronda42 = await rondaa(levon,vladimir)
    await a.sleep(0.15)
    ronda43 = await rondaa(boris,peter)
    await a.sleep(0.15)

async def ronda5():
     ronda51 = await rondaa(peter,magnus)
     await a.sleep(0.15)
     ronda52 = await rondaa(vladimir,boris)
     await a.sleep(0.15)
     ronda53 = await rondaa(alexander,levon)
     await a.sleep(0.15)

def fase_rondas_async():
    a.run(ronda1())
    a.run(ronda2())
    a.run(ronda3())
    a.run(ronda4())
    a.run(ronda5())

def fase_final_sync(ganador_fase,ganador_anterior):
    ronda1f= rondaf(ganador_fase,ganador_anterior)
    t.sleep(0.15)
    print(ganador_fase,ganador_anterior)
    ronda2f= rondaf(ganador_fase,ganador_anterior)
    t.sleep(0.15)
    print(ganador_fase,ganador_anterior)
    ronda3f= rondaf(ganador_fase,ganador_anterior)
    t.sleep(0.15)
    print(ganador_fase,ganador_anterior)
    ronda4f= rondaf(ganador_fase,ganador_anterior)
    t.sleep(0.15)
    print(ganador_fase,ganador_anterior)
    ronda5f= rondaf(ganador_fase,ganador_anterior)
    t.sleep(0.15)
    print(ganador_fase,ganador_anterior)
    ronda6f= rondaf(ganador_fase,ganador_anterior)
    t.sleep(0.15)
    print(ganador_fase,ganador_anterior)
    ronda7f= rondaf(ganador_fase,ganador_anterior)
    t.sleep(0.15)
    print(ganador_fase,ganador_anterior)
    ronda8f= rondaf(ganador_fase,ganador_anterior)
    t.sleep(0.15)
    print(ganador_fase,ganador_anterior)
    ronda9f= rondaf(ganador_fase,ganador_anterior)
    t.sleep(0.15)
    print(ganador_fase,ganador_anterior)
    ronda10f= rondaf(ganador_fase,ganador_anterior)
    t.sleep(0.15)
    print(ganador_fase,ganador_anterior)
    ronda11f= rondaf(ganador_fase,ganador_anterior)
    t.sleep(0.15)
    print(ganador_fase,ganador_anterior)
    ronda12f= rondaf(ganador_fase,ganador_anterior)
    t.sleep(0.15)
    print(ganador_fase,ganador_anterior)

def main():
    fase_rondas_sync()
    print("Puntajes con fase_rondas_sync:")
    print(magnus[2])
    print(vladimir[2])
    print(peter[2])
    print(levon[2])
    print(boris[2])
    print(alexander[2])
    magnus[2]=0#reiniciamos
    vladimir[2]=0
    peter[2]=0
    levon[2]=0
    boris[2]=0
    alexander[2]=0
    fase_rondas_async()
    print("Puntajes con fase_rondas_async:")
    print(magnus[2])
    print(vladimir[2])
    print(peter[2])
    print(levon[2])
    print(boris[2])
    print(alexander[2])
    ganador_fase_rondas = max([magnus, vladimir, alexander, peter, levon, boris], key=lambda x: x[2])
    print(f"Ganador de fase de rondas: {ganador_fase_rondas[0]}")
    #fase final
    ganador_fase_rondas[1]=0
    ganador_fase_rondas[2]=0
    anand=["Anand",0,0]
    campeon_anterior = anand
    print(ganador_fase_rondas)
    print(campeon_anterior)
    fase_final_sync(ganador_fase_rondas,campeon_anterior)
    ganador_fase_final = max([ganador_fase_rondas,campeon_anterior], key=lambda x: x[2])
    print(ganador_fase_rondas)
    print(campeon_anterior)
    print(f"Ganador de fase final: {ganador_fase_final[0]}")

if __name__ == "__main__":
    main()


        