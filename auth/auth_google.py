import os
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
import requests

SCOPES = ['https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile', 'openid']
CREDENTIALS_FILE = 'auth/client_secret.json'
TOKEN_FILE = 'auth/token.json'

def iniciar_sesion_google():
    creds = None

    # Cargar token si existe
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    
    # Renovar o iniciar autenticación si no es válido
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        # Guardar el token para futuras sesiones
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())

    # Obtener información del usuario
    return obtener_informacion_usuario(creds) if creds else None

def obtener_informacion_usuario(creds):
    headers = {'Authorization': f'Bearer {creds.token}'}
    response = requests.get('https://www.googleapis.com/oauth2/v1/userinfo', headers=headers)
    return response.json() if response.status_code == 200 else None

if __name__ == "__main__":
    user_info = iniciar_sesion_google()
    if user_info:
        print(f"Bienvenido, {user_info['name']}")
    else:
        print("Error en la autenticación o al obtener la información del usuario.")
