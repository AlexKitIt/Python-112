
lst1 = ["red", "green", "blue"]
lst2 = ["#FF0000", "#008000", "0000FF"]
f = {key: value for key, value in zip(lst1, lst2)}
print(f)
# # _______________________________________________________________________
f = {i: i ** 3 for i in range(1, 11)}
print(f)
# # _____________________________________________________________________
f = dict(zip(["color", "fruit", "pet"], ["blue", "apple", "dog"]))
print(f)
# # Либо как в 1 задании, возмжно не так понял поставлленую задачу
# # ___________________________________________________________________
def min_elem(*num):
    lst = list(num)
    min_el = min(lst)
    return min_el

print(min_elem(10, 9))
print(min_elem(2, 3, 4))
print(min_elem(3, 5, 10, 6))
# # _______________________________________________________________________
def sum_elem(*num):
    s = 0
    for i in num:
        s += i
        print(s, end=" ")
    print()

sum_elem(3, 9, 1)
sum_elem(2, 5, 4, 2)
sum_elem(3, 5, 10, 6, 3)
