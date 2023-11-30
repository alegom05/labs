import time
from werkzeug.security import check_password_hash #INSTALE ESTA LIBERIA, tipee en su terminal: pip install Werkzeug
from multiprocessing import Pool

"""
Esta es la contraseña que usted tiene que adivinar. Está encriptada para que no pueda saber cuál es la respuesta correcta a priori.
Lo que tiene que hacer es generar combinaciones de 3 letras y llamar a la función comparar_con_password_correcto(línea 20 de la plantilla)
"""
contrasena_correcta = 'pbkdf2:sha256:260000$rTY0haIFRzP8wDDk$57d9f180198cecb45120b772c1317b561f390d677f3f76e36e0d02ac269ad224'


# Arreglo con las letras del abecedario. Puede serle de ayuda, no es obligatorio que lo use
abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
vocales = ['a','e','i','o','u']
"""
Función que sirve para comparar su palabra(cadena de 3 caracteres) con la contraseña correcta.
Entrada: Su cadena de 3 caracteres
Salida: True(verdadero) si es que coincide con la contraseña correcta, caso contrario retorna False(falso)
"""
def comparar_con_password_correcto(palabra):
	return check_password_hash(contrasena_correcta, palabra)



def contrasena_sync():
	contrasena=''
	for c in abecedario:
		for b in vocales:
			for a in vocales:
				contrasena=a+b+c
				if comparar_con_password_correcto(contrasena):
					print(f"La contraseña es {contrasena}")

def contrasena_async(letra):
	contrasena=''
	a=letra
	for b in vocales:
		for c in abecedario:
			contrasena=a+b+c
			if comparar_con_password_correcto(contrasena):
				print(f"La contraseña es {contrasena}")

if __name__ == "__main__":

	#Sincrónico
	inicio=time.perf_counter()
	contrasena_sync()
	fin=time.perf_counter()
	print(f"Tiempo de ejecución sincrónico {fin-inicio}")

	#Con multiprocessing
	inicio1=time.perf_counter()
	tareas=1
	args=vocales*tareas
	p=Pool(processes=5)
	px=p.map(contrasena_async,args)
	p.close()
	p.join()
	fin1=time.perf_counter()
	print(f"Tiempo de ejecución con multiprocessing {fin1-inicio1}")


