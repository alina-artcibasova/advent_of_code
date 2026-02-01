from aoc.aoc2025.day02_product_ranges import (
    read_data_02,
    day02_1,
    day02_2,
)
import pytest
import os


@pytest.fixture
def test_input():
    return [
        "11-22",
        "95-115",
        "998-1012",
        "1188511880-1188511890",
        "222220-222224",
        "1698522-1698528",
        "446443-446449",
        "38593856-38593862",
        "565653-565659",
        "824824821-824824827",
        "2121212118-2121212124",
    ]


def test_read_data_02(test_input):
    read_lines = read_data_02(os.getcwd() + "/data/aoc2025/input02_test.txt")
    assert read_lines == test_input
