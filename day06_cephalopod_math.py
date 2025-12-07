import numpy as np
from math import prod


def read_data_06_1(file_name):
    with open(file_name) as my_file:
        input = my_file.read()
    lines = input.split("\n")

    lines = [line.split(" ") for line in lines]
    lines = [[item for item in line if item] for line in lines]
    signs = lines[-1]
    numbers = lines[:-1]
    numbers = [[int(item) for item in line if item] for line in numbers]
    arr = np.array(numbers)

    return signs, arr


def day06_1(signs, arr):
    overall_sum = 0
    for id, sign in enumerate(signs):
        # print(id, sign)
        if sign == "+":
            overall_sum += sum(arr[:, id])
        elif sign == "*":
            overall_sum += prod(arr[:, id])
    return overall_sum


def read_data_06_2(file_name):
    with open(file_name) as my_file:
        input = my_file.read()
    lines = input.split("\n")
    arr = np.array([[char for char in line] for line in lines])
    return arr


def day06_2(arr):
    overall_sum = 0
    temp = 0
    sign = "+"
    for i in range(arr.shape[1]):
        # print(arr[:,i].flatten())
        if "".join(arr[:-1, i].flatten()).strip() == "":
            overall_sum += temp
            # print(temp)
        else:
            if "".join(arr[-1, i].flatten()).strip() == "*":
                sign = "*"
                temp = 1
            elif "".join(arr[-1, i].flatten()).strip() == "+":
                sign = "+"
                temp = 0

            if sign == "*":
                temp *= int("".join(arr[:-1, i].flatten()))
            elif sign == "+":
                temp += int("".join(arr[:-1, i].flatten()))

    return overall_sum + temp


if __name__ == "__main__":

    signs_test, arr_test = read_data_06_1("data/input06_test.txt")
    signs_puzzle, arr_puzzle = read_data_06_1("data/input06_puzzle.txt")

    print("===TEST 1===")
    print(day06_1(signs_test, arr_test))

    print("===PUZZLE 1===")
    print(day06_1(signs_puzzle, arr_puzzle))

    arr_test = read_data_06_2("data/input06_test.txt")
    arr_puzzle = read_data_06_2("data/input06_puzzle.txt")

    print("===TEST 2===")
    print(day06_2(arr_test))

    print("===PUZZLE 2===")
    print(day06_2(arr_puzzle))
