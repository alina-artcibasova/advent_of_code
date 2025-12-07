def day05_1(fresh_ranges, available):
    fresh_available = set()
    for ingredient in available:
        for start, end in fresh_ranges:
            if ingredient >= start and ingredient <= end:
                fresh_available.add(ingredient)

    return len(fresh_available)


def combine_fresh_ranges(fresh_ranges):
    new_ranges = []
    id = 0
    while id < len(fresh_ranges) - 1:
        if fresh_ranges[id][1] >= fresh_ranges[id + 1][0]:
            new_val = (
                fresh_ranges[id][0],
                max(fresh_ranges[id][1], fresh_ranges[id + 1][1]),
            )
            new_ranges.append(new_val)
            # print(f"merging {fresh_ranges[id]} and {fresh_ranges[id+1]} into {new_val}")
            id += 2
        else:
            new_ranges.append(fresh_ranges[id])
            # print(f"appending {fresh_ranges[id]}")
            id += 1
    if fresh_ranges[-1][1] > new_ranges[-1][1]:
        new_ranges.append(fresh_ranges[-1])
    # print(f"new fresh_ranges length is {len(new_ranges)}")
    return sorted(new_ranges)


def day05_2(fresh_ranges):
    while True:
        fresh_ranges_previous_len = len(fresh_ranges)
        fresh_ranges = combine_fresh_ranges(fresh_ranges)
        # print(fresh_ranges_previous_len)
        # print(fresh_ranges)
        if len(fresh_ranges) == fresh_ranges_previous_len:
            break

    return sum([end - start + 1 for start, end in fresh_ranges])


if __name__ == "__main__":

    file_name = "data/input05_test.txt"
    with open(file_name) as my_file:
        input_5_test = my_file.read()

    lines_test = input_5_test.split("\n")
    fresh_ranges_str_test = [line for line in lines_test if ("-" in line)]
    fresh_ranges_test = [
        tuple(int(number) for number in range_str.split("-"))
        for range_str in fresh_ranges_str_test
    ]
    fresh_ranges_test = sorted(fresh_ranges_test)
    available_test = [int(line) for line in lines_test if (line) and ("-" not in line)]
    available_test = sorted(available_test)

    file_name = "data/input05_puzzle.txt"
    with open(file_name) as my_file:
        input_5_puzzle = my_file.read()

    lines_puzzle = input_5_puzzle.split("\n")
    fresh_ranges_str_puzzle = [line for line in lines_puzzle if ("-" in line)]
    fresh_ranges_puzzle = [
        tuple(int(number) for number in range_str.split("-"))
        for range_str in fresh_ranges_str_puzzle
    ]
    fresh_ranges_puzzle = sorted(fresh_ranges_puzzle)
    available_puzzle = [
        int(line) for line in lines_puzzle if (line) and ("-" not in line)
    ]
    available_puzzle = sorted(available_puzzle)

    print("===TEST 1===")
    print(day05_1(fresh_ranges_test, available_test))

    print("===PUZZLE 1===")
    print(day05_1(fresh_ranges_puzzle, available_puzzle))

    print("===TEST 2===")
    print(day05_2(fresh_ranges_test))

    print("===PUZZLE 2===")
    print(day05_2(fresh_ranges_puzzle))
