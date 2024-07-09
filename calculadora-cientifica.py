import tkinter as tk
from tkinter import messagebox
import math

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora Científica")

# Variable para almacenar la entrada de la calculadora
entrada_texto = tk.StringVar()

# Función para actualizar el contenido del cuadro de texto
def btn_click(item):
    entrada_actual = entrada_texto.get()
    entrada_texto.set(entrada_actual + str(item))

# Función para limpiar el contenido del cuadro de texto
def btn_clear():
    entrada_texto.set("")

# Función para calcular el resultado
def btn_equal():
    try:
        resultado = str(eval(entrada_texto.get()))
        entrada_texto.set(resultado)
    except Exception as e:
        messagebox.showerror("Error", f"Error en la entrada: {str(e)}")

# Funciones científicas
def btn_sin():
    try:
        resultado = str(math.sin(math.radians(float(entrada_texto.get()))))
        entrada_texto.set(resultado)
    except Exception as e:
        messagebox.showerror("Error", f"Error en la entrada: {str(e)}")

def btn_cos():
    try:
        resultado = str(math.cos(math.radians(float(entrada_texto.get()))))
        entrada_texto.set(resultado)
    except Exception as e:
        messagebox.showerror("Error", f"Error en la entrada: {str(e)}")

def btn_tan():
    try:
        resultado = str(math.tan(math.radians(float(entrada_texto.get()))))
        entrada_texto.set(resultado)
    except Exception as e:
        messagebox.showerror("Error", f"Error en la entrada: {str(e)}")

def btn_log():
    try:
        resultado = str(math.log10(float(entrada_texto.get())))
        entrada_texto.set(resultado)
    except Exception as e:
        messagebox.showerror("Error", f"Error en la entrada: {str(e)}")

def btn_sqrt():
    try:
        resultado = str(math.sqrt(float(entrada_texto.get())))
        entrada_texto.set(resultado)
    except Exception as e:
        messagebox.showerror("Error", f"Error en la entrada: {str(e)}")

# Crear la entrada de texto
entrada_frame = tk.Frame(root)
entrada_frame.pack(side=tk.TOP)

entrada = tk.Entry(entrada_frame, font=('arial', 18, 'bold'), textvariable=entrada_texto, width=25, bd=5, insertwidth=4, bg="powder blue", justify='right')
entrada.grid(row=0, column=0)

# Crear los botones
botones_frame = tk.Frame(root)
botones_frame.pack()

# Botones numéricos y de operaciones básicas
botones = [
    '7', '8', '9', '/', 'C',
    '4', '5', '6', '*', 'sqrt',
    '1', '2', '3', '-', 'sin',
    '0', '.', '=', '+', 'cos',
    '(', ')', 'log', 'tan'
]

fila = 0
columna = 0

for boton in botones:
    if boton == "=":
        tk.Button(botones_frame, text=boton, width=10, height=3, command=btn_equal).grid(row=fila, column=columna)
    elif boton == "C":
        tk.Button(botones_frame, text=boton, width=10, height=3, command=btn_clear).grid(row=fila, column=columna)
    elif boton == "sin":
        tk.Button(botones_frame, text=boton, width=10, height=3, command=btn_sin).grid(row=fila, column=columna)
    elif boton == "cos":
        tk.Button(botones_frame, text=boton, width=10, height=3, command=btn_cos).grid(row=fila, column=columna)
    elif boton == "tan":
        tk.Button(botones_frame, text=boton, width=10, height=3, command=btn_tan).grid(row=fila, column=columna)
    elif boton == "log":
        tk.Button(botones_frame, text=boton, width=10, height=3, command=btn_log).grid(row=fila, column=columna)
    elif boton == "sqrt":
        tk.Button(botones_frame, text=boton, width=10, height=3, command=btn_sqrt).grid(row=fila, column=columna)
    else:
        tk.Button(botones_frame, text=boton, width=10, height=3, command=lambda b=boton: btn_click(b)).grid(row=fila, column=columna)
    
    columna += 1
    if columna == 5:
        columna = 0
        fila += 1

# Iniciar la aplicación
root.mainloop()
