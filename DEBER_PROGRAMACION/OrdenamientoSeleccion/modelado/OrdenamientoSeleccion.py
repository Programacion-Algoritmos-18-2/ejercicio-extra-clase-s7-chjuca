class OrdenamientoSeleccion(object):				# Creamos una clase OrdenamientoSeleccion

	def __init__(self, datos):		# Cosntructor de la clase
		self.datos = datos
	
	def ordenar(self):				# Metodo Ordenar

		for i in range(0,len(self.datos) - 1):		# For que va desde 0 hasta la cantidad de elementos -1  
			masPequenio = i;						# masPequenio toma el valor de i
		
			for indice in range( i + 1, len(self.datos)):			# ciclo qhe va desde i+1 hasta la cantidad de datos 
				if(self.datos[indice] < self.datos[masPequenio]):	# condicion para determinar el menor numero
					masPequenio = indice					# masPequenio toma el valor de indice

			self.intercambiar(i, masPequenio)		# llamamos a la funcion intercambiar y enviamos i y masPequenio

			print(self.__str__())		# presentamos el object


	def intercambiar(self, primero, segundo):		# funcion intercambiar
		temporal = self.datos[primero]				# alacenamos datos en la posicion primero en temporal
		self.datos[primero] = self.datos[segundo]	# Intercambiamos los valores 
		self.datos[segundo] = temporal				# datos segundo es temporal

	def __str__(self):				# metodo __str__ 
		temporal = " "

		for elemento in self.datos:			# Temporar almacenara una cadena cada vez q itere en el for 
			temporal = ("%s %d"%(temporal, elemento))

		temporal = ("%s %s"%(temporal, "\n"))	# un salto de linea
		return temporal				# devlvemos temporal
	