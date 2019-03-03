import unittest
import random

from ead import EAD

import strgen  # Generador de cadenas de texto aleatorias


def generar_texto_aleatorio(caracteres, rango):
    ancho_cadena = random.randint(rango[0], rango[1])
    texto = strgen.StringGenerator(
        '{}{{{}}}'.format(caracteres, ancho_cadena)).render()
    return texto


class EADTest(unittest.TestCase):
    def test_get_name_and_ext(self):
        ead = EAD()
        nombre = generar_texto_aleatorio("[ \w]", (1, 100))
        extension = 'tar.gz'
        nombre_archivo = nombre + '.' + extension
        result = ead.get_name_and_ext(nombre_archivo)
        self.assertEqual(result, (nombre, extension))


if __name__ == '__main__':
    unittest.main()
