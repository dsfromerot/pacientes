from flask import Flask
from flask_oidc import OpenIDConnect

# Inicializar la aplicación Flask
app = Flask(__name__)

# Configuración de Flask y Keycloak
app.config.update({
    'SECRET_KEY': 'secret',  # Clave secreta para Flask
    'OIDC_CLIENT_SECRETS': 'client_secrets.json',  # Archivo de configuración de Keycloak
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_REQUIRE_VERIFIED_EMAIL': False,
    'OIDC_USER_INFO_ENABLED': True,
    'OIDC_SCOPES': ['openid', 'email', 'profile'],
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post'
})

# Inicializar la extensión Flask-OIDC
oidc = OpenIDConnect(app)
