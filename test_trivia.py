from UglyTrivia.game import Game

class TestTrivia():
    # def test_game_can_be_started(self):
    #     game = Game()
    #     game.add('Chet')
    #     game.add('Pat')
    #     game.add('Sue')

    #     self.assertEqual(len(game.players), 3)

    # def test_can_run_round(self):
    #     game = Game()
    #     game.add('Chet')
    #     game.add('Pat')

    #     # Roll 6
    #     game.roll(6)
    #     game.was_correctly_answered()

    #     self.assertEqual(game.places[0], 6)
    #     self.assertEqual(game.purses[0], 1)
    #     self.assertEqual(game.in_penalty_box[0], 0)

    #     print("Place: %s" % game.places[0])
    #     print("Purse: %s" % game.purses[0])
    #     print("Penalty: %s" % game.in_penalty_box[0])

    def test_log_1(self, capsys):
        game = Game()
        game.add('Chet')
        game.add('Pat')
        
        # Round 1
        game.roll(6)
        game.was_correctly_answered()

        game.roll(4)
        game.was_correctly_answered()

        # Round 2
        game.roll(6)
        game.was_correctly_answered()

        game.roll(6)
        game.wrong_answer()

        # Round 3
        game.roll(6)
        game.was_correctly_answered()

        game.roll(5)
        game.was_correctly_answered()

        captured = capsys.readouterr()
        
        with open('result_1.txt', 'r') as result:
            assert captured.out == result.read()

    def test_log_2(self, capsys):
        game = Game()
        game.add('Chet')

        # Round 1
        game.roll(2)
        game.wrong_answer()

        # Round 2
        game.roll(4)
        game.was_correctly_answered()

        captured = capsys.readouterr()
        
        with open('result_2.txt', 'r') as result:
            assert captured.out == result.read()
