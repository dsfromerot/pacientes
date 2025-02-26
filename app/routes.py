from flask import jsonify
from app.config import app, oidc

# Datos hardcodeados de pacientes
pacientes = [
    {"nombre": "Juan Perez", "edad": 30, "enfermedad": "Gripe"},
    {"nombre": "Maria Lopez", "edad": 25, "enfermedad": "Fiebre"},
    {"nombre": "Carlos Sanchez", "edad": 40, "enfermedad": "Diabetes"}
]

@app.route('/pacientes', methods=['GET'])
@oidc.accept_token(True)  # Protege el endpoint con Keycloak
def get_pacientes():
    return jsonify(pacientes)
