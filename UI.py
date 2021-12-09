from tkinter import Frame, StringVar, Menu, Entry, Button, Label
from tkinter import messagebox
from cuenta import get_cuenta
from pyperclip3 import copy


if __name__ != "__main__":
    class cuentaPOO(Frame):
        
        def __init__(self, raiz):
            #*****************VARIABLES DE CONTROL
            self.mi_cuenta = StringVar()
            self.mi_resultado = StringVar()
            self.root = raiz
            super().__init__(raiz)
            self.ancho_ventana = 400
            self.alto_ventana = 130
            self.x_ventana = raiz.winfo_screenwidth() // 2 - self.ancho_ventana // 2
            self.y_ventana = raiz.winfo_screenheight() // 2 - self.alto_ventana // 2
            posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)
            self.root.geometry(posicion)
            self.root.resizable(0,0)
            self.root.title("Formato cuenta GE")
            self.barraMenu = Menu(self.root)
            self.root.config(menu=self.barraMenu)
            self.crear_widgets()
            self.crear_barra_menu()


        def salir_aplicacion(self):
            self.valor_salir = messagebox.askquestion(
                "Salir", "¿Deseas salir de la aplicación?")
            
            if self.valor_salir == "yes":
                self.root.destroy()
            else:
                pass

        def ayuda(self):
            self.mensaje_ayuda = "En el campo de texto \"Nº Cuenta\" inserte el número de cuenta al cual quiere dejar en el formato del GE.\n\nAl pulsar en el botón \"Convertir\" automáticamente le mostrará el resultado en el campo de texto \"Resultado\" y lo copiará al portapapeles.\n\nUtilice el botón \"Borrar\" para eliminar el texto incorporado en las cajas de texto."
            messagebox.showinfo("Ayuda",self.mensaje_ayuda)

        def limpiar_campos(self):
            self.mi_cuenta.set("")
            self.mi_resultado.set("")

        def convertir(self):
            self.mi_resultado.set(get_cuenta(self.mi_cuenta.get()))
            copy(self.mi_resultado.get())

        def crear_widgets(self):

            # ***********************CUADROS DE TEXTO*******************
            self.miFrame = Frame(self.root)
            self.miFrame.pack()

            self.cuadroCuenta = Entry(self.miFrame, textvariable=self.mi_cuenta, width=50)
            self.cuadroCuenta.grid(row=0, column=1, padx=10, pady=10)

            self.cuadroResultado = Entry(self.miFrame, textvariable=self.mi_resultado, width=50)
            self.cuadroResultado.grid(row=1, column=1, padx=10, pady=10)

            # ************************LABELS****************************
            self.lblCuenta = Label(self.miFrame, text="Nº Cuenta")
            self.lblCuenta.grid(row=0, column=0, padx=10, pady=10, sticky="e")


            self.lblResultado = Label(self.miFrame, text="Resultado")
            self.lblResultado.grid(row=1, column=0, padx=10, pady=10, sticky="e")

            # ************************BOTONES***************************
            self.miFrameBotones = Frame(self.root)
            self.miFrameBotones.pack()



            self.btnConvertir = Button(self.miFrameBotones, text="Convertir", command=self.convertir)
            self.btnConvertir.grid(row=0, column=1, padx=10, pady=10, sticky="e")

            self.btnBorrar = Button(self.miFrameBotones, text="Borrar", command=self.limpiar_campos)
            self.btnBorrar.grid(row=0, column=3, padx=10, pady=10, sticky="e")

        def crear_barra_menu(self):
            self.salirMenu = Menu(self.barraMenu, tearoff=0)            
            self.salirMenu.add_command(label="Salir", command=self.salir_aplicacion)

            self.ayudaMenu = Menu(self.barraMenu, tearoff=0)
            self.ayudaMenu.add_command(label="Uso", command=self.ayuda)

            self.barraMenu.add_cascade(label="Archivo", menu=self.borrarMenu)
            self.barraMenu.add_cascade(label="Ayuda", menu=self.ayudaMenu)
