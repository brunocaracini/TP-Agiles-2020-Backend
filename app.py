import os
import json
from flask import Flask, request, session, jsonify
from flask_session import Session 
from flask_cors import CORS, cross_origin
from controller import Controller

port = int(os.environ.get("PORT", 5000))

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

CORS(app, supports_credentials=True)
Session(app)

@app.route('/iniciar', methods=['POST'])
def iniciar_partida():
    session['juego'] = Controller.iniciar_partida(json.loads(request.data)['nombre'])
    return jsonify(session['juego'].getEstado())


@app.route('/enviar-letra', methods=['POST'])
def enviar_letra():
    j = Controller.enviar_letra(str(json.loads(request.data)['letra']), session.get('juego'))
    session['juego'] = j
    return jsonify(j.getEstado())

@app.route('/enviar-palabra', methods=['POST'])
def enviar_palabra():
    j = Controller.enviar_palabra(str(json.loads(request.data)['palabra']), session.get('juego'))
    return jsonify(j.getEstado())




app.run(host='0.0.0.0', port=port, debug=True)
