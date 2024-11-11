import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
app = tk.Tk()
app.title("Mi Aplicación de Escritorio")
app.geometry("400x300")  # Tamaño de la ventana

# Crear una función para un botón
def saludo():
    messagebox.showinfo("Saludo", "¡Hola, bienvenido a la aplicación de escritorio!")

# Crear un botón que ejecuta la función de saludo
btn_saludo = tk.Button(app, text="Saludar", command=saludo)
btn_saludo.pack(pady=20)

# Ejecutar el bucle principal de la aplicación
app.mainloop()
