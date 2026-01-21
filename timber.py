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
