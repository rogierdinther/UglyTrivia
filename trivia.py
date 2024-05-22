#!/usr/bin/env python3

# 

# Refactors:
# * Game class naar eigen file zetten zodat deze van de main functie kan worden
# - De Game class bewaard data over spelers in parallele arrays. Die kunnen naar een Player class
# - Mogelijk kan ook informatie over de indeling van het bord hier weg

from random import randrange
from game import Game

if __name__ == '__main__':
    not_a_winner = False

    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while True:
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()

        if not not_a_winner: break
