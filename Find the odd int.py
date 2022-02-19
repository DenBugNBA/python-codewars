def find_it(seq):
    for number in seq:
        if seq.count(number) % 2 != 0:
            return number


print(find_it([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]))
