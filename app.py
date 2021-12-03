from flask import request
from crud_player import get_player, get_players
from flask_server import app
from utils import check_params, error_response
from utils import GET_PLAYER_REQUIRED_PARAMS


@app.route("/ping")
def ping():
    return {"ping": "pong"}, 200


@app.route("/player", methods=['POST', 'GET', 'DELETE', 'PUT'])
def player():
    if request.method == 'GET':
        body = request.args
        if not body:
            return get_players(), 200
        else:
            result = check_params(body, GET_PLAYER_REQUIRED_PARAMS)
            if result == '':
                response = get_player(body.get("mail"))
                return response, 200
            else:
                return error_response('ClientError', result)
    if request.method == 'POST':
        body = request.json
        return body, 201
    if request.method == 'DELETE':
        body = request.args
        return {}, 204
    if request.method == 'PUT':
        body = request.json
        return {}, 204
