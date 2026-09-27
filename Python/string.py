# assigning string in a variable;
str = 'Hello python developer!'
print(str);

# Multiline string;
a = """Lorem ipsum dolor site amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua!"""
print(a);

#String are array;
a = "Hello python developer!"
print(a[6], a[7], a[8])

# Looping through a string and string length;
for x in 'banana':
    print(x);

y = 'python'
print(len(y));

#Check string;
txt = "The best things in life are free!";
print("free" in txt);

txt = "The best things in life are free!"
if "python" in txt:
    print('Yes, "life" is present!')
else:
    print('Sorry! given txt is not present..');
# for check not string;
txt = "The best things in life are free";
if "expensive" not in txt:
    print("No, 'expensive is not present!'")

# Slicing String..
x = 'Hello python world'
print(x[6:12])

print(x[:12])

print(x[0:])

name = 'Harry'
print(len(name))
print(name[len(name)-4: len(name)-2])

# String Formate F-string...
age = 23
txt = f"My name is Nazib, I am {age}"
print(txt);

price = 60
txt = f"This price is ${price}"
print(txt)