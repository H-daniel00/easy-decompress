import subprocess


class EAD(object):
    extensiones = ['tar.gz', 'zip']

    def get_name_and_ext(self, filename):
        """Separa el nombre y la extensión del archivo"""

        return ('comprimido', 'tar.gz')

    def obtener_descompresor(self, extension):
        """Verifica la existencia de un compresor que pueda trabajar con el
        tipo de archivo relacionado a la extensión y retorna la ruta del
        ejecutable con los argumentos básicos necesarios para la descompresión
        """

        return '/bin/tar xvf {compressed} -C {outdir}'

    def ajustar_directorio_final(self, lista_archivos_descomprimidos):
        """Ajusta el directorio final, de modo que todo quede dentro de un
        directorio.
        """

        return 'comprimido'

    def validar_existencia_archivo(self, filename):
        """Valida la existencia del archivo en el directorio actual"""

        return True

    def verificar_disponibilidad_directorio_tmp(self, dirname):
        """Verifica si el directorio temporal de destino está disponible
        (no existe)"""

        return True

    def crear_directorio_salida(self, nombre_directorio):
        cmd = 'mkdir ' + nombre_directorio
        results = subprocess.run(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if results.returncode > 0:
            raise Exception(results.stderr)

    def descomprimir(self, filename):
        if not self.validar_existencia_archivo:
            raise Exception(
                'El archivo especificado no existen en el directorio actual')

        partes_archivo = self.get_name_and_ext(filename)
        if not partes_archivo:
            raise Exception('No hay soporte para el archivo indicado')

        descompresor = self.obtener_descompresor(partes_archivo[1])
        if not descompresor:
            raise Exception(
                'No se encontró un comando para descomprimir el archivo')

        nombre_archivo = partes_archivo[0]
        if not self.verificar_disponibilidad_directorio_tmp(nombre_archivo):
            raise Exception(
                'Esta utilidad no puede funcionar si existe un '
                'directorio "{}"'.format(nombre_archivo))

        self.crear_directorio_salida(nombre_archivo)
        cmd = descompresor.format(compressed=filename, outdir=nombre_archivo)
        print(cmd)
        # results = subprocess.run(
        #     cmd, shell=True, stdout=subprocess.PIP, stderr=subprocess.PIPE)
        # results.check_returncode()


if __name__ == '__main__':
    ead = EAD()
    ead.descomprimir('comprimido.tar.gz')
