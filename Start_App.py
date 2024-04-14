from tkinter import *  # Importa todos los elementos de la librería tkinter
from tkinter.ttk import Progressbar  # Importa el widget Progressbar de la sublibrería ttk de tkinter
import sys  # Importa el módulo sys para interactuar con el intérprete de Python
import AccountSystem  # Importa el módulo AccountSystem
import os  # Importa el módulo os para interactuar con el sistema operativo

root = Tk()  # Crea una instancia de la clase Tk(), que representa la ventana principal de la aplicación
root.resizable(0, 0)  # Establece que la ventana no se pueda redimensionar

#==Ventana de carga==================================================================================================================#

# Define las dimensiones y posición de la ventana de carga
width = 550
height = 450
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

root.overrideredirect(1)  # Oculta los bordes de la ventana para dar la apariencia de una ventana modal
root.config(background='#C6D9E3')  # Establece el color de fondo de la ventana

# Crea y posiciona una etiqueta de bienvenida en la ventana
welcome_label = Label(text='BIENVENIDO', bg='#C6D9E3', font=("yu gothic ui", 25, "bold"), fg='black')
welcome_label.place(x=160, y=25)

# Carga una imagen y la muestra en la ventana
image = PhotoImage(file='images\\logo1.png')
bg_label = Label(root, image=image, bg='#C6D9E3')
bg_label.place(x=160, y=105)

# Crea y posiciona una etiqueta de progreso y una barra de progreso en la ventana
progress_label = Label(root, text="Por favor espere...", font=('yu gothic ui', 13, 'bold'), fg='black', bg='#C6D9E3')
progress_label.place(x=190, y=350)
progress = Progressbar(root, orient=HORIZONTAL, length=500, mode='determinate')
progress.place(x=15, y=390)

#===============================================================================================================================#

# Define una función para abrir la ventana principal y cerrar la ventana de carga
def top():
    root.withdraw()  # Oculta la ventana de carga
    os.system("python AccountSystem.py")  # Ejecuta el script AccountSystem.py
    root.destroy()  # Destruye la ventana principal

i = 0  # Inicializa una variable de contador

# Define una función recursiva para simular el progreso de carga
def load():
    global i  # Permite acceder y modificar la variable i dentro de la función
    if i <= 10:  # Verifica si el contador es menor o igual a 10
        # Actualiza el texto de la etiqueta de progreso y el valor de la barra de progreso
        txt = 'Por favor espere...  ' + (str(10*i)+'%')
        progress_label.config(text=txt)
        progress['value'] = 10*i
        # Programa una llamada recursiva a la función load después de 1000 milisegundos (1 segundo)
        progress_label.after(1000, load)
        i += 1  # Incrementa el contador
    else:
        top()  # Llama a la función top para abrir la ventana principal

# Llama a la función load para iniciar la simulación de carga
load()

# Inicia el bucle principal de eventos de la interfaz gráfica
root.mainloop()