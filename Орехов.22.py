
names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']


def count_items(lst):
    count = 0
    for item in lst:
        if type(item) == list:
            for i in item:
                if type(i) == list:
                    for x in i:
                        count += 1
                else:
                    count += 1
        else:
            count += 1
    return count


print(count_items(names))
print("_______________________________________________________________________")
import re

s = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7(499)456-45-78"
reg = r'(?:\+?7\s?)\(?\d{3}\)?\s?\d{3}\-?\s?\d{2}\-?\s?\d{2}'
print(re.findall(reg, s))
print("_______________________________________________________________________")
