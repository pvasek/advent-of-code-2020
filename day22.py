from typing import List

p1 = [
    30,
    42,
    25,
    7,
    29,
    1,
    16,
    50,
    11,
    40,
    4,
    41,
    3,
    12,
    8,
    20,
    32,
    38,
    31,
    2,
    44,
    28,
    33,
    18,
    10,
]
p2 = [
    36,
    13,
    46,
    15,
    27,
    45,
    5,
    19,
    39,
    24,
    14,
    9,
    17,
    22,
    37,
    47,
    43,
    21,
    6,
    35,
    23,
    48,
    34,
    26,
    49,
]


def combat(a: List[int], b: List[int]):
    while a and b:
        a_item = a.pop(0)
        b_item = b.pop(0)
        if a_item > b_item:
            a.append(a_item)
            a.append(b_item)
        else:
            b.append(b_item)
            b.append(a_item)

    a = a if a else b
    result = 0
    length = len(a)
    for i in a:
        result += i * length
        length -= 1        

    return result

print(combat(p1, p2))
