import json
std_info = {
    "name": "John Doe",
    "age": 25,
    "city": "New York",
    "marks": [80, 85, 89, 90, 99]
}
with open("mydata.json", "w") as f:
    json.dump(std_info, f, indent=5);
print("Json file written successfully!");

with open ("mydata.json", "r") as fi:
    out = json.load(fi)
print(out)