import math

# Funcion para Calcular f(x)
def func1( x ):
	return (x**4)*(math.sqrt(3+(2*(x**2)))/3)
  
# Funcion para Calcular f(x)
def func2( x ):
	return (x**5)/pow(((x**2)+4),(1/5))
  
# Funcion para Simpson 1/3
def simpsons1( la, lb, n ):

	# Se calcula h
	h = ( lb - la )/n

	# Tabla de x y f(x)
	x = list()
	fx = list()
	
	# Se calculan valores de x y f(x)
	i = 0
	while i<= n:
		x.append(la + i * h)
		fx.append(func1(x[i]))
		i += 1

	# Para calcular el resultado
	res = 0
	i = 0
	while i<= n:
		if i == 0 or i == n:
			res+= fx[i]
		elif i % 2 != 0:
			res+= 4 * fx[i]
		else:
			res+= 2 * fx[i]
		i+= 1
	res = res * (h / 3)
	return res

# Funcion para Simpson 1/3
def simpsons2( la, lb, n ):

	# Se calcula h
	h = ( lb - la )/n

	# Tabla de x y f(x)
	x = list()
	fx = list()
	
	# Se calculan valores de x y f(x)
	i = 0
	while i<= n:
		x.append(la + i * h)
		fx.append(func2(x[i]))
		i += 1

	# Para calcular el resultado
	res = 0
	i = 0
	while i<= n:
		if i == 0 or i == n:
			res+= fx[i]
		elif i % 2 != 0:
			res+= 4 * fx[i]
		else:
			res+= 2 * fx[i]
		i+= 1
	res = res * (h / 3)
	return res

def menu_opciones():
  op = int(input("""Que integral?: 
1) f(x)= x^4 √(3+2x^2)/3
2) f(x)= x^5/(x^2+4)^(1/5)
"""))
  if op == 1:
    # Driver
    # Limite menor
    a = float(input("Dame el limite menor de la integral: "))
    # Limite mayor
    b = float(input("Dame el limite mayor de la integral: "))
    # Numero de Intevalos
    n = float(input("Dame el numero de Intevalos: "))
    print(f"El resultado es {simpsons1(a, b, n)}")
  elif op == 2:
    # Driver
    # Limite menor
    a = float(input("Dame el limite menor de la integral: "))
    # Limite mayor
    b = float(input("Dame el limite mayor de la integral: "))
    # Numero de Intevalos
    n = float(input("Dame el numero de Intevalos: "))
    print(f"El resultado es {simpsons2(a, b, n)}")