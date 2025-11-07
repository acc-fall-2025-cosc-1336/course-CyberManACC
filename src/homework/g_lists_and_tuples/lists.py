def get_lowest_list_value(values):
    if values is None or len(values) == 0:
        raise ValueError("values must be a non-empty list")

    lowest = values[0]
    i = 1
    n = len(values)
    while i < n:
        if values[i] < lowest:
            lowest = values[i]
        i += 1
    return lowest


def get_highest_list_value(values):
    if values is None or len(values) == 0:
        raise ValueError("values must be a non-empty list")

    highest = values[0]
    i = 1
    n = len(values)
    while i < n:
        if values[i] > highest:
            highest = values[i]
        i += 1
    return highest
