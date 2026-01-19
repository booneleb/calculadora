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