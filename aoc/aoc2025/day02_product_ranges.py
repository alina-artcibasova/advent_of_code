def read_data_02(file_name):
    """Read input data for day02."""
    with open(file_name) as my_file:
        ids = my_file.read()
    return ids.split(",")


def day02_1(ids):
    """Solve first part of the puzzle for day01."""
    invalid_ids = []

    for id_range in ids:
        start, end = (int(item) for item in id_range.split("-"))
        # print(id_range)
        for i in range(start, end + 1):
            if len(str(i)) % 2 == 0:
                half = len(str(i)) // 2
                first_half = str(i)[:half]
                second_half = str(i)[half:]
                if first_half == second_half:
                    invalid_ids.append(i)

    return invalid_ids


def day02_2(ids):
    """Solve second part of the puzzle for day02."""
    invalid_ids = set()

    for id_range in ids:
        start, end = (int(item) for item in id_range.split("-"))
        # print(id_range)
        for i in range(start, end + 1):
            # print(i)
            half = len(str(i)) // 2 + 1
            for span in range(1, half):
                if len(str(i)) % span == 0:
                    construct = str(i)[:span] * int(len(str(i)) / span)
                    if construct == str(i):
                        invalid_ids.add(i)

    return invalid_ids


if __name__ == "__main__":
    file_name = "data/aoc2025/input02_test.txt"
    ids = read_data_02(file_name)
    invalid_ids = day02_1(ids)
    print("===TEST 1===")
    print(invalid_ids)
    print(sum(invalid_ids))

    file_name = "data/aoc2025/input02_puzzle.txt"
    ids = read_data_02(file_name)
    invalid_ids = day02_1(ids)
    print("===PUZZLE 1===")
    # print(invalid_ids)
    print(sum(invalid_ids))

    file_name = "data/aoc2025/input02_test.txt"
    ids = read_data_02(file_name)
    invalid_ids = day02_2(ids)
    print("===TEST 2===")
    print(invalid_ids)
    print(sum(invalid_ids))

    file_name = "data/aoc2025/input02_puzzle.txt"
    ids = read_data_02(file_name)
    invalid_ids = day02_2(ids)
    print("===PUZZLE 2===")
    # print(invalid_ids)
    print(sum(invalid_ids))
