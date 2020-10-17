import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def test_soma_simples(self):
        a = Calculadora()
        self.assertEqual(a.soma(10, 20), 30)

    def test_soma_0ponto24(self):
        a = Calculadora()
        self.assertEqual(a.soma(0.2, 0.04), 0.24)

