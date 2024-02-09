import random

from pokemon import *

Nomes = ["lucas", "jessie", "james", "mario", "enzo", "jubileu", "matheus", "junior", "douglas", "jason", "ram", "bob"]


Pokemons_l = [
    PokemonEletrico("pikachu"),
    PokemonEletrico("electrobuzz"),
    PokemonEletrico("voltorb"),
    PokemonFogo("charmander"),
    PokemonFogo("growlithe"),
    PokemonFogo("ponyta"),
    PokemonAgua("squirtle"),
    PokemonAgua("poliwag"),
    PokemonAgua("cavala"),
    PokemonTerra("bulbassauro"),
    PokemonTerra("sandshrew"),
    PokemonTerra("diglet")
]

class Pessoa:

    def __init__(self, nome=None, Pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(Nomes)

        self.Pokemons = Pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.Pokemons:
            print("mostrando Pokemons de {}".format(self))
            for pokemon in self.Pokemons:
                print(pokemon)
        else:
            print("{} nao possui nenhum pokemon".format(self))


    def escolher_pokemon(self):
        self.mostrar_pokemons()


    def batalhar(self, pessoa):
        print("{} iniciou uma batalha com {}".format(self, pessoa))



class Player(Pessoa):
    tipo = "Player"

    def capturar_pokemon(self,pokemon):
        self.Pokemons.append(pokemon)
        print("{} capturou {}!".format(self, pokemon))


class inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, Pokemons=[]):
        if not Pokemons:
            for i in range(1, 4):
                Pokemons.append(random.choice(Pokemons_l))
        super().__init__(nome=nome, Pokemons=Pokemons)
