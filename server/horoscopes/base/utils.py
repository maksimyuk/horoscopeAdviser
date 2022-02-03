import requests


def send_request(request: requests.Request) -> requests.Response:
    """Returns response after sending request."""
    prepared_request = request.prepare()
    with requests.session() as request_send_session:
        response = request_send_session.send(prepared_request)

    return response
