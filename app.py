import os
import flask
from flask_cors import CORS, cross_origin

port = int(os.environ.get("PORT", 5000))

app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
def hello():
    return 'Esto merece una birra!'

app.run(host='0.0.0.0', port=port, debug=True)
