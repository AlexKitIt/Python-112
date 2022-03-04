def decor():
    def wrapper(func):
        def wrap(*args):
            return func(*args) / len(args)

        return wrap

    return wrapper


def sum_num(*args):
    return sum(args)


@decor()
def sum_num1(*args):
    return sum(args)


print(sum_num(2, 3, 3, 4))
print(sum_num1(2, 3, 3, 4))

print("_______________________________________________________________________")
def change_char_to_str(s, new):
    s2 = ""
    i = 0
    while i < len(s):
        if i % 2 == 0:
            s2 = s2+new
        else:
            s2 = s2 + s[i]
        i = i + 1

    return s2


str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
str2 = change_char_to_str(str1, "N")
print("str1 =", str1)
print("str2 =", str2)
print("_______________________________________________________________________")
def change_char_to_str(str1, num):
    s1 = ""
    for i in range(0, len(str1)):
        if i == int(num):
            continue
        s1 = s1 + str1[i]
    return s1


s = "0123456789"
s2 = change_char_to_str(s, "4")
print("s =", s)
print("s2 =", s2)
print("_______________________________________________________________________")
def change_char_to_str(str1, num):
    s1 = ""
    for i in range(0, len(str1)):
        if s[i] == num:
            continue
        s1 = s1 + str1[i]
    return s1


s = "012345363738494"
s2 = change_char_to_str(s, "3")
print("s =", s)
print("s2 =", s2)
