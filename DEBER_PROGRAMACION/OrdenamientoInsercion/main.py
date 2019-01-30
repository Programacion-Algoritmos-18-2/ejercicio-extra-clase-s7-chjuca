from modelado.OrdenamientoInsercion import *			# Importamos los modulos necesarios

valores = [10, 90, 1, 20, 4, 7]							# Creamos un arreglo para ordenarlo

arregloOrden = OrdenamientoInsercion(valores)			# Creamos un Objeto tipo OrdenamientoInsersion y le enviamos como parametro valores

print("Arreglo Desordenado")					# Presesntamos un mensaje en pantalla
print(arregloOrden)								# presentamos el objeto

print("%s\n"%("Arreglo Ordenado"))				# Presesntamos un mensaje en pantalla
arregloOrden.ordenar()							# Llamamos a la funcion ordenar