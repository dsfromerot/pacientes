from flask import Flask
from flask_oidc import OpenIDConnect

app = Flask(__name__)

# Configuración de Flask y Keycloak
app.config.update({
    'SECRET_KEY': 'secret',  
    'OIDC_CLIENT_SECRETS': '/app/client_secrets.json',  # Ruta absoluta
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_REQUIRE_VERIFIED_EMAIL': False,
    'OIDC_USER_INFO_ENABLED': True,
    'OIDC_SCOPES': ['openid', 'email', 'profile'],
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post'
})

oidc = OpenIDConnect(app)

if __name__ != "__main__":
    from app import routes  # Importar rutas solo si Flask no se ejecuta como módulo

def start():
    app.run(host="0.0.0.0", port=5001, debug=True)

if __name__ == "__main__":
    start()

# Importar rutas aquí para evitar importaciones circulares
from app import routes
