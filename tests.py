import unittest
from main import karatsuba

class Teste(unittest.TestCase):

    def teste_numeros_pequeno(self):
        self.assertEqual(karatsuba(12, 24, 2), 12 * 24)
        self.assertEqual(karatsuba(7, 8, 1), 7 * 8)

    def teste_numeros_grandes(self):
        self.assertEqual(karatsuba(12345678, 87654321, 8), 12345678 * 87654321)
        self.assertEqual(karatsuba(9999991, 999983, 7), 9999991 * 999983)

    def teste_potencias_de_dez(self):
        self.assertEqual(karatsuba(12345, 100000, 5), 12345 * 100000)
        self.assertEqual(karatsuba(10000, 10000, 5), 10000 * 10000)

    def teste_zero_e_identidade(self):
        self.assertEqual(karatsuba(54321, 0, 4), 0)
        self.assertEqual(karatsuba(54321, 1, 4), 54321)

    def teste_negativos(self):
        self.assertEqual(karatsuba(1234, -5678, 4), 1234 * -5678)
        self.assertEqual(karatsuba(-1234, -5678, 4), -1234 * -5678)

if __name__ == '__main__':
    unittest.main()