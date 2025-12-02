def read_data(file_name):
    with open(file_name) as my_file:
        lines = my_file.readlines()
    
    lines = [line.replace("\n", "") for line in lines]

    return lines

def day01_1(current_position, lines):
    zero_counter = 0
    positions = []
    for line in lines:
        if "L" in line:
            increment = int(line.replace("L", "")) % 100
            new_position = current_position - increment
        if "R" in line:
            increment = int(line.replace("R", "")) % 100
            new_position = current_position + increment

        if new_position < 0:
            current_position = abs(99 + new_position + 1)
        elif new_position > 99:
            current_position = abs(99 - new_position + 1)
        else:
            current_position = new_position

        positions.append((line, current_position))

        if current_position == 0:
            zero_counter += 1

    return positions, zero_counter


def day01_2(current_position, lines):
    zero_counter = 0
    positions = []
    for line in lines:
        if "L" in line:
            change = int(line.replace("L", ""))
            increment = - ( change % 100 )
        if "R" in line:
            change = int(line.replace("R", ""))
            increment = change % 100
        new_position = current_position + increment
        zero_counter += change // 100

        if new_position < 0:
            if current_position != 0:
                zero_counter += 1
            current_position = abs(99 + new_position + 1)
            
        elif new_position > 99:
            current_position = abs(99 - new_position + 1)
            if current_position != 0:
                zero_counter += 1
        else:
            current_position = new_position
        

        if current_position == 0:
            zero_counter += 1

        positions.append((line, current_position, zero_counter))


    return positions, zero_counter


if __name__ == "__main__":
    current_position = 50

    file_name = "data/input01_test.txt"
    lines = read_data(file_name)
    
    positions, zero_counter = day01_1(current_position, lines)
    print("====PART 1====")
    print(positions)
    print(zero_counter)

    positions, zero_counter = day01_2(current_position, lines)
    print("====PART 2====")
    print(positions)
    print(zero_counter)

    file_name = "data/input01_puzzle.txt"
    lines = read_data(file_name)
    positions, zero_counter = day01_1(current_position, lines)
    print("====PART 1====")
    # print(positions)
    print(zero_counter)

    print("====PART 2====")
    positions, zero_counter = day01_2(current_position, lines)
    # print(positions)
    print(zero_counter)



        