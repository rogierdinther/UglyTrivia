import unittest
from game import Game

class TriviaTest(unittest.TestCase):
    def test_game_can_be_started(self):
        game = Game()
        game.add('Chet')
        game.add('Pat')
        game.add('Sue')

        self.assertEqual(len(game.players), 3)

    def test_can_run_round(self):
        game = Game()
        game.add('Chet')
        game.add('Pat')

        # Roll 6
        game.roll(6)
        game.was_correctly_answered()

        self.assertEqual(game.places[0], 6)
        self.assertEqual(game.purses[0], 1)
        self.assertEqual(game.in_penalty_box[0], 0)

        print("Place: %s" % game.places[0])
        print("Purse: %s" % game.purses[0])
        print("Penalty: %s" % game.in_penalty_box[0])
