from pokemon import *
from pessoa import *


def escolher_pokemon(player):
    print("Olá {}, você deve escolher o pokemon que ira te acompanhar nesta jornada".format(player))

    pikachu = PokemonEletrico("Pikachu", level=1)
    charmander = PokemonFogo("Charmander", level=1)
    squirtle = PokemonAgua("Squirtle", level=1)

    print("Voce possui tres opçoes de pokemons:")
    print("1 -", pikachu)
    print("2 -", charmander)
    print("3 -", squirtle)

    while True:
        escolha = input("Qual a sua escolha?")

        if escolha == "1":
            player.capturar_pokemon(pikachu)
            break
        elif escolha == "2":
            player.capturar_pokemon(charmander)
            break
        elif escolha == "3":
            player.capturar_pokemon(squirtle)
            break
        else:
            print("Escolha invalida!")

player = Player("lucas")

player.capturar_pokemon(PokemonFogo("charmander", level=1))
inimigo1 = inimigo("James", Pokemons=[PokemonTerra("squirtle", level=1)])

player.batalhar(inimigo1)