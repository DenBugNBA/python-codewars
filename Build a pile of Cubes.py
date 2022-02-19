def find_nb(m):
    sum = 0
    num = 0
    while True:
        sum += num ** 3
        if sum == m:
            return num
        elif sum > m:
            return -1
        num += 1


print(find_nb(1071225))
print(find_nb(135440716410000))
