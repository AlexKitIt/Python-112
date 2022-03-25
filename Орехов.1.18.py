with open("text.txt", "w") as f:
    f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
with open("text.txt", "r") as f:
    rd = f.readlines()
    pos1 = int(input("Введите номер первой строки для замены: "))
    pos2 = int(input("Введите номер второй строки для замены: "))
    rd[pos1], rd[pos2] = rd[pos2], rd[pos1]
with open("text.txt", "w") as f:
    f.writelines(rd)
with open("text.txt", "r") as f:
    print(f.read())
print("_______________________________________________________________________")
with open("text.txt", "w") as f:
    f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
with open("text.txt", "r") as f:
    rd = reversed(f.readlines())
with open("text.txt", "w") as f:
    f.writelines(rd)
with open("text.txt", "r") as f:
    print(f.read())
print("_______________________________________________________________________")
