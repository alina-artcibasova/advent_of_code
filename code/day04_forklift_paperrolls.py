import numpy as np


def day04_1(input_array, box_size, access_limit, with_replacement):
    y_dim = len(input_array)
    x_dim = len(input_array[0])

    count_accessible = 0
    for i in range(y_dim):
        for j in range(x_dim):
            if input_array[i, j] == "@":
                box = input_array[
                    max(0, i - box_size) : min(y_dim, i + box_size + 1),
                    max(0, j - box_size) : min(x_dim, j + box_size + 1),
                ]
                if sum(box.flatten() == "@") - 1 < access_limit:
                    count_accessible += 1
                    if with_replacement:
                        input_array[i, j] = "x"

    return count_accessible


def day04_2(input_array, box_size, access_limit, with_replacement):
    total_sum = 0
    while True:
        accessible_current = day04_1(
            input_array, box_size, access_limit, with_replacement
        )
        total_sum += accessible_current
        if accessible_current == 0:
            break

    return total_sum


if __name__ == "__main__":

    file_name = "data/input04_test.txt"
    with open(file_name) as my_file:
        input_4_test = my_file.read()

    input_4_test_strings = input_4_test.split("\n")
    input_4_test_strings = [
        [char for char in string] for string in input_4_test_strings
    ]
    input_array_test = np.array(input_4_test_strings)

    file_name = "data/input04_puzzle.txt"
    with open(file_name) as my_file:
        input_4_puzzle = my_file.read()

    input_4_puzzle_strings = input_4_puzzle.split("\n")
    input_4_puzzle_strings = [
        [char for char in string] for string in input_4_puzzle_strings
    ]
    input_array_puzzle = np.array(input_4_puzzle_strings)

    box_size = 1
    access_limit = 4

    print("===TEST 1===")
    print(day04_1(input_array_test, box_size, access_limit, with_replacement=False))

    print("===PUZZLE 1===")
    print(day04_1(input_array_puzzle, box_size, access_limit, with_replacement=False))

    print("===TEST 1===")
    print(day04_2(input_array_test, box_size, access_limit, with_replacement=True))

    print("===PUZZLE 1===")
    print(day04_2(input_array_puzzle, box_size, access_limit, with_replacement=True))
