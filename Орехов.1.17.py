lst = [-2, 3, 8, -11, -4, 6]
count = 0
for i in lst:
    if i < 0:
        count += 1
print(count)


def count(lst):
    return (1 if lst[0] < 0 else 0) + count(lst[1:]) if lst else 0


print(count(lst))
print("_______________________________________________________________________")
lst1 = [5, 9, 6, 7]
lst2 = [3, 11, 8]
lst3 = [2, 4]
lst4 = [10, 1, 12]
lst = lst1 + lst2 + lst3 + lst3
method = int(input("Введите способ сортировки: 1-по возрастанию, 2-по убыванию -> "))


def bubble(array, met):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if met == 1:
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
            if met == 2:
                if array[j] < array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
    return print(array)


bubble(lst, method)
num = int(input("Введите число для поиска: "))


def search(s, item):
    pos = 0
    found = False
    while pos < len(s) and not found:
        if s[pos] == item:
            found = True
        else:
            pos = pos + 1
    if found:
        return print(f"Число {item} найдено")
    else:
        return print(f"Число {item} не найдено")


search(lst, num)
print("_______________________________________________________________________")
