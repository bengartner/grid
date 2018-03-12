from mock import *
import unittest

import grid


class TestGrid(unittest.TestCase):
    def test_place(self):
        board = grid.Board()
        board.place('*', 'H8')
        self.assertEqual('*', board.get((7,7)))

    def test_unit_damage(self):
        unit = grid.Unit(3)
        unit.damage()
        self.assertEqual(2, unit.get_hp())

    def test_set_unit(self):
        board = grid.Board()
        attacker = grid.Unit(3)
        victim = grid.Unit(3)
        board.place(attacker, 'A1')
        board.place(victim, 'B1')
        board.set_attack(attacker, 1, 0)
        board.execute_attacks()
        self.assertEqual(2, victim.get_hp())