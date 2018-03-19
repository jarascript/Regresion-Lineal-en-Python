#Las funciones están separadas en 3: pendiente() - interseccion() - pronostico()
#Se explica el desarrollo de cada una, y se ingresan valores de ejemplos para su prueba

def pendiente(n,x,t):
	# Fórmula de la Pendiente es:
	# b = ((n*xiti) - (xi*ti))/((n*ti2)-ti22)
	xiti=0
	xi=0
	ti=0
	ti2=0
	ti22=0
#paso 1: xi*ti
	for i in range(n):
		xiti += x[i]*t[i]

#paso 2: xi
	for i in range(n):
		xi += x[i]

#paso 3: ti
	for i in range(n):
		ti += t[i]

#paso 4: ti^2
	for i in range(n):
		ti2 +=t[i]**2

#paso 5: [ti]^2
	ti22=ti**2

#finalmente, calculamos pendiente:
	b = ((n*xiti) - (xi*ti))/((n*ti2)-ti22)
	return b


def interseccion(n,x,t):
	#Fórmula de la intersección es:
	#a = x_prom - b*t_prom
	xi=0
	x_prom = 0
	ti=0
	b = pendiente(n,x,t) #obtenida de la función anterior

#paso 1: x_prom
	for i in range(n):
		xi += x[i]
	x_prom=xi/n
#paso2: t_prom
	for j in range(n):
		ti +=t[j]
	t_prom = ti/n

#Finalmente, calculamos Intersección:
	a = x_prom - b*t_prom
	return a


def pronostico():
	#La fórmula del Pronóstico está definida por:
	# x(t) = a + b*t_pronostico
	a = interseccion(n,x,t)
	b = pendiente(n,x,t)
	t_pronostico = int(input("Ingrese el periodo que desea pronosticar: \n"))
	pronostico = a + b*t_pronostico
	return pronostico
	
  
#Comienza la ejecución del programa
if __name__ == '__main__':
	n = int(input("Ingrese la cantidad de registros actuales (n): \n"))
	x=[]
	t=[]
	print("Ingrese el valor de las variables (x)")
	for i in range(n):
		valor_x = int(input("Posición {}: \n".format(i)))
		x.append(valor_x) 

	print("Ingrese el valor de las variables (t)")
	for j in range(n):
		valor_t = int(input("Posición{}: \n".format(j)))
		t.append(valor_t) 

	print(n) #número de datos
	print(x) #lista de valores x
	print(t) #lista de valores t

#descomentar las siguientes lineas si se quiere probar con valores de ejemplo para calcular el pronósitco.
	'''n=6
	x=[7000,9000,5000,11000,10000,13000]
	t=[1,2,3,4,5,6]'''
	valor = pronostico()
	print("El valor del pronóstico es: {}".format(valor))
