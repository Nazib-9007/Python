capital = {
    "USA": "Washington D.C.",
    "BD": "Dhaka",
    "Chaina": "Beijing",
    "russia": "Moscow"
}
print(dir(capital))
print(help(capital))
print(capital.get("japan"))

if capital.get("korea"):
    print("That capital exists");
else:
    print("That capital doesn't exists")

capital.update({"japan": "Tokeyo"})
print(capital)
capital.update({"BD": "Ctg"})
print(capital)
print(capital.pop())
print(capital.popitem())

for key in capital.keys():
    print(f"Keys are {key}")

for key, value in capital.items():
    print(f"{key}: {value}")

#Exercise:
person = {
    "name": "John Doe",
    "age": 24,
    "city": "New York"
}
print(person)
score = dict(name="John Doe", id=9007, age=24, city="New York");
print(score)
print(person["name"])
print(person.get("country"))
if person.get("name"):
    print("That person exists");
else:
    print("That person doesn't exists")

del person["age"]
print(person)
student = {
    "John": {"id": 9007, "age": 25},
    "Bob": {"id": 9000, "age": 23},
    "Alice": {"id": 9009, "age": 21}
}
print(student["Alice"]["id"])