from flask import Flask, jsonify

app = Flask(__name__)

pacientes = [
    {"nombre": "Juan Perez", "edad": 30, "enfermedad": "Gripe"},
    {"nombre": "Maria Lopez", "edad": 25, "enfermedad": "Fiebre"}
]

@app.route('/pacientes', methods=['GET'])
def get_pacientes():
    return jsonify(pacientes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
