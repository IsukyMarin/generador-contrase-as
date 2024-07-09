import random

def adivina_el_numero():
    print("¡Bienvenido al juego de Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100.")
    
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False
    
    while not adivinado:
        intento = int(input("Introduce tu intento: "))
        intentos += 1
        
        if intento < numero_secreto:
            print("El número es mayor.")
        elif intento > numero_secreto:
            print("El número es menor.")
        else:
            adivinado = True
            print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")

if __name__ == "__main__":
    adivina_el_numero()
