def calcular_el_cuadrado():
    try:
        n = int(input("Ingresa un número entero: "))
        cuadrado = n*n
        print("El cuadrado del numero es: ")
        print(cuadrado)
    except ValueError:
        print("Este numero no es valido.")

def calcular_el_producto():
    try:
        n1 = float(input("Ingresa el primer numero: "))
        n2 = float(input("Ingresa el segundo numero: "))
        producto = n1 * n2
        print("El producto de numero 1 y numero 2 es: ",producto)
    except ValueError:
        print("El numero ingresado al parecer no es valido.")

if __name__ == "__main__":
    calcular_el_cuadrado()  
    calcular_el_producto()  
