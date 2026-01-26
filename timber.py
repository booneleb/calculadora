def suma_numeros():
    n = int(input("¿Cuántos números deseas sumar? "))
    suma = 0
    for i in range(n):
        num = float(input(f"Ingrese el número {i+1}: "))
        suma += num
    print("La suma es:", suma)


def producto_numeros():
    n = int(input("¿Cuántos números deseas multiplicar? "))
    producto = 1
    for i in range(n):
        num = float(input(f"Ingrese el número {i+1}: "))
        producto *= num
    print("El producto es:", producto)

def division():
    a = float(input("Ingrese el dividendo: "))
    b = float(input("Ingrese el divisor: "))
    if b != 0:
        print("El resultado de la división es:", a / b)
    else:
        print("Error: No se puede dividir entre cero")


def factorial():
    n = int(input("Ingrese un número entero positivo: "))
    if n < 0:
        print("El factorial no existe para números negativos")
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        print(f"El factorial de {n} es {fact}")

def multi_table():
    number = input("Insertar un numero (1-10): ")

    if number.isdigit():
        number = int(number)

        if 1 <= number <= 10:
            print(f"\nTabla {number}\n")
            for i in range(1,11):
                print (f"{number} x {i} = {number * i}")
        else:
            print("Insertar un numero (1-10)")
    else:
        print("Entrada no valida.")

def square_cube():
    number = input("Insertar un numero: ")

    if number.isdigit():
        number = int(number)

        square = number**2
        cube = number**3

        print(f"Numero: {number}")
        print(f"Cuadro: {square}")
        print(f"Cubo: {cube}")
    else:
        print("Entrada no valida.")

def promedio():
    suma = 0
    contador = 0
    while True:
        num = float(input("Ingrese un número (-1 para terminar): "))
        if num == -1:
            break
        suma += num
        contador += 1

    if contador > 0:
        print("El promedio es:", suma / contador)
    else:
        print("No se ingresaron números")


def maximo_minimo():
    n = int(input("¿Cuántos números enteros deseas ingresar? "))
    numeros = []

    for i in range(n):
        num = int(input(f"Ingrese el número {i+1}: "))
        numeros.append(num)

    print("Valor máximo:", max(numeros))
    print("Valor mínimo:", min(numeros))
    print("Total de valores ingresados:", len(numeros))

def menu():
    while True:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. Suma de n números")
        print("2. Producto de n números")
        print("3. División entre dos números")
        print("4. Factorial de un número")
        print("5. Tabla de multiplicar")
        print("6. Cuadrado y cubo de un número")
        print("7. Promedio de una serie de números")
        print("8. Máximo y mínimo de n números")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            suma_numeros()
        elif opcion == "2":
            producto_numeros()
        elif opcion == "3":
            division()
        elif opcion == "4":
            factorial()
        elif opcion == "5":
            tabla_multiplicar()
        elif opcion == "6":
            cuadrado_cubo()
        elif opcion == "7":
            promedio()
        elif opcion == "8":
            maximo_minimo()
        elif opcion == "9":
            print("Programa finalizado")
            break
        else:
            print("Opción no válida")


# Ejecutar el programa
menu()
