from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import messagebox
import sqlite3
import admin_start

class AccountPage: #Login
    def __init__(self, AccountSystem_window):
        self.AccountSystem_window = AccountSystem_window

        # Window Size and Placement
        AccountSystem_window.rowconfigure(0, weight=1)
        AccountSystem_window.columnconfigure(0, weight=1)
        width = 1100
        height = 650
        x = (AccountSystem_window.winfo_screenwidth()//2)-(width//2)
        y = (AccountSystem_window.winfo_screenheight()//4)-(height//4)
        AccountSystem_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        AccountSystem_window.resizable(0, 0)

        #Icono de la app
        icon = PhotoImage(file='images\\marketplace.png') 
        AccountSystem_window.iconphoto(True, icon)

        AccountSystem_window.title('ProgressBar&Login')

        # Navegacion por las ventanas
        sign_up = Frame(AccountSystem_window)
        sign_in = Frame(AccountSystem_window)
        landing_page = Frame(AccountSystem_window)

        for frame in (landing_page, sign_in, sign_up):
            frame.grid(row=0, column=0, sticky='nsew')

        def show_frame(frame):
            frame.tkraise()

        show_frame(landing_page)

#===============================================================================================================================================#    
#=====PAGINA 1 LANDING Frame izquierdo==================================================================================================================#
        
        landing_page.config(background='#C6D9E3')

        fondo = Frame(landing_page, bg="#C6D9E3",highlightbackground="gray", highlightthickness=1)
        fondo.pack()
        fondo.place(x=0, y=0, width=550, height=650)

        brand_name = Label(fondo, text='BIENVENIDO', bg='#C6D9E3', fg='black', font=("yu gothic ui", 36, "bold"))
        brand_name.place(x=120, y=20)

        logoIcon = Image.open('images\\logo1.png')
        photo = ImageTk.PhotoImage(logoIcon)
        logo = Label(fondo, image=photo, bg='#C6D9E3')
        logo.image = photo
        logo.place(x=180, y=100)

        coffeeImage = Image.open('images\\innova1.png')
        coffeeImage = coffeeImage.resize((250, 100))
        photo = ImageTk.PhotoImage(coffeeImage)
        coffee_image = Label(fondo, image=photo, bg='#C6D9E3')
        coffee_image.image = photo
        coffee_image.place(x=150, y=500)

#=====PAGINA 1 LANDING Frame derecho==================================================================================================================#
        
        fondo1 = Frame(landing_page, bg="#C6D9E3",highlightbackground="gray", highlightthickness=1)
        fondo1.pack()
        fondo1.place(x=550, y=0, width=550, height=650)
        
        # Label informacion
        heading_label = Label(fondo1, text="Para continuar,\n Por favor inicia sesión o \n crea una nueva cuenta", font=("", 20, "bold"), bg='#C6D9E3')
        heading_label.place(x=100, y=100)

        # Boton Iniciar sesión
        login_button = Button(fondo1, text='Iniciar sesión ', bg='#fd6a36', font=("", 16, "bold"), bd=0, fg='white',
                              cursor='hand2', activebackground='#fd6a36', activeforeground='white',
                              command=lambda: show_frame(sign_in))
        login_button.place(x=160, y=300, width=240, height=40)

        # Boton Registrar nueva cuentra
        signUp_button = Button(fondo1, text='Crear nueva cuenta', bg='#fd6a36', font=("", 16, "bold"), bd=0, fg='white',
                               cursor='hand2', activebackground='#fd6a36', activeforeground='white',
                               command=lambda: show_frame(sign_up))
        signUp_button.place(x=160, y=380, width=240, height=40)
        
#=======================================================================================================================================================#
#=====PAGINA 2 SIGN IN Frame izquierdo==================================================================================================================#
        
        sign_in.config(background='#C6D9E3')

        fondo = Frame(sign_in, bg="#C6D9E3",highlightbackground="gray", highlightthickness=1)
        fondo.pack()
        fondo.place(x=0, y=0, width=550, height=650)
        
        brand_name = Label(fondo, text='BIENVENIDO', bg='#C6D9E3', fg='black', font=("yu gothic ui", 36, "bold"))
        brand_name.place(x=120, y=20)

        logoIcon = Image.open('images\\logo1.png')
        photo = ImageTk.PhotoImage(logoIcon)
        logo = Label(fondo, image=photo, bg='#C6D9E3')
        logo.image = photo
        logo.place(x=180, y=100)

        coffeeImage = Image.open('images\\innova1.png')
        coffeeImage = coffeeImage.resize((250, 100))
        photo = ImageTk.PhotoImage(coffeeImage)
        coffee_image = Label(fondo, image=photo, bg='#C6D9E3')
        coffee_image.image = photo
        coffee_image.place(x=150, y=500)

#=====PAGINA 2 SIGN IN Frame derecho==================================================================================================================#
        fondo1 = Frame(sign_in, bg="#C6D9E3",highlightbackground="gray", highlightthickness=1)
        fondo1.pack()
        fondo1.place(x=550, y=0, width=550, height=650)
        
        # Titulo Iniciar sesión
        heading = Label(fondo1, text="Iniciar sesión", font=("", 36, "bold"), bg='#C6D9E3')
        heading.place(x=140, y=40)

        Username = StringVar()
        Password = StringVar()

        def login_all(): #Funcion para logearse con los 3 tipos de usuarios
            # Admin
            conn1 = sqlite3.connect("./Database/database.db")
            cursor1 = conn1.cursor()
            find_user1 = 'SELECT * FROM Admin_Account WHERE admin_username = ? and admin_password = ?'
            cursor1.execute(find_user1, [(username_entry.get()), (password_entry.get())])

            result1 = cursor1.fetchall()

            if result1:
                messagebox.showinfo("Acceso", 'Inicio de sesión con exito,\n\nClick "OK" para continuar.')
                open_admin()
            else:
                messagebox.showerror("Error", "Error, revisa los campos e intenta de nuevo.")

        #Label Usuario
        username_label = Label(fondo1, text='Usuario', fg="#27221c", bg='#C6D9E3', font=("", 16, "bold"))
        username_label.place(x=150, y=150)
        
        #Entry Usuario
        username_entry = Entry(fondo1, highlightthickness=2, relief=FLAT, bg="#fafafa", fg="#6b6a69", font=("", 16, 'bold'), textvariable=Username)
        username_entry.place(x=150, y=182, width=290, height=34)
        username_entry.config(highlightbackground="#6b6a69", highlightcolor="black")

        #Label Contraseña
        password_label = Label(fondo1, text='Contraseña', fg="#27221c", bg='#C6D9E3', font=("", 16, "bold"))
        password_label.place(x=150, y=250)
        
        #Entry Contraseña
        password_entry = Entry(fondo1, highlightthickness=2, relief=FLAT, bg="#fafafa", fg="#6b6a69", font=("", 16), show="•",textvariable=Password)
        password_entry.place(x=150, y=282, width=290, height=34)
        password_entry.config(highlightbackground="#6b6a69", highlightcolor="black")

        #Boton Iniciar sesión
        loginButton = Button(fondo1, fg='#f8f8f8', text='Iniciar sesión', bg='#ff6c38', font=("", 16, "bold"),cursor='hand2', activebackground='#ff6c38', command=login_all)
        loginButton.place(x=150, y=370, width=290, height=40)

        #Linea divisora
        line = Canvas(fondo1, width=286, height=1.5, bg="black", highlightthickness=0)
        line.place(x=150, y=440)
        
        #No tienes cuenta aún?
        label = Label(fondo1, text='No tienes una cuenta aún?', bg='#C6D9E3')
        label.place(x=200, y=430)

        #Boton crear nueva cuenta
        createButton = Button(fondo1, fg='#f8f8f8', text='Crear una nueva cuenta', bg='#4286f5', font=("", 16, "bold"),cursor='hand2', activebackground='#4286f5', command=lambda: show_frame(sign_up))
        createButton.place(x=150, y=470, width=290, height=40)

        # función para mostrar o ocultar la contraseña
        def password_command():
            if password_entry.cget('show') == "•":
                password_entry.config(show="")
            else:
                password_entry.config(show="•")

        # Check Button mostrar contraseña
        show_password = Checkbutton(fondo1, text="Mostrar contraseña", bg='#C6D9E3', fg='#27221c', command=password_command)
        show_password.place(x=150, y=332)

    #===Ventana recuperar contraseña=======================================================================================================#
        def forgot_password():
            win = Toplevel()
            window_width = 350
            window_height = 350
            screen_width = win.winfo_screenwidth()
            screen_height = win.winfo_screenheight()
            position_top = int(screen_height / 4 - window_height / 4)
            position_right = int(screen_width / 2 - window_width / 2)
            win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
            win.title('Recuperar contraseña')
            # win.iconbitmap('images\\aa.ico')
            win.configure(background='#C6D9E3')
            win.resizable(0, 0)

            # Variables
            username = StringVar()
            password = StringVar()
            confirmPassword = StringVar()

            # Usuario
            username_label2 = Label(win, text='• Usuario', fg="#89898b", bg='#C6D9E3',font=("yu gothic ui", 11, 'bold'))
            username_label2.place(x=40, y=0)
            
            username_entry3 = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2,textvariable=username)
            username_entry3.place(x=40, y=30, width=256, height=34)
            username_entry3.config(highlightbackground="black", highlightcolor="black")

            # Nueva contraseña
            new_password_label = Label(win, text='• Nueva contraseña', fg="#89898b", bg='#C6D9E3',font=("yu gothic ui", 11, 'bold'))
            new_password_label.place(x=40, y=80)
            
            new_password_entry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2,textvariable=password)
            new_password_entry.place(x=40, y=110, width=256, height=34)
            new_password_entry.config(highlightbackground="black", highlightcolor="black")
            
            # Confirmar contraseña
            confirm_password_label = Label(win, text='• Confirmar contraseña', fg="#89898b", bg='#C6D9E3',font=("yu gothic ui", 11, 'bold'))
            confirm_password_label.place(x=40, y=160)
            
            confirm_password_entry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2, textvariable=confirmPassword)
            confirm_password_entry.place(x=40, y=190, width=256, height=34)
            confirm_password_entry.config(highlightbackground="black", highlightcolor="black")

            # Boton Guardar contraseña
            update_pass = Button(win, fg='#f8f8f8', text='Guardar contraseña', bg='#ff6c38', font=("", 12, "bold"),cursor='hand2', activebackground='#ff6c38', command=lambda: change_password())
            update_pass.place(x=40, y=240, width=256, height=50)

        #==========DATABASE CONNECTION FOR FORGOT PASSWORD====================================================================================#
            def change_password():
                db = sqlite3.connect("./Database/database.db")
                cur = db.cursor()

                insert = '''update Guest_Account set guest_password=? where guest_username=? '''
                cur.execute(insert, [new_password_entry.get(), username_entry3.get(), ])
                db.commit()
                db.close()
                messagebox.showinfo('Congrats', 'Password changed successfully')

        forgotPassword = Button(fondo1, text='Recuperar contraseña', font=("", 10, "bold"), bg='#C6D9E3', fg='#4286f5',borderwidth=0, activebackground='#f8f8f8', command=lambda: forgot_password(), cursor="hand2")
        forgotPassword.place(x=295, y=332)
#=================================================================================================================================================================#        
        #Funciones para abrir el dashboard al logearse

        def open_admin():
            win = Toplevel()
            admin_start.FirstPage(win)
            AccountSystem_window.withdraw()
            win.deiconify()

#=======================================================================================================================================================#
#=====PAGINA 3 SIGN UP Frame izquierdo==================================================================================================================#
        
        sign_up.config(background='#C6D9E3')

        fondo = Frame(sign_up, bg="#C6D9E3",highlightbackground="gray", highlightthickness=1)
        fondo.pack()
        fondo.place(x=0, y=0, width=550, height=650)
        
        # Titulo bienvenido
        brand_name = Label(fondo, text='BIENVENIDO', bg='#C6D9E3', fg='black', font=("yu gothic ui", 36, "bold"))
        brand_name.place(x=120, y=20)

        #Logo app
        logoIcon = Image.open('images\\logo1.png')
        photo = ImageTk.PhotoImage(logoIcon)
        logo = Label(fondo, image=photo, bg='#C6D9E3')
        logo.image = photo
        logo.place(x=180, y=100)

        coffeeImage = Image.open('images\\innova1.png')
        coffeeImage = coffeeImage.resize((250, 100))
        photo = ImageTk.PhotoImage(coffeeImage)
        coffee_image = Label(fondo, image=photo, bg='#C6D9E3')
        coffee_image.image = photo
        coffee_image.place(x=150, y=500)

#=====PAGINA 3 SIGN UP Frame derecho==================================================================================================================#

        fondo1 = Frame(sign_up, bg="#C6D9E3",highlightbackground="gray", highlightthickness=1)
        fondo1.pack()
        fondo1.place(x=550, y=0, width=550, height=650)

        # Titulo Crear nueva cuenta
        heading = Label(fondo1, text="Crear nueva cuenta", font=("", 36, "bold"), bg='#C6D9E3')
        heading.place(x=60, y=30)

        FullName = StringVar()
        Username2 = StringVar()
        Password2 = StringVar()
        def signup_all():
            check_counter = 0
            warn = ""
            if fullname_entry.get() == "":
                warn = "Por favor ingresa tu nombre completo"
            else:
                check_counter += 1

            if username_entry2.get() == "":
                warn = "Por favor ingresa tu usuario"
            else:
                check_counter += 1

            if password_entry2.get() == "":
                warn = "Por favor asegurate de que los campos Nombre completo, Usuario y contraseña, no esten vacios"
            else:
                check_counter += 1

        #Widgets
        fullname_label = Label(fondo1, text='Nombre completo', fg="#27221c", bg='#C6D9E3', font=("", 16, "bold"))
        fullname_label.place(x=150, y=100)
        
        fullname_entry = Entry(fondo1, highlightthickness=2, relief=FLAT, bg="#fafafa", fg="#6b6a69",font=("", 12, 'bold'), textvariable=FullName)
        fullname_entry.place(x=150, y=132, width=290, height=34)
        fullname_entry.config(highlightbackground="#6b6a69", highlightcolor="black")

        username_label2 = Label(fondo1, text='Usuario', fg="#27221c", bg='#C6D9E3', font=("", 16, "bold"))
        username_label2.place(x=150, y=185)
        
        username_entry2 = Entry(fondo1, highlightthickness=2, relief=FLAT, bg="#fafafa", fg="#6b6a69",font=("", 12, 'bold'), textvariable=Username2)
        username_entry2.place(x=150, y=217, width=290, height=34)
        username_entry2.config(highlightbackground="#6b6a69", highlightcolor="black")

        password_label2 = Label(fondo1, text='Contraseña', fg="#27221c", bg='#C6D9E3', font=("", 16, "bold"))
        password_label2.place(x=150, y=270)
        
        password_entry2 = Entry(fondo1, highlightthickness=2, relief=FLAT, bg="#fafafa", fg="#6b6a69", font=("", 16), show='•',textvariable=Password2)
        password_entry2.place(x=150, y=302, width=290, height=34)
        password_entry2.config(highlightbackground="#6b6a69", highlightcolor="black")

        signupButton = Button(fondo1, fg='#f8f8f8', text='Crear cuenta', bg='#ff6c38', font=("", 16, "bold"),cursor='hand2', activebackground='#ff6c38', command=signup_all)
        signupButton.place(x=150, y=390, width=290, height=40)

        line = Canvas(fondo1, width=286, height=1.5, bg="black", highlightthickness=0)
        line.place(x=150, y=460)
        
        label = Label(fondo1, text='Ya tienes una cuenta?', bg='#C6D9E3')
        label.place(x=250, y=450)

        sign_inButton = Button(fondo1, fg='#f8f8f8', text='Iniciar sesión', bg='#4286f5', font=("", 16, "bold"), cursor='hand2', activebackground='#4286f5', command=lambda: show_frame(sign_in))
        sign_inButton.place(x=150, y=490, width=290, height=40)

        # funcion para mostrar y ocultar contraseña

        def password_command2():
            if password_entry2.cget('show') == '•':
                password_entry2.config(show='')
            else:
                password_entry2.config(show='•')

        # Check Button Mostrar contraseña
        show_password2 = Checkbutton(fondo1, text="Mostrar contraseña", bg='#C6D9E3', fg='#27221c', command=password_command2)
        show_password2.place(x=150, y=352)
#===============================================================================================================================================================#

def page():
    window = Tk()
    AccountPage(window)
    window.mainloop()

if __name__ == '__main__':
    page()
