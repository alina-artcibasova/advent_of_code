from itertools import combinations


def day03_1(lines):
    sum_of_joltages = 0
    for line in lines:
        sum_of_joltages += battery_2(line)
    return sum_of_joltages


def battery_2(line):
    possible_joltages_for_array = set()
    for comb in combinations(line, 2):
        joltage = "".join(comb)
        possible_joltages_for_array.add(int(joltage))
    return max(possible_joltages_for_array)


def day03_2(lines):
    sum_of_joltages = 0
    for line in lines:
        joltage = battery_12(line)
        sum_of_joltages += joltage
    return sum_of_joltages


def best_next(line, length):
    best = (0, line[0])
    for i, battery in enumerate(line):
        if (battery > best[1]) and (i < len(line) - length + 1):
            best = (i, battery)
    return best


def battery_12(line):
    best_rack = ""
    length = 12
    while length > 0:
        best_next_index, best_next_battery = best_next(line, length)
        line = line[best_next_index + 1 :]
        length -= 1
        best_rack += best_next_battery
    return int(best_rack)


if __name__ == "__main__":

    file_name = "data/input03_test.txt"
    with open(file_name) as my_file:
        input_3_test = my_file.read()

    file_name = "data/input03_puzzle.txt"
    with open(file_name) as my_file:
        input_3_puzzle = my_file.read()

    print("===TEST 1===")
    lines = input_3_test.split("\n")
    print(day03_1(lines))

    print("===PUZZLE 1===")
    lines = input_3_puzzle.split("\n")
    print(day03_1(lines))

    print("===TEST 1===")
    lines = input_3_test.split("\n")
    print(day03_2(lines))

    print("===PUZZLE 1===")
    lines = input_3_puzzle.split("\n")
    print(day03_2(lines))
