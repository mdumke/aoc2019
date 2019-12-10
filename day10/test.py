from unittest import TestCase
from asteroids import *


class TestFindBestPosition(TestCase):
    def test_sample_1(self):
        asteroids = parse_input('''
            ......#.#.
            #..#.#....
            ..#######.
            .#.#.###..
            .#..#.....
            ..#....#.#
            #..#....#.
            .##.#..###
            ##...#..#.
            .#....####
            ''')
        self.assertEqual(find_best_position(asteroids), ((5, 8), 33))

    def test_sample_4(self):
        asteroids = parse_input('''
            .#..##.###...#######
            ##.############..##.
            .#.######.########.#
            .###.#######.####.#.
            #####.##.#.##.###.##
            ..#####..#.#########
            ####################
            #.####....###.#.#.##
            ##.#################
            #####.##.###..####..
            ..######..##.#######
            ####.##.####...##..#
            .#####..#.######.###
            ##...#.##########...
            #.##########.#######
            .####.#.###.###.#.##
            ....##.##.###..#####
            .#.#.###########.###
            #.#.#.#####.####.###
            ###.##.####.##.#..##
            ''')
        self.assertEqual(find_best_position(asteroids), ((11, 13), 210))


class TestCountVisible(TestCase):
    def test_sample_1(self):
        asteroids = parse_input('''
            .#..#
            .....
            #####
            ....#
            ...##
            ''')
        self.assertEqual(count_visible(asteroids), {
            (1, 0): 7,
            (4, 0): 7,
            (0, 2): 6,
            (1, 2): 7,
            (2, 2): 7,
            (3, 2): 7,
            (4, 2): 5,
            (4, 3): 7,
            (3, 4): 8,
            (4, 4): 7})


class TestIsVisible(TestCase):
    def test_1(self):
        asteroids = set([(1, 0), (3, 2), (4, 3)])
        self.assertFalse(is_visible((4, 3), (1, 0), asteroids))

    def test_2(self):
        asteroids = set([(1, 0), (3, 2), (4, 3)])
        self.assertTrue(is_visible((3, 2), (1, 0), asteroids))

    def test_3(self):
        asteroids = set([(1, 0), (3, 2), (4, 3)])
        self.assertTrue(is_visible((1, 0), (3, 2), asteroids))

    def test_4(self):
        asteroids = set([(4, 0), (4, 2), (4, 3)])
        self.assertTrue(is_visible((4, 2), (4, 0), asteroids))

    def test_5(self):
        asteroids = set([(4, 0), (4, 2), (4, 3)])
        self.assertFalse(is_visible((4, 3), (4, 0), asteroids))

    def test_6(self):
        asteroids = set([(0, 2), (0, 3), (0, 6)])
        self.assertFalse(is_visible((0, 2), (0, 6), asteroids))


# class TestIsBlocked(TestCase):
#     def test_no_possible_position_between(self):
#         self.assertFalse(is_blocked((1, 1), (3, 4), (2, 2)))
# 
#     def test_blocked_1(self):
#         self.assertTrue(is_blocked((1, 1), (5, 3), (3, 2)))
# 
#     def test_blocked_2(self):
#         self.assertTrue(is_blocked((1, 1), (6, 1), (3, 1)))
# 
#     def test_linear_dependence_1(self):
#         self.assertFalse(is_blocked((1, 1), (3, 2), (5, 3)))
# 
#     def test_linear_dependence_2(self):
#         self.assertFalse(is_blocked((1, 1), (3, 2), (-1, 0)))
# 
#     def test_from_sample(self):
#         self.assertFalse(is_blocked((1, 0), (3, 2), (4, 3)))


class TestParseInput(TestCase):
    def test_sample_1(self):
        asteroids = '''
            .#..#
            ....#
            ...##
            '''
        self.assertEqual(
            parse_input(asteroids),
            set([(1, 0), (4, 0), (4, 1), (3, 2), (4, 2)]))
