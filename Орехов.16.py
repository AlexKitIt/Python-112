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
print("_______________________________________________________________________")
print((lambda a, b, c: a * b * c)(2, 5, 5))
print("_______________________________________________________________________")
test = [
    {"name": "Jennifer", "final": 95},
    {"name": "David", "final": 92},
    {"name": "Nikolas", "final": 98}]

test.sort(key=lambda i: i["name"])
print(test)
test.sort(key=lambda i: i["final"], reverse=True)
print(test)
print("_______________________________________________________________________")
test = [
    {"name": "Jennifer", "final": 95},
    {"name": "David", "final": 92},
    {"name": "Nikolas", "final": 98}]

test.sort(key=lambda i: i["final"], reverse=True)
max_final = test[0]
min_final = test[-1]
print(max_final)
print(min_final)
