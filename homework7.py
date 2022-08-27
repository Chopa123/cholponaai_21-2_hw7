def binary_search(value, lst):
    a = 0
    r = len(lst)
    found = False
    while a + 1 < r:
        m = int((a + r) / 2)
        if lst[m] == value:
            a = r = m
            found = True
        elif lst[m] > value:
            r = m
        else:
            a = m + 1
    if found:
        print(f'Элемент найден под индексом: {a}')
    else:
        print('Элемент не найден')


def bubble_sort(lst):
    for k in range(1, len(lst)):
        for i in range(1, len(lst) - k + 1):
            if lst[i] < lst[i - 1]:
                lst[i - 1], lst[i] = lst[i], lst[i - 1]
    return lst