import re


def valid_name(name):
    if re.findall(r'^[a-z0-9@_-]{6,18}$', name, flags=re.I):
        print("Корректный пароль")
    else:
        print("Не корректный пароль")


valid_name("Python_master")
valid_name("123456@s*fa")
print("_______________________________________________________________________")
text = "В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежемесячных осадков"
reg = r'\d+/\d+/\d*'
print(re.findall(reg, text))
print("_______________________________________________________________________")
