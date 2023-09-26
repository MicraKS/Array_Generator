import random


def get_length_list(n):  # Generate n keys, they will be used as the size of each array.
    len_list = set()

    while len(len_list) < n:
        for i in range(n):
            len_list.add(random.randint(1, n))

    len_list = list(len_list)
    random.shuffle(len_list)

    return len_list


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
