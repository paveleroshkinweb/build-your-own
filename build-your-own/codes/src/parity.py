def parity_check1(data: int):
    parity = 0
    while data:
        parity = parity ^ (data & 1)
        data >>= 1
    return parity


def parity_check2(data: int):
    parity = 0
    while data:
        parity = parity ^ 1
        data = data & (data-1)
    return parity


parity_table = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0]
def parity_check3(data: int):
    parity = 0
    while data:
        parity = parity ^ parity_table[data & 0b1111]
        data >>= 4
    return parity
