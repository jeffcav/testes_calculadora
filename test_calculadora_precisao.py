import unittest
from calculadora import CalculadoraPrecisao

class TestCalculadoraPrecisao(unittest.TestCase):
    def test_soma_simples(self):
        a = CalculadoraPrecisao(6)
        self.assertEqual(a.soma(10, 20), 30)

    def test_soma_0_24(self):
        a = CalculadoraPrecisao(6)
        self.assertEqual(a.soma(0.2, 0.04), 0.24)
