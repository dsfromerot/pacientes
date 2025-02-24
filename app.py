from flask import Flask, jsonify, redirect, url_for, session
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for session management
oauth = OAuth(app)

# Configure Keycloak
oauth.register(
    name='keycloak',
    client_id='pacientes',
    client_secret='EFT9lXLLTEzb9ftI59VL83V2ykza1eUW',
    authorize_url='http://100.124.235.117:8080/auth/realms/hospital-realm/protocol/openid-connect/auth',
    access_token_url='http://100.124.235.117:8080/auth/realms/hospital-realm/protocol/openid-connect/token',
    redirect_uri='http://100.93.128.110:5001/callback',
    client_kwargs={'scope': 'openid profile email'},
)

@app.route('/login')
def login():
    # Redirect the user to Keycloak for authentication
    redirect_uri = url_for('callback', _external=True)
    return oauth.keycloak.authorize_redirect(redirect_uri)

@app.route('/callback')
def callback():
    try:
        # Exchange the authorization code for an access token
        token = oauth.keycloak.authorize_access_token()
        if not token:
            return jsonify({"error": "Error en la autenticación"}), 401
        
        # Store the token in the session
        session['token'] = token
        return redirect(url_for('get_pacientes'))
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/pacientes', methods=['GET'])
def get_pacientes():
    # Check if the user is authenticated by verifying the token in the session
    token = session.get('token')
    if not token:
        return jsonify({"error": "Acceso no autorizado"}), 401
    
    # Return protected data
    pacientes = [
        {"nombre": "Juan Perez", "edad": 30, "enfermedad": "Gripe"},
        {"nombre": "Maria Lopez", "edad": 25, "enfermedad": "Fiebre"}
    ]
    return jsonify(pacientes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
