class OrdenamientoInsercion(object):				# Creamos una clase OrdenamientoInsercion

	def __init__(self, datos):				# Constructor de la Clase
		self.datos = datos


	def ordenar(self):					# Metodo Ordenar

		for siguiente in range(1, len(self.datos)):			# ciclo que va de 1 a elementos en el arreglo datos
			
			insercion = self.datos[siguiente]				# Insercion toma el valor de datos en la posicion siguiente
			moverElemento = siguiente						# moverElemento toma el valor de siguiente

			while(moverElemento > 0 and self.datos[moverElemento -1] > insercion):	# ciclo While
				self.datos[moverElemento] = self.datos[moverElemento - 1]			# datos en la posicion moverElemento es igual a datos en la posicion moverElemento-1
				moverElemento = moverElemento - 1;				# moverElemento toma el valor de moverElemento-1

			self.datos[moverElemento] = insercion   			#daros en la posicion moverElemento toma el valor de insercion

			print(self.__str__())				# Presentamos el metodo __str__

	def imprimirpasada(self,pasada,indice):							# Metodo imprimirpasada
		print("Despues de pasada %2d: "%(pasada))					# presenta un mensaje en pantalla

		for i in range(0,indice):							# ciclo que va de q a indice
			print(self.datos[i]+" ")			# Presentamos datos en la posicion i
		print(self.datos+ "* ")

		for i in range(indice+1,len(self.datos)):	# ciclo que va desde indice +1 hasta cantidad de elementos en datos
			print(self.datos[i]+ " ")			# Presentamos un mesaje
		print("\n")
		
		for i in range(0,pasada):
			print("-- ")	
		print("\n")


	def __str__(self):			# Metodo __str__

		temporal = " "			# creamos una string vacia

		for elemento in self.datos:		# For que recorrera el arreglo datos
			temporal = ("%s %d"%(temporal, elemento))		# tamporal toma el valor de temporal + elemento

		temporal = ("%s %s"%(temporal, "\n"))				# se aumenta un salto de linea

		return temporal		# se devuelve temporal