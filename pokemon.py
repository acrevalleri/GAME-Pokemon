import random

class Pokemon:
    def __init__(self, especie, level=None, nome=None):
        self.especie = especie
        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        if nome:
            self.nome = nome
        else:
            self.nome = especie


    def __str__(self):
        return "{} ({})".format(self.nome, self.level)


    def atacar(self, pokemon):
        print("{} atacou {}".format(self.especie, pokemon.especie))


class PokemonEletrico(Pokemon):
    tipo = "eletrico"

    def atacar(self, pokemon):
        print("{} lançou o choque do trovao em {}".format(self, pokemon))


class PokemonFogo(Pokemon):
    tipo = "fogo"

    def atacar(self, pokemon):
        print("{} lançou uma bola de fogo em {}".format(self, pokemon))


class PokemonAgua(Pokemon):
    tipo = "agua"

    def atacar(self, pokemon):
        print("{} lançou um jato de agua em {}".format(self, pokemon))


class PokemonTerra(Pokemon):
    tipo = "terra"

    def atacar(self, pokemon):
        print("{} lançou uma rocha em {}".format(self, pokemon))

