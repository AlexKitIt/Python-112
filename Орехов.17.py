ls1 = [3, 6, 8, 9, 1, 2]
ls2 = [i for i in range(0, len(ls1))]

print(list(map(lambda x, y: x * (y ** 3), ls1, ls2)))
print("_______________________________________________________________________")
l = [3, -4, -6, 7, -8, 3, -12, 4, 7]
res = list(filter(lambda s: s < 0, l))
print(res)
print(abs(sum(res)))
print("_______________________________________________________________________")
nums = [3, 5, 7, 3, 9, 5, 7, 2]

res1 = list(map(lambda x: x ** 2, nums))
print(res1)
res2 = list(map(lambda x: x ** 3, nums))
print(res2)
print("_______________________________________________________________________")
def func_compute(n):
    def inner(x):
        return n * x

    return inner


res = func_compute(2)
print(res(15))
print(res(20))
res = func_compute(3)
print(res(15))
print(res(20))



