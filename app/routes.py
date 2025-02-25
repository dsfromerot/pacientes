from flask import jsonify
from flask_oidc import OpenIDConnect
from .config import app, oidc

# Datos hardcodeados
pacientes = [
    {"nombre": "Juan Perez", "edad": 30, "enfermedad": "Gripe"},
    {"nombre": "Maria Lopez", "edad": 25, "enfermedad": "Fiebre"}
]

@app.route('/pacientes', methods=['GET'])
@oidc.accept_token(True)
def get_pacientes():
    return jsonify(pacientes)
