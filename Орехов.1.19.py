text = ["Первый файл", "Второй файл"]
with open("1.txt", "w") as ff, open("2.txt", "w") as fs:
    ff.write(text[0])
    fs.write(text[1])

ls = ["1.txt", "2.txt"]
with open('3.txt', 'w') as f:
    f.write("Третий файл = ")
    for i in ls:
        s = open(i).read()
        f.write(s)
        f.write('.')

with open('3.txt', 'r') as f:
    print(f.read())
print("_______________________________________________________________________")
with open('4.txt', 'w') as f:
    f.write("первая строка\nстрока номер два\nтретья строка\n4 строка")
with open('4.txt', 'r') as f:
    count = 0
    for i in f:
        print(i, f"{len(i)} симв. {len(i.split())} сл.")
        count += 1
    print(f"{count} стр.")
print("_______________________________________________________________________")
import os.path

path = "..."
for i in os.listdir(path):
    if os.path.isfile(path + i):
        print(os.path.basename(i), "- file -", f"{os.path.getsize(path + i)} bytes")
    else:
        print(os.path.basename(i), "- dir")



