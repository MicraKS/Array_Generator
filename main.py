import random


def get_length_list(n):  # Сгенирируем n-ключей, они будут использованы как размер каждого массива
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
        for j in range(length_list[i]):  # Заполняем массив случайными числами
            result_list.append(random.randint(1, n))
        if i % 2 == 0:  # Проверяем массивы на четность/нечетность и сортируем
            result_list.sort()
            nested_array.append(result_list)
        else:
            result_list.sort(reverse=True)
            nested_array.append(result_list)
    return nested_array
