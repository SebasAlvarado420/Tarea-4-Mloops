def saludo_personalizado():
    nombre = input("¡Hola! ¿Cómo te llamas? ")
    saludo = f"¡Encantado de conocerte, {nombre}! Bienvenido a nuestro programa."
    print(saludo)

def main():
    saludo_personalizado()

if __name__ == "__main__":
    main()


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

