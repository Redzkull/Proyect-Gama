from google_auth_oauthlib.flow import InstalledAppFlow # type: ignore

# Configurar el flujo de autenticación OAuth 2.0
flow = InstalledAppFlow.from_client_secrets_file(
    'data\client_secret_627613066280-6phbcjb5un56c1s53bltghac0fiiguqm.apps.googleusercontent.com.json',  # Asegúrate de que este archivo esté en el mismo directorio que el código
    scopes=['https://www.googleapis.com/auth/userinfo.email', 'openid']
)

# Ejecutar el flujo de autenticación
credentials = flow.run_local_server(port=0)
print("Autenticación exitosa!")
print("Token de acceso:", credentials.token)
