import os
import json
from flask import Flask, request, session, jsonify
from flask_session import Session 
from flask_cors import CORS
from controller import Controller

##### CONFIG #####
port = int(os.environ.get("PORT", 5000))

app = Flask(__name__)
app.secret_key = 'SecretKeyForSigningCookies'
app.config['SESSION_TYPE'] = 'filesystem'

CORS(app, supports_credentials=True)
Session(app)


##### ROUTES #####
@app.route('/api/', methods=['GET'])
def test():
    return jsonify({ 'message': 'Servidor iniciado!' })

@app.route('/api/iniciar', methods=['POST'])
def iniciar_partida():
    nombreJugador = json.loads(request.data)['nombre']
    dificultad = json.loads(request.data)['dificultad']
    session['juego'] = Controller.iniciar_partida(nombreJugador, dificultad)
    return jsonify(session['juego'].getEstado())


@app.route('/api/enviar-letra', methods=['POST'])
def enviar_letra():
    letra = str(json.loads(request.data)['letra'])
    j = Controller.enviar_letra(letra, session.get('juego'))
    session['juego'] = j
    return jsonify(j.getEstado())

@app.route('/api/enviar-palabra', methods=['POST'])
def enviar_palabra():
    palabra = str(json.loads(request.data)['palabra'])
    j = Controller.enviar_palabra(palabra, session.get('juego'))
    return jsonify(j.getEstado())

@app.route('/api/ver-ranking', methods=['POST'])
def ver_rankig():
    return jsonify(Controller.get_ranking())

app.run(host='0.0.0.0', port=port, debug=True)
