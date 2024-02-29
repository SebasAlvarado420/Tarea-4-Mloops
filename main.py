#Saludo personalizado
def saludo_personalizado():
    nombre = input("¡Hola! ¿Cómo te llamas? ")
    saludo = f"¡Encantado de conocerte, {nombre}! Bienvenido a nuestro programa."
    print(saludo)

def main():
    saludo_personalizado()

if __name__ == "__main__":
    main()

#Contador de numeros
def leer_numero():
    while True:
        entrada_usuario = input("Por favor, ingresa un número entero: ")
        try:
            numero = int(entrada_usuario)
            return numero
        except ValueError:
            print("La entrada no es un número entero válido. Intenta de nuevo.")

def contar_numero(numero):
    for i in range(1, numero + 1):
        print(i)

def main():
    print("Bienvenido al contador de números.")
    numero_usuario = leer_numero()
    print(f"Contando hasta {numero_usuario}:")
    contar_numero(numero_usuario)

if __name__ == "__main__":
    main()

#Calculadora Basica
def calculadora():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    operacion = input("Elija una operación (suma, resta, multiplicación, división): ")

    if operacion == "suma":
        resultado = num1 + num2
    elif operacion == "resta":
        resultado = num1 - num2
    elif operacion == "multiplicación":
        resultado = num1 * num2
    elif operacion == "división":
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("No se puede dividir por cero.")
            return
    else:
        print("Operación no válida.")
        return

    print(f"El resultado es: {resultado}")


if __name__ == "__main__":
    calculadora()

