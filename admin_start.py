from tkinter import *  # Importa todos los elementos de la librería tkinter
from PIL import ImageTk, Image, ImageDraw  # Importa las clases necesarias de la librería PIL
from tkinter import messagebox  # Importa el módulo messagebox de tkinter para mostrar mensajes emergentes
import os  # Importa el módulo os para interactuar con el sistema operativo
import AccountSystem  # Importa el módulo AccountSystem

class FirstPage:
    def __init__(self, dashboard_window):
        self.dashboard_window = dashboard_window  # Guarda una referencia a la ventana principal

        # Window Size and Placement
        dashboard_window.rowconfigure(0, weight=1)  # Configura la fila 0 de la ventana principal para que se expanda
        dashboard_window.columnconfigure(0, weight=1)  # Configura la columna 0 de la ventana principal para que se expanda
        screen_width = dashboard_window.winfo_screenwidth()  # Obtiene el ancho de la pantalla
        screen_height = dashboard_window.winfo_height()  # Obtiene la altura de la pantalla
        app_width = 1340  # Anchura de la aplicación
        app_height = 690  # Altura de la aplicación
        x = (screen_width/2)-(app_width/2)  # Calcula la posición x para centrar la ventana en la pantalla
        y = (screen_height/160)-(app_height/160)  # Calcula la posición y para centrar la ventana en la pantalla
        dashboard_window.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")  # Establece la geometría de la ventana

        # window Icon
        icon = PhotoImage(file='images\\carretilla.png')  # Carga el icono de la ventana desde un archivo de imagen
        dashboard_window.iconphoto(True, icon)  # Establece el icono de la ventana
        dashboard_window.title('ProgressBar&Login')  # Establece el título de la ventana

        # Navigating through windows
        homepage = Frame(dashboard_window)  # Crea un marco para la página de inicio
        dashboard_page = Frame(dashboard_window)  # Crea un marco para la página del dashboard

        for frame in (homepage, dashboard_page):  # Itera sobre los marcos creados
            frame.grid(row=0, column=0, sticky='nsew')  # Coloca cada marco en la ventana principal y lo expande

        def show_frame(frame):  # Define una función para mostrar un marco específico
            frame.tkraise()  # Eleva el marco especificado para que sea visible

        show_frame(homepage)  # Muestra inicialmente el marco de la página de inicio

        homepage.config(background='#ffffff')  # Establece el color de fondo del marco de la página de inicio

        # Creación de elementos visuales dentro del marco de la página de inicio
        frame1 = Frame(homepage, bg="#dddddd",highlightbackground="gray", highlightthickness=1) # Crea un marco con color de fondo
        frame1.pack()  # Empaqueta el marco en la página de inicio
        frame1.place(x=0, y=0, width=1366, height=100)  # Ubica y establece el tamaño del marco

        lblframe1=Label(frame1, text="AdminStart", font="sans 30 bold", bg="#dddddd", anchor="center") # Crea una etiqueta en el marco con texto y fuente
        lblframe1.place(x=3, y=5, width=1364, height=90)  # Ubica y establece el tamaño de la etiqueta

        frame2 = Frame(homepage, bg="#C6D9E3",highlightbackground="gray", highlightthickness=1) # Crea otro marco con color de fondo
        frame2.pack()  # Empaqueta el marco en la página de inicio
        frame2.place(x=0, y=100, width=1366, height=650)  # Ubica y establece el tamaño del marco

def page():  # Define una función para crear y mostrar la ventana principal
    window = Tk()  # Crea una instancia de la clase Tk() para la ventana principal
    FirstPage(window)  # Crea una instancia de la clase FirstPage dentro de la ventana principal
    window.mainloop()  # Inicia el bucle principal de eventos de la interfaz gráfica

if __name__ == '__main__':  # Verifica si el script se está ejecutando como el programa principal
    page()  # Llama a la función page para mostrar la ventana principal