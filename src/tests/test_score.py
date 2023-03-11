import unittest
from src.model.score import Score


class TestScore(unittest.TestCase):
    def setUp(self):
        self.score = Score()

    def test_get_player_move(self):
        score_vals = self.score.get_stats()
        self.assertEqual(score_vals[0], score_vals[1] + score_vals[2] + score_vals[3])
