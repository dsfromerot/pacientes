from flask import Flask, jsonify
from flask_oidc import OpenIDConnect
import os

app = Flask(__name__)

# Configuración de Keycloak desde variables de entorno
app.config.update({
    'SECRET_KEY': os.getenv('FLASK_SECRET_KEY', 'secret'),
    'OIDC_CLIENT_SECRETS': {
        "web": {
            "issuer": os.getenv('OIDC_ISSUER'),
            "auth_uri": os.getenv('OIDC_AUTH_URI'),
            "client_id": os.getenv('OIDC_CLIENT_ID'),
            "client_secret": os.getenv('OIDC_CLIENT_SECRET'),
            "redirect_uris": [os.getenv('OIDC_REDIRECT_URIS')],
            "userinfo_uri": os.getenv('OIDC_USERINFO_URI'),
            "token_uri": os.getenv('OIDC_TOKEN_URI'),
            "token_introspection_uri": os.getenv('OIDC_INTROSPECTION_URI')
        }
    },
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_REQUIRE_VERIFIED_EMAIL': False,
    'OIDC_USER_INFO_ENABLED': True,
    'OIDC_SCOPES': ['openid', 'email', 'profile'],
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post'
})
oidc = OpenIDConnect(app)

# Datos hardcodeados
pacientes = [
    {"nombre": "Juan Perez", "edad": 30, "enfermedad": "Gripe"},
    {"nombre": "Maria Lopez", "edad": 25, "enfermedad": "Fiebre"}
]

@app.route('/pacientes', methods=['GET'])
@oidc.accept_token(True)  # Protege la ruta con Keycloak
def get_pacientes():
    return jsonify(pacientes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
