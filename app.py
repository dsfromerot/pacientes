from flask import Flask, jsonify
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
oauth = OAuth(app)

# Configura Keycloak
oauth.register(
    name='keycloak',
    client_id='pacientes',
    client_secret='EFT9lXLLTEzb9ftI59VL83V2ykza1eUW',
    authorize_url='http://100.124.235.117:8080/auth/realms/hospital-realm/protocol/openid-connect/auth',
    authorize_params=None,
    access_token_url='http://100.124.235.117:8080/auth/realms/hospital-realm/protocol/openid-connect/token',
    access_token_params=None,
    refresh_token_url=None,
    redirect_uri='http://100.93.128.110:5001/callback',
    client_kwargs={'scope': 'openid profile email'},
)

@app.route('/pacientes', methods=['GET'])
def get_pacientes():
    token = oauth.keycloak.authorize_access_token()
    if not token:
        return jsonify({"error": "Acceso no autorizado"}), 401
    pacientes = [
        {"nombre": "Juan Perez", "edad": 30, "enfermedad": "Gripe"},
        {"nombre": "Maria Lopez", "edad": 25, "enfermedad": "Fiebre"}
    ]
    return jsonify(pacientes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
