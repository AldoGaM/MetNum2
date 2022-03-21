import numpy as np
from tabulate import tabulate
import math as m

def interpolacion_newton(n, datos, x, grado, deltas):
    if datos[0][1] < x < datos[1][1]:
        s = (x - datos[0][1]) / (datos[1][1]-datos[0][1])
        pol_x = deltas[0][0]
        print(pol_x)
        for i in range(grado):
            prod_s = s
            for j in range(i):
                prod_s *= s - (j+1)
            pol_x += deltas[i+1][0] * prod_s / m.factorial(i+1)
    else:
        s = (x - datos[n-1][1]) / (datos[1][1]-datos[0][1])
        pol_x = deltas[0][-1]
        for i in range(grado):
            prod_s = s
            for j in range(i):
                prod_s *= s + (j+1)
            pol_x += deltas[i+1][-1] * prod_s / m.factorial(i+1)
    print(f"El resultado de la aproximación a x = {x} con un polinomio de grado {grado} es {pol_x}")

def construir_diferencias(n, datos, grado):
    deltas = []
    deltai = []
    for i in range(n):
        deltai.append(datos[i][2])
    deltas.append(deltai)
    for i in range(grado):
        deltai = []
        for j in range(grado-i):
            deltai.append(deltas[i][j+1] - deltas[i][j])
        deltas.append(deltai)
    return deltas

def construir_tabla(datos, n):
    while True:
        x = float(input("Dame el punto a interpolar: "))
        if not(datos[0][1] < x < datos[n-1][1]):
            print("El valor no se encuentra en el intervalo")
        else:
            grado = int(input("Dame el grado del polinomio: "))
            if grado > n-1:
                print("El grado del polinomio solicitado es mayor que el grado posible")
            else:
                deltas = construir_diferencias(n, datos, grado)
                interpolacion_newton(n, datos, x, grado, deltas)
        resp = input("¿Deseas interpolar a otro punto con la misma tabla (S/N)? ")
        if resp == "n" or resp == "N":
            break

def lectura_datos():
    n = int(input("Dame el número de datos en la tabla: "))
    datos = []
    for i in range(n):
        x = float(input(f"x{i}: "))
        fx = float(input(f"f(x{i}): "))
        datos.append([i, x, fx])
    datos = sorted(datos, key = lambda x: x[1])
    for i in range(n):
        datos[i][0] = i
    while True:
        print("Tabla dada (ordenada)")
        print(tabulate(datos, headers=["i", "xi", "f(xi)"]))
        respuesta = input("¿Quieres modificar algún dato (S/N)? ")
        if respuesta == "N" or respuesta == "n":
            break
        else:
            i = int(input("Dame el índice del dato a modificar: "))
            x = float(input(f"Dame el valor de x{i}: "))
            fx = float(input(f"Dame el valor de f(x{i}): "))
            datos[i] = [i, x, fx]
        datos = sorted(datos, key = lambda x: x[1])
        for i in range(n):
            datos[i][0] = i
    return n, datos

def menu_opciones():
    while True:
        n, datos = lectura_datos()
        construir_tabla(datos, n)
        resp = input("¿Deseas trabajar con otra tabla (S/N)? ")
        if resp == "n" or resp == "N":
            print("Regresando al menú principal")
            break