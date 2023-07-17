import click

@click.command()
@click.option("-q", "--quadrado", type=int, required=True)
def quadradoNum(quadrado):
    result = quadrado ** 2
    click.echo(result)


@click.command()
@click.option("-d", "--dobro", type=int, required=True)
def dobro_num(dobro):
    result = dobro * 2
    click.echo(result)


@click.command()
@click.option("-p", "--positivo", type=int, required=True)
def verifica_positivo(positivo):
    if positivo > 0:
        click.echo(f"O número {positivo} é positivo")
    else:
        click.echo(f"O número {positivo} é negativo")


@click.command()
@click.option("-z", "--zero", type=int, required=True)
def verifica_maior_zero(z):
    if z > 0:
        click.echo(f"O número {z} é maior que zero")
    else:
        click.echo(f"O número {z} é menor que zero")


def main():
    quadradoNum()
    dobro_num()
    verifica_positivo()
    verifica_maior_zero()


if __name__ == '__main__':
    main()