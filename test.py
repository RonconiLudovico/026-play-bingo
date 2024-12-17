import unittest

from main import bingo_card, bingo_call, play_games

class Test01(unittest.TestCase):
    def test_bingo_card(self):
        '''
        Here we test the bingo_card function to produce the right keys
        '''
        data = ["b", "i", "n", "g", "o"]
        result = list(bingo_card().keys())
        self.assertEqual(data, result)

class Test02(unittest.TestCase):
    def test_bingo_card(self):
        '''
        Here we test the bingo_card function to produce the right length of lists
        '''
        data = 5
        result = bingo_card()["b"]
        self.assertEqual(data, len(result))


class Test03(unittest.TestCase):
    def test_bingo_call(self):
        '''
        Here we test if the bingo_call function produces calls in the right format
        '''
        data1 = type("b")
        data2 = type(1)
        result1 = bingo_call()[0]
        result2 = int(bingo_call()[0][1:])
        self.assertEqual((data1, data2), (type(result1[0]), type(result2)))


class Test04(unittest.TestCase):
    def test_bingo_call(self):
        '''
        Here we test the length of the calls list
        '''
        data = 75
        result = len(bingo_call())
        self.assertEqual(data, result)


class Test05(unittest.TestCase):
    def test_play_games(self):
        '''
        Here we test the function play_games
        '''
        data = True
        result = play_games() in range(0, 76)
        self.assertEqual(data, result)
