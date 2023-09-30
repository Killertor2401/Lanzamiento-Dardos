# Evaluacion #3 Metodos Cuantitativos: Simulador de Dardos

#Se procede a importar las librerias que se van a utilizar en el programa para la ejecucion del mismo

from math import pi
from random import uniform
from tkinter import Tk, Canvas, Button, Label

# Esta función es para calcular el área de un círculo dado el diámetro de el mismo
def areaD(x):
    r = x/2
    a = r*r*pi
    return a

# Esta función funciona para lanzar un dardo aleatorio dentro del tablero de dardos
def throw_dart():
    # Esta funcion genera una coordenada aleatoria dentro del tablero de dardos
    x = uniform(-dT/2, dT/2)
    y = uniform(-dT/2, dT/2)
    # Esta funcion dibuja un punto rojo en el lugar del lanzamiento del dardo
    canvas.create_oval(x+150-2, y+150-2, x+150+2, y+150+2, fill="red")
    # Esto funcion calcula la distancia al centro del tablero de dardos
    distance = (x*2 + y*2)**0.5
    # Esto determina el resultado del lanzamiento del dardo según su distancia
    if distance <= dC/2:
        result = "Centro"
    elif distance <= dT/2:
        if (x > 0 and y > 0) or (x < 0 and y < 0):
            result = "Blanco"
        else:
            result = "Negro"
    else:
        result = "Fuera"
    # Esta funcion muestra el resultado en la etiqueta
    etiqueta.config(text="Resultado: " + result)

# Se le pide al usuario insertar el diámetro del tablero de dardos
while True:
    dT = float(input("Por favor ingrese el diámetro del tablero de dardos:"))
    if dT > 0:
        break
    print("El diámetro del tablero de dardos debe ser mayor a 0")

# Luego se le pide al usuario ingresar el diámetro del centro
while True:
    dC = float(input("Por favor ingrese el diámetro del centro:"))
    if(dC > 0 and dC < dT):
        break 
    print("El diámetro tiene que ser mayor a 0 y menor al diámetro del tablero de dardos")

# Se procede a calcular las probabilidades de donde van a caer los dardos en cada zona del tablero de dardos
pC = 100 * areaD(dC) / areaD(dT)
pBN = (100 - pC) / 2

print("Si se asume que todos los tiros son puntos aleatorios dentro del tablero de dardos, entonces:")
print("La probabilidad de que el dardo caiga en el centro es de " + str(pC) + "%")
print("La probabilidad de que el dardo caiga en la parte blanca del tablero es de: " + str(pBN) + "%. Lo que vendria a ser lo mismo para la parte negra del tablero")

# Esto crea una ventana a traves de la libreria Tkinter
ventana = Tk()
ventana.title("Tablero de lanzamiento de dardos")

# Esto crea un canvas en el cual se dibujara el tablero de dardos
canvas = Canvas(ventana, width=300, height=300)
canvas.pack()

# Se dibuja el círculo exterior del tablero de dardos
canvas.create_oval(0, 0, 300, 300, fill="black")

# Luego se dibuja el círculo interior del tablero de dardos con dos colores alternos uno del otro
canvas.create_arc(150-dT/2, 150-dT/2, 150+dT/2, 150+dT/2, start=45, extent=180, fill="white")
canvas.create_arc(150-dT/2, 150-dT/2, 150+dT/2, 150+dT/2, start=225, extent=180, fill="white")

# Se dibuja el círculo central del tablero de dardos
canvas.create_oval(150-dC/2, 150-dC/2, 150+dC/2, 150+dC/2, fill="red")

# Esto procede a crear un botón para lanzar un dardo al tablero de dardos
boton = Button(ventana, text="Lanzar dardo", command=throw_dart)
boton.pack()

# Luego se crea una etiqueta para mostrar el resultado del lanzamiento al tablero de dardos
etiqueta = Label(ventana, text="Resultado: ")
etiqueta.pack()

# Y para finalizar, se inicia el bucle principal de la ventana
ventana.mainloop()
