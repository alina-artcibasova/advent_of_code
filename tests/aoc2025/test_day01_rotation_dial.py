from aoc.aoc2025.day01_rotation_dial import (
    read_data_01,
    day01_1,
    day01_2,
    calculate_change_and_increment_for_rotation,
)
import pytest
import os


@pytest.fixture
def test_input():
    return [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
        "R1000",
        "L1000",
    ]


def test_read_data_01(test_input):
    read_lines = read_data_01(os.getcwd() + "/data/aoc2025/input01_test.txt")
    assert read_lines == test_input


@pytest.mark.parametrize(
    "rotation,change,increment",
    [
        ("L68", 68, -68),
        ("R60", 60, 60),
        ("R1000", 1000, 0),
    ],
)
def test_calculate_change_and_increment_for_rotation(rotation, change, increment):
    assert change, increment == calculate_change_and_increment_for_rotation(rotation)


def test_day01_1(test_input):
    positions, zero_counter = day01_1(50, test_input)
    assert positions == [
        ("L68", 82, 0),
        ("L30", 52, 0),
        ("R48", 0, 0),
        ("L5", 95, 1),
        ("R60", 55, 1),
        ("L55", 0, 1),
        ("L1", 99, 2),
        ("L99", 0, 2),
        ("R14", 14, 3),
        ("L82", 32, 3),
        ("R1000", 32, 3),
        ("L1000", 32, 3),
    ]
    assert zero_counter == 3


def test_day01_2(test_input):
    positions, zero_counter = day01_2(50, test_input)
    assert positions == [
        ("L68", 82, 1),
        ("L30", 52, 1),
        ("R48", 0, 2),
        ("L5", 95, 2),
        ("R60", 55, 3),
        ("L55", 0, 4),
        ("L1", 99, 4),
        ("L99", 0, 5),
        ("R14", 14, 5),
        ("L82", 32, 6),
        ("R1000", 32, 16),
        ("L1000", 32, 26),
    ]
    assert zero_counter == 26


# if __name__ == "__main__":
#     test_read_data_01()
