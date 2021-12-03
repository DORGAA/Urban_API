
GET_PLAYER_REQUIRED_PARAMS = ["mail"]


def check_params(params_body, required_params):
    """
    Check if required params are in params body
    :param params_body: input
    :param required_params: params array
    """
    missing_param = []
    for param in required_params:
        if param not in params_body:
            missing_param.append(param)
    if missing_param:
        return f'missing parameters : {missing_param}'
    else:
        return ''


def error_response(error, message):
    """
    Format error dictionary
    :param error: error type
    :param message: error message
    :return:
    """
    status_code = 400
    if error == 'ClientError':
        status_code = 400
    elif error == 'ServerError':
        status_code = 500
    elif error == 'ClientErrorNotFound':
        status_code = 404
    return {
        error: message
    }, status_code
