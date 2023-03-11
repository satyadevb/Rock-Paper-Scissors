import unittest
from src.model.game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_get_move(self):
        output = self.game.get_valid_move('R')
        self.assertEqual(output, 0)
        output = self.game.get_valid_move('P')
        self.assertEqual(output, 1)
        output = self.game.get_valid_move('S')
        self.assertEqual(output, 2)


if __name__ == '__main__':
    unittest.main()
    test = TestGame()
    test.test_get_move()
