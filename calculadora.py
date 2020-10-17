class Calculadora:
    def soma(self, a, b):
        return a + b

class CalculadoraPrecisao:
    def __init__(self, precisao):
        self.precisao = precisao

    def soma(self, a, b):
        resultado = a + b

        resultado_inteiro = int(resultado * (10.0**self.precisao))
        return resultado_inteiro * (10.0**-self.precisao)