from unittest import TestCase
from asteroids import *


class TestFindNthVaporized(TestCase):
    def test_sample_1(self):
        asteroids = parse_input('''
            .#....#####...#..
            ##...##.#####..##
            ##...#...#.#####.
            ..#.....#...###..
            ..#.#.....#....##
            ''')
        position = (8, 3)
        self.assertEqual(find_nth_vaporized(asteroids, position, 1), (8, 1))
        self.assertEqual(find_nth_vaporized(asteroids, position, 9), (15, 1))

    def test_sample_2(self):
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
        position = (11, 13)
        self.assertEqual(find_nth_vaporized(asteroids, position, 200), (8, 2))

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

class TestGroupByAngle(TestCase):
    def test_sample_1(self):
        asteroids = parse_input('''
            .#..#
            .....
            #####
            ....#
            ...##
            ''')
        self.assertEqual(group_by_angle(asteroids, (4, 3)), [
            [(4, 2), (4, 0)],
            [(4, 4)],
            [(3, 4)],
            [(0, 2)],
            [(1, 2)],
            [(2, 2)],
            [(3, 2), (1, 0)]])


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

