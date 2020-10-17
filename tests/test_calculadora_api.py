import requests
import json

def test_soma_0ponto5():
    url = 'http://127.0.0.1:5000/calc?oper=soma&a=0.2&b=0.3'

    resp = requests.get(url)

    assert resp.status_code == 200

    resp_body = resp.json()
    assert resp_body['resultado'] == 0.5