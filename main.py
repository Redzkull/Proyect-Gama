# main.py
import tkinter as tk
from tkinter import messagebox
from auth import auth_google, auth_local

def login_local():
    email = entry_email.get()
    password = entry_password.get()
    user = auth_local.verificar_usuario(email, password)
    if user:
        messagebox.showinfo("Inicio de Sesión", f"Bienvenido, {user['role']}")
        abrir_dashboard(user["role"])
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

def login_google():
    user_info = auth_google.iniciar_sesion_google()
    if user_info:
        abrir_dashboard("parent")

def abrir_dashboard(role):
    ventana_dashboard = tk.Toplevel()
    if role == "parent":
        ventana_dashboard.title("Panel de Control de Padre")
        tk.Label(ventana_dashboard, text="Bienvenido, padre").pack()
    elif role == "child":
        ventana_dashboard.title("Panel de Control de Niño")
        tk.Label(ventana_dashboard, text="Bienvenido, niño").pack()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Sistema de Autenticación")
root.geometry("400x200")

# Entrada para usuario y contraseña
tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root, text="Contraseña").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Botones de inicio de sesión
btn_login_local = tk.Button(root, text="Iniciar sesión local", command=login_local)
btn_login_local.pack()

btn_login_google = tk.Button(root, text="Iniciar sesión con Google", command=login_google)
btn_login_google.pack()

root.mainloop()
