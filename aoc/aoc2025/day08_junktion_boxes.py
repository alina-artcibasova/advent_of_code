import pandas as pd
import numpy as np
from tqdm import tqdm
from math import prod


def read_data_08(file_name):
    with open(file_name) as my_file:
        input = my_file.read()
    input_strings = input.split("\n")

    input_strings = [[int(item) for item in line.split(",")] for line in input_strings]
    return np.array(input_strings)


def calculate_distances(boxes_np):
    box_names = [",".join(box.astype(str)) for box in boxes_np]
    columns = ["box_1", "box_2", "distance"]
    distances_df = pd.DataFrame(columns=columns)

    for box in tqdm(boxes_np):
        box_1 = ",".join(box.astype(str))
        distances = ((boxes_np - box) ** 2).sum(axis=1) ** 0.5
        distances_df = pd.concat(
            [
                distances_df,
                pd.DataFrame(
                    {
                        key: value
                        for key, value in zip(columns, [box_names, box_1, distances])
                    }
                ),
            ]
        )

    distances_df = distances_df[
        distances_df["distance"] > 0.0
    ]  # get rid of self distances
    distances_df = distances_df.sort_values("distance")  # sort by distance
    distances_df = distances_df.iloc[::2, :]  # get rid of repeat rows
    distances_df = distances_df.reset_index(drop=True)  # reset index for readability

    return distances_df


def day08_1(boxes_np, limit=1000):

    distances_df = calculate_distances(boxes_np)

    connection_count = 1
    row_id = 0
    # print(row_id, distances_df.iloc[row_id].values)
    circuits = [
        [distances_df.iloc[row_id]["box_1"], distances_df.iloc[row_id]["box_2"]]
    ]
    pbar = tqdm(total=limit)

    row_id += 1
    while connection_count < limit:
        # print(row_id, distances_df.iloc[row_id].values)
        # while row_id < distances_df.shape[0]:

        box_1_connected = False
        box_2_connected = False
        for circuit_id in range(len(circuits)):
            if distances_df.iloc[row_id]["box_1"] in circuits[circuit_id]:
                box_1_connected = True
                box_1_circuit = circuit_id
            if distances_df.iloc[row_id]["box_2"] in circuits[circuit_id]:
                box_2_connected = True
                box_2_circuit = circuit_id

        if box_1_connected and box_2_connected and box_1_circuit == box_2_circuit:
            pass
        elif box_1_connected and box_2_connected:
            circuits[box_1_circuit] = circuits[box_1_circuit] + circuits[box_2_circuit]
            del circuits[box_2_circuit]
            # connection_count += 1
        elif box_1_connected:
            circuits[box_1_circuit].append(distances_df.iloc[row_id]["box_2"])
            # connection_count += 1
        elif box_2_connected:
            circuits[box_2_circuit].append(distances_df.iloc[row_id]["box_1"])
            # connection_count += 1
        else:
            circuits.append(
                [distances_df.iloc[row_id]["box_1"], distances_df.iloc[row_id]["box_2"]]
            )
        connection_count += 1
        pbar.update(1)

        row_id += 1

    circuits.sort(key=len, reverse=True)

    top_n = 3

    return prod([len(circuit) for circuit in circuits[:top_n]])


def day08_2(boxes_np, limit=1000):

    distances_df = calculate_distances(boxes_np)

    connection_count = 1
    row_id = 0
    circuits = [
        [distances_df.iloc[row_id]["box_1"], distances_df.iloc[row_id]["box_2"]]
    ]
    pbar = tqdm(total=limit)

    row_id += 1
    while len(circuits[0]) < boxes_np.shape[0]:

        box_1_connected = False
        box_2_connected = False
        for circuit_id in range(len(circuits)):
            if distances_df.iloc[row_id]["box_1"] in circuits[circuit_id]:
                box_1_connected = True
                box_1_circuit = circuit_id
            if distances_df.iloc[row_id]["box_2"] in circuits[circuit_id]:
                box_2_connected = True
                box_2_circuit = circuit_id

        if box_1_connected and box_2_connected and box_1_circuit == box_2_circuit:
            pass
        elif box_1_connected and box_2_connected:
            circuits[box_1_circuit] = circuits[box_1_circuit] + circuits[box_2_circuit]
            del circuits[box_2_circuit]
        elif box_1_connected:
            circuits[box_1_circuit].append(distances_df.iloc[row_id]["box_2"])
        elif box_2_connected:
            circuits[box_2_circuit].append(distances_df.iloc[row_id]["box_1"])
        else:
            circuits.append(
                [distances_df.iloc[row_id]["box_1"], distances_df.iloc[row_id]["box_2"]]
            )
        connection_count += 1
        pbar.update(1)

        row_id += 1

    return int(distances_df.iloc[row_id - 1]["box_1"].split(",")[0]) * int(
        distances_df.iloc[row_id - 1]["box_2"].split(",")[0]
    )


if __name__ == "__main__":

    input_array_test = read_data_08("data/input08_test.txt")

    print("===TEST 1===")
    print(day08_1(input_array_test, limit=10))

    print("===TEST 2===")
    print(day08_2(input_array_test, limit=10))

    input_array_puzzle = read_data_08("data/input08_puzzle.txt")

    print("===PUZZLE 1===")
    print(day08_1(input_array_puzzle, limit=1000))

    print("===PUZZLE 2===")
    print(day08_2(input_array_puzzle, limit=1000))
