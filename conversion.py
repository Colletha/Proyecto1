import tkinter as tk
from tkinter import ttk, messagebox

USUARIO_VALIDO = "Lacolletha"
CONTRASENA_VALIDA = "20110010"

def metros_a_kilometros(x):
    return f"{x / 1000:.3f} km"

def pulgadas_a_metros(x):
    return f"{x * 0.0254:.3f} m"

def kilogramos_a_gramos(x):
    return f"{x * 1000:.2f} g"

def libras_a_kilogramos(x):
    return f"{x * 0.4536:.2f} kg"

def segundos_a_minutos(x):
    return f"{x / 60:.2f} min"

def horas_a_dias(x):
    return f"{x / 24:.2f} días"

class Conversion:
    def __init__(self, titulo, conversiones):
        self.ventana = tk.Toplevel()
        self.ventana.title(titulo)
        self.ventana.geometry("320x270")
        self.ventana.configure(bg="#f8bbd0")

        self.conversiones = conversiones

        tk.Label(self.ventana, text="Seleccione tipo de conversión:", bg="#f8bbd0", font=("Arial", 10)).pack(pady=5)
        self.tipo = ttk.Combobox(self.ventana, values=list(conversiones.keys()))
        self.tipo.pack(pady=5)

        tk.Label(self.ventana, text="Ingrese valor:", bg="#f8bbd0", font=("Arial", 10)).pack(pady=5)
        self.entrada = tk.Entry(self.ventana)
        self.entrada.pack(pady=5)

        self.btn_convertir = tk.Button(self.ventana, text="Convertir", command=self.convert,
                                       bg="#ce93d8", fg="white", font=("Arial", 10))
        self.btn_convertir.pack(pady=10)

        self.resultado = tk.Label(self.ventana, text="Resultado: ", bg="#f8bbd0", font=("Arial", 10, "bold"))
        self.resultado.pack(pady=5)

    def convert(self):
        try:
            valor = float(self.entrada.get())
            seleccion = self.tipo.get()
            if seleccion in self.conversiones:
                resultado = self.conversiones[seleccion](valor)
                self.resultado.config(text=f"Resultado: {resultado}")
            else:
                messagebox.showwarning("Advertencia", "Seleccione una conversión.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido.")


def longitud():
    conversiones = {
        "Metros a Kilómetros": metros_a_kilometros,
        "Pulgadas a Metros": pulgadas_a_metros
    }
    Conversion("Conversión de Longitud", conversiones)

def masa():
    conversiones = {
        "Kilogramos a Gramos": kilogramos_a_gramos,
        "Libras a Kilogramos": libras_a_kilogramos
    }
    Conversion("Conversión de Masa", conversiones)

def tiempo():
    conversiones = {
        "Segundos a Minutos": segundos_a_minutos,
        "Horas a Días": horas_a_dias
    }
    Conversion("Conversión de Tiempo", conversiones)


def homepage():
    ventana = tk.Tk()
    ventana.title("Conversor Universal")
    ventana.geometry("300x300")
    ventana.configure(bg="#e1f5fe")

    tk.Label(ventana, text="Escoja su opción", bg="#a5d6a7", font=("Arial", 14)).pack(pady=10)

    opciones = [("Longitud", longitud),
                ("Masa", masa),
                ("Tiempo", tiempo)]

    for texto, funcion in opciones:
        tk.Button(ventana, text=texto, command=funcion, width=20, bg="#ff8a65", fg="white").pack(pady=10)

    ventana.mainloop()


def login():
    ventana = tk.Tk()
    ventana.title("Login")
    ventana.geometry("300x200")
    ventana.configure(bg="#fce4ec")

    tk.Label(ventana, text="Usuario:", bg="#fce4ec").pack(pady=5)
    entrada_usuario = tk.Entry(ventana)
    entrada_usuario.pack()

    tk.Label(ventana, text="Contraseña:", bg="#fce4ec").pack(pady=5)
    entrada_contra = tk.Entry(ventana, show="*")
    entrada_contra.pack()

    def verify():
        if entrada_usuario.get() == USUARIO_VALIDO and entrada_contra.get() == CONTRASENA_VALIDA:
            ventana.destroy()
            homepage()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    tk.Button(ventana, text="Entrar", command=verify, bg="#f06292", fg="white").pack(pady=15)
    ventana.mainloop()

login()