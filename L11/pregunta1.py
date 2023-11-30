import random as r
import aiofiles
import asyncio
import time

t_procesamiento_envio=r.randint(10,100)
t_procesamiento_recepcion=r.randint(10,100)
t_ida_vuelta=r.randint(100,300)
t_retardo_prop=r.randint(500,700)


async def lat_sms(t_procesamiento_envio,t_procesamiento_recepcion):
    lat=t_procesamiento_envio+t_procesamiento_recepcion
    lat_r=lat*0.001
    await asyncio.sleep(lat_r)
    print(f"La corrutina de la tecnología SMS tuvo una latencia de {lat} ms")
    return lat

async def lat_3g(t_ida_vuelta,t_procesamiento_recepcion):
    lat=2*(t_ida_vuelta+t_procesamiento_recepcion)
    lat_r=lat*0.001
    await asyncio.sleep(lat_r)
    print(f"La corrutina de la tecnología 3G tuvo una latencia de {lat} ms")
    return lat

async def lat_satelital(t_retardo_prop,t_procesamiento_recepcion):
    lat=2*t_retardo_prop+t_procesamiento_recepcion
    lat_r=lat*0.001
    await asyncio.sleep(lat_r)
    print(f"La corrutina de la tecnología Satelital tuvo una latencia de {lat} ms")
    return lat

async def main():
    await asyncio.gather(lat_sms(t_procesamiento_envio,t_procesamiento_recepcion), lat_3g(t_ida_vuelta,t_procesamiento_recepcion), lat_satelital(t_retardo_prop,t_procesamiento_recepcion))

    a= await lat_sms(t_procesamiento_envio,t_procesamiento_recepcion)
    b= await lat_3g(t_ida_vuelta,t_procesamiento_recepcion)
    c= await lat_satelital(t_retardo_prop,t_procesamiento_recepcion)

    async with aiofiles.open("latencias_sms.csv", "a") as f:
        linea = f"{a},"
        linea += "\n"
        await f.write(linea)

    async with aiofiles.open("latencias_3g.csv", "a") as f:
        linea = f"{b},"
        linea += "\n"
        linea += "este es el codigo"
        await f.write(linea)

    async with aiofiles.open("latencias_satelital.csv", "a") as f:
        linea = f"{c},"
        linea += "\n"
        await f.write(linea)


if __name__=="__main__":
    asyncio.run(main())








