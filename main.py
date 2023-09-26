import random


def get_length_list(n):  # Generate n keys, they will be used as the size of each array.
    length_list = set()

    while len(length_list) < n:
        for i in range(n):
            length_list.add(random.randint(1, n))

    length_list = list(length_list)
    random.shuffle(length_list)

    return length_list


def main(n):
    length_list = get_length_list(n)
    nested_array = []

    for i in range(n):
        result_list = []

        # Fill the array with random numbers.
        for j in range(length_list[i]):
            result_list.append(random.randint(1, n))

        # Check the arrays for even/oddness and sort them.
        if i % 2 == 0:
            result_list.sort()
            nested_array.append(result_list)
        else:
            result_list.sort(reverse=True)
            nested_array.append(result_list)

    return nested_array
