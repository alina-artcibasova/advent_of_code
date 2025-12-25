import numpy as np


def read_data_07_1(file_name):
    with open(file_name) as my_file:
        input = my_file.read()
    input_strings = input.split("\n")

    input_strings = [[char for char in string] for string in input_strings]
    return np.array(input_strings)


def read_data_07_2(file_name):
    with open(file_name) as my_file:
        input = my_file.read()
    input_strings = input.split("\n")

    input_strings = [
        [char if char != "." else 0 for char in string] for string in input_strings
    ]
    return np.array(input_strings)


def day07_1(input_array):
    x_dim = input_array.shape[0]
    y_dim = input_array.shape[1]

    splits = 0
    # print("".join(input_array[0, :].flatten()))
    for iy in range(1, y_dim + 1):
        for ix in range(x_dim - 1):
            if input_array[iy - 1, ix] == "S":
                input_array[iy, ix] = "|"
            if input_array[iy - 1, ix] == "|":
                if input_array[iy, ix] == ".":
                    input_array[iy, ix] = "|"
                elif input_array[iy, ix] == "^":
                    input_array[iy, ix - 1] = "|"
                    input_array[iy, ix + 1] = "|"
                    splits += 1
        # print("".join(input_array[iy, :].flatten()))
    return splits


def day07_2(input_array):
    x_dim = input_array.shape[0]
    y_dim = input_array.shape[1]

    # print(input_array[0, :].flatten())
    for iy in range(1, y_dim + 1):
        for ix in range(x_dim - 1):
            if input_array[iy - 1, ix] == "S":
                input_array[iy, ix] = 1
            if input_array[iy - 1, ix] != "0" and input_array[iy - 1, ix] != "^":
                if input_array[iy, ix] == "0":
                    input_array[iy, ix] = input_array[iy - 1, ix]
                elif input_array[iy, ix] == "^":
                    if input_array[iy, ix - 1] == "0":
                        input_array[iy, ix - 1] = input_array[iy - 1, ix - 1]
                    if input_array[iy, ix + 1] == "0":
                        input_array[iy, ix + 1] = input_array[iy - 1, ix + 1]
                    input_array[iy, ix - 1] = int(input_array[iy, ix - 1]) + int(
                        input_array[iy - 1, ix]
                    )
                    input_array[iy, ix + 1] = int(input_array[iy, ix + 1]) + int(
                        input_array[iy - 1, ix]
                    )
    # print(input_array[iy, :].flatten())
    return int(sum((input_array[-1, :].astype(int))))


if __name__ == "__main__":

    input_array_test = read_data_07_1("data/input07_test.txt")
    input_array_puzzle = read_data_07_1("data/input07_puzzle.txt")

    print("===TEST 1===")
    print(day07_1(input_array_test))

    print("===PUZZLE 1===")
    print(day07_1(input_array_puzzle))

    input_array_test = read_data_07_2("data/input07_test.txt")
    input_array_puzzle = read_data_07_2("data/input07_puzzle.txt")

    print("===TEST 2===")
    print(day07_2(input_array_test))

    print("===PUZZLE 2===")
    print(day07_2(input_array_puzzle))
