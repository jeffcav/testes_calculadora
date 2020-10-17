from flask import Flask, request, jsonify
from calculadora import Calculadora

app = Flask(__name__)

@app.route('/calc', methods=['GET'])
def calc():
    operacao =  request.args.get('oper', default = "soma", type = str)
    a =  request.args.get('a', default = 0.0, type = float)
    b =  request.args.get('b', default = 0.0, type = float)

    print(operacao, a, b)

    calc = Calculadora()
    resultado = 0.0

    if operacao == "soma":
        resultado = calc.soma(a, b)

    return jsonify(resultado=resultado)