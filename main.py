import click


###############################################################
#  Utilidad para descomprimir archivos en distintos formatos  #
###############################################################

@click.command()
@click.argument('filename')
def cli(filename):
    """Easy Decompress"""
    click.echo('nombre archivo: ' + filename)


if __name__ == '__main__':
    cli()
