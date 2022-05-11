
import json
from random import choice


def gen_person():
    key = ""
    name = ""
    tel = ""
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    while len(key) != 10:
        key += choice(nums)
    while len(name) != 7:
        name += choice(letter)
    while len(tel) != 10:
        tel += choice(nums)
    person = {key: {
        "name": name,
        "tel": tel}}
    return person


def write_json(person):
    try:
        data = json.load(open("persons.json"))
    except FileNotFoundError:
        data = {}
    for key in person:
        data[key] = person[key]
    with open("persons.json", "w") as f:
        json.dump(data, f, indent=2)


for i in range(0, 5):
    write_json(gen_person())
print("_______________________________________________________________________")

