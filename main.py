import unittest

class calculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(sum([1, 2, 3,  4]), 10, "Resultado esperado: 10")

    def test_subtracao(self):
        self.assertEqual(10 - 5, 5, "Resultado esperado: 5")

    def test_multiplicacao(self):
        self.assertEqual(3 * 4, 12, "Resultado esperado: 12")

    def test_divisao(self):
        self.assertEqual(15 / 5, 3, "Resultado esperado: 3")

    def test_modulo(self):
        self.assertEqual(10 % 3, 1, "Resultado esperado: 1")

if __name__ == '__main__':
    unittest.main()