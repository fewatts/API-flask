from flask import Flask, make_response, jsonify, request
from BD import Carros 
app = Flask(__name__)


@app.route('/carros', methods=['GET'])
def get_carros():
    return make_response(
        jsonify(Carros)
    )


@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json
    return carro


app.run()
