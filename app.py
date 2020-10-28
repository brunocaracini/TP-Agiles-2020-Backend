import os
import json
from flask import Flask, request, session, jsonify
from flask_session import Session 
from flask_cors import CORS, cross_origin
from clases import Juego

port = int(os.environ.get("PORT", 5000))

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)

@app.route('/iniciar', methods=['POST'])
def iniciar_partida():
    nombre = json.loads(request.data)['nombre']
    j = Juego(nombre)
    j.iniciar()

    session['juego'] = j 

    return jsonify(j.getEstado())


@app.route('/enviar-letra', methods=['POST'])
def enviar_letra():
    j = session.get('juego')
    letra = str(json.loads(request.data)['letra'])

    j.arriesgarLetra(letra)

    return jsonify(j.getEstado())




app.run(host='0.0.0.0', port=port, debug=True)
