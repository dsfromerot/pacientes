from flask import Flask, jsonify
from flask_oidc import OpenIDConnect

app = Flask(__name__)

# Configuración de Keycloak
app.config.update({
    'SECRET_KEY': 'secret',
    'OIDC_CLIENT_SECRETS': 'client_secrets.json',
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
