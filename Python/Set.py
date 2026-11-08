"""
Sets are collections that only store unique values. They automatically remove duplicates.
"""
empty_set = set()
number = {1,2,3,4,5,5}
print(set(number))
fruits = set(["apple", "banana", "orange"])
print(type(fruits), fruits)

scores = [85, 89, 100, 89, 217, 85]
print(scores)
unique_score = set(scores)
print(unique_score)

colors = {"red", "green"}
colors.add("blue")
print(colors)

colors.remove("blue")
print(colors)

colors.discard("yellow")
print(f"Discard: {colors}")

if "red" in colors:
    print("Red color is exists");

# Remove duplicates..
names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names = list(set(names))
print(unique_names)