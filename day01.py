from typing import List

def load_data(file_name: str):
    with open(file_name) as f:
        return [int(i) for i in f.readlines()]

def sum_of_two(list: List[int]):
    t = 2020
    list2 = [t - i for i in list]
    for i, v in enumerate(list):
        if v in list2:
            return v * list[list2.index(v)]

    return -1

def sum_of_three(list: List[int]):
    t = 2020
    list2 = [t - i for i in list]
    for i, v in enumerate(list):
        for i2, v2 in enumerate(list):
            val = v + v2
            if val in list2:
                return v * v2 * list[list2.index(val)]

    return -1

data = load_data("./day01.data")
print(sum_of_three(data))