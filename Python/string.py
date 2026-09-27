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
    print('Sorry! given txt is not present');
# for check not string;
txt = "The best things in life are free";
if "expensive" not in txt:
    print("No, 'expensive is not present!'")