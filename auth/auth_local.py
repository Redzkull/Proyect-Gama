# auth/auth_local.py
users_db = {
    "   ": {"password": "parentpass", "role": "parent"},
    "child@example.com": {"password": "childpass", "role": "child"}
}

def verificar_usuario(email, password):
    user = users_db.get(email)
    if user and user['password'] == password:
        return user
    return None
