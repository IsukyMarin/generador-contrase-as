# Solicitar números al usuario
number1 = float(input("Ingresa un número: "))
number2 = float(input("Ingresa otro número: "))

elección = 0

while elección != 6:
    print("""
    Indique la operación a realizar:
    
    1) Suma
    2) Resta
    3) Multiplicación
    4) División
    5) Cambio de valores
    6) Salir
    """)
    
    elección = int(input("Elige una opción: "))
    
    if elección == 1:
        print(" ")
        print("Resultado: ", number1, "+", number2, "=", number1 + number2)
        
    elif elección == 2:
        print(" ")  
        print("Resultado: ", number1, "-", number2, "=", number1 - number2)
        
    elif elección == 3:
        print(" ")
        print("Resultado: ", number1, "*", number2, "=", number1 * number2)
        
    elif elección == 4:
        print(" ")
        if number2 != 0:
            print("Resultado: ", number1, "/", number2, "=", number1 / number2)
        else:
            print("Error: División por cero no permitida.")
        
    elif elección == 5:
        number1 = float(input("Ingresa un número: "))
        number2 = float(input("Ingresa otro número: "))
        
    elif elección == 6:
        print("Gracias por usar la calculadora de Isa :D")
    else:
        print("Opción no válida, por favor elige nuevamente.")
