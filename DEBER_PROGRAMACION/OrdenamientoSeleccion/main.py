from modelado.OrdenamientoSeleccion import *			# Importamos los modulos necesarios
	
valores = [10, 90, 1, 20, 4, 7]					# Creamos un arreglo para ordenarlo

arregloOrden = OrdenamientoSeleccion(valores)	# Creamos un objeto de tipo OrdenamientoSeleccion
	
print("Arreglo Desordenado")		# presentamos el arreglo desordenado
print(arregloOrden)

print("%s\n"%("Arreglo Ordenado"))	# Presentamos un arreglo ordenado llamando a la funcion ordenar
arregloOrden.ordenar()