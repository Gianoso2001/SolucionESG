import unittest
from src.Logica.EcuancionSegundogrado import EcuacionSegundogrado

class PruebaEcuacionSegundogrado(unittest.TestCase):
    def test_EcuacionSegundogrado_parametrosNumericos_RaicesReales(self):
        # arrange
        a = 3
        b = -5
        c = 1
        x1Esperado = 1.43
        x2Esperado = 0.23

        # do
        eacuacion = EcuacionSegundogrado()
        x1Actual, x2Actual = eacuacion.calculoECS(a, b , c)
        # Asser
        self.assertEqual(x1Esperado, x1Actual)
        self.assertEqual(x2Esperado, x2Actual)


