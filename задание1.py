def odd_nums(n):
    for i in range(1, n + 1, 2):
        yield i


odd_to_20 = odd_nums(20)
print(next(odd_to_20))
print(next(odd_to_20))
print(next(odd_to_20))
print(next(odd_to_20))
print(next(odd_to_20))
print(next(odd_to_20))
print(next(odd_to_20))
print(next(odd_to_20))
print(next(odd_to_20))
print(next(odd_to_20))