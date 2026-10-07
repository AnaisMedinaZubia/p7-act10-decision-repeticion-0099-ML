# Medina Anais NC 0099

# ==========================================
# EJEMPLOS DE CONDICIONES Y CICLOS EN PYTHON
# ==========================================

print("\n\n==========================================")
print("MUJERES - EJEMPLOS")
print("==========================================")


print("\n--- IF: Ejemplo 1 ---")

edad = 20

if edad >= 18:
    print("La mujer es mayor de edad.")


print("\n--- ELIF: Ejemplo 1 ---")

calificacion = 85

if calificacion >= 90:
    print("Calificación excelente.")
elif calificacion >= 80:
    print("La mujer obtuvo una buena calificación.")
else:
    print("Debe mejorar su calificación.")


print("\n--- ELSE: Ejemplo 1 ---")

edad = 16

if edad >= 18:
    print("La mujer puede votar.")
else:
    print("La mujer todavía no puede votar.")


print("\n--- FOR: Ejemplo 1 ---")

for numero in range(1, 6):
    print("Número:", numero)


print("\n--- WHILE: Ejemplo 1 ---")

contador = 1

while contador <= 5:
    print("Contador:", contador)
    contador += 1

print("Medina Anais NC 0099")