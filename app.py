from flask import request, jsonify
from crud_player import get_player, get_players, delete_player, create_player, update_player
from flask_server import app
from utils import check_params, error_response
from utils import GET_PLAYER_REQUIRED_PARAMS
import json


@app.route("/ping")
def ping():
    return {"ping": "pong"}, 200


@app.route("/player", methods=['POST', 'GET', 'DELETE', 'PUT'])
def player():
    if request.method == 'GET':
        # args : MultiDict of strings
        body = request.args
        if not body:
            return get_players(), 200
        else:
            result = check_params(json.dumps(body), GET_PLAYER_REQUIRED_PARAMS)
            if result == '':
                response = get_player(body.get("mail"))
                return json.dumps(response), 200
            else:
                return error_response('ClientError', result)

    if request.method == 'POST':
        body = request.json
        if body:
            response = create_player(body.get("mail"), body.get("name"), body.get("organiser"))
            return 'Player added', 200
        else:
            return error_response('ServerError', response)

    if request.method == 'DELETE':
        param = request.args
        if not param:
            return error_response('ClientError', param)
        else:
            result = check_params(param, GET_PLAYER_REQUIRED_PARAMS)
            if result == '':
                response = delete_player(param.get('mail'))
                return response, 200
            else:
                return error_response('ServerError', response)

        return delete_player(body), 204

    if request.method == 'PUT':
        body = request.json
        return {}, 204


@app.route("/match", methods=['POST', 'GET', 'DELETE', 'PUT'])
def match():
    if request.method == 'GET':

        return {}

    if request.method == 'POST':
        return {}

    if request.method == 'DELETE':
        return {}

    if request.method == 'PUT':
        return {}


@app.route("/team", methods=['POST', 'GET', 'DELETE', 'PUT'])
def team():
    if request.method == 'GET':

        return {}

    if request.method == 'POST':
        return {}

    if request.method == 'DELETE':
        return {}

    if request.method == 'PUT':
        return {}
