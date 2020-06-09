
#Funcion calcula secuencia de collatz
def secuencia_collatz(N):
	lista_secuencia = []			#lista que contendra la secuemcia
	lista_secuencia.append(int(N))
	while N > 1:				#mientras n sea mayor a 1
		if N%2 ==0:			#Si n es par N es igual a n/2
			N=N/2
		else:
			N=3*N+1			#Cuando N es impar
		lista_secuencia.append(int(N))	#Agregamos el nuevo N a la lista
	return lista_secuencia			#Retorna la lista de la secuencia

ultimos_digitos_carne = 114

#Secuencia de Collitz para ciertos numeros
def calcular_secuencias(tope):
	archivito = open('collatz.txt','w+')	#Creo archivo de collatz.txt
	for i in range (2,tope+1):		#Desde 2 hasta tope +1
						#Es excluyente del segundo numero
		archivito.write(str(secuencia_collatz(i))) #Escribo en el archivo la lista de i
		archivito.write('/n')		#Salto de linea para que se vea mas oordenado

calcular_secuencias(ultimos_digitos_carne)	#Llamo la funcion
