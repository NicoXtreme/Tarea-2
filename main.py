from calculadora import *

option = input("""
Seleccione una operación
1. Suma 
2. Resta
3. Division
4. Multiplicacion
""")

try:
    option = int(option)
except ValueError:
    print("Valor no válido")
    exit()

if option not in [1, 2, 3, 4]:
    print("Valor no válido")
    exit()

# Solicitar los números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Realizar la operación seleccionada
if option == 1:
    result = suma(num1, num2)
    print("La suma es:", result)
elif option == 2:
    result = resta(num1, num2)
    print("La resta es:", result)
elif option == 3:
    if num2 == 0:
        print("Error: No se puede dividir entre cero.")
    else:
        result = division(num1, num2)
        print("La división es:", result)
elif option == 4:
    result = multiplicacion(num1, num2)
    print("La multiplicación es:", result)
