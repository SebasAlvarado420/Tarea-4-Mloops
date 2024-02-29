def saludo_personalizado():
    nombre = input("¡Hola! ¿Cómo te llamas? ")
    saludo = f"¡Encantado de conocerte, {nombre}! Bienvenido a nuestro programa."
    print(saludo)

def main():
    saludo_personalizado()

if __name__ == "__main__":
    main()

