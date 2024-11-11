# auth/auth_google.py
import json
import os
import tkinter as tk
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from tkinter import messagebox

# Especifica el alcance de la información que deseas acceder. Aquí estamos solicitando perfil y email
SCOPES = ['https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile', 'openid']

# Ruta al archivo JSON de credenciales
CREDENTIALS_FILE = 'auth/client_secret.json'
TOKEN_FILE = 'auth/token.json'

def iniciar_sesion_google():
    creds = None

    # Cargar el token de acceso si existe
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    
    # Si no hay credenciales válidas, inicia el flujo de autenticación
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)  # Esto abrirá el navegador para autenticar

        # Guardar el token para futuras sesiones
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())

    # Verificar las credenciales y obtener información del usuario
    if creds:
        user_info = obtener_informacion_usuario(creds)
        if user_info:
            messagebox.showinfo("Inicio de Sesión", f"Bienvenido, {user_info['name']}")
            return user_info
    return None

def obtener_informacion_usuario(creds):
    # Llamada a la API de Google para obtener información del usuario autenticado
    from google.auth.transport.requests import Request
    import requests

    headers = {
        'Authorization': f'Bearer {creds.token}'
    }
    response = requests.get('https://www.googleapis.com/oauth2/v1/userinfo', headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        messagebox.showerror("Error", "No se pudo obtener información del usuario.")
        return None
