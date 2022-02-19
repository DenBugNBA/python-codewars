def solution(number):
    return sum(list(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(number))))


print(solution(10))
