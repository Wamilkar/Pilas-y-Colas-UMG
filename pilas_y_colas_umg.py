from tkinter import *
import queue
import time
import random

ventana1 = Tk()
ventana1.title("pilas y colas UMG")

# Generar un millón de números aleatorios
numeros_ramdom = [random.randint(-10000000, 10000000) for _ in range(1000000)]

#Pila
def pila():
# Insertar los números aleatorios en una pila
    pila = []
    #start_time = time.time()
    for numeros in numeros_ramdom:
        pila.append(numeros)
    #elapsed_time = time.time() - start_time
    #print(f'Tiempo de inserción: {elapsed_time} segundos')

    # Extraer los números aleatorios de la pila
    #start_time = time.time()
    while pila:
        numeros = pila.pop()
        # hacer algo con el número extraído
        print(numeros)
    #elapsed_time = time.time() - start_time
    #print(f'Tiempo de extracción: {elapsed_time} segundos')


#cola
def cola():
    # Insertar los números aleatorios en una cola
    q = queue.Queue()
    #start_time = time.time()
    for numero in numeros_ramdom:
        q.put(numero)
    #elapsed_time = time.time() - start_time
    #print(f'Tiempo de inserción: {elapsed_time} segundos')

    # Extraer los números aleatorios de la cola
    start_time = time.time()
    while not q.empty():
        numero = q.get()
        # hacer algo con el número extraído
        print(numero)
    #elapsed_time = time.time() - start_time
    #print(f'Tiempo de extracción: {elapsed_time} segundos')


btn1 = Button(ventana1, text="Insertar y extraer en un pila", command=pila)
btn1.pack()

btn2 = Button(ventana1, text="Insertar y extraer en una cola", command=cola)
btn2.pack()

ventana1.mainloop()