import math

def sumar(v1, v2):
    return [v1[i] + v2[i] for i in range(3)]

def restar(v1, v2):
    return [v1[i] - v2[i] for i in range(3)]

def producto_escalar(v1, v2):
    return sum(v1[i] * v2[i] for i in range(3))

def producto_vectorial(v1, v2):
    x = v1[1]*v2[2] - v1[2]*v2[1]
    y = v1[2]*v2[0] - v1[0]*v2[2]
    z = v1[0]*v2[1] - v1[1]*v2[0]
    return [x, y, z]

def longitud(v):
    return math.sqrt(sum(v[i]**2 for i in range(3)))

def angulo(v1, v2):
    prod_esc = producto_escalar(v1, v2)
    longitudes = longitud(v1) * longitud(v2)
    if longitudes == 0:
        return None
    coseno = prod_esc / longitudes
    coseno = max(min(coseno, 1), -1)
    return math.degrees(math.acos(coseno))

v1 = None
v2 = None
print("\n=== MENÚ DE VECTORES ===")
print("1. Introducir el primer vector")
print("2. Introducir el segundo vector")
print("3. Calcular la suma")
print("4. Calcular la diferencia")
print("5. Calcular el producto escalar")
print("6. Calcular el producto vectorial")
print("7. Calcular el ángulo entre ellos (en grados)")
print("8. Calcular la longitud de ambos")
print("9. Finalizar")

while True:
    opcion = input("Elige una opción: ")
    if opcion == "1":
        v1 = [float(x) for x in input("Escribe x, y, z separados por espacios: ").split()]
    elif opcion == "2":
        v2 = [float(x) for x in input("Escribe x, y, z separados por espacios: ").split()]
    elif opcion == "3":
        if v1 and v2:
            print("Suma:", sumar(v1, v2))
        else:
            print("Primero introduce ambos vectores.")
    elif opcion == "4":
        if v1 and v2:
            print("Diferencia:", restar(v1, v2))
        else:
            print("Primero introduce ambos vectores.")
    elif opcion == "5":
        if v1 and v2:
            print("Producto escalar:", producto_escalar(v1, v2))
        else:
            print("Primero introduce ambos vectores.")
    elif opcion == "6":
        if v1 and v2:
            print("Producto vectorial:", producto_vectorial(v1, v2))
        else:
            print("Primero introduce ambos vectores.")
    elif opcion == "7":
        if v1 and v2:
            ang = angulo(v1, v2)
            if ang is None:
                print("No se puede calcular el ángulo con un vector nulo.")
            else:
                print("Ángulo entre vectores:", ang, "grados")
        else:
            print("Primero introduce ambos vectores.")
    elif opcion == "8":
        if v1:
            print("Longitud del primer vector:", longitud(v1))
        if v2:
            print("Longitud del segundo vector:", longitud(v2))
        if not v1 and not v2:
            print("Introduce al menos un vector.")
    elif opcion == "9":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida. Intenta otra vez.")