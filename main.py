import click
from ead import EAD


###############################################################
#  Utilidad para descomprimir archivos en distintos formatos  #
###############################################################

@click.command()
@click.argument('filename')
def cli(filename):
    """Easy Decompress"""
    ead = EAD()
    ead.descomprimir(filename)


if __name__ == '__main__':
    cli()
