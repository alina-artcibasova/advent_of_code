DIAL_MIN = 0
DIAL_MAX = 99
DIAL_SIZE = DIAL_MAX + 1


def read_data_01(file_name: str) -> list[str]:
    """Read input data for day01."""
    with open(file_name) as my_file:
        input = my_file.read()
    lines = input.splitlines()

    return lines


def calculate_change_and_increment_for_rotation(rotation: str) -> tuple[int, int]:
    """Take in rotation string and calculate corresponding value change (absolute) and an increment (based on direction)."""
    if "L" in rotation:
        change = int(rotation.replace("L", ""))
        increment = -(change % DIAL_SIZE)
    if "R" in rotation:
        change = int(rotation.replace("R", ""))
        increment = change % DIAL_SIZE

    return change, increment


def day01_1_dial_at_0_after_rotation(
    current_position: int, lines: list[str]
) -> tuple[list[tuple[str, int]], int]:
    """Solve first part of the puzzle for day01."""
    zero_counter = 0
    positions = []
    for rotation in lines:
        change, increment = calculate_change_and_increment_for_rotation(rotation)
        new_position = current_position + increment

        if new_position < DIAL_MIN:
            current_position = abs(DIAL_MAX + new_position + 1)
        elif new_position > DIAL_MAX:
            current_position = abs(DIAL_MAX - new_position + 1)
        else:
            current_position = new_position

        positions.append((rotation, current_position, zero_counter))

        if current_position == DIAL_MIN:
            zero_counter += 1

    return positions, zero_counter


def day01_2_dial_at_0_after_any_click(
    current_position: int, lines: list[str]
) -> tuple[list[tuple[str, int]], int]:
    """Solve second part of the puzzle for day01."""
    zero_counter = 0
    positions = []
    for rotation in lines:
        change, increment = calculate_change_and_increment_for_rotation(rotation)
        new_position = current_position + increment
        zero_counter += change // DIAL_SIZE

        if new_position < DIAL_MIN:
            if current_position != 0:
                zero_counter += 1
            current_position = abs(DIAL_MAX + new_position + 1)

        elif new_position > DIAL_MAX:
            current_position = abs(DIAL_MAX - new_position + 1)
            if current_position != 0:
                zero_counter += 1
        else:
            current_position = new_position

        if current_position == DIAL_MIN:
            zero_counter += 1

        positions.append((rotation, current_position, zero_counter))

    return positions, zero_counter


if __name__ == "__main__":
    current_position = 50

    file_name = "data/aoc2025/input01_test.txt"
    lines = read_data_01(file_name)
    # print(lines)

    positions, zero_counter = day01_1_dial_at_0_after_rotation(current_position, lines)
    print("====PART 1====")
    print(positions)
    print(zero_counter)

    positions, zero_counter = _dial_at_0_after_any_click(current_position, lines)
    print("====PART 2====")
    print(positions)
    print(zero_counter)

    # file_name = "data/aoc2025/input01_puzzle.txt"
    # lines = read_data_01(file_name)
    # positions, zero_counter = day01_1_dial_at_0_after_rotation(current_position, lines)
    # print("====PART 1====")
    # # print(positions)
    # print(zero_counter)

    # print("====PART 2====")
    # positions, zero_counter = _dial_at_0_after_any_click(current_position, lines)
    # # print(positions)
    # print(zero_counter)
