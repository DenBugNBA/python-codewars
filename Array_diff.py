def array_diff(a, b):
    return [i for i in a if not i in b]


print(array_diff([1, 2], [1]))
