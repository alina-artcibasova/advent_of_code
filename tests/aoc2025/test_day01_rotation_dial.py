from aoc.aoc2025.day01_rotation_dial import read_data_01, day01_1
import pytest
import os

def test_read_data_01():
    read_lines = read_data_01(os.getcwd() + "/data/aoc2025/input01_test.txt")
    expected_lines = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82', 'R1000', 'L1000']
    assert read_lines == expected_lines

def test_day01_1():
    test_input = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82', 'R1000', 'L1000']
    positions, zero_counter = day01_1(50, test_input)
    assert positions == [('L68', 82), ('L30', 52), ('R48', 0), ('L5', 95), ('R60', 55), ('L55', 0), ('L1', 99), ('L99', 0), ('R14', 14), ('L82', 32), ('R1000', 32), ('L1000', 32)]
    assert zero_counter == 3

# if __name__ == "__main__":
#     test_read_data_01()