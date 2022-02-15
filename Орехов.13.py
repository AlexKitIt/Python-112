d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
nam = d.pop("name")
sal = d.pop("salary")
d1 = dict(name=nam, salary=sal)
print(d)
print(d1)
# # ____________________________________________________________________
d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
d["location"] = d.pop("city")
print(d)
