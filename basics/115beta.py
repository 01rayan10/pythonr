import math
v1 = [1, 2, 3]
v2 = [4, 5, 6]
suma = [v1[i] + v2[i] for i in range(3)]
print("Suma:", suma)
resta = [v1[i] - v2[i] for i in range(3)]
print("Resta:", resta)
producto_escalar = sum(v1[i] * v2[i] for i in range(3))
print("Producto escalar:", producto_escalar)
producto_vectorial = [
    v1[1]*v2[2] - v1[2]*v2[1],
    v1[2]*v2[0] - v1[0]*v2[2],
    v1[0]*v2[1] - v1[1]*v2[0]
]
print("Producto vectorial:", producto_vectorial)
longitud_v1 = math.sqrt(v1[0]**2 + v1[1]**2 + v1[2]**2)
longitud_v2 = math.sqrt(v2[0]**2 + v2[1]**2 + v2[2]**2)
print("Longitud v1:", longitud_v1)
print("Longitud v2:", longitud_v2)
coseno = producto_escalar / (longitud_v1 * longitud_v2)
angulo = math.degrees(math.acos(coseno))
print("Ángulo entre ellos:", angulo, "grados")