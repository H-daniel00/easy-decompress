import unittest
import random

from ead import EAD
from ead import ExtensionError

import strgen  # Generador de cadenas de texto aleatorias


def generar_texto_aleatorio(caracteres, rango):
    ancho_cadena = random.randint(rango[0], rango[1])
    texto = strgen.StringGenerator(
        '{}{{{}}}'.format(caracteres, ancho_cadena)).render()
    return texto


class GetNameAndExtTest(unittest.TestCase):
    extensiones = EAD.extensiones

    # Caso ideal
    def test_name_and_ext(self):
        ead = EAD()
        nombre = generar_texto_aleatorio("[ \w]", (1, 100))

        for ext in self.extensiones:
            extension = ext
            nombre_archivo = nombre + '.' + extension
            result = ead.get_name_and_ext(nombre_archivo)
            self.assertEqual(result, (nombre, extension))

    # Extensión desconocida o inexistente
    def test_ext_desconocida(self):
        ead = EAD()
        texto = generar_texto_aleatorio("[ \w]", (1, 100))
        ext = generar_texto_aleatorio("[ \w]", (1, 10))
        # Evita hacer la prueba si por casualidad se genera aleatoriamente
        # una extensión válida
        if ext not in self.extensiones:
            nombre_archivo = texto + '.' + ext
            self.assertRaises(
                ExtensionError, ead.get_name_and_ext, nombre_archivo)

        # Archivo sin extensión
        nombre_archivo = generar_texto_aleatorio("[ \w]", (1, 100))
        self.assertRaises(
            ExtensionError, ead.get_name_and_ext, nombre_archivo)


class AjustarDirectorioFinalText(unittest.TestCase):
    def test_muchos_archivos_obtenidos(self):
        ead = EAD()

        texto = generar_texto_aleatorio("[ \w]", (1, 50))
        lista_archivos = []
        # Hay al menos dos ficheros
        for i in range(random.randint(2, 10)):
            lista_archivos.append(generar_texto_aleatorio("[ \w]", (1, 50)))

        result = ead.ajustar_directorio_final(texto, lista_archivos)
        self.assertEqual(result, texto)

    def test_un_fichero_obtenido(self):
        ead = EAD()
        texto = generar_texto_aleatorio("[ \w]", (1, 50))
        # Lista con un solo elemento
        unico_archivo = generar_texto_aleatorio("[ \w]", (1, 50))
        lista_archivos = [unico_archivo, ]

        result = ead.ajustar_directorio_final(texto, lista_archivos)
        self.assertEqual(result, unico_archivo)




if __name__ == '__main__':
    unittest.main()
