def is_pangram(s):
    for i in "abcdefghigklmnopqrstuvwxyz":
        if i not in s.lower():
            return False
    return True


print(is_pangram("The quick brown fox jumps over the lazy dog"))
