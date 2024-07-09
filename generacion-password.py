import random
from werkzeug.security import generate_password_hash

# Definir los caracteres para la base de contraseñas
minus = "abcdefghijklmnopqrseuvwxyz"
mayus = minus.upper()
numeros = "0123456789"
simbolos = "@()[]{}*,;/-_¿?¡!$<#>&+%"
base = minus + mayus + numeros + simbolos

# Definir la longitud de la contraseña
longitud = 12

# Generar y encriptar 10 contraseñas
for _ in range(10):
    muestra = random.sample(base, longitud)
    password = "".join(muestra)
    password_encriptado = generate_password_hash(password)
    print("{} => {}".format(password, password_encriptado))

