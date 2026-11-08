empty = ()
point = (3,5)
colors = ("red", "greed", "blue")
"""
A single-item tuple needs a comma: (42,) not (42). Without the comma, Python thinks it's just parentheses around a number!
"""
single = (42,) # must use comma for tuple
print(type(single))
not_tuple = (42) # not tuple it's int type
print(type(not_tuple))

print(point[0])
print(point[-1])
print(point[0:])
print(point[0:2])

point = (3,5)
x, y = point # x = 3, y = 5
print(x, y)

x, y = y, x # swapable...
print(x, y)

